import pytest

from src.simple_table_dima203 import Table, SINGLE_BORDER, DOUBLE_BORDER, DEFAULT


class TestTable:
    def test_table_print(self) -> None:
        print()
        table = Table(keys=["name", "age"], style=DEFAULT)
        table.title = "User Ages for Admins"
        table.inline_title = "Test"
        table.supertitle = "Test"
        table.title_border = True
        table.min_table_width = 20
        table.max_table_width = 50
        table.min_width["name"] = 5
        table.max_width["name"] = 15
        table.add_row(["User", 13])
        table.add_row(["User2", 45])
        table.add_delimiter("Длинный текст для разделителя")
        table.add_row(["Average", 17.5])
        print(table)

    def test_empty_table_print(self) -> None:
        table = Table(style=SINGLE_BORDER)
        assert str(table) == (
            "┌─┐\n"
            "│ │\n"
            "├─┤\n"
            "└─┘"
        )

    def test_empty_table_with_title_print(self) -> None:
        table = Table(style=SINGLE_BORDER)
        table.title = "Test"
        assert str(table) == (
            "  Test  \n"
            "┌──────┐\n"
            "│      │\n"
            "├──────┤\n"
            "└──────┘"
        )

    def test_empty_table_with_adding_new_column_print(self) -> None:
        table = Table(style=SINGLE_BORDER)
        table.title = "Test"
        assert str(table) == (
            "  Test  \n"
            "┌──────┐\n"
            "│      │\n"
            "├──────┤\n"
            "└──────┘"
        )
        table.add_column("Test")
        assert str(table) == (
            "  Test  \n"
            "┌──────┐\n"
            "│ Test │\n"
            "├──────┤\n"
            "└──────┘"
        )

    def test_table_without_data_print(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        assert str(table) == (
            "┌────┬───┐\n"
            "│name│age│\n"
            "├────┼───┤\n"
            "└────┴───┘"
        )

    def test_table_without_data_deleting_column(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        assert str(table) == (
            "┌────┬───┐\n"
            "│name│age│\n"
            "├────┼───┤\n"
            "└────┴───┘"
        )
        table.delete_column("age")
        assert str(table) == (
            "┌────┐\n"
            "│name│\n"
            "├────┤\n"
            "└────┘"
        )

    def test_table_with_data_print(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.add_row(["Alex gfjdkljgkdjklfgld", 22])
        assert str(table) == (
            "┌──────────────────────┬───┐\n"
            "│         name         │age│\n"
            "├──────────────────────┼───┤\n"
            "│Alex gfjdkljgkdjklfgld│22 │\n"
            "└──────────────────────┴───┘"
        )

    def test_table_with_data_deleting_column(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.add_row(["Alex gfjdkljgkdjklfgld", 22])
        assert str(table) == (
            "┌──────────────────────┬───┐\n"
            "│         name         │age│\n"
            "├──────────────────────┼───┤\n"
            "│Alex gfjdkljgkdjklfgld│22 │\n"
            "└──────────────────────┴───┘"
        )
        table.delete_column("age")
        assert str(table) == (
            "┌──────────────────────┐\n"
            "│         name         │\n"
            "├──────────────────────┤\n"
            "│Alex gfjdkljgkdjklfgld│\n"
            "└──────────────────────┘"
        )

    def test_table_with_large_title_print(self) -> None:
        table = Table(keys=["Fullname", "age"], style=SINGLE_BORDER)
        table.add_row(["Alex", 22])
        assert str(table) == (
            "┌────────┬───┐\n"
            "│Fullname│age│\n"
            "├────────┼───┤\n"
            "│  Alex  │22 │\n"
            "└────────┴───┘"
        )

    def test_table_with_max_table_width_with_large_title_print(self) -> None:
        table = Table(keys=["Fullname", "age"], style=SINGLE_BORDER)
        table.add_row(["Alex", 22])
        table.max_table_width = 10
        assert str(table) == (
            "┌─────┬──┐\n"
            "│Fulln│ag│\n"
            "│ ame │e │\n"
            "├─────┼──┤\n"
            "│Alex │22│\n"
            "└─────┴──┘"
        )

    def test_table_min_width_print(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.min_table_width = 20
        assert str(table) == (
            "┌──────────┬───────┐\n"
            "│   name   │  age  │\n"
            "├──────────┼───────┤\n"
            "└──────────┴───────┘"
        )

    def test_table_with_title_print(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.title = "TEST"
        assert str(table) == (
            "   TEST   \n"
            "┌────┬───┐\n"
            "│name│age│\n"
            "├────┼───┤\n"
            "└────┴───┘"
        )

    def test_table_with_left_title_print(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.title = "TEST"
        table.title_align = "<"
        assert str(table) == (
            " TEST     \n"
            "┌────┬───┐\n"
            "│name│age│\n"
            "├────┼───┤\n"
            "└────┴───┘"
        )

    def test_table_with_right_title_print(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.title = "TEST"
        table.title_align = ">"
        assert str(table) == (
            "     TEST \n"
            "┌────┬───┐\n"
            "│name│age│\n"
            "├────┼───┤\n"
            "└────┴───┘"
        )

    def test_table_with_bordered_title_print(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.title = "TEST"
        table.title_border = True
        assert str(table) == (
            "┌────────┐\n"
            "│  TEST  │\n"
            "├────┬───┤\n"
            "│name│age│\n"
            "├────┼───┤\n"
            "└────┴───┘"
        )

    def test_table_with_large_title_with_max_table_width_print(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.title = "TESTING TABLE"
        table.title_border = True
        table.max_table_width = 10
        assert str(table) == (
            "┌────────┐\n"
            "│TESTING │\n"
            "│ TABLE  │\n"
            "├────┬───┤\n"
            "│name│age│\n"
            "├────┼───┤\n"
            "└────┴───┘"
        )

    def test_table_with_inline_title_print(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.inline_title = "TEST"
        assert str(table) == (
            "┌──TEST──┐\n"
            "│name│age│\n"
            "├────┼───┤\n"
            "└────┴───┘"
        )

    def test_table_with_left_inline_title_print(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.inline_title = "TEST"
        table.inline_title_align = "<"
        assert str(table) == (
            "┌─TEST───┐\n"
            "│name│age│\n"
            "├────┼───┤\n"
            "└────┴───┘"
        )

    def test_table_with_right_inline_title_print(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.inline_title = "TEST"
        table.inline_title_align = ">"
        assert str(table) == (
            "┌───TEST─┐\n"
            "│name│age│\n"
            "├────┼───┤\n"
            "└────┴───┘"
        )

    def test_table_with_wrong_inline_title_align_error(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.inline_title = "TEST"
        table.inline_title_align = ""
        with pytest.raises(ValueError):
            print(table)

    def test_table_with_large_inline_title_print(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.inline_title = "TESTING TABLE"
        assert str(table) == (
            "┌─TESTING TABLE─┐\n"
            "│  name  │ age  │\n"
            "├────────┼──────┤\n"
            "└────────┴──────┘"
        )

    def test_table_with_large_inline_title_with_max_table_width_print(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.inline_title = "TESTING TABLE"
        table.max_table_width = 10
        assert str(table) == (
            "┌─TESTIN─┐\n"
            "│name│age│\n"
            "├────┼───┤\n"
            "└────┴───┘"
        )

    def test_table_with_supertitle_print(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.supertitle = "TEST"
        assert str(table) == (
            "   TEST   \n"
            "┌────┬───┐\n"
            "│name│age│\n"
            "├────┼───┤\n"
            "└────┴───┘"
        )

    def test_table_with_supertitle_with_border_print(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.supertitle = "TEST"
        table.title_border = True
        assert str(table) == (
            "┌──TEST──┐\n"
            "├────┬───┤\n"
            "│name│age│\n"
            "├────┼───┤\n"
            "└────┴───┘"
        )

    def test_table_with_large_supertitle_print(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.supertitle = "TESTING TABLE"
        assert str(table) == (
            "  TESTING TABLE  \n"
            "┌────────┬──────┐\n"
            "│  name  │ age  │\n"
            "├────────┼──────┤\n"
            "└────────┴──────┘"
        )

    def test_table_with_large_supertitle_with_border_print(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.supertitle = "TESTING TABLE"
        table.title_border = True
        assert str(table) == (
            "┌─TESTING TABLE─┐\n"
            "├────────┬──────┤\n"
            "│  name  │ age  │\n"
            "├────────┼──────┤\n"
            "└────────┴──────┘"
        )

    def test_table_with_large_supertitle_with_max_table_width_print(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.supertitle = "TESTING TABLE"
        table.max_table_width = 10
        assert str(table) == (
            "  TESTIN  \n"
            "┌────┬───┐\n"
            "│name│age│\n"
            "├────┼───┤\n"
            "└────┴───┘"
        )

    def test_table_with_large_supertitle_with_border_with_max_table_width_print(
        self,
    ) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.supertitle = "TESTING TABLE"
        table.title_border = True
        table.max_table_width = 10
        assert str(table) == (
            "┌─TESTIN─┐\n"
            "├────┬───┤\n"
            "│name│age│\n"
            "├────┼───┤\n"
            "└────┴───┘"
        )

    def test_table_with_delimiter_print(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.add_delimiter()
        assert str(table) == (
            "┌────┬───┐\n"
            "│name│age│\n"
            "├────┼───┤\n"
            "├────┼───┤\n"
            "└────┴───┘"
        )

    def test_table_with_text_delimiter_print(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.add_delimiter("Test")
        assert str(table) == (
            "┌────┬───┐\n"
            "│name│age│\n"
            "├────┼───┤\n"
            "├─Test───┤\n"
            "└────┴───┘"
        )

    def test_table_with_large_text_delimiter_print(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.add_delimiter("Testing delimiter")
        assert str(table) == (
            "┌──────────┬────────┐\n"
            "│   name   │  age   │\n"
            "├──────────┼────────┤\n"
            "├─Testing delimiter─┤\n"
            "└──────────┴────────┘"
        )

    def test_table_with_max_table_width_with_large_text_delimiter_print(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.add_delimiter("Testing delimiter")
        table.max_table_width = 10
        assert str(table) == (
            "┌────┬───┐\n"
            "│name│age│\n"
            "├────┼───┤\n"
            "├─Testin─┤\n"
            "└────┴───┘"
        )

    def test_table_with_multiple_text_delimiter_print(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.add_delimiter("Test 1")
        table.add_delimiter("Test 2")
        table.add_delimiter("Test 3")
        assert str(table) == (
            "┌────┬───┐\n"
            "│name│age│\n"
            "├────┼───┤\n"
            "├─Test 1─┤\n"
            "├─Test 2─┤\n"
            "├─Test 3─┤\n"
            "└────┴───┘"
        )

    def test_table_with_data_with_text_delimiter_print(self) -> None:
        table = Table(keys=["name", "age"], style=SINGLE_BORDER)
        table.add_delimiter("Test 1")
        table.add_row(["Alex", 22])
        table.add_delimiter()
        table.add_row(["Dan", 25])
        assert str(table) == (
            "┌────┬───┐\n"
            "│name│age│\n"
            "├────┼───┤\n"
            "├─Test 1─┤\n"
            "│Alex│22 │\n"
            "├────┼───┤\n"
            "│Dan │25 │\n"
            "└────┴───┘"
        )
