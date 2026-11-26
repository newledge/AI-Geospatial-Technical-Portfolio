# Agricultural remote sensing and crop recognition

**Area:** Geospatial & Earth observation  
**Status:** Development and controlled experiments

## Problem

Identify crop types and agricultural land from aerial imagery, while accounting for scale, mixed land cover and uneven labels.

## Technical experience

Work has included multi-class crop mapping, crop-specific training sets, image segmentation and cross-area model assessment. Crop predictions are aligned with geographic reference layers rather than treated as independent image labels. Separate class-level performance from overall averages.

```mermaid
flowchart LR
    N0["Imagery and labels"] --> N1["Spatial alignment"]
    N1["Spatial alignment"] --> N2["Crop model"]
    N2["Crop model"] --> N3["Class-wise evaluation"]
    N3["Class-wise evaluation"] --> N4["GIS outputs"]
    N4["GIS outputs"]
```

The diagram is a high-level description of the research workflow, not a release of the original implementation.

## Validation and boundaries

Image resolution and season change the apparent crop pattern; label completeness and geographic separation are essential to interpreting validation. A national-scale independently validated crop map is not claimed.
