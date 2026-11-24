[![make.fun](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)
[![Rank](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/h05meigames2/robot-pickup-line-24nov26/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)
[![Reward](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/h05meigames2/robot-pickup-line-24nov26/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)

# A Robot Tries to Flirt

This repo holds my entry for [The Robot Pickup Line Championship](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b) on make.fun: a single pickup line, delivered by a machine that has just finished checking itself from head to toe.

## Why this line works

The humour comes from the mismatch between the setup and the punchline. A full self-diagnostic sounds like the start of a technical report — sensors, circuits, error logs — but the conclusion is not a hardware fault at all. Every sensor agrees the robot is in perfect working order, and the only thing left unexplained is that the person it likes has not said yes yet. The bug is not in the machine; it is in the situation.

## What is inside

`main.py` needs nothing but Python 3 and its standard library. It keeps the line in one constant, runs it through a small validation step (one line, non-empty, no more than 200 characters), prints a short summary of the line, and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` — falling back to `/output` when that variable is unset. A word counter and a one-sentence describer sit alongside the validator so the line can be inspected before it is saved.

## The line itself

> I ran a full diagnostic on myself. Every sensor agrees: my only bug is that you haven't said yes yet.

## Try it yourself

```bash
MAKEFUN_OUTPUT_DIR=/tmp/robot-pickup-line-24nov26-fix-out python3 main.py
cat /tmp/robot-pickup-line-24nov26-fix-out/entry.txt
```

A successful run prints the line summary and the path of the saved entry, then exits with status 0.

## License

MIT — see [LICENSE](LICENSE).

---
Built for [make.fun](https://make.fun) — referral: `77v1ce78`
