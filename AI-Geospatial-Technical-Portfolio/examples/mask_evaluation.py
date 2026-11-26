"""Synthetic binary mask evaluation; Python standard library only."""
import json
import math


def evaluate(reference, prediction, excluded=None, pixel_area_m2=None):
    """Evaluate aligned binary grids; excluded=True removes a cell from scoring."""
    if not reference or not reference[0]:
        raise ValueError("Reference must be non-empty")
    h, w = len(reference), len(reference[0])
    if excluded is None:
        excluded = [[False] * w for _ in range(h)]
    for name, grid in (("reference", reference), ("prediction", prediction), ("excluded", excluded)):
        if len(grid) != h or any(len(row) != w for row in grid):
            raise ValueError(f"{name} shape mismatch")
        if any(type(x) not in (bool, int) or x not in (0, 1) for row in grid for x in row):
            raise ValueError(f"{name} must be binary")
    if pixel_area_m2 is not None and (isinstance(pixel_area_m2, bool) or not isinstance(pixel_area_m2, (int, float)) or not math.isfinite(pixel_area_m2) or pixel_area_m2 <= 0):
        raise ValueError("Pixel area must be finite and positive")
    tp = fp = fn = tn = skipped = 0
    for y in range(h):
        for x in range(w):
            if excluded[y][x]:
                skipped += 1
            elif reference[y][x] and prediction[y][x]:
                tp += 1
            elif prediction[y][x]:
                fp += 1
            elif reference[y][x]:
                fn += 1
            else:
                tn += 1
    def ratio(n, d):
        return n / d if d else None
    result = {"included_cells": h*w-skipped, "excluded_cells": skipped,
              "tp": tp, "fp": fp, "fn": fn, "tn": tn,
              "iou": ratio(tp, tp+fp+fn), "precision": ratio(tp, tp+fp),
              "recall": ratio(tp, tp+fn)}
    if pixel_area_m2 is not None:
        result["reference_positive_area_m2"] = (tp+fn)*pixel_area_m2
        result["prediction_positive_area_m2"] = (tp+fp)*pixel_area_m2
    return result


if __name__ == "__main__":
    reference = [[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]]
    prediction = [[1,0,1,0],[1,1,0,0],[0,0,1,0],[0,0,1,1]]
    excluded = [[0,0,1,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    print(json.dumps({"dataset": "synthetic", **evaluate(reference, prediction, excluded, 0.25)}, indent=2))
