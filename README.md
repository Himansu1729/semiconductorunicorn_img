# semiconductorunicorn_img

Public image host for the Instagram account @semiconductorunicorn. Metricool pulls post images from the raw links of files in this repo.

## Layout
- `YYYY-MM-DD/` : images for that day's post (PNG, 1080x1350)
- `tools/design_helpers.py` : drawing helpers (gradient, circuit traces, chip graphic, `content()` slide, `cta()` slide, `finish()` saver)
- `tools/example_fact_post.py` : example single-fact post built with the helpers

## Usage
`OUT_DIR=./out python3 -I your_script.py` (run from `tools/`). Fonts come from `/usr/share/fonts/opentype/inter/`.

## Image links
`https://raw.githubusercontent.com/Himansu1729/semiconductorunicorn_img/main/<folder>/<file>.png`
