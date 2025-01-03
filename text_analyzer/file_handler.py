from abc import ABC, abstractmethod
from pathlib import Path
from pypdf import PdfReader
from text_analyzer.config import CHARSET


ALLOWED_EXTENSIONS = {'.txt', '.md', '.pdf'}


class FileHandler(ABC):
    """
    Abstract base class for file handlers.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.check_extension()

    @abstractmethod
    def extract_text(self) -> str:
        """
        Extracts text content from the file.
        """
        raise NotImplementedError(
            "Subclasses must implement extract_text method")

    def check_extension(self) -> bool:
        """
        Checks if the file has a valid extension.

        Raises:
            ValueError: If the file extension is not supported.
        """
        extension = Path(self.file_path).suffix.lower()
        if extension not in ALLOWED_EXTENSIONS:
            raise ValueError(f"Unsupported file type: {extension}.")


class TxtFileHandler(FileHandler):
    """
    Handles the extraction of text content from a text file.
    """

    def extract_text(self) -> str:
        """
        Extracts text content from the file.

        Returns:
            str: The content of the file as a string.

        Raises:
            FileNotFoundError: If the file is not found.
            PermissionError: If there's no permission to read the file.
            IOError: If there's an error reading the file.
        """
        try:
            with open(self.file_path, "r", encoding=CHARSET) as file:
                return file.read()
        except (FileNotFoundError, PermissionError, IOError) as e:
            print(f"Error reading the file: {e}")
            return ""


class PdfFileHandler(FileHandler):
    """
    Handles the extraction of text content from a PDF file.

    Attributes:
        file_path (str): The path to the PDF file.

    Raises:
        ValueError: If the file extension is not supported.
    """

    def extract_text(self) -> str:
        try:
            text = ""
            reader = PdfReader(self.file_path)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
            return text
        except (FileNotFoundError, PermissionError, IOError) as e:
            print(f"Unexpected error when extracting text from PDF {
                self.file_path}: {e}")
        return ""


class FileHandlerFactory:  # pylint: disable=too-few-public-methods
    """
    Factory class for creating file handlers based on file extensions.
    """
    @staticmethod
    def get_handler(file_path: str) -> FileHandler:
        """
        Creates a file handler based on the file extension.

        Args:
            file_path (str): The path to the file.

        Returns:
            FileHandler: The file handler object.

        Raises:
            ValueError: If the file extension is not supported.
        """
        extension = Path(file_path).suffix.lower()
        if extension in [".txt", ".md"]:
            return TxtFileHandler(file_path)
        if extension == ".pdf":
            return PdfFileHandler(file_path)
        raise ValueError(f"Unsupported file type: {extension}.")
