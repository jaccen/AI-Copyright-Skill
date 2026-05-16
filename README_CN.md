# ai-ip-skill

**首个面向AI领域的Agent知识产权技能**

从AI项目代码、论文、设计文档出发，一键生成发明专利申请文件、软件著作权登记材料或技术交底书。内置AI领域可专利性判定、6类权利要求模板、项目自动识别、脱敏规则、查新与量化自检。

[English](./README.md)

## 为什么需要这个Skill

现有的专利/软著Skill全部是通用型——无论什么领域都用同一套模板。AI领域有独特的知识产权挑战：

- **可专利性**：你的算法在国知局审查标准下到底能不能申请专利？
- **权利要求撰写**：怎么写神经网络的方法+系统+存储介质三件套？
- **脱敏**：如何把"A100""PyTorch""70亿参数"替换为专利安全语言？
- **软著**：源代码文档选哪些文件？GPU/CUDA要求怎么写？
- **论文转专利**：消融实验怎么变成从属权利要求？

本技能全部解决。

## 功能特性

### 三条产出路径

| 路径 | 交付物 | 目标机构 |
|------|--------|----------|
| 专利 | 权利要求书 + 说明书 + 摘要 | 国知局（CNIPA） |
| 软著 | 软件说明书 + 源代码文档 | CPCC（中国版权保护中心） |
| 交底书 | 完整技术交底书 | 专利代理人 |

### AI领域专属能力

- **可专利性预判**（Phase 0）：三要素检测——技术问题、技术手段、技术效果
- **6类方案权利要求模板**：模型架构 / 训练方法 / 推理优化 / 数据处理 / 多模态融合 / Agent系统
- **专利布局建议**：单件申请 vs 分案申请决策树
- **6类脱敏替换表**：数据集名、参数量、硬件型号、框架名、训练成本、API名
- **AI项目自动识别**：基于入口文件的决策树（train.py→训练类，serve.py→服务类...）
- **源代码优先级排序**：model.py → train.py → inference.py → dataset.py → loss.py
- **论文→专利映射**：研究问题→技术问题，贡献→技术方案，消融→从属权利要求
- **100分制质量评分**：每条路径的量化自检

### 用户体验设计

- **确认关卡**：每阶段末暂停等用户确认
- **迭代修正**：定向修改指定段落，不重跑完整流水线
- **量化自检**：自动评分，80分以下自动修正
- **斜杠指令**：`/ai-ip` 或 `/AI知产`

## 工作流程

```
Phase 0  可专利性预判（仅专利路径）
Phase A  需求诊断 → 路径选择+边界确认
Phase B  项目分析 → 自动识别AI项目类型+提取技术要点
Phase C  生成（按路径分支）
  ├── C1  专利（查新→布局建议→权利要求→说明书→摘要→自检）
  ├── C2  软著（软件说明书→源代码文档→自检）
  └── C3  交底书（映射→撰写→自检）
Phase D  确认关卡（每阶段末用户审核）
Phase E  迭代修正（定向修改，不重跑全流程）
```

## 文件结构

```
ai-ip-skill/
├── SKILL.md                              # 主技能文件（Agent入口）
├── README.md                             # 英文文档
├── README_CN.md                          # 本文件
├── LICENSE                               # MIT许可证
└── references/                           # 领域知识库
    ├── ai-patent-special.md              # 可专利性+布局策略+映射表+脱敏规则+CPC分类
    ├── ai-software-copyright-guide.md    # 项目识别+源文件优先级+说明书模板+常见问题
    └── ai-patent-claims-guide.md         # 6类权利要求模板+5层从属展开策略
```

## 安装

### 星辰超级智能体 / OpenClaw

将整个 `ai-ip-skill/` 目录复制到技能文件夹：

```bash
# 星辰超级智能体
cp -r ai-ip-skill/ ~/.config/teleai-super-agent/skills/ai-ip-skill/

# OpenClaw / Claude Code
cp -r ai-ip-skill/ .claude/skills/ai-ip-skill/
```

### ClawHub

```bash
clawhub install ai-ip-skill
```

## 使用方式

### 快速开始

安装后在Agent对话中提及专利/软著相关关键词即可触发：

- "帮我基于3DGS项目写一份发明专利申请"
- "生成这个AI项目的软著登记材料"
- "把这篇论文转成技术交底书"
- `/ai-ip` 或 `/AI知产`

### 专利路径示例

```
用户: 帮我基于我的3DGS项目写一份发明专利申请

智能体 (Phase 0): 运行可专利性预判...
  ✓ 技术问题："大规模三维场景重建中的实时渲染瓶颈"
  ✓ 技术手段："基于自适应密度控制的高斯泼溅方法"
  ✓ 技术效果："推理延迟从120ms降至35ms"
  → 可专利性：通过

智能体 (Phase A): 确认需求...
  路径：专利申请
  AI项目类型：模型架构创新
  ...

智能体 (Phase B): 扫描项目...
  识别入口：train.py → 训练类
  核心创新：gaussian_renderer.py 中的自适应密度控制模块
  提取要点：[5项]

智能体 (Phase C1): 生成专利文件...
  C1.1 现有技术检索：发现3项相关专利，已区分
  C1.2 布局建议：单件申请（架构+训练耦合）
  C1.3 权利要求：独立1项(方法)+从属5项+独立1项(系统)+存储介质1项
  C1.4 说明书：5章，3个实施例
  C1.5 摘要：280字
  C1.6 自检：92/100 → 通过

输出：outputs/3dgs-adaptive-density/
  ├── patent/
  │   ├── 3dgs-adaptive-density_claims.md
  │   ├── 3dgs-adaptive-density_specification.md
  │   ├── 3dgs-adaptive-density_abstract.md
  │   └── 3dgs-adaptive-density_full.md
```

### 软著路径示例

```
用户: 生成这个AI项目的软著登记材料

智能体 (Phase B): 自动检测项目类型...
  入口文件：app.py + serve.py → AI服务类（Web API）
  框架：FastAPI + PyTorch
  GPU要求：需要（CUDA 11.8+）

智能体 (Phase C2): 生成软著材料...
  C2.1 软件说明书：12页，8处截图占位，含AI能力描述
  C2.2 源代码文档：model.py(340行) + train.py(280行) + inference.py(195行) + ...
      合计：1560行 → 全部提交（不足3000行）
  C2.3 自检：88/100 → 通过
```

### 交底书路径示例

```
用户: 把我这篇论文转成技术交底书

智能体 (Phase C3): 论文→交底书映射...
  Research Problem → 技术问题 ✓
  Contribution → 技术方案 ✓
  Method Modules → 实施单元 ✓
  Algorithm Flow → 实施流程 ✓
  Experimental Outcome → 技术效果 ✓
  Ablation Study → 备选实施方式 ✓
```

## 与现有Skill对比

| 功能 | ai-ip-skill | Fokkyp/SoftwareCopyright-Skill (3k stars) | patent-disclosure-skill | patent-software-ip (v1.0) |
|------|:-----------:|:------------------------------------------:|:-----------------------:|:--------------------------:|
| 专利申请文件 | 完整 | -- | -- | 完整 |
| 软著登记材料 | 完整 | 完整 | -- | 完整 |
| 技术交底书 | 完整 | -- | 完整 | -- |
| AI可专利性预判 | 内建 | -- | -- | -- |
| AI权利要求模板(6类) | 内建 | -- | -- | -- |
| AI项目自动识别 | 内建 | -- | -- | -- |
| AI脱敏规则 | 内建 | -- | -- | 部分 |
| 论文→专利映射 | 内建 | -- | 部分 | -- |
| 专利布局建议 | 内建 | -- | -- | -- |
| 确认关卡 | 有 | 有 | -- | -- |
| 100分制质量评分 | 有 | -- | -- | -- |
| 量化自检 | 有 | -- | -- | 仅清单 |
| 迭代修正 | 有 | -- | 有 | 有 |

## 知识库内容

| 参考文件 | 内容 |
|----------|------|
| `ai-patent-special.md` | 可专利性三要素判定 / 单件vs分案决策 / 论文→专利6类映射 / AI附图需求 / 6类脱敏替换表 / CPC-IPC分类参考 |
| `ai-software-copyright-guide.md` | AI项目类型决策树 / 各类型说明书侧重点 / 源文件优先级 / 代码脱敏清单 / AI说明书模板 / 5大常见问题 |
| `ai-patent-claims-guide.md` | 方法+系统+介质三件套原则 / 6类AI权利要求模板(架构/训练/推理/数据/多模态/Agent) / 5层从属权利要求展开策略 |

## 许可证

MIT License — 详见 [LICENSE](./LICENSE)

## 作者

jaccen — [GitHub](https://github.com/jaccen) | [Awesome-Gaussian-Skills](https://github.com/jaccen/Awesome-Gaussian-Skills)

## 致谢

本技能设计过程中学习借鉴了以下优秀项目：

- [Fokkyp/SoftwareCopyright-Skill](https://github.com/Fokkyp/SoftwareCopyright-Skill) — 确认关卡交互设计
- [patent-disclosure-skill](https://clawhub.ai/) — prompt分子包架构 + 交底书工作流
- [na57/chinese-copyright-application-skill](https://github.com/na57/chinese-copyright-application-skill) — AI项目类型检测
- [Earl000333/paperforge](https://github.com/Earl000333/paperforge) — 论文→专利映射方法论
- [hapi-ds/mPAPA](https://github.com/hapi-ds/mPAPA) — 结构化多步工作流
- [IGTA-Tech/provisional-patent-skills](https://github.com/IGTA-Tech/provisional-patent-skills) — 100分制质量评分
