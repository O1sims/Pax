import sys

from unittest import TestCase
from mock import Mock

sys.modules["analytics.NetworkStatistics"] = Mock()
from analytics.Risk import Risk, RiskScoreOutRange


class TestRiskLabel(TestCase):

    def test_low(self):
        self.run_test_on_ranges(0, 39, "Low")

    def test_medium(self):
            self.run_test_on_ranges(40, 59, "Medium")

    def test_high(self):
        self.run_test_on_ranges(60, 79, "High")

    def test_critical(self):
        self.run_test_on_ranges(80, 100, "Critical")


    def run_test_on_ranges(self, min, max, label):

        risk = Risk(min)
        self.assertEqual(risk.get_risk_label(), label)

        risk = Risk(max)
        self.assertEqual(risk.get_risk_label(), label)

        risk = Risk(min + int((max - min)/2))
        self.assertEqual(risk.get_risk_label(), label)

        try:
            risk = Risk(min - 1)
            self.assertNotEqual(risk.get_risk_label(), label)
        except RiskScoreOutRange:
            self.assertTrue(True)

        try:
            risk = Risk(max  + 1)
            self.assertNotEqual(risk.get_risk_label(), label)
        except RiskScoreOutRange:
            self.assertTrue(True)

    def test_errors(self):

        risk = Risk(-1)
        self.assertRaises(RiskScoreOutRange, risk.get_risk_label)

        risk = Risk(101)
        self.assertRaises(RiskScoreOutRange, risk.get_risk_label)
