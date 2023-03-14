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
    """

    def __init__(self, filepath: str, content: str = '') -> None:
        self.filepath: str = filepath if filepath.endswith(
            '.md') else filepath + '.md'
        self.content: str = content

    def markdown(self, mode: str = 'w'):
        """
        Writes content to filepath
        
        Parameters
        ----------
        mode : str
            write mode (default to 'w')
        """
        with open(self.filepath, mode) as f:
            f.write(self.content)

    def heading(self, text: str, level: int = 1) -> None:
        """
        Appends formatted heading to content

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
        
        self.content += f'{text}\n'
        
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
                raise MarkdownException('rows must have the same amount of cells as the header')
                
            r += f"|{'|'.join(row)}|\n"
            
        self.content += table + r