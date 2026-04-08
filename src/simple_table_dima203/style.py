from dataclasses import dataclass


@dataclass
class TableStyle:
    vertical_character: str = "|"
    horizontal_character: str = "-"
    top_junction_character: str = "+"
    top_left_junction_character: str = "+"
    top_right_junction_character: str = "+"
    left_junction_character: str = "+"
    right_junction_character: str = "+"
    junction_character: str = "+"
    bottom_junction_char: str = "+"
    bottom_left_junction_char: str = "+"
    bottom_right_junction_char: str = "+"


DEFAULT = TableStyle()

SINGLE_BORDER = TableStyle(
    vertical_character="│",
    horizontal_character="─",
    junction_character="┼",
    top_junction_character="┬",
    bottom_junction_char="┴",
    right_junction_character="┤",
    left_junction_character="├",
    top_right_junction_character="┐",
    top_left_junction_character="┌",
    bottom_right_junction_char="┘",
    bottom_left_junction_char="└",
)

DOUBLE_BORDER = TableStyle(
    vertical_character="║",
    horizontal_character="═",
    junction_character="╬",
    top_junction_character="╦",
    bottom_junction_char="╩",
    right_junction_character="╣",
    left_junction_character="╠",
    top_right_junction_character="╗",
    top_left_junction_character="╔",
    bottom_right_junction_char="╝",
    bottom_left_junction_char="╚",
)

CLEAR = TableStyle(
    vertical_character=" ",
    horizontal_character=" ",
    junction_character=" ",
    top_junction_character=" ",
    bottom_junction_char=" ",
    right_junction_character=" ",
    left_junction_character=" ",
    top_right_junction_character=" ",
    top_left_junction_character=" ",
    bottom_right_junction_char=" ",
    bottom_left_junction_char=" ",
)

MARKDOWN = TableStyle(
    junction_character="|",
    right_junction_character="|",
    left_junction_character="|",
)
