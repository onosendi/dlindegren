DEFAULT_HOTKEYS = [
    'Space:HorizontalLine:HorizontalLine',
    'Ctrl+D:Duplicate window:DuplicateWindow',
    'F1:1 MIN CHART 1 day:MinuteChart 1 1d; ZoomFit',
    'F2:5 MIN CHART 1 day:MinuteChart 5 1d; ZoomFit',
    'F3:1H Chart 15 day:MinuteChart 15 1d; ZoomFit',
    'F4:DAILY CHART:DayChart 1d 1825d; ZoomFit',
    'F5:WEEKLY CHART:DayChart 1w 4y; ZoomFit',
    'F6:MONTHLY CHART 5 years:DayChart 1m 5y',
    'Shift+ESC:close all open positions (all orders must be cancelled'
    ' first):PANIC',

    'Shift+bkspace:Cancel all open orders of symbol in montage:CXL ALLSYMB',
    'Ctrl+PageUp:Long Sell'
    ' all:ROUTE=SMRTL;Price=Bid-0.05;Share=Pos;TIF=DAY+;SELL=Send',

    'Ctrl+Home:Long Sell'
    ' 1/2:ROUTE=SMRTL;Price=Bid-0.05;Share=Pos*0.5;TIF=DAY+;SELL=Send',

    'Ctrl+Insert:Long Sell'
    ' 1/4:ROUTE=SMRTL;Price=Bid-0.05;Share=Pos*0.25;TIF=DAY+;SELL=Send',

    'Alt+PageDown:Short Cover'
    ' all:ROUTE=SMRTL;Price=Ask+0.05;Share=Pos;TIF=DAY+;BUY=Send',

    'Alt+End:Short Cover'
    ' 1/2:ROUTE=SMRTL;Price=Ask+0.05;Share=Pos*0.5;TIF=DAY+;BUY=Send',

    'Alt+Delete:Short Cover'
    ' 1/4:ROUTE=SMRTL;Price=Ask+0.05;Share=Pos*0.25;TIF=DAY+;BUY=Send',

    'Ctrl+Shift+:Long N Shares:ROUTE=SMRTL;Price=Ask+0.05;TIF=DAY+;BUY=Send',
    'Alt+Shift+:Short N Shares:ROUTE=SMRTL;Price=Bid-0.05;TIF=DAY+;SELL=Send',
]

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


def generate_hotkeys(risk=None, route=None, sc_long_key=None,
                     sc_short_key=None, default_hotkeys=False):
    if not isinstance(risk, int):
        try:
            risk = int(risk)
        except (ValueError, TypeError):
            risk = 100
    if not route:
        route = 'SMRTL'
    if not sc_long_key:
        sc_long_key = 'Ctrl+Shift'
    if not sc_short_key:
        sc_short_key = 'Alt+Shift'
    if not default_hotkeys:
        default_hotkeys = False
    result = []
    i = 0
    while i < 2:
        if i == 0:
            shortcut_key = sc_long_key
            side_text = 'Long'
            l2 = 'Ask+'
            side_send = 'BUY'
        else:
            shortcut_key = sc_short_key
            side_text = 'Short'
            l2 = 'Bid-'
            side_send = 'SELL'
        for k, v in KEY_MAP.items():
            dollar = k / 100
            string = '{}+{}:'.format(shortcut_key, v)
            string += '{0} {1:.2f}:'.format(side_text, dollar)
            string += 'ROUTE={};'.format(route)
            string += 'Price={}0.05;'.format(l2)
            string += 'Share={};'.format(round(risk / dollar))
            string += 'TIF=DAY+;{}=Send'.format(side_send)
            result.append(string)
        i += 1
    if default_hotkeys:
        for hotkey in DEFAULT_HOTKEYS:
            result.append(hotkey)
    return result
