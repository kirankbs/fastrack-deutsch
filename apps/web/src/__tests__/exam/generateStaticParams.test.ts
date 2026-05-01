import { describe, it, expect } from 'vitest';
import { MOCK_EXAM_CATALOG, getAvailableLevels, getMocksForLevel } from '@fastrack/content';

// This test guards the static param generation that fixes #102.
// generateStaticParams() in apps/web/src/app/exam/[mockId]/page.tsx maps
// MOCK_EXAM_CATALOG to { mockId } objects. If the catalog shrinks or the id
// format changes, these assertions catch it before the build goes live.

// B1 upgrade wave adds 5 planned mocks (M11-M15, hasContent: false).
// Total catalog: A1×10 + A2×10 + B1×15 + B2×10 + C1×10 = 55.
const EXPECTED_TOTAL = 55;
const EXPECTED_B1_COUNT = 15;
const LEVEL_COUNTS: Record<string, number> = {
  A1: 10, A2: 10, B1: 15, B2: 10, C1: 10,
};

describe('MOCK_EXAM_CATALOG — static params source of truth', () => {
  it(`has exactly ${EXPECTED_TOTAL} entries (B1 expanded to 15, others at 10)`, () => {
    expect(MOCK_EXAM_CATALOG).toHaveLength(EXPECTED_TOTAL);
  });

  it('every entry has an id matching the level_mock_NN format', () => {
    // B1 now runs to mock_15; other levels stay at mock_10
    const pattern = /^(A1|A2|B2|C1)_mock_(0[1-9]|10)$|^B1_mock_(0[1-9]|1[0-5])$/;
    for (const entry of MOCK_EXAM_CATALOG) {
      expect(entry.id, `${entry.id} does not match expected format`).toMatch(pattern);
    }
  });

  it('each level has the correct number of catalog entries', () => {
    for (const level of getAvailableLevels()) {
      const mocks = getMocksForLevel(level);
      expect(mocks, `Level ${level} mock count`).toHaveLength(LEVEL_COUNTS[level]);
    }
  });

  it('B1 has exactly 15 entries', () => {
    expect(getMocksForLevel('B1')).toHaveLength(EXPECTED_B1_COUNT);
  });

  it(`all ${EXPECTED_TOTAL} mock ids are unique`, () => {
    const ids = MOCK_EXAM_CATALOG.map((e) => e.id);
    const unique = new Set(ids);
    expect(unique.size).toBe(EXPECTED_TOTAL);
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
    const params = MOCK_EXAM_CATALOG.map((entry) => ({ mockId: entry.id }));

    expect(params).toHaveLength(EXPECTED_TOTAL);
    expect(params[0]).toEqual({ mockId: 'A1_mock_01' });
    // Last entry: C1_mock_10 (C1 still has 10 mocks)
    expect(params[EXPECTED_TOTAL - 1]).toEqual({ mockId: 'C1_mock_10' });

    for (const p of params) {
      expect(typeof p.mockId).toBe('string');
      expect(p.mockId.length).toBeGreaterThan(0);
    }
  });
});
