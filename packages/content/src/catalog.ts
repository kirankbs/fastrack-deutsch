import type { Level } from '@fastrack/types';

export interface MockExamEntry {
  id: string;
  level: Level;
  mockNumber: number;
  title: string;
  /**
   * True when the JSON file for this mock is committed to
   * apps/mobile/assets/content/{level}/mock_NN.json.
   * Baked in at catalog-authoring time; never computed at request time.
   * Update this field whenever a mock JSON is added or removed.
   */
  hasContent: boolean;
}

function generateEntries(level: Level, count: number): MockExamEntry[] {
  const titles: Record<Level, string[]> = {
    A1: [
      'Alltag', 'Familie & Freunde', 'Wohnen', 'Essen & Trinken', 'Termine & Uhrzeit',
      'Arbeit & Beruf', 'Freizeit', 'Gesundheit', 'Reisen', 'Einkaufen',
    ],
    A2: [
      'Alltag', 'Familie', 'Wohnen', 'Essen', 'Termine',
      'Arbeit', 'Freizeit', 'Gesundheit', 'Reisen', 'Einkaufen',
    ],
    // B1 convergent end-state: 15 mocks (01–10 shipped; 11–15 planned WS-A wave 6–8)
    B1: [
      'Alltag', 'Berufseinstieg', 'Bildung', 'Medien', 'Wohnen & Lernen',
      'Kultur & Veranstaltungen', 'Dienste & formelle Kommunikation', 'Gesundheit', 'Reisen', 'Konsum',
      'Arbeit & Karriere', 'Gesundheit & Lebensstil', 'Reisen & Mobilität',
      'Familie & Generationen', 'Medien & digitales Leben',
    ],
    B2: [
      'Beruf & Arbeitswelt', 'Bildung & Studium', 'Gesundheit & Medizin', 'Medien & Kommunikation', 'Umwelt & Nachhaltigkeit',
      'Reisen & Mobilität', 'Technologie & Digitalisierung', 'Gesellschaft & Integration', 'Kultur & Kunst', 'Wirtschaft & Konsum',
    ],
    C1: [
      'Wissenschaftliche Erkenntnis und Verantwortung',
      'Bildung und Hochschule',
      'Medien und Künstliche Intelligenz',
      'Wirtschaft und Globalisierung',
      'Politik und Demokratie',
      'Gesellschaft und Migration',
      'Kultur und Kunst',
      'Gesundheit und Bioethik',
      'Datenschutz und digitale Sicherheit',
      'Technologie und Zukunft der Arbeit',
    ],
  };

  // Mocks 01–10 for all levels have JSON files committed as of 2026-04-26.
  // B1 mocks 11–15 are planned (WS-A waves 6–8) — hasContent: false until shipped.
  const shippedCounts: Partial<Record<Level, number>> = { B1: 10 };
  const shipped = shippedCounts[level] ?? count;

  return Array.from({ length: count }, (_, i) => ({
    id: `${level}_mock_${String(i + 1).padStart(2, '0')}`,
    level,
    mockNumber: i + 1,
    title: `${level} Übungstest ${i + 1}: ${titles[level][i]}`,
    hasContent: i < shipped,
  }));
}

export const MOCK_EXAM_CATALOG: MockExamEntry[] = [
  ...generateEntries('A1', 10),
  ...generateEntries('A2', 10),
  ...generateEntries('B1', 15),
  ...generateEntries('B2', 10),
  ...generateEntries('C1', 10),
];

export function getAvailableLevels(): Level[] {
  return ['A1', 'A2', 'B1', 'B2', 'C1'];
}

export function getMocksForLevel(level: Level): MockExamEntry[] {
  return MOCK_EXAM_CATALOG.filter((e) => e.level === level);
}
