/**
 * Regression guard for catalog hasContent integrity.
 *
 * Asserts that every currently-shipped mock has hasContent: true.
 * If a JSON file is removed from apps/mobile/assets/content/ without
 * also updating the catalog, someone must consciously update this test
 * (and the catalog) rather than silently shipping a broken entry.
 *
 * Strategy: trust the catalog as authoritative (per AC). The test does
 * not probe the filesystem — it asserts the catalog's declared state.
 *
 * B1 upgrade (wave 1): B1 M11–M15 are planned placeholders with
 * hasContent: false. These are expected and tested explicitly below.
 */

import { describe, it, expect } from 'vitest';
import { MOCK_EXAM_CATALOG, getAvailableLevels, getMocksForLevel } from '@fastrack/content';

// B1 M11-M15 are planned — hasContent: false until JSON files are shipped.
const PLANNED_B1_MOCKS = [11, 12, 13, 14, 15].map(
  (n) => `B1_mock_${String(n).padStart(2, '0')}`,
);

describe('catalog hasContent integrity', () => {
  it('every entry in MOCK_EXAM_CATALOG declares hasContent as a boolean', () => {
    for (const entry of MOCK_EXAM_CATALOG) {
      expect(typeof entry.hasContent, `${entry.id}.hasContent must be boolean`).toBe('boolean');
    }
  });

  it('all shipped mocks (hasContent: true) are not the planned B1 placeholders', () => {
    // Only B1 M11-M15 may have hasContent: false — nothing else.
    const missing = MOCK_EXAM_CATALOG.filter((e) => !e.hasContent);
    const unexpectedMissing = missing.filter((e) => !PLANNED_B1_MOCKS.includes(e.id));
    expect(
      unexpectedMissing,
      'Unexpected hasContent: false entries found outside planned B1 M11-M15',
    ).toHaveLength(0);
  });

  it('exactly 5 B1 planned mocks (M11-M15) have hasContent: false', () => {
    const planned = MOCK_EXAM_CATALOG.filter((e) => !e.hasContent);
    expect(planned).toHaveLength(5);
    const plannedIds = planned.map((e) => e.id);
    for (const id of PLANNED_B1_MOCKS) {
      expect(plannedIds).toContain(id);
    }
  });

  it('all 50 shipped mocks (B1 M01-M10 + all other levels) have hasContent: true', () => {
    const shipped = MOCK_EXAM_CATALOG.filter((e) => !PLANNED_B1_MOCKS.includes(e.id));
    const missing = shipped.filter((e) => !e.hasContent);
    expect(
      missing,
      'Shipped mock entries (non-placeholder) must all have hasContent: true',
    ).toHaveLength(0);
  });

  it('non-B1 levels have no hasContent: false entries', () => {
    for (const level of getAvailableLevels().filter((l) => l !== 'B1')) {
      const mocks = getMocksForLevel(level);
      const noContent = mocks.filter((m) => !m.hasContent);
      expect(noContent, `Level ${level} must have no hasContent: false entries`).toHaveLength(0);
    }
  });
});
