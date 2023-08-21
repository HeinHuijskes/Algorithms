import { WfcDirections } from "../util/wfcDirections";
import { WfcColours } from "../../ui/wfcColours";

export class WfcMapReader {
  /**
   * Finds the rules of a ruleSet belonging to a single cell and its neighbours. Returns a list of all found rules, one
   * per existing neighbour. A rule is formatted as an object, e.g.:
   * {firstTile:'OCEAN',secondTile:'LAND',direction:'LEFT'}
   * @param inputMap Map of cell states
   * @param rowIndex Index of the considered row
   * @param cellIndex Index of the considered cell
   */
  static findRules = (inputMap: string[][], rowIndex: number, cellIndex: number) => {
    // TODO: Add weights to directions
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

  /**
   * Removes redundant rules from a ruleSet. Removes literal doubles as well as rules that essentially mean the same,
   * e.g. {SEA,LAND,RIGHT} is the same as {LAND,SEA,LEFT}. The last part is not strictly necessary, and requires
   * additional logic in other places. Therefor it could be removed later on.
   * @param ruleSet
   */
  static reduceRules = (ruleSet: Record<any,any>[]) => {
    let reducedRules = [] as Record<any,any>[]
    for (let rule of ruleSet) {
      let containsRule = false
      for (let reducedRule of reducedRules) {
        // Check if the considered rule is either a literal duplicate or a differently written duplicate.
        // E.g. {firstTile,secondTile,direction} == rule, or {secondTile,firstTile,reversed(direction)} == rule
        if ((rule.direction === reducedRule.direction
            && reducedRule.firstTile === rule.firstTile
            && reducedRule.secondTile === rule.secondTile)
          || (rule.direction === WfcDirections.reverse(reducedRule.direction)
            && reducedRule.firstTile === rule.secondTile
            && reducedRule.secondTile === rule.firstTile)) {
          containsRule = true
        }
      }
      if (!containsRule) {
        reducedRules.push(rule)
      }
    }
    return reducedRules
  }

  /**
   * Retrieve unique tiles and their properties from an inputMap. Finds all unique tiles in the map, and how often each
   * tile occurs. If a colour mapping is provided, it maps each tile to its colour and sets it for the tiles. Otherwise
   * defaults to white colouring.
   * @param inputMap
   * @param colouring
   */
  static getTiles = (inputMap: string[][], colouring: null|Record<string,string>) => {
    let uniqueTiles = []
    inputMap.map((row) => row.map((cell) => { if (!uniqueTiles.includes(cell)) { uniqueTiles.push(cell) } }))

    let tiles = [] as Record<any,any>[]
    for (let tile of uniqueTiles) {
      let count = 0
      // Count the amount of occurrences of each tile
      inputMap.map((row) => row.map((value) => {
        if (value === tile) {
          count++
        }}))
      // If a colour mapping exists and contains the given tile, apply it. Otherwise, apply WHITE.
      let colour = colouring ? colouring[tile] ? colouring[tile] : WfcColours.WHITE : WfcColours.WHITE
      tiles.push({ name: tile, frequency: count, colour: colour})
    }
    return tiles
  }

  /**
   * Read a given input map and parse it to size, tileSet and ruleSet. Returned as objects, e.g.:
   * {size:size,rules:ruleSet,tiles:tileSet}
   * @param inputMap
   * @param colouring
   */
  static readMap = (inputMap: string[][], colouring=null) => {
    let size = inputMap.length
    let ruleSet = []

    for (let rowIndex in inputMap) {
      let row = inputMap[rowIndex]
      for (let cellIndex in row) {
        let newRules = WfcMapReader.findRules(inputMap, parseInt(rowIndex), parseInt(cellIndex))
        ruleSet = ruleSet.concat(newRules)
      }
    }

    return { size: size, rules: WfcMapReader.reduceRules(ruleSet), tiles: WfcMapReader.getTiles(inputMap, colouring)}
  }
}