# month-grid

Print a compact, locale-independent month calendar in the terminal. Choose Monday or Sunday as the first day of each week.

## Use

Requires Python 3.10+; no packages or network access required.

```sh
python month_grid.py 2026 10
python month_grid.py 2026 10 --sunday-first
```

Year must be from 1 to 9999 and month from 1 to 12. The output uses English month names and two-letter weekday labels so it stays consistent across machines.

## License

MIT
