from abc import ABC, abstractmethod
from pathlib import Path
from pypdf import PdfReader


ALLOWED_EXTENSIONS = {'.txt', '.md', '.pdf'}


class FileHandler(ABC):

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.check_extension()

    @abstractmethod
    def extract_text(self) -> str:
        pass

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

    def __init__(self, file_path: str):
        self.file_path = file_path

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
            with open(self.file_path, "r", encoding="utf-8") as file:
                return file.read()
        except (FileNotFoundError, PermissionError, IOError) as e:
            print(f"Error reading the file: {e}")


class PdfFileHandler(FileHandler):

    def __init__(self, file_path: str):
        self.file_path = file_path
    """
    Extracts text content from a PDF file.

    Args:
        file_path (str): The path to the PDF file.

    Returns:
        str: The text content of the PDF file.
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
        except Exception as e:
            print(f"Error extracting text from PDF: {e}")
            return ""


class FileHandlerFactory:
    @staticmethod
    def get_handler(file_path: str) -> FileHandler:
        extension = Path(file_path).suffix.lower()
        if extension in [".txt", ".md"]:
            return TxtFileHandler(file_path)
        elif extension == ".pdf":
            return PdfFileHandler(file_path)
        else:
            raise ValueError(f"Unsupported file type: {extension}.")
