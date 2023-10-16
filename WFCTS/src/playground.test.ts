import { beforeAll, describe, test } from "vitest";
import { testMaps, testMapColours } from "./testMaps/testMaps";
import { WfcUI } from "../ui/wfcUI";
import { WfcMap } from "./map/wfcMap";
import { WfcMapReader } from "./reader/wfcMapReader";

let maps: string[][][]
let testColours: Record<any,string>
let UI: WfcUI
let size: number

beforeAll(() => {
  maps = testMaps
  testColours = testMapColours
  UI = new WfcUI()
  size = 20
})

describe('Run something', () => {
  test('Do something', () => {
    for (let testMap of maps) {
      let mapObject = WfcMapReader.readMap(testMap, testColours)
      let newMap = new WfcMap(size, mapObject.rules, mapObject.tiles)
      let fails = newMap.createMap()
      console.log('\nTest map:')
      console.log(UI.printTestMap(testMap, testColours))
      console.log('New map:')
      console.log(`Fails: ${fails}`)
      console.log(UI.printMap(newMap))
      console.log('------------------------------')
    }
  })
})