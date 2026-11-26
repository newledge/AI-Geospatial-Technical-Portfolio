# Synthetic demonstration: mask evaluation with an exclusion region

This newly authored, standalone example illustrates one small geospatial evaluation primitive. A pair of 4 × 4 binary grids represents hypothetical reference and predicted building masks. A third grid marks excluded cells. All grids are artificial; no aerial imagery, georeferenced location, employer data or competition data is used.

The evaluator computes true positives, false positives and false negatives only on included cells, then derives IoU, precision and recall. Undefined ratios are reported as `null` rather than an invented score. It also reports included and excluded cell counts and, when supplied, areas based on an explicitly specified constant pixel area.

```bash
python3 examples/mask_evaluation.py
python3 -m unittest discover -s tests -v
```

The area result assumes that the caller has established a valid constant cell area in square metres. Real-world GIS processing additionally requires alignment, nodata handling and an appropriate coordinate reference system. This script does not perform georeferencing or reprojection.

The example is not an existing production model or the Zindi solution. See [the building extraction case study](../02_Building_Extraction/Methodology.md) for the broader research context.
