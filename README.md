# tiny-chess-01

A 4,096-byte Python chess engine for make.fun's tiny-chess-01 bounty.

`main.py` is an lzma-packed payload with its own unpacker: it decompresses the
engine source in memory and runs it. The engine talks to the env at
`MAKEFUN_ENV_URL` (`POST /game`, `POST /move`), one request at a time, in the
order they were made.

## Search

Principal variation search over a fixed node budget, with a transposition table,
killer and history move ordering, null-move pruning and late move reductions.
Quiescence is depth-capped so the budget cannot be spent on captures alone. The
evaluation is material (pawn 100, knight 320, bishop 330, rook 500, queen 900)
plus piece-square terms, a phase-blended king term and the bishop pair.

The board is a 120-square mailbox: indices 21..98 are the playable squares, and
every sliding loop carries a file guard so a rook cannot wrap from the a-file to
the h-file and report an attack it does not have.

## Determinism

Wall-clock reads are forbidden by RULES.txt: a move near the 10-second limit can
fall on the other side of it on the replay, which makes the trial
nondeterministic. This engine searches a fixed node count instead, so the same
position and history always yield the same move. No unseeded randomness, no
clock, and the transposition table, killer slots and history scores are cleared
per move.

## Size

`main.py` 3,933 bytes of the 4,096 cap; the whole snapshot 5,831 bytes of 8,192.