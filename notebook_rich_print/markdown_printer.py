#!/usr/bin/env python
"""
Markdown Printer

This module provides a MarkdownPrinter class for generating and displaying Markdown-formatted tables in Jupyter Notebook.

Author: Hermann Agossou
Email: agossouhermann7@gmail.com
Version: 1.0
"""

from IPython.display import display, Markdown
from tabulate import tabulate


def map_list_to_str(data: list):
    """Convert the elements of a list to strings"""
    return list(map(str, data))


class MarkdownPrinter:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """Initialize MarkdownPrinter"""
        self.columns = []
        self.text = ""

    def clean_table(self):
        """Clean the table and return the formatted table text"""
        if not self.columns:
            return ""
        table_text = tabulate(self.columns[1:], self.columns[0], tablefmt='pipe')
        self.columns = []
        return table_text

    def __add_text__(self, text):
        """Add text to the Markdown output"""
        table_text = self.clean_table()
        if table_text:
            self.text += "\n\n" + table_text
        if text:
            self.text += "\n\n" + text

    def print(self, *markdown_texts):
        """Print Markdown-formatted text"""
        self.__add_text__(" ".join(map_list_to_str(markdown_texts)))

    def add_header(self, *headers):
        """Add header row to the table"""
        self.__add_text__("")
        self.columns = [map_list_to_str(headers)]

    def add_row(self, *cells):
        """Add a row to the table"""
        assert self.columns
        assert isinstance(self.columns[-1], list)
        assert len(cells) == len(self.columns[-1])
        self.columns.append(map_list_to_str(cells))

    def show(self):
        """Display the Markdown output"""
        self.__add_text__("")
        if not self.text:
            return
        display(Markdown(self.text))
        self.text = ""


# Alias functions for convenience
printf = MarkdownPrinter().print
print_header = MarkdownPrinter().add_header
print_row = MarkdownPrinter().add_row
show = MarkdownPrinter().show
print = MarkdownPrinter().print
