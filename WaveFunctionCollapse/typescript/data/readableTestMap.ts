import { WfcColours } from "../ui/wfcColours";

export const readableTestMap = [
  ['SEA', 'SEA', 'SEA', 'COAST', 'LAND'],
  ['SEA', 'SEA', 'COAST', 'LAND', 'LAND'],
  ['SEA', 'COAST', 'COAST', 'LAND', 'LAND'],
  ['SEA', 'COAST', 'LAND', 'LAND', 'LAND'],
  ['SEA', 'SEA', 'COAST', 'LAND', 'LAND']
]

export const testMapColours = {'SEA': WfcColours.BLUE, 'COAST': WfcColours.YELLOW, 'LAND': WfcColours.GREEN}

export const testMapRulesReduced = [
  { firstState: 'SEA', secondState: 'SEA', direction: 'RIGHT' },
  { firstState: 'SEA', secondState: 'SEA', direction: 'DOWN' },
  { firstState: 'SEA', secondState: 'COAST', direction: 'RIGHT' },
  { firstState: 'SEA', secondState: 'COAST', direction: 'DOWN' },
  { firstState: 'SEA', secondState: 'COAST', direction: 'UP' },
  { firstState: 'COAST', secondState: 'COAST', direction: 'RIGHT' },
  { firstState: 'COAST', secondState: 'COAST', direction: 'DOWN' },
  { firstState: 'COAST', secondState: 'LAND', direction: 'RIGHT' },
  { firstState: 'COAST', secondState: 'LAND', direction: 'DOWN' },
  { firstState: 'COAST', secondState: 'LAND', direction: 'UP' },
  { firstState: 'LAND', secondState: 'LAND', direction: 'RIGHT' },
  { firstState: 'LAND', secondState: 'LAND', direction: 'DOWN' },
]

export const testMapRules = [
  { firstState: 'SEA', secondState: 'SEA', direction: 'RIGHT' },
  { firstState: 'SEA', secondState: 'SEA', direction: 'DOWN' },
  { firstState: 'SEA', secondState: 'SEA', direction: 'LEFT' },
  { firstState: 'SEA', secondState: 'COAST', direction: 'RIGHT' },
  { firstState: 'SEA', secondState: 'COAST', direction: 'DOWN' },
  { firstState: 'COAST', secondState: 'SEA', direction: 'LEFT' },
  { firstState: 'COAST', secondState: 'LAND', direction: 'RIGHT' },
  { firstState: 'COAST', secondState: 'LAND', direction: 'DOWN' },
  { firstState: 'LAND', secondState: 'COAST', direction: 'LEFT' },
  { firstState: 'LAND', secondState: 'LAND', direction: 'DOWN' },
  { firstState: 'SEA', secondState: 'SEA', direction: 'UP' },
  { firstState: 'COAST', secondState: 'SEA', direction: 'UP' },
  { firstState: 'COAST', secondState: 'COAST', direction: 'DOWN' },
  { firstState: 'LAND', secondState: 'LAND', direction: 'RIGHT' },
  { firstState: 'LAND', secondState: 'COAST', direction: 'UP' },
  { firstState: 'LAND', secondState: 'LAND', direction: 'LEFT' },
  { firstState: 'LAND', secondState: 'LAND', direction: 'UP' },
  { firstState: 'COAST', secondState: 'COAST', direction: 'RIGHT' },
  { firstState: 'COAST', secondState: 'COAST', direction: 'LEFT' },
  { firstState: 'COAST', secondState: 'COAST', direction: 'UP' },
  { firstState: 'COAST', secondState: 'SEA', direction: 'DOWN' },
  { firstState: 'LAND', secondState: 'COAST', direction: 'DOWN' },
  { firstState: 'SEA', secondState: 'COAST', direction: 'UP' },
  { firstState: 'COAST', secondState: 'LAND', direction: 'UP' }

]