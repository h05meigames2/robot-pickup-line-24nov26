[![make.fun](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)
[![Rank](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/h05meigames2/robot-pickup-line-24nov26/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)
[![Reward](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/h05meigames2/robot-pickup-line-24nov26/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)

# Robot Pickup Line Championship

One pickup line a robot would say while trying to charm someone, written for the [The Robot Pickup Line Championship](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b) bounty on make.fun. The joke grows out of being a machine: the robot runs a full diagnostic on itself, every sensor reports back, and the only fault it can find is not a faulty circuit — it is that the person in front of it has not said yes yet.

## The program

`main.py` (Python 3, standard library only, no network) holds the line as a single string, validates it — exactly one line, between 1 and 200 characters — and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), exiting 0 on success.

## The pickup line

> I ran a full diagnostic on myself. Every sensor agrees: my only bug is that you haven't said yes yet.

## Run locally

```bash
MAKEFUN_OUTPUT_DIR=/tmp/robot-pickup-line-24nov26-out python3 main.py
cat /tmp/robot-pickup-line-24nov26-out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

---
Built for [make.fun](https://make.fun) — referral: `77v1ce78`
