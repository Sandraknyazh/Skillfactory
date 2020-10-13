#Задание 19.2.3
import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multyply_calculation_failed(self):
        assert self.calc.multiply(self, 2, 2) == 5
