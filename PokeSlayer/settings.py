import math 

# Game Settings
RES = WIDTH, HEIGHT = 1600, 900
HALF_RES = HALF_WIDTH, HALF_HEIGHT = WIDTH//2, HEIGHT//2
FPS = 60

# Player Settings
PLAYER_POS = 1.5, 2.5
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.002
PLAYER_SCALE_SIZE = 120

# Mouse Settings
MOUSE_SENS = 0.00008
MOUSE_MAX_REL = 40
MOUSE_BORDER_LEFT = 100
MOUSE_BORDER_RIGHT = WIDTH - MOUSE_BORDER_LEFT

# Raycast Settings
FOV = math.pi / 3
HALF_FOV = FOV/2
RAY_NUM = WIDTH //2
HALF_RAY_NUM = RAY_NUM //2
DELTA_ANGLE = FOV / RAY_NUM
MAX_DEPTH = 20

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH//RAY_NUM

TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = TEXTURE_SIZE//2