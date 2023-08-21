import pytest

from python.src.wfc import Map


class CellTest:
    cell = None

    @pytest.fixture(autouse=True)
    def before_each(self):
        cell_map = Map(10)
        cell = Map.Cell(100, 100, cell_map)

    def test_entropy(self):
        assert self.cell.entropy() == 6
