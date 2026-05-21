# AI-Copyright-Skill

**The First AI-Native Intellectual Property Skill for Agent Workflows -- with Direct Word + PPT Output**

An Agent Skill that generates Chinese patent application documents, software copyright registration materials, and technical disclosure reports from AI project code, research papers, and design docs -- with domain-specific rules baked in, and outputs ready-to-use `.docx` + `.pptx` files by default. The patent path includes a built-in technical disclosure intermediate deliverable for handoff to patent agents.

[中文文档](./README_CN.md)

## Why This Skill Exists

Existing patent/copyright skills are all **generic** -- same templates for any domain. AI has unique IP challenges:

- **Patentability**: Is your algorithm even patentable under CNIPA guidelines?
- **Claim drafting**: How to write method+system+storage-medium triple claims for a neural network?
- **Desensitization**: How to replace "A100", "PyTorch", "7B parameters" with patent-safe language?
- **Software copyright**: Which source files to include? How to handle GPU/CUDA requirements?
- **Paper-to-patent mapping**: How to turn ablation studies into dependent claims?
- **Output format**: Can I get a Word file directly instead of Markdown?
- **Internal communication**: How to brief management or patent agents quickly?
- **3D vision / Generative AI / Embodied AI**: Domain-specific claim structures and patentability traps?

This skill answers all of them.

## Features

### Three Output Paths + Direct Word & PPT Output

| Path | Deliverables | Default Format |
|------|-------------|----------------|
| Patent | Disclosure + Claims + Specification + Abstract + Briefing PPT | `.docx` x2 (disclosure + patent) + `.pptx` |
| Software Copyright | Software Manual + Source Code Doc | 2 `.docx` files |
| Technical Disclosure | Full disclosure document | Single `.docx` file |

### 7 AI Domains x 22 Sub-Directions Coverage

| Domain | Sub-Directions | Claim Template |
|--------|---------------|----------------|
| **Perception AI** | 2D CV · 3D Vision & Graphics · Audio/Video · Sensor Fusion | 2.1 Architecture · 2.2 3D Vision |
| **Cognitive & Language** | LLM · Multimodal LLM · RAG · Knowledge Graph | 2.3 Training · 2.4 MLLM · 2.5 RAG |
| **Generative AI** | Diffusion & Controlled Gen · AIGC Watermark · Style Transfer | 2.6 Diffusion |
| **Decision & Interaction** | Agent · Embodied AI · Reinforcement Learning | 2.7 Agent · 2.8 VLA |
| **AI Engineering** | Training/Fine-tuning · Inference Optimization · Data Engineering · Edge/IoT | 2.9 Inference · 2.10 Data |
| **AI Safety & Governance** | Adversarial Defense · Watermark & Traceability · Federated Learning · Alignment | 2.11 Watermark |
| **Industry Applications** | Autonomous Driving · Industry QC · Healthcare · Finance · AI4Science · Digital Content | Domain-adapted |

### AI-Domain Specific Capabilities

- **Patentability Pre-Assessment** (Phase 0): 3-factor test + domain risk levels for 13 high-risk areas
- **15-Type Claim Templates**: Architecture / 3D Vision / Training / MLLM / RAG / Diffusion / Agent / Embodied AI / Inference / Data / Watermark / World Model / SSM / Video Generation / AI-native Application
- **Domain-Specific Dependent Claim Strategies**: 5-layer general + 9 domain-specific expansion tables
- **Patent Layout Advisory**: Single vs. divisional filing; special rules for 3D visions and Embodied AI
- **6+14+4 Desensitization Rules**: 6 general + 14 industry-specific + 4 3DGS/NeRF-specific replacements
- **AI Project Auto-Detection**: Decision tree covering 15+ project types + 9 industry categories
- **Source Code Priority**: 16-level priority with domain-specific mandatory files (3D vision, generative AI, embodied AI, RAG)
- **Paper-to-Patent Mapping**: 6-type general + 10 domain-specific mapping rules
- **5 Software Manual Templates**: General / 3D Vision / Generative AI / Embodied AI / World Model
- **13-Type AI System Figure Requirements**: From DL inference to AI watermark systems
- **6-Group CPC/IPC Classification**: 30+ codes across AI core / perception / language / decision / safety / industry
- **100-Point Quality Scoring**: Quantitative self-check for each output path
- **Technical Disclosure as Intermediate** (C1.3): Auto-generated from technical key points + search results
- **Direct Word (.docx) Output** (Phase F): Professional patent document formatting with docx-js
- **Briefing PPT (.pptx) Output** (Phase G): 5-8 slide executive briefing with AI domain tag
- **Multi-Source Prior Art Search** (Phase C1.1): CNIPA crawler + Google Patents API + arXiv + WebSearch fallback
- **Structured Prior Art Comparison** (Phase C1.1b): Feature comparison table with risk grading (Low/Medium/High)
- **Patent Figure Auto-Generation** (Phase H): Mermaid/Graphviz → PNG, 9 AI-domain-specific diagram types
- **Full OA Response Workflow** (Phase E.3): 6-step office action response with A33 compliance check
- **Iteration Traceability**: Timestamped deliverables + revision dialog log with diff tracking
- **EPO/USPTO Differentiated Drafting** (§14): 35 USC 101/102/103, Art. 52/56/83, multi-office claim formatting

### User Experience

- **Confirmation Gates**: Pause at each phase boundary for user review
- **Iterative Correction**: Modify specific sections without re-running the entire pipeline
- **Quantitative Self-Check**: Auto-score and auto-fix when score < 80
- **Slash Commands**: `/ai-copyright` or `/AI知产`
- **Format Options**: `docx` (default) / `md` / `both`
- **PPT Option**: Auto-generated for patent path; `--ppt` flag for other paths

## Workflow

```
Phase 0  Patentability Pre-Assessment + Domain Risk Detection (patent path only)
Phase A  Requirement Diagnosis -> path selection + domain attribution + risk level
Phase B  Project Analysis -> auto-detect AI project type (15+ types) + extract key points
Phase C  Generation (branch by path)
  ├── C1  Patent (search -> layout -> disclosure -> claims (15 templates) -> specification -> abstract -> self-check)
  ├── C2  Software Copyright (manual (5 templates) -> source code doc -> self-check)
  └── C3  Technical Disclosure (general + domain-specific mapping -> drafting -> self-check)
Phase D  Confirmation Gate (user review at each phase end)
Phase E  Iterative Correction (targeted fix, no full re-run)
Phase F  Word Document Output (automatic, docx-js workflow)
Phase G  Briefing PPT Output (patent path default; others optional)
Phase H  Patent Figure Generation (Mermaid/Graphviz → PNG, auto-embedded in specification)
```

## File Structure

```
AI-Copyright-Skill/
├── SKILL.md                              # Main skill file (agent entry point)
├── README.md                             # This file
├── README_CN.md                          # Chinese documentation
├── LICENSE                               # MIT License
├── tools/                                # Prior art search scripts
│   ├── cnipa_search.py                   # CNIPA patent search (Playwright)
│   └── google_patents_search.py          # Google Patents API search
├── examples/                             # Example cases
│   └── example-3dgs-denoise/             # 3DGS denoising example
└── references/                           # Domain knowledge base
    ├── ai-patent-special.md              # Patentability + domain risks + layout + mapping + desensitization + CPC + OA + EPO/USPTO (14 sections)
    ├── ai-software-copyright-guide.md    # Project detection (15+ types) + source priority (16 levels) + 5 manual templates + 14 pitfalls
    ├── ai-patent-claims-guide.md         # 15 claim templates + 5-layer + 9 domain-dependent claim expansion
    └── ai-prior-art-search.md            # Multi-source prior art search + structured comparison + risk grading
```

## Installation

### TeleAI Super Agent / OpenClaw

Copy the entire `AI-Copyright-Skill/` directory to your skills folder:

**macOS / Linux:**

```bash
# TeleAI Super Agent
cp -r AI-Copyright-Skill/ ~/.config/teleai-super-agent/skills/AI-Copyright-Skill/

# OpenClaw / Claude Code
cp -r AI-Copyright-Skill/ .claude/skills/AI-Copyright-Skill/
```

**Windows (PowerShell):**

```powershell
# TeleAI Super Agent
Copy-Item -Recurse AI-Copyright-Skill/ "$env:USERPROFILE\.config\teleai-super-agent\skills\AI-Copyright-Skill"

# OpenClaw / Claude Code
Copy-Item -Recurse AI-Copyright-Skill/ .\.claude\skills\AI-Copyright-Skill
```

### ClawHub

```bash
# Install to TeleAI Super Agent skills directory
clawhub install ai-copyright-skill --dir ~/.config/teleai-super-agent/skills

# Or install to current directory (then copy manually)
clawhub install ai-copyright-skill
```

> **Note:** The ClawHub slug is `ai-copyright-skill` (lowercase). If you haven't installed `clawhub` CLI yet, see [ClawHub](https://clawhub.ai/) for setup instructions.

## Usage

### Quick Start

Once installed, simply mention patent/copyright-related keywords in your agent chat:

- "Help me write a patent for my 3DGS reconstruction method"
- "Generate software copyright materials for this embodied AI project"
- "Convert my diffusion model paper into a technical disclosure document"
- `/ai-copyright` or `/AI知产`

### Patent Path Example (with Word + PPT output)

```
User: 帮我基于我的3DGS项目写一份发明专利申请

Agent (Phase 0): Running patentability assessment...
  ✓ Technical problem: "Real-time rendering bottleneck in large-scale 3D scene reconstruction"
  ✓ Technical means: "Gaussian splatting with adaptive density control"
  ✓ Technical effect: "Inference latency reduced from 120ms to 35ms"
  ⚠ Domain risk: MEDIUM (3D vision - ensure rendering formula in claims)
  → Patentability: PASS (with domain-specific drafting rules applied)

Agent (Phase B): Auto-detecting project type...
  Entry file: render.py + gaussian.py → 3D Vision (3DGS)
  Domain: Perception AI > 3D Vision & Graphics
  Claim template: 2.2 (3D Vision)

Agent (Phase C1): Generating patent documents...
  C1.1 Prior art search: Found 3 related patents, differentiated
  C1.2 Layout advice: Single application (reconstruction+rendering coupled)
  C1.3 Technical disclosure: Generated (for patent agent handoff)
  C1.4 Claims: Independent (method, 3D vision 4-stage) + 5 dependent + Independent (system) + storage media
  C1.5 Specification: 5 chapters, 3 embodiments, 3DGS-specific desensitization applied
  C1.6 Abstract: 280 characters
  C1.7 Self-check: 92/100 → PASS

Agent (Phase F): Generating Word documents...
  → 3dgs-adaptive-density_disclosure.docx (technical disclosure)
  → 3dgs-adaptive-density.docx (cover + claims + specification + abstract)

Agent (Phase G): Generating briefing PPT...
  → 3dgs-adaptive-density_简介.pptx (8 slides, domain: Perception AI)

Output: outputs/3dgs-adaptive-density/
  └── patent/
      ├── 3dgs-adaptive-density_disclosure.docx  ← For patent agent
      ├── 3dgs-adaptive-density.docx             ← Formal application
      ├── 3dgs-adaptive-density_简介.pptx        ← Management briefing
      ├── 3dgs-adaptive-density_claims.md
      ├── 3dgs-adaptive-density_specification.md
      └── 3dgs-adaptive-density_abstract.md
```

### Software Copyright Path Example

```
User: 生成这个AI项目的软著登记材料

Agent (Phase B): Auto-detecting project type...
  Entry file: app.py + serve.py → AI Service (Web API)
  Framework: FastAPI + PyTorch
  GPU required: Yes (CUDA 11.8+)
  Manual template: 3.1 General type

Agent (Phase C2): Generating software copyright materials...
  C2.1 Manual: 12 pages, 8 screenshots, AI-capability description included
  C2.2 Source code: model.py(340 lines) + train.py(280 lines) + ...
      Total: 1560 lines → All submitted (< 3000 lines)
  C2.3 Self-check: 88/100 → PASS

Agent (Phase F): Generating Word documents...
  → xxx_软件说明书.docx
  → xxx_源代码文档.docx
```

### Technical Disclosure Path Example

```
User: 把我这篇论文转成技术交底书

Agent (Phase B): Detecting domain...
  Paper topic: Diffusion model with ControlNet
  Domain: Generative AI > Diffusion & Controlled Generation
  Mapping: Domain-specific (noise schedule → claim step, condition injection → sub-claim)

Agent (Phase C3 → Phase F): Mapping paper→disclosure→Word...
  Research Problem → Technical Problem ✓
  Contribution → Technical Solution ✓
  Ablation Study → Alternative Embodiments ✓
  Diffusion-specific: Noise schedule → dependent claim, ControlNet injection → dependent claim ✓
  → xxx_disclosure.docx generated
```

## Comparison with Existing Skills

| Feature | AI-Copyright-Skill v3.0 | Fokkyp/SoftwareCopyright-Skill | patent-disclosure-skill | patent-software-ip (v1.0) |
|---------|:----------------------:|:------------------------------:|:-----------------------:|:-------------------------:|
| Patent application | Full | -- | -- | Full |
| Software copyright | Full | Full | -- | Full |
| Technical disclosure | Full | -- | Full | -- |
| **7 AI domains x 22 sub-directions** | **Yes** | -- | -- | -- |
| **15 claim templates** | **Yes** | -- | -- | -- |
| **Domain-dependent claim strategies** | **Yes (9 domains)** | -- | -- | -- |
| **Domain risk assessment** | **Yes (13 risk areas)** | -- | -- | -- |
| **13-type figure requirements** | **Yes** | -- | -- | -- |
| **5 software manual templates** | **Yes** | -- | -- | -- |
| Disclosure as patent intermediate | Yes | -- | -- | -- |
| Direct Word (.docx) output | Yes | -- | -- | -- |
| Briefing PPT (.pptx) output | Yes | -- | -- | -- |
| AI patentability check | Built-in | -- | -- | -- |
| AI project auto-detection | Built-in (15+ types) | -- | -- | -- |
| AI desensitization rules | 6+14+4 rules | -- | -- | Partial |
| Paper-to-patent mapping | 6-type + 10 domain | -- | Partial | -- |
| Patent layout advisory | Built-in | -- | -- | -- |
| Confirmation gates | Yes | Yes | -- | -- |
| 100-point quality scoring | Yes | -- | -- | -- |
| Quantitative self-check | Yes | -- | -- | Checklist only |
| Iterative correction | Yes | -- | Yes | Yes |
| **Multi-source prior art search** | **CNIPA+Google Patents+arXiv** | -- | **CNIPA only** | -- |
| **Structured prior art comparison** | **Feature table + risk grading** | -- | -- | -- |
| **Patent figure auto-generation** | **Mermaid/Graphviz → PNG** | -- | **Mermaid** | -- |
| **Full OA response workflow** | **6-step + A33 check** | -- | -- | -- |
| **EPO/USPTO drafting** | **§14 differential rules** | -- | -- | -- |
| **Iteration traceability** | **Timestamped + dialog log** | -- | **Timestamped** | -- |

## Knowledge Base Contents

| Reference File | Sections |
|---------------|----------|
| `ai-patent-special.md` | §1 Patentability + 13 domain risks / §2 Layout / §3 Mapping / §4 Figures / §5 Desensitization / §6 CPC / §7 Quick reference / §8 2026 guidelines / §9 Innovation mining / §10 OA response / §11 Domain algorithms / §12 Terminology / §13 PCT / §14 EPO/USPTO |
| `ai-software-copyright-guide.md` | §1 15+ type decision tree + 9 industry detection / §2 16-level source priority / §3 5 manual templates / §4 14 pitfalls |
| `ai-patent-claims-guide.md` | §1 Triple claim / §2 15 claim templates (incl. world-model/SSM/video/AI-native) / §3 5-layer + 9 domain-dependent expansion |
| `ai-prior-art-search.md` | §1 Multi-source search (CNIPA/Google/arXiv) / §2 Structured comparison + risk grading / §3 Report format |

## FAQ & Troubleshooting

### PPT generation fails with `Cannot find module 'pptxgenjs'`

PptxGenJS is required for Phase G (briefing PPT). The skill auto-installs it in the working directory, but if network or permission issues prevent this:

```bash
# Manual install in the skill's temp directory
cd .temp/{case-name}/ && npm install pptxgenjs

# Or install globally
npm install -g pptxgenjs
```

### PPT generation fails with `TypeError: Cannot create property 'options' on string`

This is a PptxGenJS API pitfall. When using `addText` with bullet lists, you **must pass an array of objects**, not an array of strings:

```javascript
// Wrong - will throw TypeError
slide.addText(["item1", "item2"], { bullet: true, ... });

// Correct - array of text objects
slide.addText([{ text: "item1\n" }, { text: "item2" }], { bullet: true, ... });
```

### Word document output fails with `Cannot find module 'docx'`

The `docx` npm package is required for Phase F (Word output). It is usually pre-installed in TeleAI Super Agent. If missing:

```bash
npm install docx
```

### ClawHub install fails with `skill not found`

The ClawHub slug is **lowercase**: `ai-copyright-skill`. Using `AI-Copyright-Skill` (mixed case) will not match.

```bash
# Correct
clawhub install ai-copyright-skill

# Wrong
clawhub install AI-Copyright-Skill
```

### Installed skill but agent doesn't recognize it

Make sure the skill folder is in the correct directory and the folder name matches exactly:

| Agent | Skills Directory |
|-------|------------------|
| TeleAI Super Agent | `~/.config/teleai-super-agent/skills/AI-Copyright-Skill/` (macOS/Linux) |
| | `%USERPROFILE%\.config\teleai-super-agent\skills\AI-Copyright-Skill\` (Windows) |
| OpenClaw / Claude Code | `.claude/skills/AI-Copyright-Skill/` |

Verify the skill is loaded by checking if `SKILL.md` exists inside the folder.

### Self-check score is below 80

The skill auto-fixes when the score is 60-80. If it stays below 60 after retries, the most common causes are:

- **Insufficient technical detail**: Add more quantified comparison data (e.g., "latency reduced from 120ms to 35ms")
- **Missing dependent claims**: Ensure the independent claim is followed by at least 5 dependent claims
- **Incomplete desensitization**: Check for brand names (A100, PyTorch) or exact parameter values (7B, 1.5B)

### Chinese characters display as boxes in generated PPT

The default font is Microsoft YaHei (微软雅黑). If it is not installed on your system (common on non-Chinese Windows or some Linux distros), install it or switch to a compatible CJK font:

```javascript
// Replace in the PptxGenJS script
fontFace: "Noto Sans CJK SC"  // or "Source Han Sans CN", "SimHei"
```

## Version History

### v3.0.0 (2026-05)

- Added **Phase H: Patent figure auto-generation** (Mermaid/Graphviz → PNG, 9 AI-domain diagram types)
- Added **multi-source prior art search** (CNIPA crawler + Google Patents API + arXiv + fallback)
- Added **structured prior art comparison** with feature table and Low/Medium/High risk grading
- Added **full OA response workflow** (6-step: parse → compare → strategy → A33 check → argument → replacement pages)
- Added **iteration traceability** (timestamped deliverables + revision dialog log)
- Added **EPO/USPTO differentiated drafting rules** (§14: 35 USC 101/102/103, Art. 52/56/83)
- Added `tools/` directory with CNIPA search and Google Patents search scripts
- Added `examples/` with 3DGS denoising example case
- Added `references/ai-prior-art-search.md` knowledge base
- Expanded claim templates from 11 to **15** (added: World Model, SSM, Video Generation, AI-native Application)
- Expanded domain risks from 8 to **13** areas
- Expanded software manual templates from 4 to **5** (added: World Model/Simulation)
- Expanded source code priority from 12 to **16 levels**
- Synchronized README numbers with SKILL.md across all metrics

### v2.0.0 (2026-05)

- Expanded from 6 claim types to **11 claim templates** covering 7 AI domains x 22 sub-directions
- Added **domain risk assessment** with 8 high/medium-risk areas and drafting countermeasures
- Added 5 new claim templates: 3D Vision, Diffusion/Generative AI, RAG, Embodied AI (VLA), AI Watermark
- Added **5 domain-specific dependent claim expansion strategies**
- Expanded desensitization from 6 to **6+14+4 rules** (general + industry + 3D-specific)
- Expanded project detection from 6 to **11 types** + **6 industry categories**
- Added **4 software manual templates** (general/3D-vision/generative-AI/embodied-AI)
- Expanded figure requirements from 5 to **13 AI system types**
- Expanded CPC/IPC from 6 to **6 groups / 30+ codes**
- Added §7 domain quick reference table to ai-patent-special.md

### v1.2.0

- Initial public release with 6 claim templates and 3 patent paths

## License

MIT License -- see [LICENSE](./LICENSE)

## Author

jaccen -- [GitHub](https://github.com/jaccen) | [AI-Copyright-Skill](https://github.com/jaccen/AI-Copyright-Skill) | [Awesome-Gaussian-Skills](https://github.com/jaccen/Awesome-Gaussian-Skills)

## Acknowledgments

This skill was designed by analyzing and learning from these excellent projects:

- [Fokkyp/SoftwareCopyright-Skill](https://github.com/Fokkyp/SoftwareCopyright-Skill) -- Confirmation gate interaction design
- [patent-disclosure-skill](https://clawhub.ai/) -- Prompt molecule architecture + disclosure workflow
- [na57/chinese-copyright-application-skill](https://github.com/na57/chinese-copyright-application-skill) -- AI project type detection
- [Earl000333/paperforge](https://github.com/Earl000333/paperforge) -- Paper-to-patent mapping methodology
- [hapi-ds/mPAPA](https://github.com/hapi-ds/mPAPA) -- Structured multi-step workflow
- [IGTA-Tech/provisional-patent-skills](https://github.com/IGTA-Tech/provisional-patent-skills) -- 100-point quality scoring
- [handsomestWei/patent-disclosure-skill](https://github.com/handsomestWei/patent-disclosure-skill) -- CNIPA crawler + Mermaid figure generation + iteration traceability
- [yycyyv/M-Cube](https://github.com/yycyyv/M-Cube) -- OA response workflow + multimodal figure analysis + multi-verification
- [RobThePCGuy/Claude-Patent-Creator](https://github.com/RobThePCGuy/Claude-Patent-Creator) -- Multi-source patent search + compliance check architecture
- [kimlawtech/korean-patent-diagram](https://github.com/kimlawtech/korean-patent-diagram) -- Patent diagram auto-generation from specification