#!/usr/bin/env python3
"""
Consolidate C1 vocabulary bundles 2-6 into a single file.

Main already has IDs 1-230 (Bundle 1, from PR #139).
Each bundle worktree authored entries independently against an empty array,
so sequential merging would cascade conflicts. This script reads each bundle
and writes a single merge-clean file.

Bundle 4/5 collision: Bundle 4 overflowed its range and authored IDs 1051-1055,
which collide with Bundle 5's start (1051). Resolution: Bundle 4's last 5 entries
are renumbered to 1521-1525 and appended at the tail.
"""

import json
import sys
from pathlib import Path

REPO_ROOT = Path("/Users/kiran.kumar/kk/worspaces/personal/fastrack-deutsch")
WORKTREES = REPO_ROOT / ".worktrees"

BUNDLE_PATHS = {
    "bundle-2": WORKTREES / "content-c1-vocab-bundle-2-wirtschaft-recht" / "apps/mobile/src/data/vocabulary/C1_vocabulary.json",
    "bundle-3": WORKTREES / "content-c1-vocab-bundle-3-wissenschaft-bildung" / "apps/mobile/src/data/vocabulary/C1_vocabulary.json",
    "bundle-4": WORKTREES / "content-c1-vocab-bundle-4-medien-politik" / "apps/mobile/src/data/vocabulary/C1_vocabulary.json",
    "bundle-5": WORKTREES / "content-c1-vocab-bundle-5-kultur-philosophie" / "apps/mobile/src/data/vocabulary/C1_vocabulary.json",
    "bundle-6": WORKTREES / "content-c1-vocab-bundle-6-fvg-abstracta" / "apps/mobile/src/data/vocabulary/C1_vocabulary.json",
}

MAIN_VOCAB = REPO_ROOT / "apps/mobile/src/data/vocabulary/C1_vocabulary.json"
OUTPUT = Path("/Users/kiran.kumar/kk/worspaces/personal/fastrack-deutsch/.worktrees/content-c1-vocab-consolidation") / "apps/mobile/src/data/vocabulary/C1_vocabulary.json"


def load(path: Path) -> list:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def main():
    # Load existing main entries (IDs 1-230)
    main_entries = load(MAIN_VOCAB)
    print(f"Main (IDs 1-230):      {len(main_entries)} entries")

    # Load each bundle — each file contains ALL entries (1 through bundle-max)
    # because each branch authored the file from scratch. We only want the NEW
    # entries relative to main (i.e., entries with IDs > 230 for bundle-2,
    # IDs > 480 for bundle-3, etc.).
    # Actually each bundle only wrote its own range; verify by checking IDs.

    b2_all = load(BUNDLE_PATHS["bundle-2"])
    b3_all = load(BUNDLE_PATHS["bundle-3"])
    b4_all = load(BUNDLE_PATHS["bundle-4"])
    b5_all = load(BUNDLE_PATHS["bundle-5"])
    b6_all = load(BUNDLE_PATHS["bundle-6"])

    # Each bundle worktree rewrote C1_vocabulary.json independently starting from
    # an empty array, so the file contains ONLY that bundle's entries.
    # Confirm ranges.
    def id_range(entries):
        ids = [e["id"] for e in entries]
        return min(ids), max(ids)

    print(f"Bundle-2 raw:          {len(b2_all)} entries, IDs {id_range(b2_all)}")
    print(f"Bundle-3 raw:          {len(b3_all)} entries, IDs {id_range(b3_all)}")
    print(f"Bundle-4 raw:          {len(b4_all)} entries, IDs {id_range(b4_all)}")
    print(f"Bundle-5 raw:          {len(b5_all)} entries, IDs {id_range(b5_all)}")
    print(f"Bundle-6 raw:          {len(b6_all)} entries, IDs {id_range(b6_all)}")

    # Detect whether each bundle file is ONLY its own range or the full cumulative file.
    # If bundle-2 starts at ID 1, it's cumulative and we need to slice.
    # If bundle-2 starts at ID 231, it's range-only.

    def extract_range(entries, id_min, id_max):
        return [e for e in entries if id_min <= e["id"] <= id_max]

    # Bundle 2: IDs 231-480
    b2 = extract_range(b2_all, 231, 480)
    # Bundle 3: IDs 481-750
    b3 = extract_range(b3_all, 481, 750)
    # Bundle 4: IDs 751-1050 (first 300 entries, not the 5 spillover)
    b4_main = extract_range(b4_all, 751, 1050)
    # Bundle 4 spillover: IDs 1051-1055
    b4_spillover = extract_range(b4_all, 1051, 1055)
    # Bundle 5: IDs 1051-1290
    b5 = extract_range(b5_all, 1051, 1290)
    # Bundle 6: IDs 1291-1520
    b6 = extract_range(b6_all, 1291, 1520)

    print(f"\nAfter range extraction:")
    print(f"Bundle-2 (231-480):    {len(b2)} entries")
    print(f"Bundle-3 (481-750):    {len(b3)} entries")
    print(f"Bundle-4 (751-1050):   {len(b4_main)} entries")
    print(f"Bundle-4 spillover:    {len(b4_spillover)} entries (IDs 1051-1055 -> 1521-1525)")
    print(f"Bundle-5 (1051-1290):  {len(b5)} entries")
    print(f"Bundle-6 (1291-1520):  {len(b6)} entries")

    # Renumber Bundle 4 spillover: 1051->1521, 1052->1522, ..., 1055->1525
    spillover_renumbered = []
    for i, entry in enumerate(b4_spillover):
        new_entry = dict(entry)
        original_id = new_entry["id"]
        new_entry["id"] = 1521 + i
        spillover_renumbered.append(new_entry)
        print(f"  Renumbered: ID {original_id} -> {new_entry['id']} ({new_entry['german']})")

    # Build consolidated array
    consolidated = (
        main_entries +  # 1-230
        b2 +            # 231-480
        b3 +            # 481-750
        b4_main +       # 751-1050
        b5 +            # 1051-1290
        b6 +            # 1291-1520
        spillover_renumbered  # 1521-1525
    )

    print(f"\nConsolidated total:    {len(consolidated)} entries")

    # Validate ID monotonicity
    ids = [e["id"] for e in consolidated]
    expected = list(range(1, len(consolidated) + 1))
    if ids != expected:
        gaps = [i for i in expected if i not in set(ids)]
        dupes = [i for i in ids if ids.count(i) > 1]
        print(f"ERROR: ID validation failed!")
        print(f"  Gaps: {gaps[:20]}")
        print(f"  Duplicates: {list(set(dupes))[:20]}")
        sys.exit(1)
    print(f"ID monotonicity:       PASS (1 through {len(consolidated)}, no gaps, no duplicates)")

    # Validate schema — every entry must have required fields
    required_fields = ["id", "level", "german", "english", "exampleSentence", "topic",
                       "audioFile", "easeFactor", "intervalDays", "repetitions",
                       "nextReviewDate", "lastReviewedAt"]
    missing_fields_count = 0
    for entry in consolidated:
        for field in required_fields:
            if field not in entry:
                print(f"ERROR: Entry ID {entry['id']} missing field '{field}'")
                missing_fields_count += 1
    if missing_fields_count == 0:
        print(f"Schema validation:     PASS (all {len(required_fields)} required fields present on all entries)")
    else:
        print(f"Schema validation:     FAIL ({missing_fields_count} missing fields)")
        sys.exit(1)

    # Write output
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(consolidated, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"\nWritten to:            {OUTPUT}")
    print(f"Final count:           {len(consolidated)} entries")


if __name__ == "__main__":
    main()
