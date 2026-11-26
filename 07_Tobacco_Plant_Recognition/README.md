# Tobacco plant detection and growth-stage monitoring

**Area:** Geospatial & Earth observation  
**Status:** Internal development and validation

## Problem

Identify plants and missing or poorly growing plants in aerial or field imagery at different growth stages.

## Technical experience

Explored object detection followed by region-of-interest classification, including seedling-stage detection and mature-stage status recognition. Keypoint localization, class-balanced learning and structured inference outputs were investigated.

```mermaid
flowchart LR
    N0["Growth-stage imagery"] --> N1["Plant candidates"]
    N1["Plant candidates"] --> N2["ROI classification"]
    N2["ROI classification"] --> N3["Status records"]
    N3["Status records"] --> N4["Field review"]
    N4["Field review"]
```

The diagram is a high-level description of the research workflow, not a release of the original implementation.

## Validation and boundaries

Growth stage and acquisition conditions affect transfer. Stage-specific validation and representative field checks are needed; no deployment or crop-yield accuracy is claimed.
