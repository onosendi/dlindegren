"""
    das_trader_hotkey_generator
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Generate hotkeys with given values.
"""
# Map alpha keys to risk.
key_map = {
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


def generate_hotkeys(risk, route, sc_long_key, sc_short_key):
    # Make sure :param:`risk` is an integer.
    if not isinstance(risk, int):
        try:
            risk = int(risk)
        except ValueError:
            risk = 100
    if not route:
        route = 'SMRTL'
    if not sc_long_key:
        sc_long_key = 'Ctrl+Shift'
    if not sc_short_key:
        sc_short_key = 'Alt+Shift'
    result = []
    i = 0
    while i < 2:
        if i == 0:
            shortcut_key = sc_long_key
            side_text = 'Long'
            l2 = 'Ask+'
        else:
            shortcut_key = sc_short_key
            side_text = 'Short'
            l2 = 'Bid-'
        for k, v in key_map.items():
            dollar = k / 100
            string = '{}+{}:'.format(shortcut_key, v)
            string += '{0} {1:.2f}:'.format(side_text, dollar)
            string += 'ROUTE={};'.format(route)
            string += 'Price={}0.05;'.format(l2)
            string += 'Share={};'.format(round(risk / dollar))
            string += 'TIF=DAY+;SELL=Send'
            result.append(string)
        i += 1
    return result
