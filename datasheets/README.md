# Datasheets

`build.py` renders each `products/<KEY>.toml` to `<KEY>/datasheet/<KEY>_Datasheet.pdf`. Commit the TOML and the PDF together.

```
uv run --no-project --python 3.12 --with weasyprint==70.0 python datasheets/build.py [KEY ...]
```

No KEY builds every product. `--out DIR --flat` writes review copies to DIR instead.

## New datasheet

1. Copy `template.toml` to `products/<KEY>.toml`, where KEY is the product's directory in this repo. The template shows every field and section kind.
2. Add the product photo to `photos/`: JPEG, about 1080 px wide, product on a light background. Set `photo_frame = true` for a photo on white.
3. Fill it from the sources, build, and read every page.
4. Have someone who didn't write it check every value against the sources before publishing.

## Layout

`build.py` fixes the layout; data files can't change it.

- **Page 1:** title block, intro, key features and specifications, with a side column of photo, at a glance, compliance and resources. Everything must fit on page 1: if the build pushes the columns to page 2, cut content.
- **Page 2 onward:** the `[[sections]]` in order, usually variants, interfaces and pinouts, bus maps, firmware, then notes. `new_page = true` starts a page, e.g. for a full page of pinouts.
- **Running header:** product, datasheet version and hardware revision. The footer line is built from `doc_id`, `version`, `date` and `sources`.

## Content

- **Sources:** every value comes from a source named in `sources`: schematic and its revision, BOM, STEP model, PX4 or ArduPilot board definition, component data sheets, ARK measurements, ARK docs.
- **Firmware:** support that changes from release to release belongs in the docs, not here.
- **Sizes:** intro 2–3 sentences. Key features: 8 one-line bullets at most. Specifications: about 12–16 rows in 2–3 groups. At a glance: 10 rows at most.
- **Variants:** SKUs that share a board share a datasheet. A `compare` section lists what differs between them. The ARK SCH16T and SCH16T-K10 keep separate sheets, which the store and docs already link.
- **Temperature:** give operating and storage ranges. If they come from component data sheets rather than a test, say so in `sources`.
- **Compliance:** only claims we can back: made in the USA, NDAA compliant, Blue UAS Framework listed (when listed), and open standards the product implements (e.g. Pixhawk Autopilot Bus). No FCC claim.
- **Unmeasured values:** start them with `TBD`; they render marked.
- **Notation:**
  - Units take a space: `5 V`, `±32 g`, `7.5 g`.
  - Ranges use an en dash and the minus sign: `−25 °C to +85 °C`, `5.5–54 V`.
  - Dimensions use `×`.
  - Headings are capitals and unnumbered.

## Versions

- **`version`:** the datasheet's own version. Bump it with every published change: minor for corrections and additions, major for a new hardware revision.
- **`date`:** the day that version was issued.
- **`rev`:** the schematic revision of the shipping board.

## Files

- **`products/`:** one TOML per datasheet. `out` overrides the output path when two datasheets share a product directory.
- **`photos/`:** product photos, plus figures such as block diagrams (SVG or PNG).
- **`assets/`:** stylesheet, logo and IBM Plex fonts (SIL Open Font License, `assets/fonts/OFL.txt`).

`ARK_12S_CAN_ESC/datasheet/` is a preliminary sheet made outside this generator.
