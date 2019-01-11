import re
from numpy import arange


def loadingbar(width, p=0, p_precision=2, symbol=u'#'):
    class LBFormatter:
        def __init__(self, bar, percentage, wheel):
            self.format_dict = {'%b': bar, '%w': wheel, '%p': percentage}
            self.format_pattern = re.compile("(%\w)")

        def __format__(self, format_spec):
            # print(format_spec)
            out_string = format_spec
            # print(self.format_dict)
            for match in self.format_pattern.finditer(format_spec):
                key = match.group(1)
                out_string = re.sub(key, self.format_dict[key], out_string)
            return out_string

        def __str__(self):
            return " {%w} | {%b} | {%p} ".format(**self.format_dict)

    wheel = (u'-', r'\\', u'|', u'/')
    i = 0
    while p <= 1:
        kwargs = {'bar': f"{f'''{'':<{width * (1 - p)}}''':{symbol}>{width}}",
                  'percentage': f"{f'''{p:.{p_precision}%}''':>{p_precision + 5}}",
                  'wheel': f"{wheel[i]}"}
        p = yield LBFormatter(**kwargs)
        i = (i + 1) % 4

