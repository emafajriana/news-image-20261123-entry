# The World in One Picture — Monday 23 November 2026

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/emafajriana/news-image-20261123-entry/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/emafajriana/news-image-20261123-entry/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

A one-image front page summing up the world's news of Monday 23 November 2026,
built for the make.fun **news-image-20261123** bounty. The program is
`main.py` (Python 3.13, standard library only): it copies the bundled
`entry.png` to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`
outside the grader), verifying the image signature before the copy and
the written byte length afterwards. It runs with no network and writes
the same bytes on every run.

## What's in the picture

A newspaper front page, "THE WORLD IN ONE PICTURE — MONDAY 23 NOVEMBER 2026",
with four illustrated panels and an ALSO TODAY strip:

- **CLIMATE** — COP31 collapses: no deal in Antalya. The summit ends with no
  agreement after the EU and some 130 nations reject a text with no fossil
  fuels. Art: an empty summit hall, a broken globe and a snapped pencil on
  the table, delegates walking away.
- **UKRAINE** — Boy, 7, pulled alive from rubble in Dymer. Rescuers lift a
  small boy from the debris of a damaged village house at dawn; a Russian
  strike killed at least 10 north of Kyiv.
- **MARKETS** — AI sell-off rattles world markets. The Nikkei falls 5.06%
  and the S&P 500 3.7% as Asian regulators step in; gold rises 2.72%.
  Art: a plunging red chart line over blank trading boards, one gold bar
  rising the other way.
- **POLITICS** — Democrats take biggest House majority since 1992, winning
  258 seats. Art: the US Capitol dome behind a rising blue wave.

**ALSO TODAY** — a Ukrainian sea drone sinks the Russian corvette Merkury
off Libya · Trump, Putin and Xi meet in Shenzhen · a magnitude 6.5 quake
shakes Vanuatu · Belgian airports shut as a strike grounds flights.

## How it was made

The four panel illustrations were generated as flat, bold editorial art
with no text in them; the front page itself — masthead, headlines, sublines,
date lines and the ALSO TODAY strip — was lettered locally with Python PIL
so every word is spelled exactly and stays legible at thumbnail size.
News facts are the verified 23 November 2026 roundup recorded in the
project brief (One Turn daily digest, BBC via NewsBites, Inshorts,
Dow Jones/Morningstar).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Writes `out/entry.png` (1024 × 1024 PNG, under the 1 MiB cap).

## License

MIT — see `LICENSE`.
