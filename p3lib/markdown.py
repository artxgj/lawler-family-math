from typing import List
from enum import Enum

MdCellAlign = Enum('MdCellAlign', 'left center right')


class Markdown:
    cellalign = {MdCellAlign.left: '-----', MdCellAlign.right: '----:', MdCellAlign.center: ':---:'}
    celldelim = '|'

    @staticmethod
    def h1(s: str) -> str:
        return f"# {s}"

    @staticmethod
    def h2(s: str) -> str:
        return f"## {s}"

    @staticmethod
    def h3(s: str) -> str:
        return f"### {s}"

    @staticmethod
    def h4(s: str) -> str:
        return f"#### {s}"

    @staticmethod
    def h5(s: str) -> str:
        return f"##### {s}"

    @staticmethod
    def h6(s: str) -> str:
        return f"###### {s}"

    @staticmethod
    def hr() -> str:
        return "___"

    @staticmethod
    def line(s: str) -> str:
        return f"{s}  "

    @staticmethod
    def link(text: str, url: str) -> str:
        return f"[{text}]({url})"

    @staticmethod
    def table_header(field_names: List[str], cells_align: List[str] = None) -> str:
        if not isinstance(field_names, list):
            raise TypeError('field_names is not a list')

        aligns = cells_align or [MdCellAlign.left for _ in range(len(field_names))]
        header = f" {Markdown.celldelim} ".join(field_names)
        cells_alignment = f" {Markdown.celldelim} ".join([Markdown.cellalign[align] for align in aligns])
        return f"{Markdown.celldelim} {header} |\n| {cells_alignment} {Markdown.celldelim}"

    @staticmethod
    def table_row(row: List[str]) -> str:
        trow = f" {Markdown.celldelim} ".join([cell.replace('\n', '<br/>') for cell in row])
        return f"{Markdown.celldelim} {trow} {Markdown.celldelim}"


