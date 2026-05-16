---
AIGC:
  ContentProducer: '001191110102MAD55U9H0F10002'
  ContentPropagator: '001191110102MAD55U9H0F10002'
  Label: '1'
  ProduceID: 'aa96c903-dad6-485f-8823-f2be6cd1a490'
  PropagateID: 'aa96c903-dad6-485f-8823-f2be6cd1a490'
  ReservedCode1: '620997b4-9049-4c1d-a2f3-5e1ad83e59ef'
  ReservedCode2: '620997b4-9049-4c1d-a2f3-5e1ad83e59ef'
---

# AI-Copyright-Skill

**首个面向AI领域的Agent知识产权技能 -- 支持直接输出Word + 简介PPT**

从AI项目代码、论文、设计文档出发，一键生成发明专利申请文件、软件著作权登记材料或技术交底书 -- 内置AI领域专业规则，默认直接输出可用的 `.docx` + `.pptx` 文件。专利路径内置技术交底书中间产物，可直接交给专利代理人。

[English](./README.md)

## 为什么需要这个Skill

现有的专利/软著Skill全部是**通用型** -- 无论什么领域都用同一套模板。AI领域有独特的知识产权挑战：

- **可专利性**：你的算法在国知局审查标准下到底能不能申请专利？
- **权利要求撰写**：怎么写神经网络的方法+系统+存储介质三件套？
- **脱敏**：如何把"A100""PyTorch""70亿参数"替换为专利安全语言？
- **软著**：源代码文档选哪些文件？GPU/CUDA要求怎么写？
- **论文转专利**：消融实验怎么变成从属权利要求？
- **输出格式**：能直接给我Word文件而不是Markdown吗？
- **内部沟通**：怎么快速向管理层或专利代理人介绍发明方案？
- **3D视觉/生成式AI/具身智能**：领域专用的权利要求结构和可专利性风险？

本技能全部解决。

## 功能特性

### 三条产出路径 + 直接Word & PPT输出

| 路径 | 交付物 | 默认格式 |
|------|--------|----------|
| 专利 | 交底书 + 权利要求书 + 说明书 + 摘要 + 简介PPT | `.docx` x2（交底书+专利）+ `.pptx` |
| 软著 | 软件说明书 + 源代码文档 | 2个 `.docx` 文件 |
| 交底书 | 完整技术交底书 | 单个 `.docx` 文件 |

### 7大AI领域 · 22细分方向覆盖

| 领域 | 细分方向 | 权利要求模板 |
|------|----------|-------------|
| **感知智能** | 2D计算机视觉 · 3D视觉与图形学 · 音视频感知 · 传感器融合 | 2.1 模型架构 · 2.2 3D视觉 |
| **认知与语言** | NLP与大语言模型 · 多模态大模型 · RAG · 知识图谱与推理 | 2.3 训练方法 · 2.4 多模态大模型 · 2.5 RAG |
| **生成式AI** | 扩散模型与可控生成 · AIGC版权与水印 · 风格迁移与编辑 | 2.6 扩散模型与可控生成 |
| **决策与交互** | 智能体(Agent) · 具身智能 · 强化学习 | 2.7 Agent · 2.8 具身智能 |
| **AI工程化** | 训练与微调 · 推理部署与优化 · 数据工程 · 边缘与IoT AI | 2.9 推理优化 · 2.10 数据处理 |
| **AI安全与治理** | AI安全与对抗 · AI水印与溯源 · 隐私计算与联邦学习 · AI对齐与可解释性 | 2.11 AI水印与溯源 |
| **行业应用** | 自动驾驶 · 工业制造与质检 · 医疗健康 · 金融风控 · AI4Science · 数字内容与文旅 | 按领域适配对应模板 |

### AI领域专属能力

- **可专利性预判 + 领域风险**（Phase 0）：三要素检测 + 8个高风险领域风险判定与撰写对策
- **11类权利要求模板**：模型架构 / 3D视觉 / 训练方法 / 多模态大模型 / RAG / 扩散模型 / Agent / 具身智能 / 推理优化 / 数据处理 / AI水印
- **领域专用从属权利要求展开策略**：5层通用 + 5个领域专用展开方向表
- **专利布局建议**：单件vs分案决策树 + 3D视觉/具身智能特例
- **6+14+4脱敏替换表**：6类通用 + 14行业项 + 4项3DGS/NeRF专项
- **AI项目自动识别**：11类项目决策树 + 6行业特征检测
- **源代码优先级排序**：12级优先级 + 领域必选文件（3D视觉/生成式AI/具身智能/RAG）
- **论文→专利映射**：6类通用 + 10领域专用映射规则
- **4套软件说明书模板**：通用 / 3D视觉 / 生成式AI / 具身智能
- **13类AI系统附图需求**：从深度学习推理到AI水印系统
- **6组CPC/IPC分类**：30+分类号覆盖AI核心/感知/语言/决策/安全/行业
- **100分制质量评分**：每条路径的量化自检
- **交底书中间产物**（C1.3）：基于技术要点+检索结果自动生成
- **直接Word(.docx)输出**（Phase F）：基于docx-js的专业专利文档排版
- **简介PPT(.pptx)输出**（Phase G）：5-8页执行级汇报，含AI领域标签

### 用户体验设计

- **确认关卡**：每阶段末暂停等用户确认
- **迭代修正**：定向修改指定段落，不重跑完整流水线
- **量化自检**：自动评分，80分以下自动修正
- **斜杠指令**：`/ai-copyright` 或 `/AI知产`
- **格式选项**：`docx`（默认）/ `md` / `both`
- **PPT选项**：专利路径自动生成；其他路径加 `--ppt` 触发

## 工作流程

```
Phase 0  可专利性预判 + 领域风险判定（仅专利路径）
Phase A  需求诊断 -> 路径选择+领域归属+风险等级
Phase B  项目分析 -> 自动识别AI项目类型(11类)+6行业检测+提取技术要点
Phase C  生成（按路径分支）
  ├── C1  专利（查新 -> 布局建议 -> 交底书 -> 权利要求(11类模板) -> 说明书 -> 摘要 -> 自检）
  ├── C2  软著（软件说明书(4套模板) -> 源代码文档 -> 自检）
  └── C3  交底书（通用+领域专用映射 -> 撰写 -> 自检）
Phase D  确认关卡（每阶段末用户审核）
Phase E  迭代修正（定向修改，不重跑全流程）
Phase F  Word文档输出（默认自动执行，基于docx-js）
Phase G  简介PPT输出（专利路径默认，其他路径可选）
```

## 文件结构

```
AI-Copyright-Skill/
├── SKILL.md                              # 主技能文件（Agent入口）
├── README.md                             # 英文文档
├── README_CN.md                          # 本文件
├── LICENSE                               # MIT许可证
└── references/                           # 领域知识库
    ├── ai-patent-special.md              # 可专利性+领域风险+布局策略+映射表+脱敏规则+CPC分类(7节)
    ├── ai-software-copyright-guide.md    # 项目识别(11类)+6行业检测+源文件12级优先级+4套说明书模板+10大避坑
    └── ai-patent-claims-guide.md         # 11类权利要求模板+5层通用+5领域专用从属展开策略
```

## 安装

### 星辰超级智能体 / OpenClaw

将整个 `AI-Copyright-Skill/` 目录复制到技能文件夹：

```bash
# 星辰超级智能体
cp -r AI-Copyright-Skill/ ~/.config/teleai-super-agent/skills/AI-Copyright-Skill/

# OpenClaw / Claude Code
cp -r AI-Copyright-Skill/ .claude/skills/AI-Copyright-Skill/
```

### ClawHub

```bash
clawhub install AI-Copyright-Skill
```

## 使用方式

### 快速开始

安装后在Agent对话中提及专利/软著相关关键词即可触发：

- "帮我基于3DGS项目写一份发明专利申请"
- "生成这个具身智能项目的软著登记材料"
- "把这篇扩散模型论文转成技术交底书"
- `/ai-copyright` 或 `/AI知产`

### 专利路径示例（含Word + PPT输出）

```
用户: 帮我基于我的3DGS项目写一份发明专利申请

智能体 (Phase 0): 运行可专利性预判...
  ✓ 技术问题："大规模三维场景重建中的实时渲染瓶颈"
  ✓ 技术手段："基于自适应密度控制的高斯泼溅方法"
  ✓ 技术效果："推理延迟从120ms降至35ms"
  ⚠ 领域风险：中（3D视觉 - 需在权利要求中展开渲染公式）
  → 可专利性：通过（需应用领域专用撰写规则）

智能体 (Phase B): 自动检测项目类型...
  入口文件：render.py + gaussian.py → 3D视觉类（3DGS）
  领域归属：感知智能 > 3D视觉与图形学
  权利要求模板：2.2（3D视觉）

智能体 (Phase C1): 生成专利文件...
  C1.1 现有技术检索：发现3项相关专利，已区分
  C1.2 布局建议：单件申请（重建+渲染耦合）
  C1.3 技术交底书：已生成（可交付专利代理人）
  C1.4 权利要求：独立(方法，3D视觉四段式)+从属5项+独立(系统)+存储介质1项
  C1.5 说明书：5章，3个实施例，3DGS专项脱敏已应用
  C1.6 摘要：280字
  C1.7 自检：92/100 → 通过

智能体 (Phase F): 生成Word文档...
  → 3dgs-adaptive-density_disclosure.docx（技术交底书）
  → 3dgs-adaptive-density.docx（封面+权利要求+说明书+摘要）

智能体 (Phase G): 生成简介PPT...
  → 3dgs-adaptive-density_简介.pptx（8页，领域：感知智能）

输出：outputs/3dgs-adaptive-density/
  └── patent/
      ├── 3dgs-adaptive-density_disclosure.docx  ← 交专利代理人
      ├── 3dgs-adaptive-density.docx             ← 正式申请文件
      ├── 3dgs-adaptive-density_简介.pptx        ← 管理层汇报
      ├── 3dgs-adaptive-density_claims.md
      ├── 3dgs-adaptive-density_specification.md
      └── 3dgs-adaptive-density_abstract.md
```

### 软著路径示例

```
用户: 生成这个AI项目的软著登记材料

智能体 (Phase B): 自动检测项目类型...
  入口文件：app.py + serve.py → AI服务类（Web API）
  框架：FastAPI + PyTorch
  GPU要求：需要（CUDA 11.8+）
  说明书模板：3.1 通用型

智能体 (Phase C2): 生成软著材料...
  C2.1 软件说明书：12页，8处截图占位，含AI能力描述
  C2.2 源代码文档：model.py(340行) + train.py(280行) + ...
      合计：1560行 → 全部提交（不足3000行）
  C2.3 自检：88/100 → 通过

智能体 (Phase F): 生成Word文档...
  → xxx_软件说明书.docx
  → xxx_源代码文档.docx
```

### 交底书路径示例

```
用户: 把我这篇论文转成技术交底书

智能体 (Phase B): 检测领域...
  论文主题：扩散模型+ControlNet
  领域：生成式AI > 扩散模型与可控生成
  映射：领域专用（噪声调度→权利要求步骤，条件注入→从属权利要求）

智能体 (Phase C3 → Phase F): 论文→交底书映射→Word...
  Research Problem → 技术问题 ✓
  Contribution → 技术方案 ✓
  Ablation Study → 备选实施方式 ✓
  生成式AI专用：噪声调度策略→从属权利要求，ControlNet注入方式→从属权利要求 ✓
  → xxx_disclosure.docx 已生成
```

## 与现有Skill对比

| 功能 | AI-Copyright-Skill v2.0 | Fokkyp/SoftwareCopyright-Skill | patent-disclosure-skill | patent-software-ip (v1.0) |
|------|:----------------------:|:------------------------------:|:-----------------------:|:-------------------------:|
| 专利申请文件 | 完整 | -- | -- | 完整 |
| 软著登记材料 | 完整 | 完整 | -- | 完整 |
| 技术交底书 | 完整 | -- | 完整 | -- |
| **7大AI领域·22细分方向** | **支持** | -- | -- | -- |
| **11类权利要求模板** | **支持** | -- | -- | -- |
| **领域专用从属展开策略** | **5领域** | -- | -- | -- |
| **领域风险判定** | **8风险区** | -- | -- | -- |
| **13类系统附图需求** | **支持** | -- | -- | -- |
| **4套软件说明书模板** | **支持** | -- | -- | -- |
| 交底书作为专利中间产物 | 支持 | -- | -- | -- |
| 直接Word(.docx)输出 | 支持 | -- | -- | -- |
| 简介PPT(.pptx)输出 | 支持 | -- | -- | -- |
| AI可专利性预判 | 内建+领域风险 | -- | -- | -- |
| AI项目自动识别 | 内建(11类+6行业) | -- | -- | -- |
| AI脱敏规则 | 6+14+4条 | -- | -- | 部分 |
| 论文→专利映射 | 6类通用+10领域 | -- | 部分 | -- |
| 专利布局建议 | 内建+3D/具身特例 | -- | -- | -- |
| 确认关卡 | 有 | 有 | -- | -- |
| 100分制质量评分 | 有 | -- | -- | -- |
| 量化自检 | 有 | -- | -- | 仅清单 |
| 迭代修正 | 有 | -- | 有 | 有 |

## 知识库内容

| 参考文件 | 内容 |
|----------|------|
| `ai-patent-special.md` | §1 可专利性三要素+8领域风险 / §2 布局策略(含3D/具身特例) / §3 6类通用+10领域专用映射 / §4 13类系统附图 / §5 6+14+4脱敏替换 / §6 6组CPC/IPC分类 / §7 7大领域速查 |
| `ai-software-copyright-guide.md` | §1 11类决策树+6行业检测 / §2 12级源文件优先级+脱敏清单 / §3 4套说明书模板(通用/3D视觉/生成式AI/具身智能) / §4 10大避坑 |
| `ai-patent-claims-guide.md` | §1 三件套原则 / §2 11类权利要求模板(架构/3D视觉/训练/多模态/RAG/扩散/Agent/具身/推理/数据/水印) / §3 5层通用+5领域专用从属展开 |

## 版本历史

### v2.0.0 (2026-05)

- 从6类权利要求模板扩展为 **11类**，覆盖7大AI领域·22细分方向
- 新增 **领域风险判定**，8个高/中风险领域及撰写对策
- 新增5类权利要求模板：3D视觉、扩散模型/生成式AI、RAG、具身智能(VLA)、AI水印与溯源
- 新增 **5个领域专用从属权利要求展开策略**
- 脱敏规则从6条扩展为 **6+14+4**（通用+行业+3DGS/NeRF专项）
- 项目检测从6类扩展为 **11类 + 6行业特征**
- 新增 **4套软件说明书模板**（通用/3D视觉/生成式AI/具身智能）
- 系统附图需求从5类扩展为 **13类AI系统**
- CPC/IPC分类从6个扩展为 **6组30+分类号**
- 新增ai-patent-special.md第7节7大领域速查表

### v1.2.0

- 首次公开发布，6类权利要求模板和3条产出路径

## 许可证

MIT License -- 详见 [LICENSE](./LICENSE)

## 作者

jaccen -- [GitHub](https://github.com/jaccen) | [AI-Copyright-Skill](https://github.com/jaccen/AI-Copyright-Skill) | [Awesome-Gaussian-Skills](https://github.com/jaccen/Awesome-Gaussian-Skills)

## 致谢

本技能设计过程中学习借鉴了以下优秀项目：

- [Fokkyp/SoftwareCopyright-Skill](https://github.com/Fokkyp/SoftwareCopyright-Skill) -- 确认关卡交互设计
- [patent-disclosure-skill](https://clawhub.ai/) -- prompt分子包架构 + 交底书工作流
- [na57/chinese-copyright-application-skill](https://github.com/na57/chinese-copyright-application-skill) -- AI项目类型检测
- [Earl000333/paperforge](https://github.com/Earl000333/paperforge) -- 论文→专利映射方法论
- [hapi-ds/mPAPA](https://github.com/hapi-ds/mPAPA) -- 结构化多步工作流
- [IGTA-Tech/provisional-patent-skills](https://github.com/IGTA-Tech/provisional-patent-skills) -- 100分制质量评分

> AI生成