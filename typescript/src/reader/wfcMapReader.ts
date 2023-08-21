import { WfcMap } from "../map/wfcMap";
import { WfcDirections } from "../util/wfcDirections";
import { WfcColours } from "../../ui/wfcColours";

export class WfcMapReader {
  /**
   * Finds the rules of a ruleSet belonging to a single cell and its neighbours. Returns a list of all found rules, one
   * per existing neighbour. A rule is formatted as an object, e.g.:
   *
   * {firstTile: 'OCEAN', secondTile: 'LAND', direction: 'LEFT'}
   * @param inputMap Map of cell states
   * @param rowIndex Index of the considered row
   * @param cellIndex Index of the considered cell
   */
  static findRules = (inputMap: string[][], rowIndex: number, cellIndex: number) => {
    let ruleSet = [] as Record<any,any>[]
    const cell = inputMap[rowIndex][cellIndex]
    let neighbour: string

    if (cellIndex > 0) {
      neighbour = inputMap[rowIndex][cellIndex-1]
      ruleSet.push({firstTile: cell, secondTile: neighbour, direction: 'LEFT'})
    }
    if (cellIndex < inputMap.length-1) {
      neighbour = inputMap[rowIndex][cellIndex+1]
      ruleSet.push({firstTile: cell, secondTile: neighbour, direction: 'RIGHT'})
    }
    if (rowIndex > 0) {
      neighbour = inputMap[rowIndex-1][cellIndex]
      ruleSet.push({firstTile: cell, secondTile: neighbour, direction: 'UP'})
    }

    if (rowIndex < inputMap.length-1) {
      neighbour = inputMap[rowIndex+1][cellIndex]
      ruleSet.push({firstTile: cell, secondTile: neighbour, direction: 'DOWN'})
    }

    return ruleSet
  }

  static reduceRules = (ruleSet: Record<any,any>[]) => {
    let reducedRules = [] as Record<any,any>[]
    for (let rule of ruleSet) {
      let containsRule = false
      for (let reducedRule of reducedRules) {
        if ((rule.direction === reducedRule.direction
            && reducedRule.firstTile === rule.firstTile
            && reducedRule.secondTile === rule.secondTile)
          || (rule.direction === WfcDirections.reverse(reducedRule.direction)
            && reducedRule.firstTile === rule.secondTile
            && reducedRule.secondTile === rule.firstTile
            && reducedRule.firstTile !== reducedRule.secondTile)) {
          containsRule = true
        }
      }
      if (!containsRule) {
        reducedRules.push(rule)
      }
    }
    return reducedRules
  }

  static getTiles = (inputMap: string[][], colouring) => {
    let uniqueTiles = []
    inputMap.map((row) => row.map((cell) => { if (!uniqueTiles.includes(cell)) { uniqueTiles.push(cell) } }))

    let tiles = [] as Record<any,any>[]
    for (let tile of uniqueTiles) {
      let count = 0
      inputMap.map((row) => row.map((value) => {
        if (value === tile) {
          count++
        }}))
      let colour = colouring ? colouring[tile] : WfcColours.WHITE
      tiles.push({ name: tile, frequency: count, colour: colour})
    }
    return tiles
  }

  static readMap = (inputMap: string[][], colouring=null) => {
    let size = inputMap.length
    let ruleSet = []

    for (let rowIndex in inputMap) {
      let row = inputMap[rowIndex]
      for (let cellIndex in row) {
        let cell = row[cellIndex]
        let newRules = WfcMapReader.findRules(inputMap, parseInt(rowIndex), parseInt(cellIndex))
        ruleSet = ruleSet.concat(newRules)
      }
    }

    return { size: size, rules: WfcMapReader.reduceRules(ruleSet), tiles: WfcMapReader.getTiles(inputMap, colouring)}
  }
}