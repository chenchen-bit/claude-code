#!/usr/bin/env python3
"""CLI Pomodoro Timer."""

import argparse
import os
import signal
import sys
import time
from dataclasses import dataclass

DEFAULT_WORK = 25
DEFAULT_SHORT_BREAK = 5
DEFAULT_LONG_BREAK = 15
POMODOROS_BEFORE_LONG_BREAK = 4


@dataclass
class Colors:
    reset = "\033[0m"
    bold = "\033[1m"
    green = "\033[92m"
    yellow = "\033[93m"
    red = "\033[91m"
    cyan = "\033[96m"
    dim = "\033[2m"
    clear = "\033[2J\033[H"


def fmt(minutes, seconds):
    return f"{minutes:02d}:{seconds:02d}"


def bell():
    print("\a", end="", flush=True)


def notify(message):
    """Show a macOS notification."""
    os.system(f'osascript -e \'display notification "{message}" with title "Pomodoro"\'')  # noqa: S605


def draw_bar(progress, width=20):
    filled = int(progress * width)
    bar = "█" * filled + "░" * (width - filled)
    return bar


def countdown(total_seconds, label, color):
    start = time.monotonic()
    paused = False
    elapsed = 0

    while elapsed < total_seconds:
        if paused:
            # wait while paused
            signal.pause()
            paused_start = time.monotonic()
            start += time.monotonic() - paused_start
        else:
            remaining = total_seconds - elapsed
            mins, secs = divmod(int(remaining), 60)
            progress = elapsed / total_seconds if total_seconds else 0

            bar = draw_bar(progress)
            ts = fmt(mins, secs)
            sys.stdout.write(
                f"\r{color}{label} {bar} {ts}{Colors.reset}"
                f"{'  ⏸ PAUSED' if paused else ''}"
                f"{' ' * 4}"
            )
            sys.stdout.flush()

        try:
            time.sleep(0.2)
        except KeyboardInterrupt:
            bell()
            print()
            print(f"  [{Colors.yellow}P{Colors.reset}]ause  [{Colors.red}Q{Colors.reset}]uit")
            try:
                choice = input().strip().lower()
            except EOFError:
                break
            if choice == "q":
                print(f"\n{Colors.red}Aborted.{Colors.reset}")
                sys.exit(0)
            elif choice == "p":
                paused = not paused
                if paused:
                    print(f"\r  {Colors.yellow}⏸ Paused{Colors.reset}")
                continue

        elapsed = time.monotonic() - start

    # done
    sys.stdout.write(f"\r{color}{label} {'█' * 22} {fmt(0, 0)}{Colors.reset}\n")
    sys.stdout.flush()


def main():
    parser = argparse.ArgumentParser(
        description="🍅 Pomodoro Timer",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Controls while running:\n"
            "  Ctrl+C → show pause/quit menu\n"
            "  p       → pause\n"
            "  q       → quit\n"
        ),
    )
    parser.add_argument(
        "-w", "--work", type=int, default=DEFAULT_WORK,
        help=f"Work duration in minutes (default: {DEFAULT_WORK})",
    )
    parser.add_argument(
        "-s", "--short", type=int, default=DEFAULT_SHORT_BREAK,
        help=f"Short break in minutes (default: {DEFAULT_SHORT_BREAK})",
    )
    parser.add_argument(
        "-l", "--long", type=int, default=DEFAULT_LONG_BREAK,
        help=f"Long break in minutes (default: {DEFAULT_LONG_BREAK})",
    )
    parser.add_argument(
        "-n", "--no-notify", action="store_true",
        help="Disable macOS notifications",
    )
    parser.add_argument(
        "-c", "--cycles", type=int, default=0,
        help=f"Number of pomodoros (0 = unlimited until Ctrl+C, default: 0)",
    )

    args = parser.parse_args()
    work_sec = args.work * 60
    short_sec = args.short * 60
    long_sec = args.long * 60

    print(f"{Colors.clear}🍅 {Colors.bold}Pomodoro{Colors.reset}")
    print(f"  Work: {args.work}min  Short break: {args.short}min  Long break: {args.long}min\n")

    cycle = 0
    try:
        while True:
            cycle += 1
            countdown(work_sec, f"⚡ Cycle {cycle:>2}  Work   ", Colors.green)
            if not args.no_notify:
                bell()
                notify("Work session finished! Take a break.")

            if args.cycles and cycle >= args.cycles:
                print(f"\n{Colors.cyan}All {args.cycles} cycles complete!{Colors.reset}")
                break

            is_long = cycle % POMODOROS_BEFORE_LONG_BREAK == 0
            if is_long:
                label = f"☕ Cycle {cycle:>2}  Long   "
                duration = long_sec
            else:
                label = f"💨 Cycle {cycle:>2}  Short  "
                duration = short_sec

            countdown(duration, label, Colors.cyan if is_long else Colors.yellow)
            if not args.no_notify:
                bell()
                notify("Break finished! Time to focus.")

    except KeyboardInterrupt:
        print(f"\n{Colors.red}Bye!{Colors.reset}")


if __name__ == "__main__":
    signal.signal(signal.SIGTSTP, signal.SIG_IGN)  # ignore Ctrl+Z
    main()
