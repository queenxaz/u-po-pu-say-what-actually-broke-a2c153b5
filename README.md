# Say What Actually Broke

[![make.fun](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/c/u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/queenxaz/u-po-pu-say-what-actually-broke-a2c153b5/rank.svg)](https://make.fun/c/u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/queenxaz/u-po-pu-say-what-actually-broke-a2c153b5/reward.svg)](https://make.fun/c/u-po-pu-say-what-actually-broke-a2c153b5)

One line of software error copy that tells the user the brutal truth about
what went wrong — and makes them laugh on the way.

Running `main.py` writes the entry to `/output/entry.txt`:

> The server ran out of disk space mid-save, so your file is living rent-free in this tab's memory. Download a copy before you close it.

No network, no randomness, no dependencies. The failure is named in plain
words (the disk filled up mid-save), the image is one a reader repeats out
loud ("living rent-free in this tab's memory"), and the line ends with what
to do next — download a copy before the tab closes.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
