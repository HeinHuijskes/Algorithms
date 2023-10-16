import { beforeAll, describe, expect, test } from "vitest";
import { WfcMapReader } from "../../src/reader/wfcMapReader";

let testMap: string[][]
let cell: string
let ruleSet: Record<any,any>[]

beforeAll(() => {
  testMap = [['SEA', 'SEA', 'COAST'],
            ['SEA', 'COAST', 'COAST'],
            ['COAST', 'LAND', 'LAND']]
})

describe('WFC Reader', () => {
  describe('Finds rules', () => {
    test('Returns correct middle rules', () => {
      cell = testMap[1][1]
      ruleSet = WfcMapReader.findRules(testMap, 1, 1)
      expect(ruleSet.length).toBe(4)
      expect(ruleSet[0].firstTile).toBe(cell)
      expect(ruleSet[0].secondTile).toBe('SEA')
      expect(ruleSet[0].direction).toBe('LEFT')

      expect(ruleSet[1].firstTile).toBe(cell)
      expect(ruleSet[1].secondTile).toBe('COAST')
      expect(ruleSet[1].direction).toBe('RIGHT')

      expect(ruleSet[2].firstTile).toBe(cell)
      expect(ruleSet[2].secondTile).toBe('SEA')
      expect(ruleSet[2].direction).toBe('UP')

      expect(ruleSet[3].firstTile).toBe(cell)
      expect(ruleSet[3].secondTile).toBe('LAND')
      expect(ruleSet[3].direction).toBe('DOWN')
    })
    test('Returns correct corner rules', () => {
      cell = testMap[0][0]
      ruleSet = WfcMapReader.findRules(testMap, 0, 0)
      expect(ruleSet.length).toBe(2)
      expect(ruleSet[0].firstTile).toBe(cell)
      expect(ruleSet[0].secondTile).toBe('SEA')
      expect(ruleSet[0].direction).toBe('RIGHT')

      expect(ruleSet[1].firstTile).toBe(cell)
      expect(ruleSet[1].secondTile).toBe('SEA')
      expect(ruleSet[1].direction).toBe('DOWN')

      cell = testMap[2][2]
      ruleSet = WfcMapReader.findRules(testMap, 2, 2)
      expect(ruleSet.length).toBe(2)
      expect(ruleSet[0].firstTile).toBe(cell)
      expect(ruleSet[0].secondTile).toBe('LAND')
      expect(ruleSet[0].direction).toBe('LEFT')

      expect(ruleSet[1].firstTile).toBe(cell)
      expect(ruleSet[1].secondTile).toBe('COAST')
      expect(ruleSet[1].direction).toBe('UP')
    })
  })
  describe('Reduces ruleset', () => {
    test('Removes exact copies', () => {
      ruleSet = WfcMapReader.findRules(testMap, 0, 0)
      expect(ruleSet.length).toBe(2)
      ruleSet = ruleSet.concat(WfcMapReader.findRules(testMap, 0, 0))
      expect(ruleSet.length).toBe(4)
      ruleSet = WfcMapReader.reduceRules(ruleSet)
      expect(ruleSet.length).toBe(2)
      expect(ruleSet[0].direction).not.toBe(ruleSet[1].direction)
    })

    test('Removes reversed copies', () => {
      ruleSet = [{firstTile: 'SEA', secondTile: 'COAST', direction: 'RIGHT'},
                {firstTile: 'COAST', secondTile: 'SEA', direction: 'LEFT'}]
      ruleSet = WfcMapReader.reduceRules(ruleSet)
      expect(ruleSet.length).toBe(1)
      expect(ruleSet[0].firstTile).toBe('SEA')
      expect(ruleSet[0].secondTile).toBe('COAST')
      expect(ruleSet[0].direction).toBe('RIGHT')
    })

    test('Removes reversed self copies', () => {
      ruleSet = [{firstTile: 'SEA', secondTile: 'SEA', direction: 'RIGHT'},
                {firstTile: 'SEA', secondTile: 'SEA', direction: 'LEFT'},]
      ruleSet = WfcMapReader.reduceRules(ruleSet)
      expect(ruleSet.length).toBe(1)
      expect(ruleSet[0].firstTile).toBe('SEA')
      expect(ruleSet[0].secondTile).toBe('SEA')
      expect(ruleSet[0].direction).toBe('RIGHT')
    })
  })
  describe('Gets tiles', () => {
    test('Formats tiles correctly', () => {
      const tiles = WfcMapReader.getTiles(testMap, null)
      expect(tiles.length).toBe(3)

      expect(tiles[0].name).toBe('SEA')
      expect(tiles[0].frequency).toBe(3)

      expect(tiles[1].name).toBe('COAST')
      expect(tiles[1].frequency).toBe(4)

      expect(tiles[2].name).toBe('LAND')
      expect(tiles[2].frequency).toBe(2)
    })
  })
});