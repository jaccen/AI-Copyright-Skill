# ai-ip-skill

**The First AI-Native Intellectual Property Skill for Agent Workflows**

An Agent Skill that generates Chinese patent application documents, software copyright registration materials, and technical disclosure reports from AI project code, research papers, and design docs — with domain-specific rules baked in.

[中文文档](./README_CN.md)

## Why This Skill Exists

Existing patent/copyright skills are all **generic** — same templates for any domain. AI has unique IP challenges:

- **Patentability**: Is your algorithm even patentable under CNIPA guidelines?
- **Claim drafting**: How to write method+system+storage-medium triple claims for a neural network?
- **Desensitization**: How to replace "A100", "PyTorch", "7B parameters" with patent-safe language?
- **Software copyright**: Which source files to include? How to handle GPU/CUDA requirements?
- **Paper-to-patent mapping**: How to turn ablation studies into dependent claims?

This skill answers all of them.

## Features

### Three Output Paths

| Path | Deliverables | Target |
|------|-------------|--------|
| Patent | Claims + Specification + Abstract | CNIPA (China National Intellectual Property Administration) |
| Software Copyright | Software Manual + Source Code Doc | CPCC (China Copyright Protection Center) |
| Technical Disclosure | Full disclosure document | Patent agents / attorneys |

### AI-Domain Specific Capabilities

- **Patentability Pre-Assessment** (Phase 0): 3-factor test — technical problem, technical means, technical effect
- **6-Type Claim Templates**: Model architecture / Training method / Inference optimization / Data processing / Multi-modal fusion / Agent system
- **Patent Layout Advisory**: Single application vs. divisional filing decision tree
- **6-Type Desensitization Table**: Dataset names, parameter counts, hardware models, framework names, training costs, API names
- **AI Project Auto-Detection**: Decision tree based on entry files (train.py → Training, serve.py → API Service, ...)
- **Source Code Priority**: model.py → train.py → inference.py → dataset.py → loss.py
- **Paper-to-Patent Mapping**: Research Problem → Technical Problem, Contribution → Technical Solution, Ablation → Dependent Claims
- **100-Point Quality Scoring**: Quantitative self-check for each output path

### User Experience

- **Confirmation Gates**: Pause at each phase boundary for user review
- **Iterative Correction**: Modify specific sections without re-running the entire pipeline
- **Quantitative Self-Check**: Auto-score and auto-fix when score < 80
- **Slash Commands**: `/ai-ip` or `/AI知产`

## Workflow

```
Phase 0  Patentability Pre-Assessment (patent path only)
Phase A  Requirement Diagnosis → path selection + boundary
Phase B  Project Analysis → auto-detect AI project type + extract key points
Phase C  Generation (branch by path)
  ├── C1  Patent (search → layout → claims → specification → abstract → self-check)
  ├── C2  Software Copyright (manual → source code doc → self-check)
  └── C3  Technical Disclosure (mapping → drafting → self-check)
Phase D  Confirmation Gate (user review at each phase end)
Phase E  Iterative Correction (targeted fix, no full re-run)
```

## File Structure

```
ai-ip-skill/
├── SKILL.md                              # Main skill file (agent entry point)
├── README.md                             # This file
├── README_CN.md                          # Chinese documentation
├── LICENSE                               # MIT License
└── references/                           # Domain knowledge base
    ├── ai-patent-special.md              # Patentability + layout + mapping + desensitization + CPC codes
    ├── ai-software-copyright-guide.md    # Project detection + source priority + manual template + pitfalls
    └── ai-patent-claims-guide.md         # 6-type claim templates + 5-layer dependent claim strategy
```

## Installation

### TeleAI Super Agent / OpenClaw

Copy the entire `ai-ip-skill/` directory to your skills folder:

```bash
# TeleAI Super Agent
cp -r ai-ip-skill/ ~/.config/teleai-super-agent/skills/ai-ip-skill/

# OpenClaw / Claude Code
cp -r ai-ip-skill/ .claude/skills/ai-ip-skill/
```

### ClawHub

```bash
clawhub install ai-ip-skill
```

## Usage

### Quick Start

Once installed, simply mention patent/copyright-related keywords in your agent chat:

- "Help me write a patent for my 3DGS重建方法"
- "Generate software copyright materials for this project"
- "Convert my paper into a technical disclosure document"
- `/ai-ip` or `/AI知产`

### Patent Path Example

```
User: 帮我基于我的3DGS项目写一份发明专利申请

Agent (Phase 0): Running patentability assessment...
  ✓ Technical problem: "Real-time rendering bottleneck in large-scale 3D scene reconstruction"
  ✓ Technical means: "Gaussian splatting with adaptive density control"
  ✓ Technical effect: "Inference latency reduced from 120ms to 35ms"
  → Patentability: PASS

Agent (Phase A): Confirming requirements...
  Path: Patent application
  AI project type: Model architecture innovation
  ...

Agent (Phase B): Scanning project...
  Detected entry: train.py → Training class
  Core innovation: Adaptive density control module in gaussian_renderer.py
  Key points extracted: [5 items]

Agent (Phase C1): Generating patent documents...
  C1.1 Prior art search: Found 3 related patents, differentiated
  C1.2 Layout advice: Single application (architecture+training coupled)
  C1.3 Claims: 1 independent (method) + 5 dependent + 1 independent (system) + 1 storage media
  C1.4 Specification: 5 chapters, 3 embodiments
  C1.5 Abstract: 280 characters
  C1.6 Self-check: 92/100 → PASS

Output: outputs/3dgs-adaptive-density/
  ├── patent/
  │   ├── 3dgs-adaptive-density_claims.md
  │   ├── 3dgs-adaptive-density_specification.md
  │   ├── 3dgs-adaptive-density_abstract.md
  │   └── 3dgs-adaptive-density_full.md
```

### Software Copyright Path Example

```
User: 生成这个AI项目的软著登记材料

Agent (Phase B): Auto-detecting project type...
  Entry file: app.py + serve.py → AI Service (Web API)
  Framework: FastAPI + PyTorch
  GPU required: Yes (CUDA 11.8+)

Agent (Phase C2): Generating software copyright materials...
  C2.1 Manual: 12 pages, 8 screenshots, AI-capability description included
  C2.2 Source code: model.py(340 lines) + train.py(280 lines) + inference.py(195 lines) + ...
      Total: 1560 lines → All submitted (< 3000 lines)
  C2.3 Self-check: 88/100 → PASS
```

### Technical Disclosure Path Example

```
User: 把我这篇论文转成技术交底书

Agent (Phase C3): Mapping paper to disclosure...
  Research Problem → Technical Problem ✓
  Contribution → Technical Solution ✓
  Method Modules → Implementation Units ✓
  Algorithm Flow → Implementation Procedure ✓
  Experimental Outcome → Technical Effect ✓
  Ablation Study → Alternative Embodiments ✓
```

## Comparison with Existing Skills

| Feature | ai-ip-skill | Fokkyp/SoftwareCopyright-Skill (3k stars) | patent-disclosure-skill | patent-software-ip (v1.0) |
|---------|:-----------:|:------------------------------------------:|:-----------------------:|:--------------------------:|
| Patent application | Full | -- | -- | Full |
| Software copyright | Full | Full | -- | Full |
| Technical disclosure | Full | -- | Full | -- |
| AI patentability check | Built-in | -- | -- | -- |
| AI claim templates (6 types) | Built-in | -- | -- | -- |
| AI project auto-detection | Built-in | -- | -- | -- |
| AI desensitization rules | Built-in | -- | -- | Partial |
| Paper-to-patent mapping | Built-in | -- | Partial | -- |
| Patent layout advisory | Built-in | -- | -- | -- |
| Confirmation gates | Yes | Yes | -- | -- |
| 100-point quality scoring | Yes | -- | -- | -- |
| Quantitative self-check | Yes | -- | -- | Checklist only |
| Iterative correction | Yes | -- | Yes | Yes |

## Knowledge Base Contents

| Reference File | Sections |
|---------------|----------|
| `ai-patent-special.md` | Patentability 3-factor test / Single vs. divisional filing / Paper-to-patent 6-type mapping / AI figure requirements / 6-type desensitization table / CPC-IPC classification |
| `ai-software-copyright-guide.md` | AI project type decision tree / Per-type manual focus / Source file priority / Code desensitization checklist / AI manual template / 5 common pitfalls |
| `ai-patent-claims-guide.md` | Method+System+Media triple claim principle / 6-type AI claim templates (architecture/training/inference/data/multimodal/agent) / 5-layer dependent claim expansion |

## License

MIT License — see [LICENSE](./LICENSE)

## Author

jaccen — [GitHub](https://github.com/jaccen) | [Awesome-Gaussian-Skills](https://github.com/jaccen/Awesome-Gaussian-Skills)

## Acknowledgments

This skill was designed by analyzing and learning from these excellent projects:

- [Fokkyp/SoftwareCopyright-Skill](https://github.com/Fokkyp/SoftwareCopyright-Skill) — Confirmation gate interaction design
- [patent-disclosure-skill](https://clawhub.ai/) — Prompt molecule architecture + disclosure workflow
- [na57/chinese-copyright-application-skill](https://github.com/na57/chinese-copyright-application-skill) — AI project type detection
- [Earl000333/paperforge](https://github.com/Earl000333/paperforge) — Paper-to-patent mapping methodology
- [hapi-ds/mPAPA](https://github.com/hapi-ds/mPAPA) — Structured multi-step workflow
- [IGTA-Tech/provisional-patent-skills](https://github.com/IGTA-Tech/provisional-patent-skills) — 100-point quality scoring
