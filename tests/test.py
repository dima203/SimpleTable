import pytest

from src.simple_table_dima203 import Table, SINGLE_BORDER


class TestTable:
    def test_table_print(self) -> None:
        print()
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.title = "User Ages for Admins"
        table.inline_title = "Test Table"
        table.title_border = False
        table.min_table_width = 20
        table.min_width["id"] = 5
        table.add_row(["User", 13])
        table.add_row(["User2", 45])
        table.add_delimiter()
        table.add_row(["Average", 17.5])
        print(table)

    def test_empty_table_print(self) -> None:
        table = Table(style=SINGLE_BORDER)
        assert str(table) == ("┌┐\n"
                              "├┤\n"
                              "└┘")

    def test_table_without_data_print(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        assert str(table) == ("┌────┬───┐\n"
                              "│name│age│\n"
                              "├────┼───┤\n"
                              "└────┴───┘")

    def test_table_with_data_print(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.add_row(["Alex gfjdkljgkdjklfgld", 22])
        assert str(table) == ("┌──────────────────────┬───┐\n"
                              "│         name         │age│\n"
                              "├──────────────────────┼───┤\n"
                              "│Alex gfjdkljgkdjklfgld│22 │\n"
                              "└──────────────────────┴───┘")

    def test_table_min_width_print(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.min_table_width = 20
        assert str(table) == ("┌──────────┬───────┐\n"
                              "│   name   │  age  │\n"
                              "├──────────┼───────┤\n"
                              "└──────────┴───────┘")

    def test_table_with_title_print(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.title = "TEST"
        assert str(table) == ("   TEST   \n"
                              "┌────┬───┐\n"
                              "│name│age│\n"
                              "├────┼───┤\n"
                              "└────┴───┘")

    def test_table_with_left_title_print(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.title = "TEST"
        table.title_align = "<"
        assert str(table) == (" TEST     \n"
                              "┌────┬───┐\n"
                              "│name│age│\n"
                              "├────┼───┤\n"
                              "└────┴───┘")

    def test_table_with_right_title_print(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.title = "TEST"
        table.title_align = ">"
        assert str(table) == ("     TEST \n"
                              "┌────┬───┐\n"
                              "│name│age│\n"
                              "├────┼───┤\n"
                              "└────┴───┘")

    def test_table_with_bordered_title_print(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.title = "TEST"
        table.title_border = True
        assert str(table) == ("┌────────┐\n"
                              "│  TEST  │\n"
                              "├────┬───┤\n"
                              "│name│age│\n"
                              "├────┼───┤\n"
                              "└────┴───┘")

    def test_table_with_inline_title_print(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.inline_title = "TEST"
        assert str(table) == ("┌──TEST──┐\n"
                              "│name│age│\n"
                              "├────┼───┤\n"
                              "└────┴───┘")

    def test_table_with_left_inline_title_print(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.inline_title = "TEST"
        table.inline_title_align = "<"
        assert str(table) == ("┌─TEST───┐\n"
                              "│name│age│\n"
                              "├────┼───┤\n"
                              "└────┴───┘")

    def test_table_with_right_inline_title_print(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.inline_title = "TEST"
        table.inline_title_align = ">"
        assert str(table) == ("┌───TEST─┐\n"
                              "│name│age│\n"
                              "├────┼───┤\n"
                              "└────┴───┘")

    def test_table_with_wrong_inline_title_align_error(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.inline_title = "TEST"
        table.inline_title_align = ""
        with pytest.raises(ValueError) as e_info:
            print(table)


    def test_table_with_large_inline_title_print(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.inline_title = "TESTING TABLE"
        assert str(table) == ("┌─TESTING TABLE─┐\n"
                              "│  name  │ age  │\n"
                              "├────────┼──────┤\n"
                              "└────────┴──────┘")

    def test_table_with_large_inline_title_with_max_table_width_print(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.inline_title = "TESTING TABLE"
        table.max_table_width = 10
        assert str(table) == ("┌─TESTIN─┐\n"
                              "│name│age│\n"
                              "├────┼───┤\n"
                              "└────┴───┘")
