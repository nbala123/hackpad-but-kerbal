import board
from kmk.kmk_keyboard import KMKKeybaord
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()
layers = Layers()

keyboard.modules.append(layer)
keyboard.modules.append(encoder)

encoder_handler.pins(board.D3, board.D4)
encoder.map = [(KC.NO, KC.NO)]
KEY_PINS = [board.D1, board.D6, board.D7, board.D8, board.D9, board.D10, board.D11]

keyboard_matrix = DigitalIO(keys=KEY_PINS, pull=False)

MAIN_LAYER = [KC.SPACE, KC.Q, KC.W, KC.e, KC.A, KC.S, KC.D]
SEC_LAYER = [KC.SPACE, KC.H, KC.I, KC.N, KC.J, KC.K, KC.L]

keyboard.keymap = [
    MAIN_LAYER,
    SEC_LAYER
]

layer = 0

def encoder_callback(direction, position):
    if direction > 0:
        layer += 1
    if direction < 0:
        layer -= 1
    keyboard.active_layers.clear()
    keyboard.active_layers.append(layer%2)

keyboard.encoder_callbacks = [(0, encoder_callback)]

if __name__ == "__main__":
    keyboard.go()
