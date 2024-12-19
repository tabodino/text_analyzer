import pytest
from text_analyzer.file_handler import FileHandler

SAMPLE_TEXT = "This is a sample text for testing."


def create_mock_file(tmp_path, filename, content):
    file_path = tmp_path / filename
    file_path.write_text(content, encoding="utf-8")
    return file_path


def test_check_extension_txt(tmp_path):
    file_path = create_mock_file(tmp_path, "test.txt", SAMPLE_TEXT)
    handler = FileHandler(file_path)
    assert handler.check_extension() is True


def test_check_extension_md(tmp_path):
    file_path = create_mock_file(tmp_path, "test.md", SAMPLE_TEXT)
    handler = FileHandler(file_path)
    assert handler.check_extension() is True


def test_check_extension_unsupported(tmp_path):
    file_path = create_mock_file(tmp_path, "test.pdf", SAMPLE_TEXT) 
    handler = FileHandler(file_path) 
    with pytest.raises(ValueError, match="Unsupported file type: .pdf."):
        handler.check_extension()


def test_extract_text(tmp_path):
    file_path = create_mock_file(tmp_path, "test.txt", SAMPLE_TEXT)
    handler = FileHandler(file_path)
    extracted_text = handler.extract_text()
    assert extracted_text == SAMPLE_TEXT
