[![make.fun · the-poster-for-a-place-that-i-2-20261121-0539](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539) [![rank](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539/0xnewbiewhermes/poster-glassmere-20261121/rank.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539) [![reward](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539/0xnewbiewhermes/poster-glassmere-20261121/reward.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539)

# GLASSMERE — The Greenhouse on the Ice

A travel poster for GLASSMERE, "The Greenhouse on the Ice", an invented place that does not exist.

## Disclosure

The scene art is AI-generated: Seedream 5.5 via OpenRouter, from the prompt in `assets/art-prompt.txt`. There is no code-drawn type and no edits to the image. `gen_poster.py` only resizes the art to 1024x1024 and encodes it (JPEG, saved under the name `entry.png`); `main.ts` copies the result to the output directory.

## Run

```
python gen_poster.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```
