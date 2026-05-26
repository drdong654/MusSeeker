# MusSeeker_bot

## Commands

```bash
uv pip install .        # install deps
python __main__.py      # run bot
docker compose up --build  # run via Docker
```

## Setup

- `TOKEN=...` in `.env` (already gitignored)
- JS runtime required for yt-dlp: install `deno` or `nodejs`
- `ffmpeg` required for mp3 conversion (in Dockerfile but not documented for local dev)
- PO tokens generated automatically via `bgutil-ytdlp-pot-provider` — no cookies needed

## Architecture

- Flat package (`musbot`), no `src/` dir
- Entrypoint: `__main__.py` — creates `Bot`, `Dispatcher`, registers 2 routers
- Router registration order matters: `commands_router` (commands) → `download_router` (catch-all)
- `handlers/download.py` catches all unmatched messages via bare `@router.message()`
- yt-dlp runs synchronously in a thread via `asyncio.to_thread(download_music, url)` in `services/downloader.py`
- Output goes to `downloads/` (gitignored); files cleaned up after sending

## Gotchas

- No tests, no linter, no type checker configured
- Uses `mweb` + `android` player clients with auto PO tokens — no cookies required
- `ffmpeg` must be installed on the host (mp3 postprocessor)
