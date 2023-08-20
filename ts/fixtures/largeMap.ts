export const mapRules = [
  { firstTile: 'HEAVEN', secondTile: 'HEAVEN', direction: 'RIGHT' },
  { firstTile: 'HEAVEN', secondTile: 'MOUNTAIN', direction: 'RIGHT' },
  { firstTile: 'HEAVEN', secondTile: 'HEAVEN', direction: 'LEFT' },
  { firstTile: 'HEAVEN', secondTile: 'MOUNTAIN', direction: 'LEFT' },
  { firstTile: 'HEAVEN', secondTile: 'HEAVEN', direction: 'UP' },
  { firstTile: 'HEAVEN', secondTile: 'MOUNTAIN', direction: 'UP' },
  { firstTile: 'HEAVEN', secondTile: 'HEAVEN', direction: 'DOWN' },
  { firstTile: 'HEAVEN', secondTile: 'MOUNTAIN', direction: 'DOWN' },
  { firstTile: 'MOUNTAIN', secondTile: 'MOUNTAIN', direction: 'RIGHT' },
  { firstTile: 'MOUNTAIN', secondTile: 'LAND', direction: 'RIGHT' },
  { firstTile: 'MOUNTAIN', secondTile: 'MOUNTAIN', direction: 'LEFT' },
  { firstTile: 'MOUNTAIN', secondTile: 'LAND', direction: 'LEFT' },
  { firstTile: 'MOUNTAIN', secondTile: 'MOUNTAIN', direction: 'UP' },
  { firstTile: 'MOUNTAIN', secondTile: 'LAND', direction: 'UP' },
  { firstTile: 'MOUNTAIN', secondTile: 'MOUNTAIN', direction: 'DOWN' },
  { firstTile: 'MOUNTAIN', secondTile: 'LAND', direction: 'DOWN' },
  { firstTile: 'LAND', secondTile: 'LAND', direction: 'RIGHT' },
  { firstTile: 'LAND', secondTile: 'COAST', direction: 'RIGHT' },
  { firstTile: 'LAND', secondTile: 'LAND', direction: 'LEFT' },
  { firstTile: 'LAND', secondTile: 'COAST', direction: 'LEFT' },
  { firstTile: 'LAND', secondTile: 'LAND', direction: 'UP' },
  { firstTile: 'LAND', secondTile: 'COAST', direction: 'UP' },
  { firstTile: 'LAND', secondTile: 'LAND', direction: 'DOWN' },
  { firstTile: 'LAND', secondTile: 'COAST', direction: 'DOWN' },
  { firstTile: 'COAST', secondTile: 'COAST', direction: 'RIGHT' },
  { firstTile: 'COAST', secondTile: 'SEA', direction: 'RIGHT' },
  { firstTile: 'COAST', secondTile: 'COAST', direction: 'LEFT' },
  { firstTile: 'COAST', secondTile: 'SEA', direction: 'LEFT' },
  { firstTile: 'COAST', secondTile: 'COAST', direction: 'UP' },
  { firstTile: 'COAST', secondTile: 'SEA', direction: 'UP' },
  { firstTile: 'COAST', secondTile: 'COAST', direction: 'DOWN' },
  { firstTile: 'COAST', secondTile: 'SEA', direction: 'DOWN' },
  { firstTile: 'SEA', secondTile: 'SEA', direction: 'RIGHT' },
  { firstTile: 'SEA', secondTile: 'OCEAN', direction: 'RIGHT' },
  { firstTile: 'SEA', secondTile: 'SEA', direction: 'LEFT' },
  { firstTile: 'SEA', secondTile: 'OCEAN', direction: 'LEFT' },
  { firstTile: 'SEA', secondTile: 'SEA', direction: 'UP' },
  { firstTile: 'SEA', secondTile: 'OCEAN', direction: 'UP' },
  { firstTile: 'SEA', secondTile: 'SEA', direction: 'DOWN' },
  { firstTile: 'SEA', secondTile: 'OCEAN', direction: 'DOWN' },
  { firstTile: 'OCEAN', secondTile: 'OCEAN', direction: 'RIGHT' },
  { firstTile: 'OCEAN', secondTile: 'OCEAN', direction: 'LEFT' },
  { firstTile: 'OCEAN', secondTile: 'OCEAN', direction: 'UP' },
  { firstTile: 'OCEAN', secondTile: 'OCEAN', direction: 'DOWN' },

]

export const mapTiles = [
  { name: 'HEAVEN', frequency: 8, colour: '\u001b[47m' },
  { name: 'MOUNTAIN', frequency: 15, colour: '\u001b[40m' },
  { name: 'LAND', frequency: 15, colour: '\u001b[42m' },
  { name: 'COAST', frequency: 15, colour: '\u001b[43m' },
  { name: 'SEA', frequency: 15, colour: '\u001b[46m' },
  { name: 'OCEAN', frequency: 8, colour: '\u001b[44m' },
]

export const largeMap = {
  rules: mapRules,
  tiles: mapTiles
}

export default largeMap
