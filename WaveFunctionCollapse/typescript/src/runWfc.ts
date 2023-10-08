import { WfcMap } from "./map/wfcMap";
import { WfcUI } from "../ui/wfcUI";
import largeMap from "../data/largeMap"

export const runAlgorithm = (size: number) => {
  const rules = largeMap.rules
  const tiles = largeMap.tiles
  let wfcMap = new WfcMap(size, rules, tiles)
  wfcMap.createMap()
  return wfcMap
}

export const runAlgorithmPrint = (size = 10, consoleLog = false, stepwise = false) => {
  let maps = []
  const rules = largeMap.rules
  const tiles = largeMap.tiles
  const wfcMap = new WfcMap(size, rules, tiles)
  const UI =  new WfcUI()
  let fails = 0
  while (fails < 5) {
    if (wfcMap.isSolved()) {
      break
    }
    if (stepwise) {
      maps.push(UI.printMap(wfcMap))
    }
    let cell = wfcMap.findLowestEntropyCell()
    wfcMap.collapse(cell)
    if (wfcMap.hasContradiction) {
      wfcMap.reset()
      fails++
    }
  }
  if (consoleLog) {
    console.log(UI.printMap(wfcMap))
    for (let wfcMap of maps) {
      console.log(wfcMap)
      console.log(fails)
    }
  }
  return wfcMap
}
