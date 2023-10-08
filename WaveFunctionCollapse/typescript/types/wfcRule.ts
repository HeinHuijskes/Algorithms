export class WfcRule {
  firstState: string
  secondState: string
  direction: string
  constructor(firstState: string, secondState: string, direction: string) {
    this.firstState = firstState
    this.secondState = secondState
    this.direction = direction
  }
}