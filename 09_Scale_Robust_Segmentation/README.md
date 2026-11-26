# Scale robustness in aerial image segmentation

**Area:** Geospatial & Earth observation  
**Status:** Controlled research; manuscript development

## Problem

Changing image scale can alter segmentation performance even when the underlying geographic scene has not changed.

## Technical experience

Investigated the relationship between scale-dependent input distributions and normalization statistics. Controlled comparisons separated frozen-weight inference interventions from model retraining. The research considers scale-aware normalization and matched preprocessing as diagnostic tools.

```mermaid
flowchart LR
    N0["Same scene at different scales"] --> N1["Frozen model"]
    N1["Frozen model"] --> N2["Normalization intervention"]
    N2["Normalization intervention"] --> N3["Matched evaluation"]
    N3["Matched evaluation"] --> N4["Transfer checks"]
    N4["Transfer checks"]
```

The diagram is a high-level description of the research workflow, not a release of the original implementation.

## Validation and boundaries

Development-set results do not establish independent geographic generalization. External baselines and held-out evaluation remain necessary; manuscript and unpublished experiment details are excluded.
