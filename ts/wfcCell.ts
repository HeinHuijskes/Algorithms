import { WfcMap } from "./wfcMap";
import { WfcTile } from "./wfcTile";

export class WfcCell {
  x = 0
  y = 0
  wfcMap = null
  states = [] as WfcTile[]
  collapsed = false
  state = null as null|WfcTile
  constructor(x: number, y: number, wfcMap: WfcMap) {
    this.x = x
    this.y = y
    this.wfcMap = wfcMap
    this.setStates()
  }

  setStates = () => {
    this.states = this.wfcMap.tiles.map((tile: WfcTile) => tile)
  }

  entropy = () => {
    return this.states.length
  }

  pickState = () => {
    const totalWeight = this.states.map((state: WfcTile) => state.frequency).reduce((a, b) => a + b)
    const randomValue = Math.random() * totalWeight
    let weight = 0
    let index = this.states.length - 1
    for (let key in this.states) {
      weight += this.states[key].frequency
      if (weight > randomValue) {
        index = parseInt(key)
        break
      }
    }
    this.state = this.states[index]
    this.collapsed = true
    this.states = [this.state]
  }

  restrict = (cell: WfcCell) => {
    let possible = false
    const direction = this.getDirection(cell)
    let possibleStates = [] as WfcTile[]
    for (let state of this.states) {
      for (let rule of this.wfcMap.ruleSet) {
        if ((rule.direction == direction) && ((rule.firstState === state.name && rule.secondState === cell.state.name)
                                          || (rule.secondState === state.name && rule.firstState === cell.state.name))) {
          possible = true
        }
      }
      if (possible) {
        possibleStates.push(state)
        possible = false
      }
    }
    this.states = possibleStates
    if (this.states.length == 0) {
      this.wfcMap.hasContradiction = true
    }
  }

  restrictPropagate = (cell: WfcCell) => {
    // TODO: implement propagation properly and working
    return false
  }

  getDirection = (cell: WfcCell) => {
    if (cell.x > this.x && cell.y == this.y) {
      return this.wfcMap.DIRECTIONS.RIGHT
    }
    if (cell.x < this.x && cell.y == this.y) {
      return this.wfcMap.DIRECTIONS.LEFT
    }
    if (cell.x == this.x && cell.y > this.y) {
      return this.wfcMap.DIRECTIONS.DOWN
    }
    return this.wfcMap.DIRECTIONS.UP
  }
}