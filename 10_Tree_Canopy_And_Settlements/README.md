# Tree canopy and rural settlement mapping

**Area:** Geospatial & Earth observation  
**Status:** Research and engineering development

## Problem

Individual tree crowns and rural built-up parcels require spatially coherent boundaries for inventory and monitoring.

## Technical experience

Explored high-resolution image segmentation, canopy-aware recognition, parcel mapping, boundary quality checks and comparison with reference vector data. Foundation-model and task-specific segmentation approaches were investigated in related workflows.

```mermaid
flowchart LR
    N0["Aerial imagery"] --> N1["Segmentation candidates"]
    N1["Segmentation candidates"] --> N2["Boundary review"]
    N2["Boundary review"] --> N3["Vector features"]
    N3["Vector features"] --> N4["Inventory support"]
    N4["Inventory support"]
```

The diagram is a high-level description of the research workflow, not a release of the original implementation.

## Validation and boundaries

Canopy overlap and ambiguous property boundaries require appropriate labels and field or GIS review. Individual asset identity cannot be inferred from a canopy mask alone.
