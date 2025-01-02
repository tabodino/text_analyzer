import json
import re
from .config import OUTPUT_FOLDER, TOP_WORDS_COUNT
from collections import Counter
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class TextStats:
    total_words: int
    unique_words: int
    average_sentence_length: float
    most_common_words: List[Tuple[str, int]]


class TextAnalyzer:
    """
    A utility class for analyzing textual data, providing insights into word and sentence-level statistics.

    Methods:
        analyze(text: str) -> Tuple[TextStats, Counter]:
            Analyzes the input text and calculates various statistics, including total words, unique words, 
            average sentence length, and the most common words.

        _extract_words(text: str) -> List[str]:
            Extracts all words from the input text using word boundaries and converts them to lowercase.

        _extract_sentences(text: str) -> List[str]:
            Splits the input text into sentences based on punctuation (.!?), trimming whitespace.

    Example:
        analyzer = TextAnalyzer()
        text = "Hello world! This is a test. Analyze this text, please."
        stats, word_count = analyzer.analyze(text)

        # stats will contain:
        # TextStats(total_words=10, unique_words=9, average_sentence_length=5.0, ...)
        # word_count will be a Counter object with word frequencies.
    """

    def analyze(self, text: str) -> Tuple[TextStats, Counter]:
        words = self._extract_words(text)
        word_count = Counter(words)
        sentences = self._extract_sentences(text)
        sentence_lengths = [len(self._extract_words(s)) for s in sentences]

        stats = TextStats(
            total_words=sum(Counter(words).values()),
            unique_words=len(word_count),
            average_sentence_length=(
                sum(sentence_lengths) / len(sentence_lengths)
                if sentence_lengths else 0
            ),
            most_common_words=word_count.most_common(TOP_WORDS_COUNT)
        )

        return stats, word_count

    def save_results(self,
                     stats: TextStats,
                     output_path: str = "analyzer_result.json") -> None:
        """
        Save the analysis results to a JSON file.

        Args:
            stats (TextStats): The text statistics object.
            output_path (str, optional): The path to save the results. 
            Defaults to "analyzer_result.json".
        """
        with open(OUTPUT_FOLDER / output_path, "w") as json_file:
            json.dump(stats.__dict__, json_file, ensure_ascii=False, indent=4)

    def _extract_words(self, text: str) -> List[str]:
        return re.findall(r"\b\w+\b", text.lower())

    def _extract_sentences(self, text: str) -> List[str]:
        return [s.strip() for s in re.split(r"[.!?]", text) if s.strip()]
