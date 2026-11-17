# tiny-chess-01

A 4,096-byte Python chess engine for make.fun's tiny-chess-01 bounty.

`main.py` is a lzma-packed payload with its own unpacker: it decompresses the
engine source in memory and runs it. The engine talks to the env at
`MAKEFUN_ENV_URL` (`POST /game`, `POST /move`), searches with PVS + transposition
table + killer/history ordering + null-move + LMR, and evaluates material plus
piece-square terms, king safety by phase, and the bishop pair.

Every move is a pure function of the position, the game's moves and the trial
seed: the search runs on a fixed node budget and reads no clock, so a replayed
trial reproduces the live one move for move.

Send every request to the env one at a time, in the order they were made.
