# Figures for the OSCAR website.  The .tex files are the sources; the outputs
# committed beside them are the ones the site and talks use.
#
# Needs lualatex (TeX Live) plus poppler for pdftocairo and pdftoppm.

all: OSCAR-organigram.pdf OSCAR-organigram.svg OSCAR-overview.png

%.pdf: %.tex
	lualatex -interaction=nonstopmode -halt-on-error $<

# poppler, not dvisvgm: dvisvgm drops the axial shading of the organigram
%.svg: %.pdf
	pdftocairo -svg $< $@

# about.md shows this at 70% width, so 1190px is plenty
OSCAR-overview.png: OSCAR-overview.pdf
	pdftoppm -png -singlefile -scale-to-x 1190 -scale-to-y -1 $< $(basename $@)

# print resolution, e.g. `make OSCAR-organigram.png`
%.png: %.pdf
	pdftoppm -png -singlefile -r 300 $< $(basename $@)

clean:
	rm -f *.aux *.log *.synctex.gz

distclean: clean
	rm -f OSCAR-organigram.pdf OSCAR-organigram.svg OSCAR-overview.pdf OSCAR-overview.png

.PHONY: all clean distclean
