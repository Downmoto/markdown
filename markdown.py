from typing import Callable

class MarkdownException(Exception):
    """
    Exception raised for errors in Markdown Class

    Attributes
    ----------
    message : str
      explanation of the error
    """

    def __init__(self, message: str = "Incorrect Markdown") -> None:
        super().__init__(message)


class Markdown:
    """
    Markdown class.

    all methods append a single newline

    Attributes
    ----------
    filepath : str
        write path, should include filename at the end
    content : str
        stores the content of the markdown file (default is '')
        
    Notes
    -----
    content, filepath, and paragraph pre_processors are exposed to end user.
    """

    def __init__(self, filepath: str, content: str = '') -> None:
        self.filepath: str = filepath if filepath.endswith(
            '.md') else filepath + '.md'
        self.content: str = content
        
        self.pre_processors: list[Callable[[str], str]] = []

    def markdown(self, mode: str = 'w') -> str:
        """
        Writes content to filepath, returns filepath

        Parameters
        ----------
        mode : str
            write mode (default to 'w')
        """
        
        with open(self.filepath, mode) as f:
            if mode == 'a' or mode == 'a+':
                f.write('\n')
            f.write(self.content)
            
        return self.filepath
            
    def add(self, func: Callable[[str], str]) -> None:
        """
        Add a paragraph pre_processor. They run on the text param of paragraphs
        directly before being appended to content
        
        Parameters
        ----------
        func : function
            pre processer function must take in a string and return a string
            they run in the order they are added
        """
        
        self.pre_processors.append(func)

    def heading(self, text: str, level: int = 1) -> None:
        """
        Appends formatted heading to cont

        Parameters
        ----------
        text : str
            text to be formatted into heading
        level : int
            heading level, i.e. amount of '#' added before text (default is 1)
        """

        self.content += f'{"#"*level} {text}\n'

    def paragraph(self, text: str) -> None:
        """
        Appends paragraph to content

        Parameters
        ----------
        text : str
            paragraph to append
        """
        
        t = text
        
        for f in self.pre_processors:
            t = f(t)

        self.content += f'{t}\n'

    def table(self, header: list, rows: 'list[list[str]]') -> None:
        """
        Appends a formatted table to content

        Parameters
        ----------
        header : list
            list of table headers in order of appearance
        rows : list
            2D array of table rows

        Throws
        ------
        MarkdownException
            length of row and header diff
        MarkdownException    
            rows param not a 2D array
        """

        table: str = f"|{'|'.join(header)}|\n|{'|'.join(['---' for _ in header])}|\n"
        r: str = ''
        for row in rows:
            if type(row) is not list:
                raise MarkdownException('rows must be a 2D array of lists')
            if len(row) is not len(header):
                raise MarkdownException(
                    'rows must have the same amount of cells as the header')

            r += f"|{'|'.join(row)}|\n"

        self.content += table + r


if __name__ == '__main__':
    print("Do not run this file directly, import it.\n"
          "[from markdown import Markdown]")