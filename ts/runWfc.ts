import {WfcMap} from "./wfcMap";
import {WfcUI} from "./wfcUI";
import largeMap from "./fixtures/largeMap"

const rules = largeMap.rules
const tiles = largeMap.tiles

export const runAlgorithm = (size: number) => {
  let wfcMap = new WfcMap(size, rules, tiles)
  wfcMap.createMap()
  return wfcMap
}

export const runAlgorithmPrint = (size = 10, consoleLog = false, stepwise = false) => {
  let maps = []
  const wfcMap = new WfcMap(size, rules, tiles)
  const UI =  new WfcUI()
  let fails = 0
  while (fails < 5) {
    if (wfcMap.isSolved()) {
      console.log('Success!')
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
      console.log('Fail!')
    }
  }
  if (consoleLog) {
    console.log(UI.printMap(wfcMap))
    for (let wfcMap of maps) {
      console.log(wfcMap)
    }
  }
  return wfcMap
}
