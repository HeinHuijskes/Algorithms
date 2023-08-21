import { WfcColours } from "../../ui/wfcColours";

export const BBLOCK = 'BBLOCK'
export const WBLOCK = 'WBLOCK'
export const GBLOCK = 'GBLOCK'
export const BLLOCK = 'BLLOCK'
export const LBLOCK = 'LBLOCK'
export const YBLOCK = 'YBLOCK'

export const testMapColours = {
  BBLOCK: WfcColours.BLACK,
  WBLOCK: WfcColours.WHITE,
  GBLOCK: WfcColours.GREEN,
  BLLOCK: WfcColours.BLUE,
  LBLOCK: WfcColours.LIGHTBLUE,
  YBLOCK: WfcColours.YELLOW,
} as Record<any, string>

export const map1 = [
  [BBLOCK, GBLOCK, BBLOCK],
  [GBLOCK, WBLOCK, GBLOCK],
  [BBLOCK, GBLOCK, BBLOCK]
]
export const map2 = [
  [BBLOCK, BBLOCK, BBLOCK, BBLOCK, BBLOCK],
  [BBLOCK, BBLOCK, GBLOCK, BBLOCK, BBLOCK],
  [BBLOCK, GBLOCK, WBLOCK, GBLOCK, BBLOCK],
  [BBLOCK, BBLOCK, GBLOCK, BBLOCK, BBLOCK],
  [BBLOCK, BBLOCK, BBLOCK, BBLOCK, BBLOCK]
]

export const map3 = [
  [BBLOCK, BBLOCK, BBLOCK],
  [GBLOCK, WBLOCK, GBLOCK],
  [BBLOCK, GBLOCK, BBLOCK]
]

export const map4 = [
  [BBLOCK, BLLOCK, YBLOCK, BLLOCK, BBLOCK],
  [BLLOCK, YBLOCK, GBLOCK, YBLOCK, BLLOCK],
  [YBLOCK, GBLOCK, WBLOCK, GBLOCK, YBLOCK],
  [BLLOCK, YBLOCK, GBLOCK, YBLOCK, BLLOCK],
  [BBLOCK, BLLOCK, YBLOCK, BLLOCK, BBLOCK]
]

export const map5 = [
  [WBLOCK, BLLOCK, YBLOCK, BLLOCK, WBLOCK],
  [BLLOCK, YBLOCK, GBLOCK, YBLOCK, BLLOCK],
  [YBLOCK, GBLOCK, WBLOCK, GBLOCK, YBLOCK],
  [BLLOCK, YBLOCK, GBLOCK, YBLOCK, BLLOCK],
  [WBLOCK, BLLOCK, YBLOCK, BLLOCK, WBLOCK]
]

export const map6 = [
  [YBLOCK, YBLOCK, YBLOCK, YBLOCK, YBLOCK],
  [GBLOCK, GBLOCK, GBLOCK, GBLOCK, GBLOCK],
  [BLLOCK, BLLOCK, BLLOCK, BLLOCK, BLLOCK],
  [WBLOCK, WBLOCK, WBLOCK, WBLOCK, WBLOCK],
  [YBLOCK, YBLOCK, YBLOCK, YBLOCK, YBLOCK]
]


export const map7 = [
  [YBLOCK, YBLOCK, YBLOCK, YBLOCK, YBLOCK, YBLOCK, YBLOCK],
  [GBLOCK, GBLOCK, GBLOCK, GBLOCK, GBLOCK, GBLOCK, GBLOCK],
  [BLLOCK, BLLOCK, BLLOCK, BLLOCK, BLLOCK, BLLOCK, BLLOCK],
  [WBLOCK, WBLOCK, WBLOCK, WBLOCK, WBLOCK, WBLOCK, WBLOCK],
  [BBLOCK, BBLOCK, BBLOCK, BBLOCK, BBLOCK, BBLOCK, BBLOCK],
  [LBLOCK, LBLOCK, LBLOCK, LBLOCK, LBLOCK, LBLOCK, LBLOCK],
  [YBLOCK, YBLOCK, YBLOCK, YBLOCK, YBLOCK, YBLOCK, YBLOCK]
]

export const map8 = [
  [YBLOCK, YBLOCK, YBLOCK, GBLOCK, GBLOCK, GBLOCK, GBLOCK],
  [GBLOCK, GBLOCK, GBLOCK, BLLOCK, BLLOCK, BLLOCK, BLLOCK],
  [BLLOCK, BLLOCK, BLLOCK, WBLOCK, WBLOCK, WBLOCK, WBLOCK],
  [WBLOCK, WBLOCK, WBLOCK, BBLOCK, BBLOCK, BBLOCK, BBLOCK],
  [BBLOCK, BBLOCK, BBLOCK, LBLOCK, LBLOCK, LBLOCK, LBLOCK],
  [LBLOCK, LBLOCK, LBLOCK, YBLOCK, YBLOCK, YBLOCK, YBLOCK],
  [YBLOCK, YBLOCK, YBLOCK, GBLOCK, GBLOCK, GBLOCK, GBLOCK]
]
export const map9 = [
  [YBLOCK, YBLOCK, YBLOCK, BLLOCK, BLLOCK, BLLOCK, BLLOCK],
  [GBLOCK, GBLOCK, GBLOCK, WBLOCK, WBLOCK, WBLOCK, WBLOCK],
  [BLLOCK, BLLOCK, BLLOCK, BBLOCK, BBLOCK, BBLOCK, BBLOCK],
  [WBLOCK, WBLOCK, WBLOCK, LBLOCK, LBLOCK, LBLOCK, LBLOCK],
  [BBLOCK, BBLOCK, BBLOCK, YBLOCK, YBLOCK, YBLOCK, YBLOCK],
  [LBLOCK, LBLOCK, LBLOCK, GBLOCK, GBLOCK, GBLOCK, GBLOCK],
  [YBLOCK, YBLOCK, YBLOCK, BLLOCK, BLLOCK, BLLOCK, BLLOCK]
]

export const map10 = [
  [WBLOCK, WBLOCK, WBLOCK, LBLOCK, WBLOCK, WBLOCK, WBLOCK],
  [BBLOCK, BBLOCK, BBLOCK, YBLOCK, BBLOCK, BBLOCK, BBLOCK],
  [WBLOCK, WBLOCK, WBLOCK, LBLOCK, WBLOCK, WBLOCK, WBLOCK],
  [WBLOCK, WBLOCK, WBLOCK, LBLOCK, WBLOCK, WBLOCK, WBLOCK],
  [WBLOCK, WBLOCK, WBLOCK, LBLOCK, WBLOCK, WBLOCK, WBLOCK],
  [GBLOCK, GBLOCK, GBLOCK, YBLOCK, GBLOCK, GBLOCK, GBLOCK],
  [WBLOCK, WBLOCK, WBLOCK, LBLOCK, WBLOCK, WBLOCK, WBLOCK],
]

export const map11 = [
  [WBLOCK, WBLOCK, WBLOCK, LBLOCK, WBLOCK, WBLOCK, WBLOCK, WBLOCK],
  [BBLOCK, BBLOCK, BBLOCK, YBLOCK, BBLOCK, BBLOCK, BBLOCK, BBLOCK],
  [WBLOCK, WBLOCK, WBLOCK, LBLOCK, WBLOCK, WBLOCK, WBLOCK, WBLOCK],
  [WBLOCK, WBLOCK, WBLOCK, LBLOCK, WBLOCK, WBLOCK, WBLOCK, WBLOCK],
  [BLLOCK, BLLOCK, BLLOCK, YBLOCK, BLLOCK, BLLOCK, BLLOCK, BLLOCK],
  [WBLOCK, WBLOCK, WBLOCK, LBLOCK, WBLOCK, WBLOCK, WBLOCK, WBLOCK],
  [WBLOCK, WBLOCK, WBLOCK, LBLOCK, WBLOCK, WBLOCK, WBLOCK, WBLOCK],
  [GBLOCK, GBLOCK, GBLOCK, YBLOCK, GBLOCK, GBLOCK, GBLOCK, GBLOCK],
  [WBLOCK, WBLOCK, WBLOCK, LBLOCK, WBLOCK, WBLOCK, WBLOCK, WBLOCK],
]

export const map12 = [
  [BLLOCK, BLLOCK, LBLOCK, YBLOCK, YBLOCK],
  [BLLOCK, LBLOCK, LBLOCK, YBLOCK, WBLOCK],
  [LBLOCK, LBLOCK, YBLOCK, WBLOCK, WBLOCK],
  [YBLOCK, YBLOCK, WBLOCK, WBLOCK, BBLOCK],
  [YBLOCK, WBLOCK, WBLOCK, BBLOCK, BBLOCK]
]

export const map13 = [
  [BLLOCK, BLLOCK, LBLOCK, YBLOCK, YBLOCK],
  [BLLOCK, LBLOCK, LBLOCK, YBLOCK, LBLOCK],
  [LBLOCK, LBLOCK, YBLOCK, YBLOCK, LBLOCK],
  [YBLOCK, YBLOCK, YBLOCK, LBLOCK, BLLOCK],
  [YBLOCK, LBLOCK, LBLOCK, BLLOCK, BLLOCK]
]

export const map14 = [
  [BLLOCK, BLLOCK, LBLOCK, YBLOCK, GBLOCK, BBLOCK, GBLOCK],
  [BLLOCK, BLLOCK, LBLOCK, YBLOCK, GBLOCK, BBLOCK, GBLOCK],
  [LBLOCK, LBLOCK, YBLOCK, GBLOCK, BBLOCK, GBLOCK, YBLOCK],
  [YBLOCK, YBLOCK, GBLOCK, BBLOCK, GBLOCK, YBLOCK, LBLOCK],
  [GBLOCK, GBLOCK, BBLOCK, GBLOCK, YBLOCK, LBLOCK, BLLOCK],
  [BBLOCK, BBLOCK, GBLOCK, YBLOCK, LBLOCK, BLLOCK, BLLOCK],
  [GBLOCK, GBLOCK, YBLOCK, LBLOCK, BLLOCK, BLLOCK, BLLOCK]
]

export const testMaps = [map1, map2, map3, map4, map5, map6, map7, map8, map9, map10, map11, map12, map13, map14]
