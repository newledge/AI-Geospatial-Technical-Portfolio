"""Synthetic evidence-register demonstration, not a municipal or contest solver."""
import json
from decimal import Decimal, InvalidOperation

STATUSES = {"planned", "approved", "field_confirmed"}

def summarize(records, allowed_sources):
    """Validate provenance and distinguish plans from field-confirmed assets."""
    seen = set()
    buckets = {s: {"count": 0, "area_m2": Decimal("0"), "evidence": []} for s in sorted(STATUSES)}
    unresolved = []
    for row in records:
        asset = row.get("asset_id")
        if not isinstance(asset, str) or not asset.strip() or asset in seen:
            raise ValueError("missing or duplicate asset identifier")
        seen.add(asset)
        if row.get("source_id") not in allowed_sources or not row.get("locator"):
            unresolved.append({"asset_id": asset, "reason": "missing or unauthorized evidence"})
            continue
        status = row.get("status")
        try:
            area = Decimal(str(row.get("area_m2")))
            valid_area = area.is_finite() and area >= 0
        except (InvalidOperation, ValueError):
            valid_area = False
        if status not in STATUSES or not valid_area:
            unresolved.append({"asset_id": asset, "reason": "invalid status or area"})
            continue
        b = buckets[status]
        b["count"] += 1
        b["area_m2"] += area
        b["evidence"].append({"source_id": row["source_id"], "locator": row["locator"], "asset_id": asset})
    for b in buckets.values():
        b["area_m2"] = str(b["area_m2"])
    return {"by_status": buckets, "unresolved": unresolved}

if __name__ == "__main__":
    sample = [
        {"asset_id": "demo-1", "status": "planned", "area_m2": "12.5", "source_id": "synthetic-A", "locator": "row 1"},
        {"asset_id": "demo-2", "status": "field_confirmed", "area_m2": "8", "source_id": "synthetic-A", "locator": "row 2"},
        {"asset_id": "demo-3", "status": "approved", "area_m2": "10", "source_id": "unknown", "locator": "row 3"},
    ]
    print(json.dumps({"dataset": "synthetic", **summarize(sample, {"synthetic-A"})}, indent=2))
