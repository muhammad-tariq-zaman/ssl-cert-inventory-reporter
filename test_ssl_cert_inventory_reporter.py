import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from datetime import date
from main import report

NOW = date(2026, 11, 2)


def row(d, expiry):
    return {"domain": d, "expiry": expiry}


class TestCertInventory(unittest.TestCase):
    def test_expired(self):
        self.assertEqual(report([row("a.com", "2026-11-01")], NOW, 30)[0][2], "EXPIRED")

    def test_expiring_soon(self):
        self.assertEqual(report([row("a.com", "2026-11-20")], NOW, 30)[0][2], "EXPIRING SOON")

    def test_ok(self):
        self.assertEqual(report([row("a.com", "2027-06-01")], NOW, 30)[0][2], "OK")

    def test_soonest_first(self):
        result = report([row("late.com", "2027-01-01"), row("soon.com", "2026-11-10")], NOW, 30)
        self.assertEqual(result[0][0], "soon.com")
