# OSCAR website figures

Two TikZ drawings and everything needed to rebuild them:

| source                  | output            | used by                   |
|-------------------------|-------------------|---------------------------|
| `OSCAR-overview.tex`    | `.pdf` and `.svg` | `about.md`                |
| `OSCAR-organigram.tex`  | `.pdf` and `.svg` | talks; more technical     |

The two are deliberately different in kind: the overview is the friendly
picture, the organigram is the detailed one. Both stay.

    make            # everything committed here
    make clean      # LaTeX by-products
    make OSCAR-organigram.svg   # build the organigram SVG and its PDF prerequisite
    make OSCAR-overview.svg         # build the overview SVG and its PDF prerequisite
    make OSCAR-organigram.png   # optional 300 dpi raster
    make OSCAR-overview.png         # optional 300 dpi raster

Needs LuaLaTeX with TikZ and Fira Sans (TeX Live's `fira`), plus poppler
(`pdftocairo`, `pdftoppm`).

The figure builds are designed to be reproducible within a consistent build
environment, so a rebuild should only show up in `git diff` when the drawing
changed. Generated files may vary between build environments.

## Editing the organigram

Colours and all layout dimensions sit in two blocks at the top of the
`.tex`; the body is one node per box. The five columns are chained left
to right, so a new one is a single node and their widths may differ —
the middle three are narrower than `\colw` to leave `\gutter`, the strip
on the right that the f4ncgb arrow runs down. The area row is placed by
index via `\topicx{n}` and re-centres itself over the whole width.

Arrows use two helpers:

    \dropto {<from>}{<to>}            straight down
    \routeto{<from>}{<depth>}{<to>}   down, sideways, down

`<depth>` is millimetres below the source; the existing values are chosen
so that the horizontal runs neither overlap nor cross needlessly.

The leftmost column is one box with a light-to-dark green gradient
because Hecke/Nemo/AbstractAlgebra are Julia *and* cornerstone at once.

## Credits

`OSCAR-overview.tex` is by Martin Bies, who contributed it in
[#483](https://github.com/oscar-system/oscar-website/pull/483); its
colours and fonts were later aligned with the organigram.

`OSCAR-organigram.tex` was written by Claude Opus 5 (Anthropic), directed
and reviewed by OSCAR developers; the commits carry `Co-Authored-By`
trailers for the individual steps.
