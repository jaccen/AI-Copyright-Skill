---
name: AI-Copyright-Skill
description: "AI-native IP skill: generate patent applications, software copyright materials, or technical disclosures from AI project code/papers/docs, with direct Word and PPT output. Covers 7 AI domains, 11 claim templates, patentability check, desensitization, prior-art search, and self-check."
version: "2.0.0"
author: jaccen
tags: ["patent", "software-copyright", "ip", "ai", "intellectual-property", "docx", "pptx", "3d-vision", "generative-ai", "embodied-ai", "rag", "ai-watermark"]
---

# AI知识产权文件生成

面向AI研发与AI行业应用的知识产权文件生成技能，覆盖三条路径：

- **专利路径**：发明专利申请文件（权利要求书+说明书+摘要），含技术交底书中间产物
- **软著路径**：软件著作权登记材料（说明书+源代码文档）
- **交底书路径**：从论文/研究笔记生成技术交底书

覆盖 **7大AI领域(感知智能/认知与语言/生成式AI/决策与交互/AI工程化/AI安全与治理/行业应用) 22细分方向**，11类权利要求模板。

## 触发条件

专利申请/权利要求书/说明书/软著/技术交底书/IP申请/论文转专利/`/ai-copyright`/`/AI知产`

**迭代意图**：已有产出上继续修改时，直接进入迭代修正流程。

## 总体流程

```
Phase 0  可专利性预判（仅专利路径）
Phase A  需求诊断 → 路径+领域归属+风险等级
Phase B  资料解读与项目识别 → 自动识别11类AI项目+6行业+提取技术要点
Phase C  生成（按路径分支）
  C1 专利：查新→布局→交底书→权利要求(11类模板)→说明书→摘要→自检
  C2 软著：软件说明书(4套模板)→源代码文档→自检
  C3 交底书：映射(通用6类+领域专用)→撰写→自检
Phase D  确认关卡
Phase E  迭代修正
Phase F  Word文档输出（docx-js，默认自动执行）
Phase G  简介PPT输出（PptxGenJS工作流，专利路径默认）
```

## Phase 0 可专利性预判

依据 `references/ai-patent-special.md` §1 检测三要素：技术问题（锚定具体场景）、技术手段（步骤与系统架构绑定）、技术效果（可量化）。

领域风险判定（依据 §1.3）：8个高/中风险领域（生成式AI、金融风控、AI对齐、具身智能、强化学习、RAG、AIGC水印等）需应用领域专用撰写对策。

判定：全过+低风险→继续；全过+高风险→继续但强制领域对策；技术手段不过→转交底书路径；技术效果不过→补充定量对比。

## Phase A 需求诊断

向用户确认：路径选择、技术主题、AI领域归属（7大领域22方向、自动检测辅助）、申请人/发明人信息、已有材料。

确认关卡：输出3-5行诊断摘要（含领域归属和风险等级）。

## Phase B 资料解读与项目识别

B.1 自动识别（依据 `references/ai-software-copyright-guide.md` §1.1 决策树）：app.py→AI服务、train.py→训练、inference.py→推理、render.py/gaussian.py→3D视觉、diffusion.py→生成式AI、robot.py/vla.py→具身智能、pipeline.py+langchain→Agent、pipeline.py+rag→RAG、package.json→前端全栈。同时检测6行业特征（§1.3）。

B.2 技术要点提取：按优先级读取模型定义→训练/推理→渲染/生成/控制→论文→设计文档→README。形成技术要点清单（创新点/方案骨架/参数/区别/量化效果/领域归属）。

确认关卡：展示技术要点清单。

## Phase C1 专利申请文件

C1.1 现有技术检索：联网搜索2-3轮，范围含国知局/Google Patents/arXiv，建议CPC分类（§6）。

C1.2 布局建议（§2）：单件/分案/3件系列/具身2件，等用户确认。

C1.3 技术交底书（中间产物）：7章结构（发明名称→技术领域→背景→发明内容→附图→实施方式→创新点摘要），用于交付专利代理人。

C1.4 权利要求书（`references/ai-patent-claims-guide.md`）：方法+系统+介质三件套，11类模板按领域适配（2.1模型架构/2.2 3D视觉/2.3训练/2.4多模态/2.5 RAG/2.6扩散模型/2.7 Agent/2.8具身智能/2.9推理优化/2.10数据处理/2.11 AI水印）。领域特殊要求：3D视觉需四段式+渲染公式；生成式AI需条件注入步骤；具身智能需绑定传感器+执行器；RAG需完整技术链路；AI水印需注入层/位置/编码。从属权利要求：通用5层递进+领域专用展开（§3.2）。

C1.5 说明书：五章结构（技术领域→背景→发明内容→附图→实施方式）。脱敏规则（§5）：6类通用+14行业+4项3D专项。附图（§4）：13类AI系统必备附图。

C1.6 摘要：300字内，技术领域+核心方案+技术效果。

C1.7 量化自检（100分制）：完整特征15+回引10+三件套10+充分公开15+实施覆盖15+效果量化10+术语5+摘要对应5+脱敏10+附图5。≥80交付，60-80自动修正，<60重写。

## Phase C2 软著登记材料

（`references/ai-software-copyright-guide.md`）

C2.1 说明书（10-15页，截图≥6张）：4套模板按项目类型选用——3.1通用/3.2 3D视觉/3.3生成式AI/3.4具身智能。面向审查员避免行话，需人机交互描述，开源权重声明不在保护范围。

C2.2 源代码文档（前30+后30页，每页≥50行）：12级源文件优先级（§2.1），3D视觉类必选render.py、生成式AI类必选generate.py、具身智能类必选control.py、RAG类必选retriever.py。脱敏清单（§2.2）：删API Key/绝对路径/内网/邮箱/硬件型号/云服务URL。

C2.3 量化自检：页数15+截图10+功能覆盖15+非技术描述10+GPU信息10+代码页数15+每页行数10+一致性5+无泄露10。

## Phase C3 技术交底书

C3.1 映射（§3）：通用6类（Problem→技术问题/Contribution→技术方案/Modules→实施单元/Flow→实施流程/Outcome→预期效果/Ablation→备选方案）+7领域专用映射（3D视觉渲染公式/生成式AI采样调度/具身Sim2Real/RL奖励函数/RAG检索策略/AI水印鲁棒性/AI4Sci物理约束）。

C3.2 撰写：7章结构（同C1.3）。

C3.3 量化自检：场景锚定15+可实施20+量化对比15+区别清晰15+附图15+可理解10+完整10。

## Phase D 确认关卡

每Phase后展示摘要，选项：确认继续/修改/切换路径/暂停存档(.temp/ai-ip-progress.md)。

## Phase E 迭代修正

识别→定位→定向修正→差异标注(`<!-- 修订 -->`)→另存v{N}→重跑自检。禁止重跑完整流水线。

## Phase G 简介PPT输出

专利路径默认执行，其他路径`--ppt`触发。

### G.1 内容预处理（MANDATORY）

从 Phase C1 产出中提取每页要点，每页正文 ≤80 字，每条要点 ≤25 字。按以下结构规划页面大纲：

| 页码 | 标题 | 内容来源 | 核心要点（≤25字/条） |
|------|------|----------|---------------------|
| 1 | 封面 | Phase A诊断 | 发明名称 + 申请人 + 领域标签 |
| 2 | 背景与痛点 | C1.5说明书·背景 | 2-3个技术痛点 |
| 3 | 核心创新 | C1.4权利要求·独立项 | 方法核心步骤（3-5步） |
| 4 | 系统架构 | C1.4权利要求·系统项 | 模块组成 + 数据流 |
| 5 | 效果对比 | C1.5说明书·发明内容 | 量化指标对比（vs现有技术） |
| 6 | 专利布局 | C1.2布局建议 | 单件/分案 + 保护范围 |
| 7 | 实施计划 | C1.5说明书·实施方式 | 关键里程碑 + 预期节点 |

布局建议：内容 ≤6 页用全幅布局；7-8 页用左右分栏（文字35%+图示65%）；禁止逐字搬运说明书原文。

### G.2 PPT生成（PptxGenJS工作流）

使用 Node.js + PptxGenJS 编程式创建 PPT，与 Phase F 的 docx-js 模式一致。**禁止使用 python-pptx**（未预装，需 pip install）。**禁止使用 html2pptx 工作流**（依赖 Playwright + Chromium ~150MB，首次运行需下载浏览器，极易失败）。

**步骤**：

1. **安装依赖**：在 `.temp/{案件名}/` 下执行 `npm install pptxgenjs`（~2秒，轻量）
2. **生成脚本**：`.temp/{案件名}/{案件名}-pptx.js`，内容按下方模板
3. **执行**：`node .temp/{案件名}/{案件名}-pptx.js`
4. **输出**：`outputs/{案件标识}/patent/{案件名}_简介.pptx`

**脚本模板**：

```javascript
const pptxgen = require("pptxgenjs");
const pptx = new pptxgen();
pptx.layout = "LAYOUT_16x9";
pptx.author = "AI-Copyright-Skill";

// 配色
const C = { primary: "0052D9", secondary: "0033A0", light: "E6F0FF",
            text: "333333", white: "FFFFFF" };

// 字体
const F = { title: { fontFace: "Microsoft YaHei", fontSize: 24, bold: true, color: C.white },
            body:  { fontFace: "Microsoft YaHei", fontSize: 14, color: C.text },
            note:  { fontFace: "Microsoft YaHei", fontSize: 10, color: "999999" },
            big:   { fontFace: "Arial", fontSize: 36, bold: true, color: C.primary } };

// --- 逐页添加（按 G.1 大纲填充） ---

// 第1页：封面
let s1 = pptx.addSlide();
s1.background = { fill: C.primary };
s1.addText("{{发明名称}}", { x: 0.8, y: 1.5, w: 8.4, h: 1.2, ...F.title, fontSize: 32, color: C.white, align: "center" });
s1.addText("{{申请人}} | {{领域标签}}", { x: 0.8, y: 3.0, w: 8.4, h: 0.6, fontFace: "Microsoft YaHei", fontSize: 14, color: "B0C4DE", align: "center" });

// 第2页：背景与痛点（蓝色标题栏 + 白色内容卡）
let s2 = pptx.addSlide();
s2.addShape(pptx.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.9, fill: { color: C.primary } });
s2.addText("背景与痛点", { x: 0.5, y: 0.1, w: 9, h: 0.7, ...F.title, color: C.white });
s2.addText([{ text: "{{痛点1}}\n" }, { text: "{{痛点2}}\n" }, { text: "{{痛点3}}" }], { x: 0.8, y: 1.2, w: 8.4, h: 3.5, ...F.body, bullet: true, lineSpacingMultiple: 1.5 });

// 第3-7页：按 G.1 大纲继续添加，结构同第2页（标题栏+内容区）

// 保存
pptx.writeFile({ fileName: "outputs/{{案件标识}}/patent/{{案件名}}_简介.pptx" });
```

**页面结构统一规范**：
- 标题栏：顶部 0.9in 蓝色矩形 + 白色标题文字
- 内容区：0.8in 起始，左右各 0.8in 边距
- 列表项用 `bullet: true` + `lineSpacingMultiple: 1.5`
- 效果对比页用 `addTable` 渲染指标对比表

配色方案（科技蓝）：
- 主色：`#0052D9`（标题栏、封面背景）
- 辅色：`#0033A0`（副标题、装饰）
- 浅底：`#E6F0FF`（卡片背景）
- 正文：`#333333`
- 背景：`#FFFFFF`

字体规范：
- 标题：微软雅黑 24pt Bold / 封面 32pt
- 正文：微软雅黑 14pt Regular
- 注释：微软雅黑 10pt / 灰色
- 数据展示：Arial 36pt Bold（大数字）

### G.3 验证

生成后读取输出文件确认非空，用 `python -m markitdown {文件}.pptx` 提取文字校验内容完整性。如需视觉验证，可调用内置 pptx skill 的 thumbnail.py。

## Phase F Word文档输出

默认自动执行（用户要求md时除外）。docx-js工作流：`.temp/{案件名}-docx.js`。

输出策略：专利→交底书.docx+专利.docx(封面+权利要求+说明书+摘要)；软著→2个.docx；交底书→1个.docx。

格式：正文宋体24pt/标题黑体32-28pt/行距1.5倍/首行缩进480DXA/页边距1英寸。源代码Courier New 18pt每页50行。

备选：`md`/`docx`(默认)/`both`。

## 输出交付规范

```
outputs/{案件标识}/
├── patent/     {案件名}_disclosure.docx + {案件名}.docx + _简介.pptx + .md中间文件
├── software-copyright/  {软件名}_manual.docx + _source_code.docx + .md中间文件
└── disclosure/ {案件名}_disclosure.docx + .md
```

禁止：skill名/仓库路径/自检清单/虚构专利号/"大约""左右"/商业术语。

## 知识索引

| 参考文件 | 内容 |
|----------|------|
| `references/ai-patent-special.md` | §1可专利性+8领域风险 §2布局(含3D/具身) §3 6类+10领域映射 §4 13类附图 §5 6+14+4脱敏 §6 6组CPC §7速查 |
| `references/ai-patent-claims-guide.md` | §1三件套 §2 11类模板 §3 5层+5领域从属展开 |
| `references/ai-software-copyright-guide.md` | §1 11类+6行业检测 §2 12级优先级+脱敏 §3 4套模板 §4 10避坑 |
