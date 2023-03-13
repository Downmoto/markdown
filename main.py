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
        Adds formatted heading to content

        Parameters
        ----------
        test: str
            text to be formatted into heading
        level : int
            heading level, i.e. amount of '#' added before text (default is 1)
        """

        self.content += f'{"#"*level} {text}\n'
