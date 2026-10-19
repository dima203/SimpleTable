# SimpleTable

[![PyPI version](https://badge.fury.io/py/simple-table-dima203.svg)](https://pypi.org/project/simple_table_dima203/)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://pypi.org/project/simple_table_dima203/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

**SimpleTable** is a lightweight, zero-dependency Python library for creating pretty text tables for the terminal, logs, CLI tools and reports.

No configuration required — just add rows and print. With one line you get a clean table, and with a few attributes you can tune titles, alignment, borders, column widths and line wrapping.

```
      Users
┌─────┬───┬──────┐
│name │age│ city │
├─────┼───┼──────┤
│Alex │22 │Berlin│
│Maria│35 │Madrid│
├─Summary─┼──────┤
│Total│57 │      │
└─────┴───┴──────┘
```

## Features

- Simple, intuitive API — `Table`, `add_row()`, `print()`
- **Zero dependencies** — pure standard library
- Built-in styles: `DEFAULT`, `SINGLE_BORDER`, `DOUBLE_BORDER`, `CLEAR`, `MARKDOWN`, or fully custom styles via `TableStyle`
- Three kinds of titles: `title`, `inline_title` (embedded in the top border) and `supertitle`
- Horizontal separators with optional text: `add_delimiter("Summary")`
- Per-column alignment (`<`, `^`, `>`), aliases, and min/max widths
- Automatic table width control (`min_table_width` / `max_table_width`) with proportional column resizing
- Word wrapping for long cells (`wrap`)
- Custom rendering of `None` values (`none_format`)

## Installation

```bash
pip install simple_table_dima203
```

> [!NOTE]
> The code uses modern typing syntax (`list[str] | None`), so **Python 3.10+** is required.

## Quick start

```python
from simple_table_dima203 import Table, SINGLE_BORDER

table = Table(keys=["name", "age", "city"], style=SINGLE_BORDER)
table.add_row(["Alex", 22, "Berlin"])
table.add_row(["Maria", 35, "Madrid"])

print(table)
```

```
┌─────┬───┬──────┐
│name │age│ city │
├─────┼───┼──────┤
│Alex │22 │Berlin│
│Maria│35 │Madrid│
└─────┴───┴──────┘
```

## Usage

### Titles

```python
table = Table(keys=["name", "age"])
table.title = "Users"            # centered above the table
table.title_border = True        # wrap the title into a bordered row
table.title_align = "^"          # "^" center, "<" left, ">" right
```

<details>
<summary>Examples of output</summary>

```python
table = Table(keys=["name", "age"], style=SINGLE_BORDER)
table.title = "Users"
```
```
  Users   
┌────┬───┐
│name│age│
├────┼───┤
└────┴───┘
```

With `table.title_border = True`:
```
┌────────┐
│ Users  │
├────┬───┤
│name│age│
├────┼───┤
└────┴───┘
```

</details>

You can also embed a title directly into the top border:

```python
table = Table(keys=["name", "age"], style=SINGLE_BORDER)
table.inline_title = "Report"
table.inline_title_align = "^"   # "^", "<" or ">"
```

```
┌─Report─┐
│name│age│
├────┼───┤
└────┴───┘
```

And put a line **above** the whole table:

```python
table = Table(keys=["name", "age"], style=SINGLE_BORDER)
table.supertitle = "Data"
```

```
   Data
┌────┬───┐
│name│age│
├────┼───┤
└────┴───┘
```

### Columns and rows

```python
table = Table(keys=["name", "age"])
table.add_row(["Alex", 22])

table.add_column("city", default="—")   # existing rows get the default value
table.delete_column("city")             # remove a column entirely
```

```python
table = Table(keys=["name", "years"])
table.key_alias["years"] = "age"        # custom header text
```

### Delimiters (section separators)

Insert a horizontal line between rows, optionally with text:

```python
table = Table(keys=["name", "age"], style=SINGLE_BORDER)
table.add_row(["Alex", 22])
table.add_delimiter("Summary")
table.add_row(["Total", 22])
```

```
┌─────┬───┐
│name │age│
├─────┼───┤
│Alex │22 │
├─Summary─┤
│Total│22 │
└─────┴───┘
```

### Alignment

Alignment uses Python format-spec chars, set per column:

```python
table = Table(keys=["text", "count"])
table.align["text"] = "<"     # left
table.align["count"] = ">"    # right
```

### Width control

```python
table = Table(keys=["name", "description"])

table.min_width["name"] = 10          # column is at least 10 chars wide
table.max_width["description"] = 40   # column is capped at 40 chars

table.min_table_width = 60            # whole table at least 60 chars wide
table.max_table_width = 120           # whole table at most 120 chars wide

table.wrap = True                     # long cells wrap to multiple lines
```

With narrow `max_table_width` the columns shrink and long text wraps:

```python
table = Table(keys=["name", "age"], style=SINGLE_BORDER)
table.add_row(["Alex Constantinopole", 22])
table.max_table_width = 15
```

```
┌──────────┬──┐
│          │ag│
│   name   │e │
├──────────┼──┤
│Alex Const│  │
│antinopole│22│
└──────────┴──┘
```

### `None` values

```python
table = Table(keys=["name", "age"])
table.none_format = "n/a"     # "" (empty) by default
table.add_row([None, 5])
```

```
+----+---+
|name|age|
+----+---+
|n/a | 5 |
+----+---+
```

## Styles

Built-in styles are imported from the package:

| Style | Look |
|---|---|
| `DEFAULT` (default) | ASCII: `+`, `-`, `\|` |
| `SINGLE_BORDER` | Unicode single lines: `┌─┬┐ │ ├─┼┤ └─┴┘` |
| `DOUBLE_BORDER` | Unicode double lines: `╔═╦╗ ║ ╠═╬╣ ╚═╩╝` |
| `CLEAR` | no borders at all |
| `MARKDOWN` | `\|-` layout compatible with GitHub tables |

```python
from simple_table_dima203 import Table, SINGLE_BORDER, MARKDOWN

table = Table(keys=["name", "age"], style=SINGLE_BORDER)
```

Any style can be customized or created from scratch:

```python
from simple_table_dima203 import Table, TableStyle

style = TableStyle(
    vertical_character="|",
    horizontal_character="-",
    junction_character="+",
    # ... top/left/right/bottom characters
)

table = Table(keys=["name", "age"], style=style)
```


Full list of `TableStyle` fields:
`vertical_character`, `horizontal_character`, `top_junction_character`, `top_left_junction_character`, `top_right_junction_character`, `left_junction_character`, `right_junction_character`, `junction_character`, `bottom_junction_char`, `bottom_left_junction_char`, `bottom_right_junction_char`.

## API reference

### `Table(*, keys: list[str] | None = None, style: TableStyle = DEFAULT)`

| Method / attribute | Description |
|---|---|
| `add_column(name, *, alias, default, align, min_width, max_width)` | Add a column after creation; `alias` sets header text, `default` fills existing rows |
| `delete_column(name)` | Remove a column and all its data |
| `add_row(row: list)` | Append a row (values in the order of `keys`) |
| `add_delimiter(text=None)` | Append a horizontal separator, optionally with centered text |
| `title` | Title above the table (may contain `\n`) |
| `title_border` | Draw a bordered box around `title` |
| `title_align` / `inline_title_align` / `supertitle_align` | `"^"`, `"<"`, `">"` |
| `inline_title` | Text embedded into the top border |
| `supertitle` | Text written into a line above the table |
| `key_alias: dict[str, str]` | Header text per column |
| `align: dict[str, str]` | Alignment per column: `"^"`, `"<"`, `">"` |
| `min_width` / `max_width: dict[str, int \| None]` | Column width limits |
| `min_table_width` / `max_table_width: int \| None` | Table width limits |
| `none_format: str` | How `None` cells are rendered (default: `""`) |
| `wrap: bool` | Wrap long cell contents across lines (default: `True`) |
| `style: TableStyle` | Border characters preset |

## Testing

The project uses `pytest`:

```bash
pytest
```

## Development

Build the package:

```bash
python -m build
```

## License

[MIT](LICENSE) © dima203
