# Terrain processing and above-ground object filtering

**Area:** Geospatial & Earth observation  
**Status:** Engineering development

## Problem

Above-ground moving objects can introduce unwanted elevations into a digital surface model used for terrain or urban analysis.

## Technical experience

Work combined image-based object recognition with spatial alignment to elevation data and localized height correction. The workflow distinguishes objects to preserve from objects selected for review or removal and checks alignment before modifying elevation values.

```mermaid
flowchart LR
    N0["Imagery and surface model"] --> N1["Object candidates"]
    N1["Object candidates"] --> N2["Spatial alignment"]
    N2["Spatial alignment"] --> N3["Height correction"]
    N3["Height correction"] --> N4["Terrain quality review"]
    N4["Terrain quality review"]
```

The diagram is a high-level description of the research workflow, not a release of the original implementation.

## Validation and boundaries

Correcting a surface model is not equivalent to recovering independently measured bare-earth elevation. Validation requires reference terrain, vertical datum and no-data checks.
