#!/bin/bash

set -e

# --- Info Message ---
echo "--------------------------------------------------"
echo "This script requires the following tools to run:"
echo " - pdflatex (TeX Live or MiKTeX)"
echo " - ImageMagick (for the 'convert' command)"
echo "Make sure they are installed and available in PATH."
echo "--------------------------------------------------"
echo ""

# --- Check dependencies ---
command -v pdflatex >/dev/null 2>&1 || { echo >&2 "Error: pdflatex is not installed."; exit 1; }
command -v convert >/dev/null 2>&1 || { echo >&2 "Error: ImageMagick 'convert' is not installed."; exit 1; }

# --- Set paths ---
TEX_DIR="../_data"
OUTPUT_DIR="../public"
BASENAME="OSCAR-overview"

# --- Compile LaTeX to PDF in the data folder ---
echo "Compiling LaTeX..."
(
  cd "$TEX_DIR"
  pdflatex "$BASENAME.tex" > /dev/null
)

# --- Convert PDF to PNG (high-res) ---
echo "Converting PDF to high-res PNG..."
convert -density 300 "$TEX_DIR/$BASENAME.pdf" -quality 100 "$TEX_DIR/$BASENAME.png"

# --- Resize and compress PNG for web ---
echo "Resizing and optimizing PNG for web..."
convert "$TEX_DIR/$BASENAME.png" -resize 1190x1000 -strip -quality 85 "$OUTPUT_DIR/$BASENAME.png"

# --- Clean up intermediate files ---
echo "Cleaning up..."
rm -f "$TEX_DIR/$BASENAME.aux" "$TEX_DIR/$BASENAME.log" "$TEX_DIR/$BASENAME.pdf" "$TEX_DIR/$BASENAME.png"

# --- Signal success ---
echo "Done! Output image: $OUTPUT_DIR/$BASENAME.png"
