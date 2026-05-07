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
 * B1 final state: all 15 mocks shipped. No planned placeholders remain.
 */

import { describe, it, expect } from 'vitest';
import { MOCK_EXAM_CATALOG, getAvailableLevels, getMocksForLevel } from '@fastrack/content';

// All 15 B1 mocks are now shipped — no planned placeholders.
const PLANNED_B1_MOCKS: string[] = [];

describe('catalog hasContent integrity', () => {
  it('every entry in MOCK_EXAM_CATALOG declares hasContent as a boolean', () => {
    for (const entry of MOCK_EXAM_CATALOG) {
      expect(typeof entry.hasContent, `${entry.id}.hasContent must be boolean`).toBe('boolean');
    }
  });

  it('all shipped mocks (hasContent: true) are not the planned B1 placeholders', () => {
    // No B1 placeholders remain — every entry must have hasContent: true.
    const missing = MOCK_EXAM_CATALOG.filter((e) => !e.hasContent);
    const unexpectedMissing = missing.filter((e) => !PLANNED_B1_MOCKS.includes(e.id));
    expect(
      unexpectedMissing,
      'Unexpected hasContent: false entries found outside planned B1 placeholders',
    ).toHaveLength(0);
  });

  it('exactly 0 B1 planned mocks have hasContent: false (all 15 shipped)', () => {
    const planned = MOCK_EXAM_CATALOG.filter((e) => !e.hasContent);
    expect(planned).toHaveLength(0);
  });

  it('B1 mock 11 has hasContent: true', () => {
    const entry = MOCK_EXAM_CATALOG.find((e) => e.id === 'B1_mock_11');
    expect(entry).toBeDefined();
    expect(entry?.hasContent).toBe(true);
  });

  it('B1 mock 12 has hasContent: true', () => {
    const entry = MOCK_EXAM_CATALOG.find((e) => e.id === 'B1_mock_12');
    expect(entry).toBeDefined();
    expect(entry?.hasContent).toBe(true);
  });

  it('B1 mock 13 has hasContent: true', () => {
    const entry = MOCK_EXAM_CATALOG.find((e) => e.id === 'B1_mock_13');
    expect(entry).toBeDefined();
    expect(entry?.hasContent).toBe(true);
  });

  it('B1 mock 14 has hasContent: true', () => {
    const entry = MOCK_EXAM_CATALOG.find((e) => e.id === 'B1_mock_14');
    expect(entry).toBeDefined();
    expect(entry?.hasContent).toBe(true);
  });

  it('B1 mock 15 has hasContent: true', () => {
    const entry = MOCK_EXAM_CATALOG.find((e) => e.id === 'B1_mock_15');
    expect(entry).toBeDefined();
    expect(entry?.hasContent).toBe(true);
  });

  it('all 55 shipped mocks (all 15 B1 + all other levels) have hasContent: true', () => {
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
