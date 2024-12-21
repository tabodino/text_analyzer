import pytest
from pathlib import Path
from unittest.mock import MagicMock, mock_open, patch
from pypdf import PdfReader
from text_analyzer.file_handler import (
    FileHandler,
    TxtFileHandler,
    PdfFileHandler,
    FileHandlerFactory,
    ALLOWED_EXTENSIONS
)


# Test data
SAMPLE_TEXT = "This is a sample text."
SAMPLE_PDF_TEXT = "This is a sample PDF text."


@pytest.fixture
def sample_txt_file(tmp_path):
    file = tmp_path / "sample.txt"
    file.write_text(SAMPLE_TEXT)
    return str(file)


@pytest.fixture
def sample_pdf_file(tmp_path):
    file = tmp_path / "sample.pdf"
    file.write_bytes(b'%PDF-1.3 (mock PDF content)')  # Mock PDF content
    return str(file)


def test_file_handler_init():
    with pytest.raises(TypeError):
        FileHandler("test.txt")


def test_txt_file_handler_init(sample_txt_file):
    handler = TxtFileHandler(sample_txt_file)
    assert handler.file_path == sample_txt_file


def test_pdf_file_handler_init(sample_pdf_file):
    handler = PdfFileHandler(sample_pdf_file)
    assert handler.file_path == sample_pdf_file


def test_check_extension_valid():
    for ext in ALLOWED_EXTENSIONS:
        handler = TxtFileHandler(f"test{ext}")
        assert handler.check_extension() is None


def test_txt_file_handler_extract_text(sample_txt_file):
    handler = TxtFileHandler(sample_txt_file)
    assert handler.extract_text() == SAMPLE_TEXT


def test_txt_file_handler_extract_text_file_not_found():
    handler = TxtFileHandler("nonexistent.txt")
    with patch("builtins.print") as mock_print:
        result = handler.extract_text()
        assert result is None
        mock_print.assert_called_once()
        assert "Error reading the file" in mock_print.call_args[0][0]


def test_pdf_file_handler_extract_text(sample_pdf_file):
    handler = PdfFileHandler(sample_pdf_file)
    with patch("text_analyzer.file_handler.PdfReader") as mock_pdf_reader:
        mock_page = MagicMock()
        mock_page.extract_text.return_value = SAMPLE_PDF_TEXT
        mock_pdf_reader.return_value.pages = [mock_page]
        assert handler.extract_text() == SAMPLE_PDF_TEXT


def test_file_handler_factory_txt():
    handler = FileHandlerFactory.get_handler("test.txt")
    assert isinstance(handler, TxtFileHandler)


def test_file_handler_factory_md():
    handler = FileHandlerFactory.get_handler("test.md")
    assert isinstance(handler, TxtFileHandler)


def test_file_handler_factory_pdf():
    handler = FileHandlerFactory.get_handler("test.pdf")
    assert isinstance(handler, PdfFileHandler)


def test_file_handler_factory_invalid():
    with pytest.raises(ValueError):
        FileHandlerFactory.get_handler("test.invalid")


def test_txt_file_handler_permission_error():
    with patch("builtins.open", side_effect=PermissionError):
        handler = TxtFileHandler("test.txt")
        with patch("builtins.print") as mock_print:
            result = handler.extract_text()
            assert result is None
            mock_print.assert_called_once()
            assert "Error reading the file" in mock_print.call_args[0][0]


def test_file_handler_factory_case_insensitive():
    handler = FileHandlerFactory.get_handler("TEST.TXT")
    assert isinstance(handler, TxtFileHandler)
