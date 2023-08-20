export class WfcTile {
  name = ''
  frequency = 0
  colourLevel = 0
  constructor(name: string, frequency: number, colourLevel: number) {
    this.name = name
    this.frequency = frequency
    this.colourLevel = colourLevel
  }
}