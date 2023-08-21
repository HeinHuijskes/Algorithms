import { beforeAll, describe, expect, test } from "vitest";
import { WfcMapReader } from "../../src/reader/wfcMapReader";
import { readableTestMap, testMapColours } from "../../data/readableTestMap";
import { WfcUI } from "../../ui/wfcUI";
import { WfcMap } from "../../src/map/wfcMap";
import { WfcColours } from "../../ui/wfcColours";

let unreadMap: string[][]

beforeAll(() => {
  unreadMap = readableTestMap
})

describe('WFC Reader', () => {
  test('Reads a map correctly', () => {
    const resultMapObject = WfcMapReader.readMap(unreadMap, testMapColours)
    const resultMap = new WfcMap(10, resultMapObject.rules, resultMapObject.tiles)
    expect(resultMap.tiles.length).toBe(3)
    expect(resultMap.tiles[0].name).toBe('SEA')
    expect(resultMap.tiles[0].frequency).toBe(9)
    expect(resultMap.tiles[0].colour).toBe(WfcColours.BLUE)

    expect(resultMap.ruleSet.length).toBe(12)
    expect(resultMap.ruleSet[0].firstState).toBe('SEA')
    expect(resultMap.ruleSet[0].secondState).toBe('SEA')
    expect(resultMap.ruleSet[0].direction).toBe('RIGHT')
  })

  test('Can build a map from a read map', () => {
    const resultMapObject = WfcMapReader.readMap(unreadMap, testMapColours)
    const resultMap = new WfcMap(10, resultMapObject.rules, resultMapObject.tiles)
    const fails = resultMap.createMap()
    console.log(`Fails: ${fails}`)
    console.log('Printed map:')
    console.log(new WfcUI().printMap(resultMap))
  })
});