import { WfcMap } from "./wfcMap";

export class WfcUI {
  // grey_gradient = ['\u001b[48;5;240m', '\u001b[48;5;242m', '\u001b[48;5;244m', '\u001b[48;5;246m', '\u001b[48;5;248m',
  //                    '\u001b[48;5;250m']
  // map_colours = ['\u001b[47m', '\u001b[40m', '\u001b[42m', '\u001b[43m', '\u001b[46m', '\u001b[44m']

  printMap = (wfcMap: WfcMap) => {
    let mapString = ''
    for (let row of wfcMap.cells) {
      for (let cell of row) {
        if (cell.state && wfcMap.tiles.map((tile) => tile.name).includes(cell.state.name)) {
          mapString += [cell.state.colour]
          // mapString += '   '
          mapString += ' '
          mapString += cell.state.name.charAt(0)
          mapString += ' \u001b[0m'
        } else {
          mapString += '   \u001b[0m'
        }
      }
      mapString += '\n'
    }
    return mapString
  }
}