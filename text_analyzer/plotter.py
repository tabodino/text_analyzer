from collections import Counter
from .config import TOP_WORDS_COUNT, PLOT_BAR_COLOR, OUTPUT_FOLDER
import matplotlib.pyplot as plt


class WordFrequencyPlotter:
    """
    A class to visualize word frequencies using bar plots.

    This class provides a method to generate a bar plot from a Counter object containing word frequencies 
    and save the plot to a specified file path.

    Methods:
        plot(word_count: Counter, output_path: str = "word_frequencies.png") -> None:
            Creates a bar plot of the most common words and their frequencies, and saves it as an image file.

    Example:
        from collections import Counter

        word_count = Counter({
            "example": 10,
            "word": 7,
            "frequency": 5,
            "plot": 3
        })

        plotter = WordFrequencyPlotter()
        plotter.plot(word_count, output_path="example_plot.png")
        # This will generate a bar plot saved as 'example_plot.png'.
    """
    def plot(self,
             word_count: Counter,
             output_path: str = "word_frequencies.png") -> None:
        most_common = word_count.most_common(TOP_WORDS_COUNT)
        words, counts = zip(*most_common)

        plt.bar(words, counts, color=PLOT_BAR_COLOR)
        plt.title(f"Top {TOP_WORDS_COUNT} Most Common Words")
        plt.xlabel("Words")
        plt.ylabel("Freqency")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(OUTPUT_FOLDER / output_path)
        plt.close()

        print(f"Word frequency plot saved as {output_path}")
