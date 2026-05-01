import { describe, it, expect } from 'vitest';
import { MOCK_EXAM_CATALOG, getAvailableLevels, getMocksForLevel } from '@fastrack/content';

// This test guards the static param generation that fixes #102.
// generateStaticParams() in apps/web/src/app/exam/[mockId]/page.tsx maps
// MOCK_EXAM_CATALOG to { mockId } objects. If the catalog shrinks or the id
// format changes, these assertions catch it before the build goes live.

// B1 now has 15 entries (10 shipped + 5 planned stubs for WS-A waves 6–8).
// Total catalog size: A1(10) + A2(10) + B1(15) + B2(10) + C1(10) = 55.
const TOTAL_CATALOG_SIZE = 55;
const LEVEL_COUNTS: Record<string, number> = { A1: 10, A2: 10, B1: 15, B2: 10, C1: 10 };

describe('MOCK_EXAM_CATALOG — static params source of truth', () => {
  it(`has exactly ${TOTAL_CATALOG_SIZE} entries (B1 has 15 planned; others 10 each)`, () => {
    expect(MOCK_EXAM_CATALOG).toHaveLength(TOTAL_CATALOG_SIZE);
  });

  it('every entry has an id matching the level_mock_NN format', () => {
    const pattern = /^(A1|A2|B1|B2|C1)_mock_(0[1-9]|1[0-5])$/;
    for (const entry of MOCK_EXAM_CATALOG) {
      expect(entry.id).toMatch(pattern);
    }
  });

  it('each level has the expected number of catalog entries', () => {
    for (const level of getAvailableLevels()) {
      const mocks = getMocksForLevel(level);
      expect(mocks).toHaveLength(LEVEL_COUNTS[level]);
    }
  });

  it(`all ${TOTAL_CATALOG_SIZE} mock ids are unique`, () => {
    const ids = MOCK_EXAM_CATALOG.map((e) => e.id);
    const unique = new Set(ids);
    expect(unique.size).toBe(TOTAL_CATALOG_SIZE);
  });

  it('ids are sequential within each level', () => {
    for (const level of getAvailableLevels()) {
      const mocks = getMocksForLevel(level);
      for (let i = 0; i < mocks.length; i++) {
        const expectedId = `${level}_mock_${String(i + 1).padStart(2, '0')}`;
        expect(mocks[i].id).toBe(expectedId);
      }
    }
  });

  it('generateStaticParams shape — each entry produces { mockId: string }', () => {
    // Mirrors the exact logic in [mockId]/page.tsx generateStaticParams()
    const params = MOCK_EXAM_CATALOG.map((entry) => ({ mockId: entry.id }));

    expect(params).toHaveLength(TOTAL_CATALOG_SIZE);
    expect(params[0]).toEqual({ mockId: 'A1_mock_01' });
    // Last entry is C1_mock_10 (index 54 = 10 A1 + 10 A2 + 15 B1 + 10 B2 + 10 C1 - 1)
    expect(params[TOTAL_CATALOG_SIZE - 1]).toEqual({ mockId: 'C1_mock_10' });

    for (const p of params) {
      expect(typeof p.mockId).toBe('string');
      expect(p.mockId.length).toBeGreaterThan(0);
    }
  });
});
