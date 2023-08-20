import { WfcTile } from "./wfcTile";
import { WfcCell } from "./wfcCell";
import { WfcRule } from "./wfcRule";

export class WfcMap {
  DIRECTIONS = {
    RIGHT: 'RIGHT',
    LEFT: 'LEFT',
    UP: 'UP',
    DOWN: 'DOWN',
  }
  allDirections = () => [this.DIRECTIONS.RIGHT, this.DIRECTIONS.LEFT, this.DIRECTIONS.UP, this.DIRECTIONS.DOWN]

  tiles: WfcTile[]
  ruleSet: WfcRule[]
  cells: WfcCell[][]
  size: number
  hasContradiction: boolean
  constructor(size: number) {
    this.size = size
    this.reset()
  }

  reset = () => {
    this.setTiles()
    this.setRules()
    this.setCells()
    this.hasContradiction = false
  }

  setTiles = () => {
    // TODO: Use fixture in yaml or json file
    this.tiles = []
    this.tiles.push(new WfcTile('HEAVEN', 8, 0))
    this.tiles.push(new WfcTile('MOUNTAIN', 15, 1))
    this.tiles.push(new WfcTile('LAND', 15, 2))
    this.tiles.push(new WfcTile('COAST', 15, 3))
    this.tiles.push(new WfcTile('SEA', 15, 4))
    this.tiles.push(new WfcTile('OCEAN', 8, 5))
  }

  setRules = () => {
    // TODO: Also fixture
    this.ruleSet = []
    this.allDirections().map((direction) => this.ruleSet.push(new WfcRule('HEAVEN', 'HEAVEN', direction)))
    this.allDirections().map((direction) => this.ruleSet.push(new WfcRule('HEAVEN', 'MOUNTAIN', direction)))
    this.allDirections().map((direction) => this.ruleSet.push(new WfcRule('MOUNTAIN', 'MOUNTAIN', direction)))
    this.allDirections().map((direction) => this.ruleSet.push(new WfcRule('MOUNTAIN', 'LAND', direction)))
    this.allDirections().map((direction) => this.ruleSet.push(new WfcRule('LAND', 'LAND', direction)))
    this.allDirections().map((direction) => this.ruleSet.push(new WfcRule('LAND', 'COAST', direction)))
    this.allDirections().map((direction) => this.ruleSet.push(new WfcRule('COAST', 'COAST', direction)))
    this.allDirections().map((direction) => this.ruleSet.push(new WfcRule('COAST', 'SEA', direction)))
    this.allDirections().map((direction) => this.ruleSet.push(new WfcRule('SEA', 'SEA', direction)))
    this.allDirections().map((direction) => this.ruleSet.push(new WfcRule('SEA', 'OCEAN', direction)))
    this.allDirections().map((direction) => this.ruleSet.push(new WfcRule('OCEAN', 'OCEAN', direction)))
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