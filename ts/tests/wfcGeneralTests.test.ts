import { test, expect, describe } from "vitest";
import { runAlgorithm, runAlgorithmPrint } from '../runWfc'

// TODO: Add fixtures for map settings and rule sets
// TODO: Add unit tests for all code blocks
// TODO: Extract functions where needed/useful for unit tests

const timeTest = (size = 20, iterations = 100) => {
  let attempts = []
  const timerStart = new Date().getTime()
  for (let iteration = 0; iteration < iterations; iteration++) {
    attempts.push(runAlgorithm(size).isSolved())
  }
  const timerEnd = new Date().getTime()
  const runTime = (timerEnd - timerStart) / 1000
  const successes = attempts.filter(Boolean).length
  console.log(`Ran ${iterations} iterations of size ${size*size} in ${runTime} seconds`)
  console.log(`${successes} successful attempts and ${iterations - successes} failures`)
  return runTime
}

describe('General algorithm functionality', () => {
  test('Algorithm looks good',  () => {
    const consoleLog = true
    expect(runAlgorithmPrint(5, consoleLog, true).isSolved()).toBe(true)
    expect(runAlgorithmPrint(30, consoleLog).isSolved()).toBe(true)
  })

  test('Algorithm runs fast', () => {
    const size = 20
    const iterations = 1000
    const unAcceptable = size * size * iterations / 50000
    const time = timeTest(size, iterations)
    console.log(`Acceptable time: ${unAcceptable}`)
    console.log(`Actual time:     ${time}`)
    expect(time).toBeLessThan(unAcceptable)
  })

  test('Algorithm can handle big maps', () => {
    expect(runAlgorithm(100).isSolved()).toBe(true)
  })
})
