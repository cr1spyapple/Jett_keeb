print("Starting")
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kb import data_pin
from kmk.modules.split import Split, SplitSide
from storage import getmount

keyboard = KMKKeyboard()

side = SplitSide.RIGHT if str(getmount('/').label)[-1] == 'R' else SplitSide.LEFT

if side == SplitSide.RIGHT:
    keyboard.col_pins = (board.GP21, board.GP20, board.GP19, board.GP18, board.GP17, board.GP16) 
    keyboard.row_pins = (board.GP28, board.GP27, board.GP26, board.GP22, board.GP14)
    keyboard.diode_orientation = DiodeOrientation.COL2ROW 
    keyboard.keymap = [
    [
        KC.N7, KC.N8, KC.N9, KC.N0, KC.MINS, KC.EQL,
        KC.Y, KC.U, KC.I, KC.O, KC.P, KC.BSPC,
        KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT,
        KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.NO,
        KC.SPC, KC.RSFT, KC.RCTL, KC.NO, KC.NO, KC.NO
    ]
]
else:
    keyboard.col_pins = (board.GP5, board.GP4, board.GP3, board.GP2, board.GP1, board.GP16) 
    keyboard.row_pins = (board.GP6, board.GP7, board.GP8, board.GP9, board.GP10)
    keyboard.diode_orientation = DiodeOrientation.COL2ROW
    keyboard.keymap = [
    [
        KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6,
        KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y,
        KC.A, KC.S, KC.D, KC.F, KC.G, KC.H,
        KC.Z, KC.X, KC.C, KC.V, KC.B, KC.NO,
        KC.NO, KC.NO, KC.MO(1), KC.SPC, KC.LSFT, KC.LCTL
    ]
]

split = Split(split_side=none,  data_pin=GP0)
keyboard.modules.append(split)

if __name__ == '__main__':
    keyboard.go()
