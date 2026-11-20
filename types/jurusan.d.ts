// Tipe data untuk data/*.json (dokumentasi dan bantuan autocomplete editor)
export type TraitId = 'tek' | 'kre' | 'bis' | 'mes' | 'kes' | 'sos' | 'sai';
export interface Major {
  id: number; lv: 'SMK' | 'Kuliah'; n: string; ic: string;
  w: Partial<Record<TraitId, 1 | 2 | 3>>;
  d: string; why: string; jobs: string; mp: string;
}
export interface Question { text: string; trait: TraitId }
export interface TestResult { p: Record<TraitId, number>; top: { id: number; p: number }[]; lv: 'SMK' | 'Kuliah' }
