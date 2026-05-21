#!/usr/bin/env python3
"""
Google Patents 检索脚本
数据源：Google Patents (patents.google.com)
用途：AI领域专利查新 - P1补充数据源（全球专利覆盖）
依赖：pip install requests
降级：API不可用时生成手动检索URL
"""

import argparse
import json
import sys
import urllib.parse
from datetime import datetime

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

GOOGLE_PATENTS_BASE = "https://patents.google.com"
SEARCH_URL = "https://patents.google.com/api/search"

def search_google_patents(keyword, cpc=None, country="US", max_results=10, output=None):
    """
    在Google Patents检索专利

    Args:
        keyword: 检索关键词
        cpc: CPC分类号 (如 "G06N3/08")
        country: 国家代码 (US/CN/EP/JP/KR/WO)
        max_results: 最大结果数
        output: 输出文件路径 (JSON)

    Returns:
        list[dict]: 检索结果列表
    """
    if not HAS_REQUESTS:
        print("[降级] requests库不可用。请执行：pip install requests")
        url = _generate_manual_url(keyword, cpc, country)
        print(f"[手动检索] 请在浏览器中访问: {url}")
        return []

    query = keyword
    if cpc:
        query += f" (CPC:{cpc})"

    params = {
        "q": query,
        "oq": query,
        "page": 0,
    }

    results = []

    try:
        resp = requests.get(SEARCH_URL, params=params, timeout=15,
                          headers={"User-Agent": "Mozilla/5.0"})
        if resp.status_code == 200:
            data = resp.json()
            for item in data.get("results", [])[:max_results]:
                result = {
                    "patent_id": item.get("id", ""),
                    "title": item.get("title", ""),
                    "assignee": item.get("assignee", ""),
                    "country": item.get("country_code", ""),
                    "filing_date": item.get("filing_date", ""),
                    "publication_date": item.get("publication_date", ""),
                    "abstract": item.get("abstract", ""),
                    "cpc": item.get("cpc", []),
                    "source": "Google Patents",
                    "retrieved_at": datetime.now().isoformat()
                }
                results.append(result)
        else:
            print(f"[警告] API返回状态码 {resp.status_code}")
            url = _generate_manual_url(keyword, cpc, country)
            print(f"[手动检索] 请在浏览器中访问: {url}")
    except Exception as e:
        print(f"[警告] API请求失败: {e}")
        url = _generate_manual_url(keyword, cpc, country)
        print(f"[手动检索] 请在浏览器中访问: {url}")

    if output and results:
        with open(output, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f"[完成] 已输出 {len(results)} 条结果到 {output}")
    elif results:
        print(json.dumps(results, ensure_ascii=False, indent=2))

    return results

def _generate_manual_url(keyword, cpc=None, country="US"):
    """生成Google Patents手动检索URL"""
    query = keyword
    if cpc:
        query += f" (CPC:{cpc})"
    encoded = urllib.parse.quote(query)
    return f"{GOOGLE_PATENTS_BASE}/?q={encoded}&oq={encoded}"

def main():
    parser = argparse.ArgumentParser(
        description="Google Patents 检索",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python google_patents_search.py --keyword "gaussian splatting 3D reconstruction"
  python google_patents_search.py --keyword "diffusion model conditional generation" --cpc "G06N3/0845"
  python google_patents_search.py --keyword "RAG retrieval augmented" --country US --output results.json
        """
    )
    parser.add_argument("--keyword", "-k", required=True, help="检索关键词")
    parser.add_argument("--cpc", "-c", default=None, help="CPC分类号 (如 G06N3/08)")
    parser.add_argument("--country", "-n", default=None, help="国家代码过滤")
    parser.add_argument("--max_results", "-m", type=int, default=10, help="最大结果数 (默认: 10)")
    parser.add_argument("--output", "-o", default=None, help="输出JSON文件路径")

    args = parser.parse_args()
    search_google_patents(
        keyword=args.keyword,
        cpc=args.cpc,
        country=args.country,
        max_results=args.max_results,
        output=args.output
    )

if __name__ == "__main__":
    main()
