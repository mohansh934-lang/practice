# Traffic Signal Simulator (`khar.py`)

## Overview

`khar.py` is a small command‑line traffic‑signal simulator written in pure Python. It displays the current colour of a traffic light, a countdown timer for that colour, and an optional advertisement/footer appended to every line.

The script now supports:
- **Configurable line width** – controls how many characters are printed on each line (so the previous output is fully overwritten).
- **Customisable footer** – useful for advertising or any extra text you want to show after the status message.
- **Optional colourised output** using ANSI escape codes via the `colorama` package (works on most Linux terminals).
- **Limiting the number of cycles** – handy for quick testing; the program can run a single full‑cycle and then exit.
- **Graceful handling of Ctrl‑C** – prints a clean newline when you interrupt the script.
- **Typed signatures and extensive doc‑strings** for easier maintenance.

## Requirements

```bash
pip install -r requirements.txt   # optional, only `colorama` is needed
```

If you don’t have `colorama` installed the script will fall back to plain text (no colour).

## Usage

```bash
python3 khar.py [options]
```

### Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--width` | `int` | `50` | Width of the printed line. The script pads the output with spaces so the previous line is fully cleared.
| `--footer` | `str` | `" | Downloaded from khar software solutions"` | Text appended after the status line (e.g., an ad banner).
| `--cycles` | `int` | `None` (run forever) | Number of **full colour cycles** to execute before exiting. A full cycle consists of Red → Yellow → Green.

### Examples

1. **Run indefinitely with default settings**
   ```bash
   python3 khar.py
   ```

2. **Run a single cycle for testing**
   ```bash
   python3 khar.py --cycles 1
   ```

3. **Custom width and custom ad/footer**
   ```bash
   python3 khar.py --width 70 --footer " | My Awesome Ad" --cycles 2
   ```

4. **Disable colour (e.g., when colourama is not available)**
   ```bash
   python3 khar.py --footer " | Plain Text" --cycles 1
   ```

## How it works

- The signal configuration is stored in the global list `signal_config` where each entry is a tuple `(colour_name, duration_seconds, colour_code)`.
- `display_signal()` loops through this list, counting down each colour and printing a formatted line.
- `build_message()` builds the output string, applying the ANSI colour code only to the colour name, then concatenates the footer.
- `parse_args()` uses the standard `argparse` library to expose the command‑line interface.
- A `KeyboardInterrupt` exception is caught so that pressing **Ctrl‑C** cleanly exits the program.

## Testing in the terminal

Run the script with the `--cycles` flag to see a deterministic short run:

```bash
python3 khar.py --width 60 --footer " | Test Ad" --cycles 1
```

You should see output similar to:
```
Signal is now: Red | Changing in: 20 seconds | Test Ad

Signal is now: Red | Changing in: 19 seconds | Test Ad
... (counts down) ...

Signal is now: Green | Changing in: 12 seconds | Test Ad
```
The `\r` returns the cursor to the start of the line, and `ljust` pads the line so the previous content is fully overwritten.

If you have `colorama` installed, the colour name will appear in its respective colour (red, yellow, green).

---

Feel free to experiment with the arguments to suit your needs.  
Happy coding!

