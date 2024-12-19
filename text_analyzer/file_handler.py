from pathlib import Path


class FileHandler:

    def __init__(self, file_path: str):
        self.file_path = file_path

    def check_extension(self):
        extension = Path(self.file_path).suffix.lower()
        print(extension)
        if extension in [".md", ".txt"]:
            return True
        else:
            raise ValueError(f"Unsupported file type: {extension}.")

    def extract_text(self) -> str:
        if self.check_extension():
            with open(self.file_path, "r", encoding="utf-8") as file:
                return file.read()
        else:
            return None
