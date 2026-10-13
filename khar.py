# Traffic Signal Simulator with Dynamic Ads

"""Enhanced traffic‑signal simulator.

Features
--------
- Configurable line width and footer (ad) via ``--width`` and ``--footer``.
- Optional colour output (requires ``colorama``).
- Ability to limit cycles with ``--cycles`` for quick tests.
- **Dynamic instructional messages** that change each cycle.
- **Dynamic ads** that appear *between* instructional messages (simulating a university‑ad banner, etc.).
- Graceful ``Ctrl‑C`` handling.
"""

import argparse
import json
import sys
import time
from typing import List, Tuple, Optional

# Optional colour support – works on Linux terminals.
try:
    from colorama import init as colorama_init, Fore, Style
    colorama_init(autoreset=True)
    RED = Fore.RED
    YELLOW = Fore.YELLOW
    GREEN = Fore.GREEN
    RESET = Style.RESET_ALL
except Exception:
    RED = YELLOW = GREEN = RESET = ""

# ---------------------------------------------------------------------------
# Types
# ---------------------------------------------------------------------------
Signal = Tuple[str, int, str]          # (name, duration, colour code)
MessageAdPair = Tuple[str, str]        # (instruction, ad)

# Default signal configuration.
signal_config: List[Signal] = [
    ("Red", 20, RED),
    ("Yellow", 3, YELLOW),
    ("Green", 12, GREEN),
]

# Default footer – can be overridden via ``--footer``.
DEFAULT_FOOTER = " | Downloaded from khar software solutions"

# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def build_signal_message(color_name: str, seconds_left: int, colour_code: str) -> str:
    """Return the coloured status line for the traffic signal.

    The colour code is applied only to the colour name for readability.
    """
    base = f"Signal is now: {colour_code}{color_name}{RESET} | Changing in: {seconds_left} seconds"
    return base


def clear_previous_lines(count: int = 2) -> None:
    """Erase the previously printed ``count`` terminal lines.

    Uses ANSI escape sequences to move the cursor up and clear each line.
    """
    for _ in range(count):
        # Move cursor up one line
        sys.stdout.write("\x1b[1A")
        # Clear the entire line
        sys.stdout.write("\x1b[2K")
    sys.stdout.flush()


def display_cycle(width: int, footer: str, messages: List[MessageAdPair], cycles: Optional[int] = None) -> None:
    """Run the traffic‑signal loop while interleaving dynamic messages and ads.

    Parameters
    ----------
    width:
        Fixed line width for left‑justifying output.
    footer:
        Text appended after every printed line (acts as a static banner).
    messages:
        A list of ``(instruction, ad)`` pairs. The pair for the *current*
        cycle is displayed before the signal countdown. After the countdown
        finishes, the next pair is used.
    cycles:
        Number of full colour cycles to execute; ``None`` means run forever.
    """
    try:
        cycle_index = 0
        while True:
            instr, ad = messages[cycle_index % len(messages)]
            # Print instruction line
            print(instr.ljust(width), end="\n", flush=True)
            # Print ad line (the dynamic ad between instructions)
            print(ad.ljust(width), end="\n", flush=True)

            # Now run the traffic‑signal countdown for this cycle
            for colour_name, duration, colour_code in signal_config:
                for sec in range(duration, 0, -1):
                    status = build_signal_message(colour_name, sec, colour_code) + footer
                    # Overwrite the *status* line (third line)
                    print(status.ljust(width), end="\r", flush=True)
                    time.sleep(1)
                    # Clear the status line before next update to avoid artefacts
                    sys.stdout.write("\x1b[2K")
                    sys.stdout.flush()

            # After the whole colour sequence, move cursor up three lines
            # (instruction, ad, last status) to prepare for the next pair.
            clear_previous_lines(3)

            cycle_index += 1
            if cycles is not None and cycle_index >= cycles:
                break
    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting.")


def parse_args() -> argparse.Namespace:
    """Parse command‑line arguments.

    Returns
    -------
    argparse.Namespace with ``width``, ``footer``, ``cycles`` and ``messages``.
    """
    parser = argparse.ArgumentParser(description="Traffic signal simulator with dynamic messages and ads.")
    parser.add_argument("--width", type=int, default=50, help="Line width for left‑justified output (default: 50).")
    parser.add_argument("--footer", type=str, default=DEFAULT_FOOTER, help="Static footer appended to every line.")
    parser.add_argument("--cycles", type=int, default=None, help="Number of full colour cycles to run (default: run forever).")
    parser.add_argument(
        "--messages",
        type=str,
        default=json.dumps([
            ["Welcome to the University Admission Portal", "Apply now and get a scholarship!"],
            ["Check eligibility criteria", "Early‑bird discount ends soon!"],
            ["Submit your documents", "Visit our campus for a tour!"],
        ]),
        help="JSON array of [instruction, ad] pairs. Example: '[[\"Info1\",\"Ad1\"],[\"Info2\",\"Ad2\"]]'.",
    )
    args = parser.parse_args()
    # Convert the JSON string into a Python list of tuples
    try:
        msgs = json.loads(args.messages)
        if not isinstance(msgs, list) or any(not isinstance(pair, list) or len(pair) != 2 for pair in msgs):
            raise ValueError
        args.messages = [(pair[0], pair[1]) for pair in msgs]
    except Exception:
        parser.error("--messages must be a JSON list of [instruction, ad] pairs.")
    return args


if __name__ == "__main__":
    cfg = parse_args()
    display_cycle(width=cfg.width, footer=cfg.footer, messages=cfg.messages, cycles=cfg.cycles)
