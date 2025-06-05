import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from co2_app.sensor import read_co2_level


def test_read_co2_level_range():
    value = read_co2_level()
    assert 400.0 <= value <= 2000.0

