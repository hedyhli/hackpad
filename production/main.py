# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros

keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)

PINS = [board.D1, board.D3, board.D4, board.D2]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.UP, KC.LEFT, KC.DOWN, KC.LEFT]
]

if __name__ == '__main__':
    keyboard.go()
