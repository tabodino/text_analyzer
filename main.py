from text_analyzer.file_handler import FileHandler


def main(file_path: str):
    try:
        file_handler = FileHandler(file_path)
        text = file_handler.extract_text()
        print(text)
    except Exception as ex:
        print(f"An error occurred: {ex}")


if __name__ == "__main__":
    # !-- Replace with your text file here
    file_path = "README.md"
    main(file_path)
