import pytest
from collections import Counter
from unittest.mock import patch
from text_analyzer.plotter import WordFrequencyPlotter


@pytest.fixture
def word_count():
    return Counter(
        {
            "the": 5,
            "quick": 3,
            "brown": 3,
            "fox": 2,
            "jumps": 2,
            "over": 2,
            "lazy": 1,
            "dog": 1,
        }
    )


def test_plot_creation(word_count, tmp_path):
    plotter = WordFrequencyPlotter()
    output_path = tmp_path / "test_plot.png"

    with patch("matplotlib.pyplot.savefig") as mock_savefig:
        plotter.plot(word_count, output_path)
        mock_savefig.assert_called_once()

    # Check if the correct number of words are plotted
    with patch("matplotlib.pyplot.bar") as mock_bar:
        plotter.plot(word_count, output_path)
        assert mock_bar.call_count == 1
        args, kwargs = mock_bar.call_args
        assert len(args[0]) == 8
