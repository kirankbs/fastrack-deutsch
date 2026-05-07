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
    // B1 final state: all 15 mocks shipped (01–15)
    B1: [
      'Alltag', 'Berufseinstieg', 'Bildung', 'Medien', 'Wohnen & Lernen',
      'Kultur & Veranstaltungen', 'Dienste & formelle Kommunikation', 'Konsum & Tausch', 'Tiere & Stadt', 'Feste & Feiern',
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
      'Recht und Verfassung',
      'Kultur und Kunst',
      'Gesundheit und Medizin',
      'Philosophie und Ethik',
      'Klima und Nachhaltigkeit',
    ],
  };

  // All 15 B1 mocks are now shipped. Set is kept for structural consistency
  // with earlier waves; hasContent is true for every B1 entry.
  const B1_SHIPPED: Set<number> = new Set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]);

  return Array.from({ length: count }, (_, i) => {
    const mockNumber = i + 1;
    const hasContent = level === 'B1'
      ? B1_SHIPPED.has(mockNumber)
      : true;
    return {
      id: `${level}_mock_${String(mockNumber).padStart(2, '0')}`,
      level,
      mockNumber,
      title: `${level} Übungstest ${mockNumber}: ${titles[level][i]}`,
      hasContent,
    };
  });
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
