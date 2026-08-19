# Figures for the OSCAR website.  The .tex files are the sources; the outputs
# committed beside them are the ones the site and talks use.
#
# Needs lualatex (TeX Live) plus poppler for pdftocairo and pdftoppm.

FIGURES = OSCAR-organigram OSCAR-overview

all: $(FIGURES:=.pdf) $(FIGURES:=.svg)

%.pdf: %.tex
	lualatex -interaction=nonstopmode -halt-on-error $<

# poppler, not dvisvgm: dvisvgm drops the axial shading of the organigram.
# Dropping the pt size leaves the viewBox, so a browser opening the file on its
# own scales it to the window instead of showing it at a fixed small size.
%.svg: %.pdf
	pdftocairo -svg $< $@
	sed 's/\(<svg [^>]*\) width="[^"]*" height="[^"]*"/\1/' $@ > $@.tmp
	mv $@.tmp $@

# a raster, if one is ever needed: `make OSCAR-organigram.png`
%.png: %.pdf
	pdftoppm -png -singlefile -r 300 $< $(basename $@)

clean:
	rm -f *.aux *.log *.synctex.gz

distclean: clean
	rm -f $(FIGURES:=.pdf) $(FIGURES:=.svg) $(FIGURES:=.png)

.PHONY: all clean distclean
