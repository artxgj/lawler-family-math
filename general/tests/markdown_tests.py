import unittest

from markdown import Markdown, MdCellAlign


class TestMarkdown(unittest.TestCase):
    def setUp(self):
        self.sep = Markdown.celldelim
        self.left = Markdown.cellalign[MdCellAlign.left]
        self.right = Markdown.cellalign[MdCellAlign.right]
        self.center = Markdown.cellalign[MdCellAlign.center]
        self.c1 = 'cell 1'
        self.c2 = 'cell 2'
        self.c3 = 'cell 3'
        self.table_header = [self.c1, self.c2, self.c3]

    def test_tableheader(self):
        alignments = [MdCellAlign.left, MdCellAlign.center, MdCellAlign.right]
        actual = Markdown.table_header(self.table_header, alignments)
        expected = f"{self.sep} {self.c1} {self.sep} {self.c2} {self.sep} {self.c3} {self.sep}\n{self.sep} {self.left} {self.sep} {self.center} {self.sep} {self.right} {self.sep}"
        self.assertEqual(expected, actual)

    def test_tableheader_noalignments(self):
        actual = Markdown.table_header(self.table_header)
        expected = f"{self.sep} {self.c1} {self.sep} {self.c2} {self.sep} {self.c3} {self.sep}\n{self.sep} {self.left} {self.sep} {self.left} {self.sep} {self.left} {self.sep}"
        self.assertEqual(expected, actual)

    def test_tablerow(self):
        actual = Markdown.table_row(['1', '2', '3'])
        expected = "| 1 | 2 | 3 |"
        self.assertEqual(expected, actual)

    def test_link(self):
        actual = Markdown.link('Seven of Nine', 'https://startrek.com/seven-of-nine')
        expected = "[Seven of Nine](https://startrek.com/seven-of-nine)"
        self.assertEqual(expected, actual)




