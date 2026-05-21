#!/usr/bin/env python3
"""
国知局公布公告站定向检索脚本
数据源：国家知识产权局专利公布公告网 (epub.cnipa.gov.cn)
用途：AI领域专利查新 - P0优先数据源
依赖：pip install playwright && python -m playwright install chromium
降级：Playwright不可用时返回提示，建议用WebSearch替代
"""

import argparse
import json
import sys
from datetime import datetime

def check_playwright():
    """检查Playwright是否可用"""
    try:
        from playwright.sync_api import sync_playwright
        return True
    except ImportError:
        return False

def search_cnipa(keyword, field="all", start_date=None, end_date=None, max_results=10, output=None):
    """
    在国知局公布公告站检索专利

    Args:
        keyword: 检索关键词
        field: 检索字段 (all/name/abstract/claims)
        start_date: 起始日期 (YYYYMMDD)
        end_date: 截止日期 (YYYYMMDD)
        max_results: 最大结果数
        output: 输出文件路径 (JSON)

    Returns:
        list[dict]: 检索结果列表
    """
    if not check_playwright():
        print("[降级] Playwright不可用。请执行以下命令安装：")
        print("  pip install playwright")
        print("  python -m playwright install chromium")
        print("或使用 WebSearch 搜索国知局网站作为替代。")
        return []

    try:
        from playwright.sync_api import sync_playwright
    except Exception as e:
        print(f"[错误] Playwright导入失败: {e}")
        return []

    results = []

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            )
            page = context.new_page()

            # 访问国知局公布公告网
            page.goto("http://epub.cnipa.gov.cn/", timeout=30000)
            page.wait_for_load_state("networkidle")

            # 选择检索字段
            field_map = {"all": "", "name": "1", "abstract": "3", "claims": "5"}
            field_value = field_map.get(field, "")
            if field_value:
                page.select_option("#searchField", field_value)

            # 输入关键词
            page.fill("#searchKeyword", keyword)

            # 设置时间范围（如果提供）
            if start_date:
                page.fill("#startDate", start_date)
            if end_date:
                page.fill("#endDate", end_date)

            # 点击检索
            page.click("#searchBtn")
            page.wait_for_load_state("networkidle")

            # 解析结果
            items = page.query_selector_all(".patent-item")
            for item in items[:max_results]:
                try:
                    title_el = item.query_selector(".patent-title")
                    abstract_el = item.query_selector(".patent-abstract")
                    meta_el = item.query_selector(".patent-meta")

                    result = {
                        "title": title_el.inner_text().strip() if title_el else "",
                        "abstract": abstract_el.inner_text().strip() if abstract_el else "",
                        "meta": meta_el.inner_text().strip() if meta_el else "",
                        "source": "CNIPA",
                        "retrieved_at": datetime.now().isoformat()
                    }
                    results.append(result)
                except Exception:
                    continue

            browser.close()
    except Exception as e:
        print(f"[警告] 检索过程中发生错误: {e}")
        print("[建议] 请改用 WebSearch 作为降级方案")

    # 输出结果
    if output and results:
        with open(output, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f"[完成] 已输出 {len(results)} 条结果到 {output}")
    elif results:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        print("[结果] 未找到相关专利")

    return results

def main():
    parser = argparse.ArgumentParser(
        description="国知局公布公告站定向检索",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python cnipa_search.py --keyword "高斯泼溅 三维重建" --max_results 5
  python cnipa_search.py --keyword "扩散模型 条件生成" --field abstract --start_date 20230101
  python cnipa_search.py --keyword "RAG 检索增强" --output results.json
        """
    )
    parser.add_argument("--keyword", "-k", required=True, help="检索关键词")
    parser.add_argument("--field", "-f", default="all", choices=["all", "name", "abstract", "claims"],
                        help="检索字段 (默认: all)")
    parser.add_argument("--start_date", "-s", default=None, help="起始日期 YYYYMMDD")
    parser.add_argument("--end_date", "-e", default=None, help="截止日期 YYYYMMDD")
    parser.add_argument("--max_results", "-n", type=int, default=10, help="最大结果数 (默认: 10)")
    parser.add_argument("--output", "-o", default=None, help="输出JSON文件路径")

    args = parser.parse_args()
    search_cnipa(
        keyword=args.keyword,
        field=args.field,
        start_date=args.start_date,
        end_date=args.end_date,
        max_results=args.max_results,
        output=args.output
    )

if __name__ == "__main__":
    main()
