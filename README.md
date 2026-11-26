# AI & Geospatial Engineering | Technical Portfolio

**Applied AI • Earth observation • Multimodal systems • Scientific computing**

This portfolio presents selected technical work across several years of applied algorithm development, domain AI and scientific computing. It is organized as an English-language, reviewable index of research and engineering experience, with emphasis on data provenance, reproducible evaluation and responsible deployment.

## Featured work for the GenAI for Good Challenge

Start with [urban data reasoning](01_GenAI_Cities_Challenge/Architecture.md), [building extraction](02_Building_Extraction/Methodology.md), [satellite embeddings](03_Global_Geospatial_AI/README.md) and [land-use monitoring](04_Land_Use_Monitoring/README.md) for work most relevant to sustainable cities. The underlying design experience is transferable to proposed staff-facing municipal GIS workflows; no Skopje deployment or municipal partnership is claimed.

## Project index

### Geospatial & Earth observation

| Project | Status |
| --- | --- |
| [High-resolution building extraction and change monitoring](02_Building_Extraction/Methodology.md) | Internal engineering development and evaluation |
| [Satellite embeddings for road and building mapping](03_Global_Geospatial_AI/README.md) | Local research pilot |
| [AI-assisted land-use status monitoring](04_Land_Use_Monitoring/README.md) | Internal evaluation |
| [Agricultural remote sensing and crop recognition](06_Agricultural_Remote_Sensing/README.md) | Development and controlled experiments |
| [Tobacco plant detection and growth-stage monitoring](07_Tobacco_Plant_Recognition/README.md) | Internal development and validation |
| [Terrain processing and above-ground object filtering](08_Terrain_And_Object_Heights/README.md) | Engineering development |
| [Scale robustness in aerial image segmentation](09_Scale_Robust_Segmentation/README.md) | Controlled research; manuscript development |
| [Tree canopy and rural settlement mapping](10_Tree_Canopy_And_Settlements/README.md) | Research and engineering development |

### Language models & AI engineering

| Project | Status |
| --- | --- |
| [Evidence-aware urban data reasoning](01_GenAI_Cities_Challenge/Architecture.md) | Public competition result; exact solver provenance not independently verified |
| [Domain-specific knowledge retrieval for natural resources](11_Natural_Resources_RAG/README.md) | Applied system development |
| [Multimodal model training and inference engineering](12_Multimodal_AI_Engineering/README.md) | Experimental and engineering work |

### Biomedical & scientific AI

| Project | Status |
| --- | --- |
| [Evidence-aware scientific AI and molecular screening](05_Scientific_AI/README.md) | Computational research |
| [Anatomically structured hand X-ray analysis](13_Bone_Maturity_AI/README.md) | Multi-stage computational research |
| [Pediatric heart-sound analysis](14_Pediatric_Heart_Sound_AI/README.md) | Computational model development and evaluation |
| [Structure-based molecular research and docking](15_Structure_Based_Molecular_Research/README.md) | Computational investigation; experimental validation pending |
| [Radiopharmaceutical chemistry informatics](16_Radiopharmaceutical_Chemistry_AI/README.md) | Exploratory data and modeling research |
| [Mass spectrometry and molecular identification](17_Mass_Spectrometry_Identification/README.md) | Competition-oriented research and local validation |

### Computer vision & applied ML

| Project | Status |
| --- | --- |
| [Monocular vision and distance estimation](18_Monocular_Vision/README.md) | Research and engineering development |
| [Predictive modeling, ranking and recommender systems](19_Predictive_And_Recommender_Systems/README.md) | Earlier applied algorithm work |
| [Food image recognition](20_Food_Recognition/README.md) | Computer vision research |

## Research and engineering trajectory

Earlier work focused on prediction, advertising and recommendation algorithms. Subsequent work expanded into medical-image analysis and anatomically structured AI. From 2024 onward the research emphasis broadened to natural-resource knowledge systems, remote sensing and geospatial intelligence, alongside computational scientific AI. The 2025–2026 case studies document this continuing transition toward evidence-aware multimodal systems. These periods are broad career stages, not exact project start or end dates.

## Reproducible public demonstrations

The examples use synthetic data and newly prepared, standalone code. They do not reproduce private projects or competition submissions.

- [Binary segmentation evaluation](examples/README.md): IoU, precision, recall and explicit exclusion masks.
- [Evidence-aware register example](examples/evidence_register.py): validation of source IDs, planned versus confirmed statuses and reviewable count/area outputs on invented municipal records.

```bash
python3 examples/mask_evaluation.py
python3 examples/evidence_register.py
python3 -m unittest discover -s tests -v
```

## Evidence and release policy

Public case studies are high-level descriptions of work, not claims of sole authorship or releases of employer-owned intellectual property. Internal metrics, code, data, medical records and unpublished patent mechanisms are withheld. No contest questions, answers, source data or solver code are published while the competition is active. Proposed, exploratory and internally evaluated work are explicitly distinguished from independently validated or publicly scored results. The portfolio owner should review project descriptions and attribution before public release.

GitHub: [newledge](https://github.com/newledge)
