# OSCAR website figures

Two TikZ drawings and everything needed to rebuild them:

| source                  | output                | used by                       |
|-------------------------|-----------------------|-------------------------------|
| `OSCAR-overview.tex`    | `OSCAR-overview.png`  | `about.md`                    |
| `OSCAR-organigram.tex`  | `.pdf` and `.svg`     | talks; more technical         |

The two are deliberately different in kind: the overview is the friendly
picture, the organigram is the detailed one. Both stay.

    make            # everything committed here
    make clean      # LaTeX by-products
    make OSCAR-organigram.png   # 300 dpi raster of any figure

Needs LuaLaTeX with TikZ and Fira Sans (TeX Live's `fira`), plus poppler
(`pdftocairo`, `pdftoppm`).

Both figures build byte for byte reproducibly, so a rebuild only shows up
in `git diff` when the drawing really changed.

## Editing the organigram

Colours and all layout dimensions sit in two blocks at the top of the
`.tex`; the body is one node per box. Columns are placed by index via
`\colx{n}` / `\topicx{n}`, so a new column means bumping `\ncols` and
adding a node — the area row re-centres itself and the frame grows with
it.

Arrows use two helpers:

    \dropto {<from>}{<to>}            straight down
    \routeto{<from>}{<depth>}{<to>}   down, sideways, down

`<depth>` is millimetres below the source; the existing values are chosen
so that the horizontal runs neither overlap nor cross needlessly.

The leftmost column is one box with a light-to-dark green gradient
because Hecke/Nemo/AbstractAlgebra are Julia *and* cornerstone at once.

## Credits

`OSCAR-organigram.tex` was written by Claude Opus 5 (Anthropic), directed
and reviewed by OSCAR developers; the commits carry `Co-Authored-By`
trailers for the individual steps.
