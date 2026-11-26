# Pediatric heart-sound analysis

**Area:** Biomedical & scientific AI  
**Status:** Computational model development and evaluation

## Problem

Heart-sound recordings vary by auscultation site, noise and duration; patient-level assessment requires combining multiple signal segments without data leakage.

## Technical experience

Research explored acoustic quality assessment, cardiac cycle extraction, time-window representations, encoder training and patient-level fusion. Patient-group splitting and separate handling of low-quality signals were important evaluation controls.

```mermaid
flowchart LR
    N0["Audio recordings"] --> N1["Quality assessment"]
    N1["Quality assessment"] --> N2["Cycle and window features"]
    N2["Cycle and window features"] --> N3["Patient-level aggregation"]
    N3["Patient-level aggregation"] --> N4["Research validation"]
    N4["Research validation"]
```

The diagram is a high-level description of the research workflow, not a release of the original implementation.

## Validation and boundaries

Internal model evaluations do not establish clinical screening validity. Representative prospective cohorts, device and site transfer assessment and clinician review are necessary; no medical advice or patient records are provided.
