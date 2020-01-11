from collections import Counter

from django.test import SimpleTestCase

from ..hotkey_generator import (
    generate_hotkeys,
    KEY_MAP
)


class DasHotkeyGeneratorTestCase(SimpleTestCase):
        
    KEY_MAP = { 
        5: 'Q',
        10: 'W',
        15: 'E',
        20: 'R',
        25: 'T',
        30: 'Y',
        35: 'U',
        40: 'I',
        45: 'O',
        50: 'P',
        55: 'A',
        60: 'S',
        65: 'D',
        70: 'F',
        75: 'G',
        80: 'H',
        85: 'J',
        90: 'K',
        95: 'L',
        100: 'Z',
        105: 'X',
        110: 'C',
        115: 'V',
        120: 'B',
        125: 'N',
        130: 'M',
    }

    def _generate_hotkeys(self):
        return generate_hotkeys(risk=92, route='tst', sc_long_key='c',
                                sc_short_key='a')

    def test_key_map_keys(self):
        ''' Test both key sets are the same. '''
        k1 = list(KEY_MAP.keys())
        k2 = list(self.KEY_MAP.keys())
        remaining_keys = list(Counter(k1) - Counter(k2))
        self.assertFalse(len(remaining_keys))

    def test_key_map_values(self):
        ''' Test both value sets are the same. '''
        v1 = list(KEY_MAP.values())
        v2 = list(self.KEY_MAP.values())
        remaining_values = list(Counter(v1) - Counter(v2))
        self.assertFalse(len(remaining_values))
        
    def test_key_map_length(self):
        ''' Test both sets are the same length. '''
        k1 = len(KEY_MAP.keys())
        k2 = len(self.KEY_MAP.keys())
        self.assertEquals(k1, k2)

    def test_generator_long_keys(self):
        ''' Test generated output for long keys equals ``output``. '''
        ghk = self._generate_hotkeys()[0]
        output = ('c+Q:Long 0.05:ROUTE=tst;Price=Ask+0.05;Share=1840;'
                  'TIF=DAY+;BUY=Send')
        self.assertEquals(ghk, output)

    def test_generator_short_keys(self):
        ''' Test generated output for short keys equals ``output``. '''
        ghk = self._generate_hotkeys()[26]
        output = ('a+Q:Short 0.05:ROUTE=tst;Price=Bid-0.05;Share=1840;'
                  'TIF=DAY+;SELL=Send')
        self.assertEquals(ghk, output)
