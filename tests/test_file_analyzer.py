import pytest
from text_analyzer.text_analyzer import TextAnalyzer, TextStats
from text_analyzer.config import TOP_WORDS_COUNT

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
