#! /usr/bin/env python
"""IWYU output filter

Copyright (C) 2019-2026 kaoru  https://www.tetengo.org/
"""

import re
import sys


def main() -> None:
    """The main function."""
    no_error_pattern: re.Pattern[str] = re.compile(
        r"has correct #includes/fwd-decls\)$"
    )
    ignorable_warning_pattern: re.Pattern[str] = re.compile(
        r"warning: no private include name for @headername mapping$"
    )
    exit_code: int = 0
    for line in sys.stdin:
        line = line.rstrip("\n")
        if len(line) == 0:
            continue
        if no_error_pattern.search(line):
            continue
        if ignorable_warning_pattern.search(line):
            continue
        print(line)
        exit_code = 1
    exit(exit_code)


if __name__ == "__main__":
    main()
