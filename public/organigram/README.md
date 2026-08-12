# OSCAR organigram

`OSCAR-organigram.tex` redraws the old organigram in LuaLaTeX + TikZ.

    make            # PDF and SVG
    make png        # 300 dpi PNG

Needs LuaLaTeX with TikZ and Fira Sans (TeX Live's `fira`), plus poppler
(`pdftocairo`, `pdftoppm`) for SVG and PNG.

## Editing

Colours and all layout dimensions sit in two blocks at the top of the
`.tex`; the body is one node per box. Columns are placed by index via
`\colx{n}` / `\topicx{n}`, so a new column means bumping `\ncols` and
adding a node — the area row re-centres itself and the frame grows with
it.

Arrows use two helpers:

    \dropto {<from>}{<to>}            straight down
    \routeto{<from>}{<depth>}{<to>}   down, sideways, down

`<depth>` is millimetres below the source; the existing values are chosen
so that the horizontal runs do not overlap.

The leftmost column is one box with a light-to-dark green gradient
because Hecke/Nemo/AbstractAlgebra are Julia *and* cornerstone at once.
