export class WfcDirections {
  static RIGHT = 'RIGHT'
  static LEFT = 'LEFT'
  static UP = 'UP'
  static DOWN = 'DOWN'

  static reverse = (direction: string) => {
    if (direction === WfcDirections.RIGHT) { return WfcDirections.LEFT}
    if (direction === WfcDirections.LEFT) { return WfcDirections.RIGHT}
    if (direction === WfcDirections.UP) { return WfcDirections.DOWN}
    if (direction === WfcDirections.DOWN) { return WfcDirections.UP }
  }
}