NAME = OSCAR-organigram

all: $(NAME).pdf $(NAME).svg

$(NAME).pdf: $(NAME).tex
	latexmk -lualatex $<

# poppler, not dvisvgm: dvisvgm drops the axial shading of the leftmost column
$(NAME).svg: $(NAME).pdf
	pdftocairo -svg $< $@

png: $(NAME).png
$(NAME).png: $(NAME).pdf
	pdftoppm -r 300 -png -singlefile $< $(NAME)

clean:
	latexmk -C
	rm -f $(NAME).svg $(NAME).png

.PHONY: all clean png
