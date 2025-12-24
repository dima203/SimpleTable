from src.simple_table_dima203 import Table


class TestTable:
    def test_table_print(self) -> None:
        table = Table(keys=["name", "age"])
        table.none_format = '-'
        table.min_table_width = 20
        table.max_table_width = 30
        table.max_width["age"] = 3
        table.min_width["age"] = 3
        table.align["name"] = "<"
        table.add_row(["Alex gfjdkljgkdjklfgld", 22])
        print(table)
        table.add_column("id", alias="tabel", align="<")
        table.min_width["id"] = 5
        print(table)
