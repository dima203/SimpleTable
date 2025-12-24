import textwrap
from typing import Any


class Table:
    def __init__(self, *, headers: list[str] | None = None) -> None:
        self.__data: list[dict[str, Any]] = []

        self.headers: list[str] = [] if headers is None else headers

        self.align = {key: "^" for key in headers}

        self.min_width: dict[str, int | None] = {key: None for key in headers}
        self.max_width: dict[str, int | None] = {key: None for key in headers}

        self.max_table_width = None
        self.min_table_width = None

        self.none_format = ''
        self.wrap = True

        self.vertical_character = "|"
        self.horizontal_character = "="
        self.top_junction_character = "+"
        self.top_left_junction_character = "+"
        self.top_right_junction_character = "+"
        self.left_junction_character = "+"
        self.right_junction_character = "+"
        self.junction_character = "+"
        self.bottom_junction_char = "+"
        self.bottom_left_junction_char = "+"
        self.bottom_right_junction_char = "+"

    def add_column(
        self,
        column_name: str,
        *,
        default: Any = None,
        align: str = "^",
        min_width: int | None = None,
        max_width: int | None = None,
    ) -> None:
        self.headers.append(column_name)
        self.align[column_name] = align
        self.min_width[column_name] = min_width
        self.max_width[column_name] = max_width

        for row in self.__data:
            row[column_name] = default

    def add_row(self, row: list[Any]) -> None:
        self.__data.append(dict(zip(self.headers, row)))

    def __str__(self) -> str:
        strings = [
            self.__get_top_delimiter_string(),
            self.__get_header_string(),
            self.__get_delimiter_string(),
            *self.__get_table_strings(),
            self.__get_bottom_delimiter_string(),
        ]
        return "\n".join(strings)

    def __get_top_delimiter_string(self) -> str:
        columns_length = self.__get_formated_columns_length().values()
        return (
            self.top_left_junction_character
            + self.top_junction_character.join(
                self.horizontal_character * length for length in columns_length
            )
            + self.top_right_junction_character
        )

    def __get_delimiter_string(self) -> str:
        columns_length = self.__get_formated_columns_length().values()
        return (
            self.left_junction_character
            + self.junction_character.join(
                self.horizontal_character * length for length in columns_length
            )
            + self.right_junction_character
        )

    def __get_bottom_delimiter_string(self) -> str:
        columns_length = self.__get_formated_columns_length().values()
        return (
            self.bottom_left_junction_char
            + self.bottom_junction_char.join(
                self.horizontal_character * length for length in columns_length
            )
            + self.bottom_right_junction_char
        )

    def __get_header_string(self) -> str:
        columns_length = self.__get_formated_columns_length()
        return (
            "".join(
                f"{self.vertical_character}{key: {self.align[key]}{columns_length[key]}}"
                for key in self.headers
            )
            + self.vertical_character
        )

    def __get_table_strings(self) -> list[str]:
        strings = []
        for row in self.__data:
            strings.extend(self.__get_row_strings(row))
        return strings

    def __get_row_strings(self, row: dict[str, Any]) -> list[str]:
        columns_length = self.__get_formated_columns_length()
        row_data_strings = {key: self.__get_data_strings(data, columns_length[key]) for key, data in row.items()}
        strings = []
        max_data_length = len(max(row_data_strings.values(), key=len))
        for i in range(max_data_length):
            string = ""
            for key, data in row_data_strings.items():
                index = len(data) - max_data_length + i
                if index >= 0:
                    string += f"{self.vertical_character}{data[index]: {self.align[key]}{columns_length[key]}}"
                else:
                    string += f"{self.vertical_character}{"": {self.align[key]}{columns_length[key]}}"
            string += self.vertical_character
            strings.append(string)
        return strings

    def __get_data_strings(self, data: Any, length: int) -> list[str]:
        return self.__format_data(data, length).split('\n')

    def __format_data(self, data: Any, length: int) -> str:
        return self.__format_length(self.__format_none(data), length)

    def __format_length(self, data: str, length: int) -> str:
        return textwrap.fill(
            data,
            length,
            placeholder="",
            max_lines=None if self.wrap else 1,
        )

    def __format_none(self, data: Any) -> str:
        return str(data) if data is not None else self.none_format

    def __get_formated_columns_length(self) -> dict[str, int]:
        columns_length = self.__get_max_columns_length()
        for key, length in columns_length.items():
            if self.min_width[key] is not None:
                columns_length[key] = self.min_width[key]

        table_width = sum(columns_length.values()) + len(columns_length) + 1

        if self.min_table_width is not None and table_width < self.min_table_width:
            need_length = self.min_table_width - table_width
        elif self.max_table_width is not None and table_width > self.max_table_width:
            need_length = self.max_table_width - table_width
        else:
            need_length = 0

        added_length = self.__get_added_columns_length(need_length, columns_length)
        return {key: columns_length[key] + added_length[key] for key in columns_length}

    def __get_added_columns_length(self, need_length: int, current_length: dict[str, int]) -> dict[str, int]:
        allocations = {key: 0 for key in current_length}
        weights = current_length.copy()
        total_weight = sum(weights.values())
        is_growth = True if need_length >= 0 else False  # Нужно увеличить или уменьшить размер таблицы

        for _ in range(abs(need_length)):
            for key in weights:
                if is_growth:
                    if self.max_width[key] is not None:
                        if weights[key] + allocations[key] >= self.max_width[key]:
                            weights[key] = 0
                            total_weight = sum(weights.values())
                else:
                    if self.min_width[key] is not None:
                        if weights[key] - allocations[key] <= self.min_width[key]:
                            weights[key] = 0
                            total_weight = sum(weights.values())

            # Для каждого объекта вычисляем, насколько он "недополучил"
            deficits = {}
            for key, length in weights.items():
                expected = length / total_weight * (sum(allocations.values()) + 1)
                deficit = expected - allocations[key]
                deficits[key] = deficit

            # Даем единицу объекту с наибольшим дефицитом
            idx = max(deficits, key=lambda key: deficits[key])
            allocations[idx] += 1

        if not is_growth:
            allocations = {key: -value for key, value in allocations.items()}

        return allocations

    def __get_max_columns_length(self) -> dict[str, int]:
        return {
            key: self.__get_max_length_for_column(key) for key in self.headers
        }

    def __get_max_length_for_column(self, column_name: str) -> int:
        max_data_length = len(
            str(
                max(self.__data, key=lambda row: len(str(row[column_name])))[
                    column_name
                ]
            )
        )
        return (
            max_data_length if max_data_length >= len(column_name) else len(column_name)
        )

    def __get_max_length(self) -> int:
        strings = self.__get_raw_strings()
        max_length = len(max(strings, key=len))
        return max_length

    def __get_raw_strings(self) -> list[str]:
        strings = []
        header_string = ""
        for header in self.headers:
            header_string += f"{self.vertical_character}{header}"
        header_string += self.vertical_character
        strings.append(header_string)
        for row in self.__data:
            string = ""
            for header in self.headers:
                string += f"{self.vertical_character}{row[header]}"
            string += self.vertical_character
            strings.append(string)
        return strings
