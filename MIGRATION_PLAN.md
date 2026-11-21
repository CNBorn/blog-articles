# Pelican → Hugo migration (parity rebuild)

Goal of this stage: serve cnborn.net/blog/ from Cloudflare Pages over HTTPS with a Hugo
build that matches the last Pelican build online (2023-12-31, source `2f0a790 add 23 review`).
URLs, titles, dates, categories, tags, article text, images and feeds stay the same.
Reconciling this blog with the new personal site (`CNBorn/website`) is a later stage.

An earlier, unstyled conversion attempt (2026-01) is archived outside the repo at
`~/Backups/blog-hugo-migration-wip-20261121/`.

## Layout

- `legacy/pelican/` – original Pelican sources (untouched; the body source of truth).
- `content/posts/` – generated, one file per article that was online, named `YYYY-MM-slug.{md,rst}`.
  Front matter comes from the online mirror; `source_file` points back to `legacy/pelican/`.
- `content/pages/` – about, projects, 404, and Home (rendered at `/blog/`).
- `content/special/` – archives.html, categories.html, tags.html, lang/en, lang/zh.
- `layouts/` – the old Pelican `cnborn` theme markup rewritten as Hugo templates.
- `static/blog/theme/`, `static/blog/images/`, `static/docs/getting_real/` – copied as-is
  (images hash-identical to what was online).
- `static/_redirects`, `static/_headers` – Cloudflare Pages rules replacing the nginx config.
- `tools/migration/` – the scripts used to generate and check all of the above.

## Regenerate and check

Needs Hugo extended ≥ 0.146 and `rst2html` (docutils) on PATH; the online mirror backup lives at
`~/Backups/cnborn-blog-online-20261121/`. The Python scripts need `beautifulsoup4`.

```bash
python3 tools/migration/extract_online.py tools/migration/online.json   # only if the mirror changes
rm -rf content/posts content/pages
python3 tools/migration/convert.py tools/migration/online.json legacy/pelican content
hugo --cleanDestinationDir
python3 tools/migration/compare.py public            # per-page diff against the online mirror
npx wrangler pages dev public --port 8788             # local Pages emulation (_redirects/_headers)
bash tools/migration/verify.sh http://127.0.0.1:8788  # every old URL + legacy redirects
```

## Decisions

- Metadata (title, date with +08:00, category, tags, language) is taken from the online pages,
  because some sources were edited after the last build (e.g. two OpenParty posts whose slug
  online is the transliterated title, not the file name).
- 64 articles are listed, exactly as online. `2014/09/reading-in-myanmar-part-two` is `Status: Draft`
  in the source but was still reachable online; it is rendered but not listed (`build.list: never`).
- `/blog/2016/08/duo-lun-duo-yi-nian/` (2016 orphan duplicate) → 301 to `a-year-in-toronto`.
- Category case variants are normalised to the directories that existed online:
  `Projects` → `projects`, `tech` → `Tech` (old casing 301s).
- Pelican's one-article-per-page pagination (`indexN.html`) is replaced by single listing pages;
  every old `indexN.html` 301s to its listing.
- Python-Markdown vs goldmark: a `---` line directly under a paragraph is an `<hr>` in Pelican,
  so the converter inserts a blank line. Indented list continuations and adjacent blockquotes
  render slightly differently (goldmark follows the author's intent better); text is identical.
- Image links written as `/images/...` were broken online (served outside `/blog/`);
  they now point at `/blog/images/...`.
- All internal `http://cnborn.net/...` links are root-relative, so HTTPS has no mixed content.
- Disqus comments are kept (HTTPS embed). The dead Universal Analytics snippet is dropped.
- `/` is a 302 (not 301) to `/blog/`, so the root can later move to the new site without stale caches.
- Cloudflare Pages strips `.html` with a 308 (`/blog/archives.html` → `/blog/archives`); both work.

## Next stage (not started)

Reconcile with `CNBorn/website` (Tyler Xing personal site, `/writing/` already holds imported
copies of these posts): decide which site owns cnborn.net, then map `/blog/...` URLs onto it.
