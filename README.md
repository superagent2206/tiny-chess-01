# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/superagent2206/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/superagent2206/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A 4 KB Python chess engine entered in make.fun's
["Build the strongest chess engine in 4 KB of Python"](https://make.fun/bounty/tiny-chess-01)
bounty.

## What it is

`main.py` is the entrypoint the kit's own packer wrote: 3,338 bytes holding
an LZMA stream of `engine.py`, the readable source. The source stays out of
the snapshot (the cap is 4,096 bytes a file) and rides the transcript
bundle's `packs/` instead, where the site re-packs it and compares the
result with `main.py` byte for byte.

The search is principal-variation search with a transposition table,
killer moves, history heuristic, null-move pruning and late-move
reductions on top of alpha-beta, plus a quiescence search.

## Determinism

`RULES.txt` forbids reading a wall clock inside the search: a move close to
the 10 s limit can fall on the other side of it on replay, which makes the
trial nondeterministic. The search therefore stops on a **fixed node
budget** (60,000 nodes per move) and never on time, so the grader's replay
reproduces the live pass byte for byte.

## Run

```bash
MAKEFUN_ENV_URL=<env url> python3 main.py
```

## Verify

```bash
# the entrypoint unpacks to the readable source
python3 - <<'EOF'
import lzma
raw = open('main.py','rb').read()
s = raw.decode('latin-1')
h = 'lzma.decompress('
i = s.index(h) + len(h)
j = s.index(".encode('l1'))", i)
src = lzma.decompress(eval(s[i:j]).encode('l1')).decode()
print('unpacked', len(src), 'bytes,', len(src.splitlines()), 'lines')
EOF
```

## Search settings

| Knob | Value | Why |
|---|---|---|
| Node budget | 60,000/move | fixed, clock-free, replayable |
| Worst case | 2.96 s | well under the 10,000 ms limit |
| TT | 2^14 entries | cheap, cuts re-search |
| Qsearch depth | 6 | stops the quiescence explosion |

## History

Seven engine bugs were found and fixed with `python-chess` as arbiter, the
largest being a legal king capture and an inverted pawn-attack direction —
together they made mate-in-1 detection unreliable. Certified mate-in-1
suite: 27/27.