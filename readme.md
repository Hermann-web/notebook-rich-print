# Notebook Rich Print

Notebook Rich Print is a Python library that enhances the standard print function in notebook environments, allowing you to generate rich-text output. With Notebook Rich Print, you can create visually appealing and formatted text output directly within your notebooks, making them more interactive and presentable.

## Key Features

- Print with Rich Text: Replace the standard print function in your notebooks with a rich-text printing alternative. Format your output using bold, italics, headings, bullet points, and more to create visually appealing and well-structured text.

- Markdown Support: Leverage the power of Markdown within your print statements. Write Markdown syntax directly in your code, and Notebook Rich Print will render it appropriately, enabling you to create formatted text, tables, lists, and more.

- Table Generation: Generate tables seamlessly within your notebooks using Markdown syntax. Simply use the provided `print_header`, `print_row`, and `show` functions to create and display tables.

- Easy Integration: Notebook Rich Print seamlessly integrates into Jupyter Notebooks and other notebook environments. Simply import the library and start using the enhanced print function right away.

## Usage

1. Install Notebook Rich Print using pip:

```bash
pip install notebook-rich-print
```

2. Import the required functions in your notebook:

```python
from markdown_printer import print, print_header, print_row, show
```

3. Start using the enhanced print function:

```python
# Print some text
print("This is some **bold** text.")

# Print a list
print("- List item 1")
print("- List item 2")

# Print a table
print("This is a Markdown table:")
print_header("Name", "Age")
print_row("John", "30")
print_row("Jane", "25")
show()
```

4. Run your notebook and observe the rich-text output in the notebook cells. Enjoy the visually appealing and well-formatted text, including tables, within your notebooks.

To automatically display the output of `show()` after running each cell, you can register it as a callback using the `post_run_cell` event in IPython. Add the following code snippet to the beginning of your notebook:

```python
from IPython import get_ipython
from markdown_printer import MarkdownPrinter, printf, print, print_header, print_row, show
get_ipython().events.register('post_run_cell', show)
```

By doing this, you no longer need to manually call `show()` after each cell. The output will be automatically displayed, providing a more seamless and convenient experience.

## Markdown Usage

Notebook Rich Print utilizes Markdown syntax for formatting text and generating tables. Markdown is a lightweight markup language that allows you to style your text using simple and intuitive syntax. You can learn more about Markdown syntax and its features in the [Markdown Guide](https://www.markdownguide.org/basic-syntax/).

When using the enhanced print function, you can include Markdown syntax directly in your code strings. For example, surround text with double asterisks (`**`) for bold formatting or use hyphens (`-`) to create bullet points. To create a table, use the `print_header`, `print_row`, and `show` functions provided by Notebook Rich Print.

The `print_header` function is used to add the table header, `print_row` is used to add individual rows to the table, and `show` is used to display the table in the notebook.

## Requirements

- Python 3.9 or above

## Installation

Install the library using pip:

```bash
pip install notebook-rich-print
```

## License

This project is licensed under the MIT License. See the [LICENSE

](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to open issues and submit pull requests to contribute to the development of Notebook Rich Print. Please follow the guidelines in [CONTRIBUTING](CONTRIBUTING.md).

## Acknowledgements

We would like to thank the open-source community for their valuable contributions and the developers of the underlying libraries that make Notebook Rich Print possible.

## Get in Touch

For any questions, suggestions, or feedback, please feel free to contact me:

- Name: Hermann Agossou
- Email: agossouhermann7@gmail.com
