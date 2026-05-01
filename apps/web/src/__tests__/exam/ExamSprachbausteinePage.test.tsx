/**
 * Integration test for /exam/[mockId]/sprachbausteine server component.
 *
 * AC requirement (#108): do NOT mock getMockExam, loadMockExam, or fs.
 * Key assertions:
 * - B1, B2, and C1 mockIds resolve and have a sprachbausteine section
 *   (telc C1 Hochschule has Sprachbausteine: 1 part, 22 MCQ-4opt cloze items)
 * - A1 and A2 mockIds resolve but call notFound() because no sprachbausteine section
 * - generateStaticParams returns exactly 35 entries (B1×15 + B2×10 + C1×10)
 *   (B1 now has 15 catalog entries: 10 shipped + 5 planned stubs for WS-A waves 6–8)
 */
import { describe, it, expect, vi } from 'vitest';

vi.mock('next/navigation', () => ({
  notFound: vi.fn(() => {
    throw new Error('NEXT_NOT_FOUND');
  }),
}));

import { notFound } from 'next/navigation';
import { getMockExamOrNotFound } from '../../lib/loadMockExam';
import { MOCK_EXAM_CATALOG } from '@fastrack/content';

// Mirrors the sprachbausteine page logic: get exam, then check for section
async function resolveSprachbausteinePage(mockId: string) {
  const { exam } = await getMockExamOrNotFound(mockId);
  if (!exam.sections.sprachbausteine) notFound();
  return exam;
}

describe('SprachbausteinePage — static data, no fs at request time', () => {
  it('B1_mock_01 resolves with sprachbausteine section', async () => {
    const exam = await resolveSprachbausteinePage('B1_mock_01');
    expect(exam.level).toBe('B1');
    expect(exam.sections.sprachbausteine).toBeDefined();
  });

  it('B2_mock_01 resolves with sprachbausteine section', async () => {
    const exam = await resolveSprachbausteinePage('B2_mock_01');
    expect(exam.level).toBe('B2');
    expect(exam.sections.sprachbausteine).toBeDefined();
  });

  it('all 10 B1 mocks have sprachbausteine', async () => {
    for (let n = 1; n <= 10; n++) {
      const mockId = `B1_mock_${String(n).padStart(2, '0')}`;
      const exam = await resolveSprachbausteinePage(mockId);
      expect(exam.sections.sprachbausteine, `${mockId} should have sprachbausteine`).toBeDefined();
    }
  });

  it('all 10 B2 mocks have sprachbausteine', async () => {
    for (let n = 1; n <= 10; n++) {
      const mockId = `B2_mock_${String(n).padStart(2, '0')}`;
      const exam = await resolveSprachbausteinePage(mockId);
      expect(exam.sections.sprachbausteine, `${mockId} should have sprachbausteine`).toBeDefined();
    }
  });

  it('A1_mock_01 calls notFound() — no sprachbausteine at A1 level', async () => {
    await expect(resolveSprachbausteinePage('A1_mock_01')).rejects.toThrow('NEXT_NOT_FOUND');
  });

  it('A2_mock_01 calls notFound() — no sprachbausteine at A2 level', async () => {
    await expect(resolveSprachbausteinePage('A2_mock_01')).rejects.toThrow('NEXT_NOT_FOUND');
  });

  it('C1_mock_01 resolves with sprachbausteine section (C1 Hochschule has 1-part 22-item cloze)', async () => {
    const exam = await resolveSprachbausteinePage('C1_mock_01');
    expect(exam.level).toBe('C1');
    expect(exam.sections.sprachbausteine).toBeDefined();
    expect(exam.sections.sprachbausteine?.parts).toHaveLength(1);
    expect(exam.sections.sprachbausteine?.parts[0].questions).toHaveLength(22);
  });

  it('invalid mockId (foo) calls notFound()', async () => {
    await expect(resolveSprachbausteinePage('foo')).rejects.toThrow('NEXT_NOT_FOUND');
  });

  it('generateStaticParams returns 35 entries (B1×15 + B2×10 + C1×10)', () => {
    // Mirrors the generateStaticParams function in the sprachbausteine page.
    // B1 now has 15 catalog entries (10 shipped + 5 planned stubs); B2 and C1 still 10 each.
    const params = MOCK_EXAM_CATALOG.filter(
      (entry) => entry.level === 'B1' || entry.level === 'B2' || entry.level === 'C1',
    ).map((entry) => ({ mockId: entry.id }));

    expect(params).toHaveLength(35);
    expect(params[0]).toEqual({ mockId: 'B1_mock_01' });
    expect(params[14]).toEqual({ mockId: 'B1_mock_15' });
    expect(params[15]).toEqual({ mockId: 'B2_mock_01' });
    expect(params[24]).toEqual({ mockId: 'B2_mock_10' });
    expect(params[25]).toEqual({ mockId: 'C1_mock_01' });
    expect(params[34]).toEqual({ mockId: 'C1_mock_10' });

    // All entries must be B1, B2, or C1
    for (const p of params) {
      expect(p.mockId).toMatch(/^(B1|B2|C1)_mock_\d{2}$/);
    }
  });
});
