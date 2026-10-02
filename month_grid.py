#!/usr/bin/env python3
"""Print a locale-independent month calendar in the terminal."""

import argparse
import calendar


MONTHS = (
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
)
WEEKDAYS = ("Mo", "Tu", "We", "Th", "Fr", "Sa", "Su")


def main():
    parser = argparse.ArgumentParser(description="Print a month calendar without locale or network dependencies.")
    parser.add_argument("year", type=int, help="year from 1 to 9999")
    parser.add_argument("month", type=int, help="month from 1 to 12")
    parser.add_argument("--sunday-first", action="store_true", help="start each week on Sunday")
    args = parser.parse_args()
    if not 1 <= args.year <= 9999:
        parser.error("year must be between 1 and 9999")
    if not 1 <= args.month <= 12:
        parser.error("month must be between 1 and 12")

    first_day = 6 if args.sunday_first else 0
    weekdays = WEEKDAYS[first_day:] + WEEKDAYS[:first_day]
    weeks = calendar.Calendar(firstweekday=first_day).monthdayscalendar(args.year, args.month)
    print(f"{MONTHS[args.month - 1]} {args.year}".center(20))
    print(" ".join(weekdays))
    for week in weeks:
        print(" ".join(f"{day:2}" if day else "  " for day in week))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
