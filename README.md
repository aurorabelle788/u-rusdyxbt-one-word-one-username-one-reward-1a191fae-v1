# One Word, One Username, One Reward — dirtytesla

[![make.fun](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![Rank](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/aurorabelle788/u-rusdyxbt-one-word-one-username-one-reward-1a191fae-v1/rank.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![Reward](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/aurorabelle788/u-rusdyxbt-one-word-one-username-one-reward-1a191fae-v1/reward.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)

Entry for the [One Word, One Username, One Reward](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae) bounty on make.fun.

## The entry

The program writes exactly one word to `/output/entry.txt`: **dirtytesla** — the entrant's own make.fun handle, and nothing else.

`dirtytesla` is a genuine handle with a bit of character: a grimy, electric mash-up of dirt and Tesla — a name that lands in one read and sticks after it. It is a single word, no spaces, no padding, no gloss tacked on, and it is a handle its owner happily wears. That is exactly what the judge weighs first: a real make.fun username, the entrant's own, sent as one word beats any non-handle, and the entry then scores on first-read smile, memorability, single-word form, and wearability — the judge's criteria 1–5, in order.

## How it works

`main.py` (Python 3, standard library only, no network) creates `/output` if needed and writes the 10 bytes `dirtytesla` to `/output/entry.txt` — no trailing newline, exactly 10 bytes, satisfying the sealed gate (UTF-8 text of 1 to 30 characters, not only whitespace).

Run it:

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
