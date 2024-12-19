from text_analyzer.file_handler import FileHandler
from text_analyzer.plotter import WordFrequencyPlotter
from text_analyzer.text_analyzer import TextAnalyzer


def main(file_path: str):
    try:
        file_handler = FileHandler(file_path)
        text = file_handler.extract_text()

        analyzer = TextAnalyzer()
        stats, word_count = analyzer.analyze(text)

        print(stats)

        plotter = WordFrequencyPlotter()
        plotter.plot(word_count)
    except Exception as ex:
        print(f"An error occurred: {ex}")


if __name__ == "__main__":
    # !-- Replace with your text file here
    file_path = "README.md"
    main(file_path)
