name: Code Quality

on:
  push:
    paths:
      - "**.py"

jobs:
  lint:
    name: Python Lint
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: "3.9"
      - name: Run flake8
        uses: julianwachholz/flake8-action@v2
        with:
          checkName: "Python Lint"
          path: path/to/files
          plugins: flake8-spellcheck
          config: path/to/flake8.ini
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
