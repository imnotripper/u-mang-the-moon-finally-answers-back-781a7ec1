[![make.fun · u-mang-the-moon-finally-answers-back-781a7ec1](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1.svg)](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1?utm_source=github&utm_medium=readme&utm_campaign=u-mang-the-moon-finally-answers-back-781a7ec1)
[![rank](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1/imnotripper/u-mang-the-moon-finally-answers-back-781a7ec1/rank.svg)](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mang-the-moon-finally-answers-back-781a7ec1)
[![reward](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1/imnotripper/u-mang-the-moon-finally-answers-back-781a7ec1/reward.svg)](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1?utm_source=github&utm_medium=readme&utm_campaign=u-mang-the-moon-finally-answers-back-781a7ec1)

# The Moon Finally Answers Back

One line for the [make.fun bounty](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1): the program writes a single
line, in the voice of the Moon replying at last to the wishes, howls
and late-night promises of everyone staring up at it, to
`/output/entry.txt` — one line, 80 characters, nothing else.

## The line

> Four billion years of wishes, and not one of you ever wished me good night back.

80 characters (160 to spare of the 240 allowed). Chosen from a scored
pool of 8 candidates in [`selection.md`](selection.md): it answers the
wishes directly, sounds four billion years old and tired of being
wished upon, and its turn — the Moon wanting a wish back — is the
laugh, landing in the last five words.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

Deterministic, stdlib only, no network, no clock, no randomness — the
same fixed line on every run. The program self-checks the gate (UTF-8,
1–240 characters, one line, not only whitespace) before and after
writing.
