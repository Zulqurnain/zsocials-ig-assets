# zsocials-ig-assets

Public host for ZSocials Instagram approved-visual assets.

## Why this exists
Instagram Graph (`INSTAGRAM_CREATE_MEDIA_CONTAINER`) hard-requires a public
`http(s)` image URL. The content queue stored only local `image_path` values,
which returned HTTP 400 "not a valid URL". This repo is the public hosting
layer: each approved visual is committed here and referenced by its permanent
`raw.githubusercontent.com` URL.

Notes on host choice:
- Discord webhook CDN URLs expire in ~24h (signed `ex=` param) — unsafe for
  items scheduled days out. REJECTED.
- catbox.moe / 0x0.st anonymous upload — rejected/disabled.
- **GitHub raw (this repo) = permanent, no expiry, no new creds** — CHOSEN.
  `gh` is already authenticated as owner `Zulqurnain`.

## Layout
```
nirmal-shah/<visual_brief_id>_4x5.jpg
zj-the-nomad/<visual_brief_id>_4x5.jpg
```
Filenames preserve the `visual_brief_id` so the queue mapping is reversible.

## Public URL form
https://raw.githubusercontent.com/Zulqurnain/zsocials-ig-assets/main/<brand-slug>/<filename>

## Backfilling a queue item
The publish pipeline should read, in priority order:
`visual_image_url` → `image_url` → `public_url`. `image_path` (local) is NOT
publishable and must not be passed to Instagram Graph.

## Adding a new visual (pipeline step)
1. Copy the generated image into `<brand-slug>/`.
2. `git add -A && git commit -m "..." && git push`
3. Set `visual_image_url` = the raw.githubusercontent URL on the queue item.

See `host_visual.py` for a one-shot helper.
