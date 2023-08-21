import { WfcTile } from "../../types/wfcTile";
import { WfcCell } from "./wfcCell";
import { WfcRule } from "../../types/wfcRule";

export class WfcMap {
  tiles: WfcTile[]
  ruleSet: WfcRule[]
  cells: WfcCell[][]
  size: number
  hasContradiction: boolean
  constructor(size: number, rules: Record<any,any>[], tiles: Record<any,any>[]) {
    this.size = size
    this.setTiles(tiles)
    this.setRules(rules)
    this.setCells()
  }

  reset = () => {
    this.setCells()
    this.hasContradiction = false
  }

  setTiles = (tiles: Record<any,any>[]) => {
    this.tiles = []
    for (let tile of tiles) {
      this.tiles.push(new WfcTile(tile.name, tile.frequency, tile.colour))
    }
  }

  setRules = (rules: Record<any,any>[]) => {
    this.ruleSet = []
    for (let rule of rules) {
      this.ruleSet.push(new WfcRule(rule.firstTile, rule.secondTile, rule.direction))
    }
  }

  setCells = () => {
    this.cells = []
    for (let y = 0; y < this.size; y++) {
      this.cells.push([])
      for (let x = 0; x < this.size; x++) {
        this.cells[y].push(new WfcCell(x, y, this))
      }
    }
  }

  isSolved = () => {
    for (let row of this.cells) {
      for (let cell of row) {
        if (!cell.collapsed) {
          return false
        }
      }
    }
    return true
  }

  findLowestEntropyCell = () => {
    let lowest = null as null|WfcCell
    for (let row of this.cells) {
      for (let cell of row) {
        if (!cell.collapsed && (lowest == null || cell.entropy() < lowest.entropy())) {
          lowest = cell
        }
      }
    }

    let lowCells = [] as WfcCell[]
    for (let row of this.cells) {
      for (let cell of row) {
        if (!cell.collapsed && cell.entropy() == lowest.entropy()) {
          lowCells.push(cell)
        }
      }
    }

    const index = Math.floor(Math.random() * lowCells.length)
    return lowCells[index]
  }

  collapse = (cell: WfcCell) => {
    cell.pickState()
    for (let neighbour of this.neighbours(cell)) {
      if (!neighbour.collapsed) {
        neighbour.restrict(cell)
      }
    }
    // this.propagateChange(cell)
  }

  propagateChange = (cell: WfcCell) => {
    let changeQueue = this.neighbours(cell)
    let queueCell = null as null|WfcCell
    let change = false
    while (changeQueue.length > 0) {
      queueCell = changeQueue.pop()
      change = cell.restrictPropagate(queueCell)
      if (this.hasContradiction) {
        break
      }
      if (change) {
        this.propagateChange(queueCell)
      }
    }
  }

  neighbours = (cell: WfcCell) => {
    let neighbours = [] as WfcCell[]
    if (cell.x > 0) {
      neighbours.push(this.cells[cell.y][cell.x-1])
    }
    if (cell.x < this.size-1) {
      neighbours.push(this.cells[cell.y][cell.x+1])
    }
    if (cell.y > 0) {
      neighbours.push(this.cells[cell.y-1][cell.x])
    }
    if (cell.y < this.size-1) {
      neighbours.push(this.cells[cell.y+1][cell.x])
    }
    return neighbours
  }

  createMap = () => {
    let fails = 0
    let cell = null as null|WfcCell
    while (fails < 5) {
      if (this.isSolved()) {
        break
      }
      cell = this.findLowestEntropyCell()
      this.collapse(cell)
      if (this.hasContradiction) {
        this.reset()
        fails++
      }
    }
    return fails
  }
}