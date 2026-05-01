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
 */

import { describe, it, expect } from 'vitest';
import { MOCK_EXAM_CATALOG, getAvailableLevels, getMocksForLevel } from '@fastrack/content';

describe('catalog hasContent integrity', () => {
  it('every entry in MOCK_EXAM_CATALOG declares hasContent as a boolean', () => {
    for (const entry of MOCK_EXAM_CATALOG) {
      expect(typeof entry.hasContent, `${entry.id}.hasContent must be boolean`).toBe('boolean');
    }
  });

  it('all currently-shipped mocks have hasContent: true (B1 11–15 are planned stubs)', () => {
    // B1 mocks 11–15 are catalog stubs for the WS-A wave 6–8 new mocks.
    // They intentionally declare hasContent: false until their JSON is committed.
    const unexpectedMissing = MOCK_EXAM_CATALOG.filter(
      (e) => !e.hasContent && !e.id.match(/^B1_mock_(1[1-5])$/),
    );
    expect(
      unexpectedMissing,
      'These catalog entries claim no JSON but should have content',
    ).toHaveLength(0);
  });

  it('B1 mocks 11–15 are declared as planned (hasContent: false)', () => {
    const plannedB1 = MOCK_EXAM_CATALOG.filter((e) => e.id.match(/^B1_mock_(1[1-5])$/));
    expect(plannedB1).toHaveLength(5);
    for (const entry of plannedB1) {
      expect(entry.hasContent, `${entry.id} should be planned (hasContent: false)`).toBe(false);
    }
  });

  it('hasContent is true for all shipped entries in every level', () => {
    // B1 has 5 planned stubs (11–15) — skip those; all others must be true.
    for (const level of getAvailableLevels()) {
      const mocks = getMocksForLevel(level);
      const noContent = mocks.filter((m) => !m.hasContent && !m.id.match(/^B1_mock_(1[1-5])$/));
      expect(noContent, `Level ${level} has unexpected entries with hasContent: false`).toHaveLength(0);
    }
  });
});
