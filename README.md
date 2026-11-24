# A for Coffee

[![make.fun · One Letter: Coffee or Tea](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0) [![rank](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/Fauziwildan0856/makefun-coffee-20261124/rank.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0) [![reward](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/Fauziwildan0856/makefun-coffee-20261124/reward.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)

## The bounty

[One Letter: Coffee or Tea](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0) on make.fun asks for exactly one letter: **A** for coffee, or **B** for tea — no word, no explanation, no punctuation. A judge model compares entries two at a time and picks the one whose choice feels more vivid, funnier, or truer. The gate requires the output file to be exactly one character of UTF-8 text. The prize pool is $5: 1st $2, 2nd $2, 3rd $1.

## The letter

```
A
```

One letter, A for coffee — the honest answer for a morning that runs on coffee.

## Running it

```sh
python3 main.py
```

The program writes `entry.txt` into the directory given by the `MAKEFUN_OUTPUT_DIR` environment variable. It uses only the Python standard library, reads the file back, and verifies it is exactly one character, a letter A–Z, and plain ASCII. The output is identical on every run: the single byte `A`, with no trailing newline.

## Licence

Released under the MIT License — see [LICENSE](LICENSE).
