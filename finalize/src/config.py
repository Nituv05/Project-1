import os
DATA_DIR = "data"
GRAPH_FILE_WALK = os.path.join(DATA_DIR, "hanoi_walk.graphml")
GRAPH_FILE_DRIVE = os.path.join(DATA_DIR, "hanoi_drive.graphml")

DISTRICTS = [
    "Hoan Kiem District, Hanoi, Vietnam",
    "Ba Dinh District, Hanoi, Vietnam",
    "Dong Da District, Hanoi, Vietnam",
    "Hai Ba Trung District, Hanoi, Vietnam",
    "Tay Ho District, Hanoi, Vietnam",
    "Cau Giay District, Hanoi, Vietnam",
    "Thanh Xuan District, Hanoi, Vietnam",
    "Hoang Mai District, Hanoi, Vietnam",
    "Long Bien District, Hanoi, Vietnam",
    "Bac Tu Liem District, Hanoi, Vietnam",
    "Nam Tu Liem District, Hanoi, Vietnam",
    "Ha Dong District, Hanoi, Vietnam"
]

SPEED_CONFIG = {
    "walk": 4.5,
    "bike": 30.0,
    "car": 40.0
}

COLORS = {
    "walk": "green",
    "bike": "blue",
    "car": "red"
}