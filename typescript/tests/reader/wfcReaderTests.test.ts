import { beforeAll, describe, test } from "vitest";
import { WfcMapReader } from "../../src/reader/wfcMapReader";
import {readableTestMap, testMapColours} from "../../data/readableTestMap";
import { WfcUI } from "../../ui/wfcUI";
import { WfcMap } from "../../src/map/wfcMap";

let unreadMap: string[][]

beforeAll(() => {
  unreadMap = readableTestMap
})

describe('WFC Reader', () => {
  test('Reads a map correctly', () => {
    const resultMapObject = WfcMapReader.readMap(unreadMap, testMapColours)
    const resultMap = new WfcMap(10, resultMapObject.rules, resultMapObject.tiles)
  })

  test('Can build a map from a read map', () => {
    const resultMapObject = WfcMapReader.readMap(unreadMap, testMapColours)
    const resultMap = new WfcMap(10, resultMapObject.rules, resultMapObject.tiles)
    const fails = resultMap.createMap()
    console.log(`Fails: ${fails}`)
    console.log(resultMap.cells[0][0])
    console.log('Printed map:')
    console.log(new WfcUI().printMap(resultMap))
  })
});