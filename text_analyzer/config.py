from pathlib import Path


TOP_WORDS_COUNT = 10

PLOT_BAR_COLOR = "skyblue"

OUTPUT_FOLDER = Path(__file__).parent.parent / "output"

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

CHARSET = "utf-8"
