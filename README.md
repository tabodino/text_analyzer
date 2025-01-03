# 📈 Text Analysis Project

This project analyzes text files and generates word frequency plots.

![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)
![Pylint Score](https://img.shields.io/badge/pylint-10.00-brightgreen.svg)
![Python](https://img.shields.io/badge/python->3.10-blue.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
## 🖥️ Setup

### Using Poetry (Recommended)

1. Install Poetry if you haven't already:

*For Linux, macOS, Windows (WSL)*
   ```
   curl -sSL https://install.python-poetry.org | python3 -
   ```
*Add export PATH if necessary*

2. Install dependencies:
   ```
   poetry install
   ```

3. Activate the virtual environment:
   ```
   poetry shell
   ```

### Using pip and venv

1. Create a virtual environment:

   *For Linux and Mac*
   ```
   python3 -m venv venv
   ```
   *or for Windows*
   ```
   python -m venv venv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## ⌨️ Usage

Run the main script:

```
poetry run python main.py
```

Or, if using pip and venv:

```
python main.py
```

### With Docker

Build the image
```
docker build -t text-analyzer .
```

Run the container
```
docker run -v $(pwd)/output:/app/output text-analyzer

```

## Running Tests

### With Poetry

```
poetry run pytest
```

### With pip and venv

```
pytest
```

### Run code coverage
```
pytest --cov=text_analyzer --cov-report=html tests/
```

## 📂 Project Structure

```bash
+
|   main.py           # Entry point of the application
|   pyproject.toml    # Configuration file for poetry
|   requirements.txt  # Required dependencies for this project 
+---output            # Default output folder for generated plot
+---tests             # Directory containing test files
\---text_analyzer     # Package containing the core functionality
|   |   config.py
|   |   file_handler.py
|   |   plotter.py
|   |   text_analyzer.py
|   |   __init__.py
|   |
```

## ✨ Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add some feature'`)
5. Push to the branch (`git push origin feature/your-feature`)
6. Create a new Pull Request

## 📄 License

This project is licensed under the MIT License.