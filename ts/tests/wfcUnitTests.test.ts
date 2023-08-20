import { beforeAll, describe, expect, test } from "vitest";
import { WfcMap } from "../wfcMap";
import largeMap from "../fixtures/largeMap";

let wfcMap: WfcMap

beforeAll(() => {
  const rules = largeMap.rules
  const tiles = largeMap.tiles
  wfcMap = new WfcMap(10, rules, tiles)
})

describe('Unit tests', () => {
  describe('Map', () => {
    describe('Neighbours', () => {
      test('Map finds correct neighbours in the middle', () => {
        const x = 3
        const y = 3
        const cell = wfcMap.cells[x][y]
        const neighbours = wfcMap.neighbours(cell)
        expect(neighbours.length).toBe(4)
        expect(neighbours[0].x).toBe(x-1)
        expect(neighbours[1].x).toBe(x+1)
        expect(neighbours[2].x).toBe(x)
        expect(neighbours[3].x).toBe(x)
        expect(neighbours[0].y).toBe(y)
        expect(neighbours[1].y).toBe(y)
        expect(neighbours[2].y).toBe(y-1)
        expect(neighbours[3].y).toBe(y+1)
      })

      test('Map finds correct neighbours on the edges', () => {
        let x = 0
        let y = 0
        let cell = wfcMap.cells[x][y]
        let neighbours = wfcMap.neighbours(cell)
        expect(neighbours.length).toBe(2)
        expect(neighbours[0].x).toBe(x+1)
        expect(neighbours[1].x).toBe(x)
        expect(neighbours[0].y).toBe(y)
        expect(neighbours[1].y).toBe(y+1)

        x = wfcMap.cells.length-1
        y = wfcMap.cells.length-1
        cell = wfcMap.cells[x][y]
        neighbours = wfcMap.neighbours(cell)
        expect(neighbours.length).toBe(2)
        expect(neighbours[0].x).toBe(x-1)
        expect(neighbours[1].x).toBe(x)
        expect(neighbours[0].y).toBe(y)
        expect(neighbours[1].y).toBe(y-1)
      })
    })
  })
})
