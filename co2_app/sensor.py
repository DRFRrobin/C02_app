import random
from typing import Tuple

def read_co2_level() -> float:
    """Simulate reading a CO2 level from a sensor in parts per million (ppm)."""
    return random.uniform(400.0, 2000.0)


def sample_levels(num_samples: int = 10) -> Tuple[float, ...]:
    """Return a tuple of simulated CO2 readings."""
    return tuple(read_co2_level() for _ in range(num_samples))

