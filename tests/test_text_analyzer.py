import pytest
from unittest.mock import patch, mock_open
from text_analyzer.text_analyzer import TextAnalyzer, TextStats
from text_analyzer.config import OUTPUT_FOLDER, TOP_WORDS_COUNT

SAMPLE_TEXT = "This is a sample text for testing.\n Test with a new sentence"


@pytest.fixture
def analyzer():
    return TextAnalyzer()


@pytest.fixture
def sample_text():
    return SAMPLE_TEXT


def test_analyze_empty_text(analyzer):
    text = ""
    stats, word_count = analyzer.analyze(text)

    assert isinstance(stats, TextStats)
    assert stats.total_words == 0
    assert stats.unique_words == 0
    assert stats.average_sentence_length == 0
    assert stats.most_common_words == []
    assert len(word_count) == 0


def test_analyze_simple_text(analyzer):
    text = SAMPLE_TEXT
    stats, word_count = analyzer.analyze(text)

    assert stats.total_words == 12
    assert stats.unique_words == 11
    assert pytest.approx(stats.average_sentence_length, 0.1) == 6.0
    assert len(stats.most_common_words) == TOP_WORDS_COUNT
    assert word_count["a"] == 2


def test_extract_words(analyzer, sample_text):
    words = analyzer._extract_words(sample_text)
    assert len(words) == 12


def test_extract_sentences(analyzer, sample_text):
    sentences = analyzer._extract_sentences(sample_text)
    assert len(sentences) == 2


def test_save_results(analyzer):

    stats = TextStats(
        total_words=10,
        unique_words=8,
        average_sentence_length=3.0,
        most_common_words=[
            ("hello", 3), ("world", 2)])

    output_path = "test_result.json"

    with patch("builtins.open", mock_open()) as mocked_file:
        with patch("json.dump") as mocked_json_dump:
            analyzer.save_results(stats, output_path)

            mocked_file.assert_called_once_with(
                OUTPUT_FOLDER / output_path, "w")

            mocked_json_dump.assert_called_once_with(
                stats.__dict__, mocked_file(), ensure_ascii=False, indent=4)
