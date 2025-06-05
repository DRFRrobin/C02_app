from __future__ import annotations

import csv
import time
from pathlib import Path

from .sensor import read_co2_level


DATA_FILE = Path("co2_readings.csv")


def run_monitor(num_samples: int = 10, delay: float = 1.0) -> None:
    """Run the CO2 monitor and write results to ``DATA_FILE``."""
    with DATA_FILE.open("w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["timestamp", "co2_ppm"])
        for _ in range(num_samples):
            value = read_co2_level()
            timestamp = time.time()
            writer.writerow([timestamp, f"{value:.2f}"])
            print(f"{timestamp}: CO2 level {value:.2f} ppm")
            time.sleep(delay)


def main() -> None:
    run_monitor()


if __name__ == "__main__":
    main()

