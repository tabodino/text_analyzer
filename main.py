from text_analyzer.file_handler import FileHandlerFactory
from text_analyzer.plotter import WordFrequencyPlotter
from text_analyzer.text_analyzer import TextAnalyzer


def main(file_path: str) -> None:
    """Main function to run the text analyzer and plotter."""
    try:
        file_handler = FileHandlerFactory.get_handler(file_path)
        text = file_handler.extract_text()

        analyzer = TextAnalyzer()
        stats, word_count = analyzer.analyze(text)

        analyzer.save_results(stats)

        plotter = WordFrequencyPlotter()
        plotter.plot(word_count)
    except FileNotFoundError as ex:
        print(f"File not found: {ex}")
    except ValueError as ex:
        print(f"Value error: {ex}")
    except PermissionError as ex:
        print(f"Permission error: {ex}")
    except OSError as ex:
        print(f"OS error: {ex}")


if __name__ == "__main__":
    # !-- Replace with your text file here
    FILE_PATH = "samples/poetry.md"
    main(FILE_PATH)
