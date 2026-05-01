"""
Apply approved C1-contamination deletion list to B2 vocabulary.
Issue #146 — B2-vocab-c1-contamination-cleanup

Dispositions from .planning/reports/B2-vocab-c1-deletion-list-2026-04-27.md:
- DELETE 27 entries from B2 (table rows are canonical; summary count of 26 has an off-by-one)
- DEMOTE 4 entries from B2 to C1 (new C1 ids 1526-1529)
- KEEP-WITH-TAG 4 entries (no-op — leave untouched)
"""

import json
import sys
from pathlib import Path

WORKTREE = Path(__file__).parent
B2_PATH = WORKTREE / "apps/mobile/src/data/vocabulary/B2_vocabulary.json"
C1_PATH = WORKTREE / "apps/mobile/src/data/vocabulary/C1_vocabulary.json"

# IDs to DELETE from B2
DELETE_IDS = {
    # Research methodology (8)
    745, 746, 747, 750, 751, 752, 753, 754,
    # Evidence-based medicine (6)
    3452, 3453, 3454, 3455, 3456, 3457,
    # Software architecture (4)
    4004, 4005, 4007, 4008,
    # Management consulting (2)
    3590, 4012,
    # Education research (7 — table rows are canonical)
    3425, 3426, 3427, 3428, 3429, 3587, 3588,
}

# IDs to DEMOTE from B2 → C1
DEMOTE_IDS = {741, 3449, 4014, 713}

# IDs to KEEP-WITH-TAG (no-op, just verified)
KEEP_IDS = {526, 742, 744, 740}


def main():
    print(f"Reading B2: {B2_PATH}")
    with open(B2_PATH, encoding="utf-8") as f:
        b2 = json.load(f)

    print(f"Reading C1: {C1_PATH}")
    with open(C1_PATH, encoding="utf-8") as f:
        c1 = json.load(f)

    b2_before = len(b2)
    c1_before = len(c1)
    c1_max_id = max(e["id"] for e in c1)

    print(f"B2 before: {b2_before}")
    print(f"C1 before: {c1_before}, max id: {c1_max_id}")

    # Validate all target IDs exist in B2
    b2_by_id = {e["id"]: e for e in b2}
    all_target = DELETE_IDS | DEMOTE_IDS | KEEP_IDS
    missing = [i for i in all_target if i not in b2_by_id]
    if missing:
        print(f"ERROR: IDs not found in B2: {sorted(missing)}", file=sys.stderr)
        sys.exit(1)

    # Validate no overlap between DELETE and DEMOTE
    overlap = DELETE_IDS & DEMOTE_IDS
    if overlap:
        print(f"ERROR: IDs in both DELETE and DEMOTE: {overlap}", file=sys.stderr)
        sys.exit(1)

    # Extract demoted entries (preserve all fields, change level)
    demoted_entries = []
    demote_ordered = [713, 741, 3449, 4014]  # consistent ordering for new IDs
    for orig_id in demote_ordered:
        entry = dict(b2_by_id[orig_id])
        entry["level"] = "C1"
        demoted_entries.append(entry)

    # Filter B2: remove DELETE + DEMOTE ids
    remove_ids = DELETE_IDS | DEMOTE_IDS
    b2_new = [e for e in b2 if e["id"] not in remove_ids]

    b2_after = len(b2_new)
    deleted_count = b2_before - b2_after - len(DEMOTE_IDS)
    print(f"\nB2 after: {b2_after}")
    print(f"  Deleted: {deleted_count}")
    print(f"  Demoted: {len(DEMOTE_IDS)}")
    print(f"  Total removed from B2: {b2_before - b2_after}")

    # Verify KEEP-WITH-TAG entries are still in B2
    b2_new_by_id = {e["id"]: e for e in b2_new}
    for kid in KEEP_IDS:
        assert kid in b2_new_by_id, f"KEEP-WITH-TAG id {kid} missing from B2 after filter!"
    print(f"  KEEP-WITH-TAG ({len(KEEP_IDS)} entries): all present in B2 ✓")

    # Assign new C1 IDs starting from c1_max_id + 1
    new_c1_start = c1_max_id + 1
    for i, entry in enumerate(demoted_entries):
        entry["id"] = new_c1_start + i
        print(f"  Demoted: B2 id was tracked → C1 id {entry['id']} | {entry['german']}")

    # Append demoted entries to C1
    c1_new = c1 + demoted_entries
    c1_after = len(c1_new)
    print(f"\nC1 after: {c1_after} (added {c1_after - c1_before})")

    # Write B2
    print(f"\nWriting B2...")
    with open(B2_PATH, "w", encoding="utf-8") as f:
        json.dump(b2_new, f, ensure_ascii=False, indent=2)

    # Write C1
    print(f"Writing C1...")
    with open(C1_PATH, "w", encoding="utf-8") as f:
        json.dump(c1_new, f, ensure_ascii=False, indent=2)

    # Print sample of demoted entries in their new C1 form
    print("\n=== Sample of demoted entries (new C1 form) ===")
    for entry in demoted_entries:
        print(f"  id={entry['id']} level={entry['level']} german={entry['german']} topic={entry['topic']}")

    print("\nDone.")
    return b2_after, c1_after, deleted_count


if __name__ == "__main__":
    main()
