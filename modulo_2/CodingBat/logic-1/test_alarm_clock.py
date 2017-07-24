# coding=utf-8
from unittest import TestCase
from alarm_clock import alarm_clock


class AlarmClockTest(TestCase):
    def test_alarmclock_wk_off(self):
        self.assertEqual(alarm_clock(1, False), '7:00')

    def test_alarmclock_wk_off_1(self):
        self.assertEqual(alarm_clock(5, False), '7:00')

    def test_alarmclock_wk_on(self):
        self.assertEqual(alarm_clock(0, False), '10:00')

    def test_alarmclock_vacation_on(self):
        self.assertEqual(alarm_clock(0, True), 'off')

    def test_alarmclock_vacation_on_1(self):
        self.assertEqual(alarm_clock(3, True), '10:00')