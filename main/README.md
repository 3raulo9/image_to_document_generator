# Image to Document Generator

A simple Python GUI tool for converting multiple images into a single PDF document.

## Features

- Add images one by one
- Add multiple images at once
- Remove selected images
- Merge images into a single PDF
- Simple dark-themed interface

## Installation

Clone the repository:

cd IMAGE_TO_DOCUMENT_GENERATOR/main

Create virtual environment (optional but recommended):

python -m venv venv

Activate virtual environment:

Windows:
venv\\Scripts\\activate

Linux / macOS:
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

## Generate requirements.txt

Run:

pip freeze > requirements.txt

## Run the Application

python main.py

## Build Executable

Install PyInstaller:

pip install pyinstaller

Build executable:

pyinstaller --onefile --windowed main.py

Executable output:

dist/main.exe

## .gitignore

build/
dist/
*.spec
venv/
__pycache__/

