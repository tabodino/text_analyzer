from pathlib import Path


class FileHandler:

    def __init__(self, file_path: str):
        self.file_path = file_path

    def check_extension(self) -> bool:
        """
        Checks if the file has a valid extension.

        Returns:
            bool: True if the extension is valid ('.md' or '.txt').

        Raises:
            ValueError: If the file extension is not supported.
        """
        extension = Path(self.file_path).suffix.lower()
        if extension in [".md", ".txt"]:
            return True
        else:
            raise ValueError(f"Unsupported file type: {extension}.")

    def extract_text(self) -> str:
        """
        Extracts text content from the file if it has a valid extension.

        Returns:
            str: The content of the file as a string if the extension is valid.
                Returns an empty string if the file extension is invalid or an error occurs during reading.

        Raises:
            ValueError: If the file extension is invalid and `check_extension` raises an exception.
        """
        try:
            if self.check_extension():
                with open(self.file_path, "r", encoding="utf-8") as file:
                    return file.read()
            else:
                return ""
        except (FileNotFoundError, PermissionError, IOError) as e:
            print(f"Error reading the file: {e}")
