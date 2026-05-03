/**
 * Regression test for the loadVocabulary shim.
 *
 * After #110, loadVocabulary is a static wrapper around getVocabulary — it must
 * not import fs/promises or call readFile. This test asserts the public contract:
 * all 5 levels return arrays of the correct length.
 */

import { describe, it, expect } from 'vitest';
import { loadVocabulary } from '../../lib/loadVocabulary';

describe('loadVocabulary shim — no fs, static data only', () => {
  it('A1 returns 723 vocabulary words', async () => {
    const words = await loadVocabulary('A1');
    expect(words).toHaveLength(723);
  });

  it('A2 returns 1338 vocabulary words', async () => {
    const words = await loadVocabulary('A2');
    expect(words).toHaveLength(1338);
  });

  it('B1 returns 2739 vocabulary words (post combined batches B1-B10 #232)', async () => {
    const words = await loadVocabulary('B1');
    expect(words).toHaveLength(2739);
  });

  it('B2 returns words', async () => {
    const words = await loadVocabulary('B2');
    expect(words.length).toBeGreaterThan(0);
  });

  it('C1 returns 3022 vocabulary words (Phase 1b: +300 Recht #179, +300 Gesundheit #180, +300 Technologie #181, +400 Soziales #182, +193 Sprache+Geschichte #183)', async () => {
    const words = await loadVocabulary('C1');
    expect(Array.isArray(words)).toBe(true);
    expect(words).toHaveLength(3022);
  });

  it('C1 bundle 3 — IDs 2130-2429 are present and sequential (Technologie & KI)', async () => {
    const words = await loadVocabulary('C1');
    const b3 = words.filter((w) => w.id >= 2130 && w.id <= 2429);
    expect(b3).toHaveLength(300);
    const ids = b3.map((w) => w.id).sort((a, b) => a - b);
    expect(ids[0]).toBe(2130);
    expect(ids[ids.length - 1]).toBe(2429);
  });

  it('C1 bundle 3 — Technologie topic coverage', async () => {
    const words = await loadVocabulary('C1');
    const b3 = words.filter((w) => w.id >= 2130 && w.id <= 2429);
    const topics = new Set(b3.map((w) => w.topic));
    expect(topics.has('Medien und Digitalisierung')).toBe(true);
  });

  it('C1 bundle 4 — IDs 2430-2829 are present and sequential', async () => {
    const words = await loadVocabulary('C1');
    const b4 = words.filter((w) => w.id >= 2430 && w.id <= 2829);
    expect(b4).toHaveLength(400);
    const ids = b4.map((w) => w.id).sort((a, b) => a - b);
    expect(ids[0]).toBe(2430);
    expect(ids[ids.length - 1]).toBe(2829);
  });

  it('C1 bundle 4 — Soziales topic coverage', async () => {
    const words = await loadVocabulary('C1');
    const b4 = words.filter((w) => w.id >= 2430 && w.id <= 2829);
    const topics = new Set(b4.map((w) => w.topic));
    expect(topics.has('Gesellschaft')).toBe(true);
    expect(topics.has('Politik und Internationale Beziehungen')).toBe(true);
    expect(topics.has('Philosophie und Ethik')).toBe(true);
  });

  it('unknown level returns empty array', async () => {
    expect(await loadVocabulary('D1')).toHaveLength(0);
    expect(await loadVocabulary('foo')).toHaveLength(0);
  });

  it('lowercase level is handled', async () => {
    const words = await loadVocabulary('a1');
    expect(words).toHaveLength(723);
  });

  it('each word has required fields', async () => {
    const words = await loadVocabulary('A1');
    const sample = words[0];
    expect(typeof sample.id).toBe('number');
    expect(typeof sample.german).toBe('string');
    expect(typeof sample.english).toBe('string');
    expect(typeof sample.level).toBe('string');
  });
});
