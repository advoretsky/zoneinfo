"""
generated zoneinfo file

Generated from: https://github.com/garrickp/tzinfo_py

Copyright (c) 2014 Garrick Peterson

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

from datetime import tzinfo, datetime, timedelta
from calendar import Calendar

# Support functions for rules that rely on calendar days
def __lastSun(year, month, hour, min):
    c = Calendar().monthdayscalendar(year, month)
    day = 0
    for w in reversed(c):
        day = w[6]
        if day != 0:
            break
    return datetime(year, month, day, hour, min)
def __lastSat(year, month, hour, min):
    c = Calendar().monthdayscalendar(year, month)
    day = 0
    for w in reversed(c):
        day = w[5]
        if day != 0:
            break
    return datetime(year, month, day, hour, min)
def __lastFri(year, month, hour, min):
    c = Calendar().monthdayscalendar(year, month)
    day = 0
    for w in reversed(c):
        day = w[4]
        if day != 0:
            break
    return datetime(year, month, day, hour, min)
def __lastThu(year, month, hour, min):
    c = Calendar().monthdayscalendar(year, month)
    day = 0
    for w in reversed(c):
        day = w[3]
        if day != 0:
            break
    return datetime(year, month, day, hour, min)
def __lastWed(year, month, hour, min):
    c = Calendar().monthdayscalendar(year, month)
    day = 0
    for w in reversed(c):
        day = w[2]
        if day != 0:
            break
    return datetime(year, month, day, hour, min)
def __lastTue(year, month, hour, min):
    c = Calendar().monthdayscalendar(year, month)
    day = 0
    for w in reversed(c):
        day = w[1]
        if day != 0:
            break
    return datetime(year, month, day, hour, min)
def __lastMon(year, month, hour, min):
    c = Calendar().monthdayscalendar(year, month)
    day = 0
    for w in reversed(c):
        day = w[0]
        if day != 0:
            break
    return datetime(year, month, day, hour, min)
def __SunGtEq(year, month, min_day, hour, min):
    c = Calendar().monthdayscalendar(year, month)
    day = 0
    for w in c:
        day = w[6]
        if day >= min_day:
            break
    return datetime(year, month, day, hour, min)
def __SatGtEq(year, month, min_day, hour, min):
    c = Calendar().monthdayscalendar(year, month)
    day = 0
    for w in c:
        day = w[5]
        if day >= min_day:
            break
    return datetime(year, month, day, hour, min)
def __FriGtEq(year, month, min_day, hour, min):
    c = Calendar().monthdayscalendar(year, month)
    day = 0
    for w in c:
        day = w[4]
        if day >= min_day:
            break
    return datetime(year, month, day, hour, min)
def __ThuGtEq(year, month, min_day, hour, min):
    c = Calendar().monthdayscalendar(year, month)
    day = 0
    for w in c:
        day = w[3]
        if day >= min_day:
            break
    return datetime(year, month, day, hour, min)
def __WedGtEq(year, month, min_day, hour, min):
    c = Calendar().monthdayscalendar(year, month)
    day = 0
    for w in c:
        day = w[2]
        if day >= min_day:
            break
    return datetime(year, month, day, hour, min)
def __TueGtEq(year, month, min_day, hour, min):
    c = Calendar().monthdayscalendar(year, month)
    day = 0
    for w in c:
        day = w[1]
        if day >= min_day:
            break
    return datetime(year, month, day, hour, min)
def __MonGtEq(year, month, min_day, hour, min):
    c = Calendar().monthdayscalendar(year, month)
    day = 0
    for w in c:
        day = w[0]
        if day >= min_day:
            break
    return datetime(year, month, day, hour, min)

# Constant rules
def _rule_constant_1hour(dt):
    return (timedelta(hours=1), '')
def _rule_constant_30min(dt):
    return (timedelta(minutes=30), '')
def _rule_constant_20min(dt):
    return (timedelta(minutes=20), '')

# Rule sets
def _Canada(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1918) and (dt >= datetime(dt.year, 4, 14, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1918) and (dt >= datetime(dt.year, 10, 27, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1942) and (dt >= datetime(dt.year, 2, 9, 2, 0)):
        l = 'W'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 8, 14, 23, 0)):
        l = 'P'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 9, 30, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1974) and (dt.year <= 1986) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1974) and (dt.year <= 2006) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1987) and (dt.year <= 2006) and (dt >= __SunGtEq(dt.year, 4, 1, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2007) and (dt >= __SunGtEq(dt.year, 3, 8, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2007) and (dt >= __SunGtEq(dt.year, 11, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Regina(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1918) and (dt >= datetime(dt.year, 4, 14, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1918) and (dt >= datetime(dt.year, 10, 27, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1930) and (dt.year <= 1934) and (dt >= __SunGtEq(dt.year, 5, 1, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1930) and (dt.year <= 1934) and (dt >= __SunGtEq(dt.year, 10, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1937) and (dt.year <= 1941) and (dt >= __SunGtEq(dt.year, 4, 8, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1937) and (dt >= __SunGtEq(dt.year, 10, 8, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1938) and (dt >= __SunGtEq(dt.year, 10, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1939) and (dt.year <= 1941) and (dt >= __SunGtEq(dt.year, 10, 8, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1942) and (dt >= datetime(dt.year, 2, 9, 2, 0)):
        l = 'W'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 8, 14, 23, 0)):
        l = 'P'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1945) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1946) and (dt >= __SunGtEq(dt.year, 4, 8, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1946) and (dt >= __SunGtEq(dt.year, 10, 8, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1947) and (dt.year <= 1957) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1947) and (dt.year <= 1957) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1959) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1959) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Mongol(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1983) and (dt.year <= 1984) and (dt >= datetime(dt.year, 4, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1983) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1985) and (dt.year <= 1998) and (dt >= __lastSun(dt.year, 3, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1984) and (dt.year <= 1998) and (dt >= __lastSun(dt.year, 9, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2001) and (dt >= __lastSat(dt.year, 4, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2001) and (dt.year <= 2006) and (dt >= __lastSat(dt.year, 9, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2002) and (dt.year <= 2006) and (dt >= __lastSat(dt.year, 3, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    return (s, l)
def _SpainAfrica(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1967) and (dt >= datetime(dt.year, 6, 3, 12, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1967) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1974) and (dt >= datetime(dt.year, 6, 24, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1974) and (dt >= datetime(dt.year, 9, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1976) and (dt.year <= 1977) and (dt >= datetime(dt.year, 5, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1976) and (dt >= datetime(dt.year, 8, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1977) and (dt >= datetime(dt.year, 9, 28, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1978) and (dt >= datetime(dt.year, 6, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1978) and (dt >= datetime(dt.year, 8, 4, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _WS(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 2010) and (dt >= __lastSun(dt.year, 9, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2011) and (dt >= __SatGtEq(dt.year, 4, 1, 4, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2011) and (dt >= __lastSat(dt.year, 9, 3, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2012) and (dt >= __SunGtEq(dt.year, 4, 1, 4, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2012) and (dt >= __lastSun(dt.year, 9, 3, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    return (s, l)
def _Palestine(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1999) and (dt.year <= 2005) and (dt >= __FriGtEq(dt.year, 4, 15, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1999) and (dt.year <= 2003) and (dt >= __FriGtEq(dt.year, 10, 15, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2004) and (dt >= datetime(dt.year, 10, 1, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2005) and (dt >= datetime(dt.year, 10, 4, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2006) and (dt.year <= 2007) and (dt >= datetime(dt.year, 4, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2006) and (dt >= datetime(dt.year, 9, 22, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2007) and (dt >= __ThuGtEq(dt.year, 9, 8, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2008) and (dt.year <= 2009) and (dt >= __lastFri(dt.year, 3, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2008) and (dt >= datetime(dt.year, 9, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2009) and (dt >= __FriGtEq(dt.year, 9, 1, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2010) and (dt >= datetime(dt.year, 3, 26, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2010) and (dt >= datetime(dt.year, 8, 11, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2011) and (dt >= datetime(dt.year, 4, 1, 0, 1)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2011) and (dt >= datetime(dt.year, 8, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2011) and (dt >= datetime(dt.year, 8, 30, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2011) and (dt >= datetime(dt.year, 9, 30, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2012) and (dt >= __lastThu(dt.year, 3, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2012) and (dt >= datetime(dt.year, 9, 21, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2013) and (dt >= __FriGtEq(dt.year, 9, 21, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _NYC(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1920) and (dt >= __lastSun(dt.year, 3, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1920) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1921) and (dt.year <= 1966) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1921) and (dt.year <= 1954) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1955) and (dt.year <= 1966) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Kyrgyz(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1992) and (dt.year <= 1996) and (dt >= __SunGtEq(dt.year, 4, 7, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1992) and (dt.year <= 1996) and (dt >= __lastSun(dt.year, 9, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1997) and (dt.year <= 2005) and (dt >= __lastSun(dt.year, 3, 2, 30)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1997) and (dt.year <= 2004) and (dt >= __lastSun(dt.year, 10, 2, 30)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Azer(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1997) and (dt >= __lastSun	(dt.year, 3, 4, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1997) and (dt >= __lastSun	(dt.year, 10, 5, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Ghana(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1920) and (dt.year <= 1942) and (dt >= datetime(dt.year, 9, 1, 0, 0)):
        l = 'GHST'
        s = timedelta(seconds=0, hours=0, minutes=20)
    if (dt.year >= 1920) and (dt.year <= 1942) and (dt >= datetime(dt.year, 12, 31, 0, 0)):
        l = 'GMT'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _NBorneo(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1935) and (dt.year <= 1941) and (dt >= datetime(dt.year, 9, 14, 0, 0)):
        l = 'TS'
        s = timedelta(seconds=0, hours=0, minutes=20)
    if (dt.year >= 1935) and (dt.year <= 1941) and (dt >= datetime(dt.year, 12, 14, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _PRC(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1986) and (dt >= datetime(dt.year, 5, 4, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1986) and (dt.year <= 1991) and (dt >= __SunGtEq(dt.year, 9, 11, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1987) and (dt.year <= 1991) and (dt >= __SunGtEq(dt.year, 4, 10, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    return (s, l)
def _Jordan(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1973) and (dt >= datetime(dt.year, 6, 6, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1973) and (dt.year <= 1975) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1974) and (dt.year <= 1977) and (dt >= datetime(dt.year, 5, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1976) and (dt >= datetime(dt.year, 11, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1977) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1978) and (dt >= datetime(dt.year, 4, 30, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1978) and (dt >= datetime(dt.year, 9, 30, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1985) and (dt >= datetime(dt.year, 4, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1985) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1986) and (dt.year <= 1988) and (dt >= __FriGtEq(dt.year, 4, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1986) and (dt.year <= 1990) and (dt >= __FriGtEq(dt.year, 10, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1989) and (dt >= datetime(dt.year, 5, 8, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1990) and (dt >= datetime(dt.year, 4, 27, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1991) and (dt >= datetime(dt.year, 4, 17, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1991) and (dt >= datetime(dt.year, 9, 27, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1992) and (dt >= datetime(dt.year, 4, 10, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1992) and (dt.year <= 1993) and (dt >= __FriGtEq(dt.year, 10, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1993) and (dt.year <= 1998) and (dt >= __FriGtEq(dt.year, 4, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1994) and (dt >= __FriGtEq(dt.year, 9, 15, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1995) and (dt.year <= 1998) and (dt >= __FriGtEq(dt.year, 9, 15, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1999) and (dt >= datetime(dt.year, 7, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1999) and (dt.year <= 2002) and (dt >= __lastFri(dt.year, 9, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2000) and (dt.year <= 2001) and (dt >= __lastThu(dt.year, 3, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2002) and (dt.year <= 2012) and (dt >= __lastThu(dt.year, 3, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2003) and (dt >= datetime(dt.year, 10, 24, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2004) and (dt >= datetime(dt.year, 10, 15, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2005) and (dt >= __lastFri(dt.year, 9, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2006) and (dt.year <= 2011) and (dt >= __lastFri(dt.year, 10, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2013) and (dt >= datetime(dt.year, 12, 20, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2014) and (dt >= __lastThu(dt.year, 3, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2014) and (dt >= __lastFri(dt.year, 10, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Taiwan(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1946) and (dt >= datetime(dt.year, 5, 15, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1946) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1947) and (dt >= datetime(dt.year, 4, 15, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1947) and (dt >= datetime(dt.year, 11, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1948) and (dt.year <= 1951) and (dt >= datetime(dt.year, 5, 1, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1948) and (dt.year <= 1951) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1952) and (dt >= datetime(dt.year, 3, 1, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1952) and (dt.year <= 1954) and (dt >= datetime(dt.year, 11, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1953) and (dt.year <= 1959) and (dt >= datetime(dt.year, 4, 1, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1955) and (dt.year <= 1961) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1960) and (dt.year <= 1961) and (dt >= datetime(dt.year, 6, 1, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1974) and (dt.year <= 1975) and (dt >= datetime(dt.year, 4, 1, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1974) and (dt.year <= 1975) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1979) and (dt >= datetime(dt.year, 7, 1, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1979) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Spain(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1917) and (dt >= datetime(dt.year, 5, 5, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1917) and (dt.year <= 1919) and (dt >= datetime(dt.year, 10, 6, 23, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1918) and (dt >= datetime(dt.year, 4, 15, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1919) and (dt >= datetime(dt.year, 4, 5, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1924) and (dt >= datetime(dt.year, 4, 16, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1924) and (dt >= datetime(dt.year, 10, 4, 23, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1926) and (dt >= datetime(dt.year, 4, 17, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1926) and (dt.year <= 1929) and (dt >= __SatGtEq(dt.year, 10, 1, 23, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1927) and (dt >= datetime(dt.year, 4, 9, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1928) and (dt >= datetime(dt.year, 4, 14, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1929) and (dt >= datetime(dt.year, 4, 20, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1937) and (dt >= datetime(dt.year, 5, 22, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1937) and (dt.year <= 1939) and (dt >= __SatGtEq(dt.year, 10, 1, 23, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1938) and (dt >= datetime(dt.year, 3, 22, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1939) and (dt >= datetime(dt.year, 4, 15, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1940) and (dt >= datetime(dt.year, 3, 16, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1942) and (dt >= datetime(dt.year, 5, 2, 22, 0)):
        l = 'M'
        s = timedelta(seconds=0, hours=2, minutes=0)
    if (dt.year == 1942) and (dt >= datetime(dt.year, 9, 1, 22, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1943) and (dt.year <= 1946) and (dt >= __SatGtEq(dt.year, 4, 13, 22, 0)):
        l = 'M'
        s = timedelta(seconds=0, hours=2, minutes=0)
    if (dt.year == 1943) and (dt >= datetime(dt.year, 10, 3, 22, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1944) and (dt >= datetime(dt.year, 10, 10, 22, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 9, 30, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1946) and (dt >= datetime(dt.year, 9, 30, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1949) and (dt >= datetime(dt.year, 4, 30, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1949) and (dt >= datetime(dt.year, 9, 30, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1974) and (dt.year <= 1975) and (dt >= __SatGtEq(dt.year, 4, 13, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1974) and (dt.year <= 1975) and (dt >= __SunGtEq(dt.year, 10, 1, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1976) and (dt >= datetime(dt.year, 3, 27, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1976) and (dt.year <= 1977) and (dt >= __lastSun	(dt.year, 9, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1977) and (dt.year <= 1978) and (dt >= datetime(dt.year, 4, 2, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1978) and (dt >= datetime(dt.year, 10, 1, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Mont(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1917) and (dt >= datetime(dt.year, 3, 25, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1917) and (dt >= datetime(dt.year, 4, 24, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1919) and (dt >= datetime(dt.year, 3, 31, 2, 30)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1919) and (dt >= datetime(dt.year, 10, 25, 2, 30)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1920) and (dt >= datetime(dt.year, 5, 2, 2, 30)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1920) and (dt.year <= 1922) and (dt >= __SunGtEq(dt.year, 10, 1, 2, 30)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1921) and (dt >= datetime(dt.year, 5, 1, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1922) and (dt >= datetime(dt.year, 4, 30, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1924) and (dt >= datetime(dt.year, 5, 17, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1924) and (dt.year <= 1926) and (dt >= __lastSun(dt.year, 9, 2, 30)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1925) and (dt.year <= 1926) and (dt >= __SunGtEq(dt.year, 5, 1, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1927) and (dt >= datetime(dt.year, 5, 1, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1927) and (dt.year <= 1932) and (dt >= __lastSun(dt.year, 9, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1928) and (dt.year <= 1931) and (dt >= __lastSun(dt.year, 4, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1932) and (dt >= datetime(dt.year, 5, 1, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1933) and (dt.year <= 1940) and (dt >= __lastSun(dt.year, 4, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1933) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1934) and (dt.year <= 1939) and (dt >= __lastSun(dt.year, 9, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1946) and (dt.year <= 1973) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1945) and (dt.year <= 1948) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1949) and (dt.year <= 1950) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1951) and (dt.year <= 1956) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1957) and (dt.year <= 1973) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _E_Eur(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1977) and (dt.year <= 1980) and (dt >= __SunGtEq(dt.year, 4, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1977) and (dt >= __lastSun	(dt.year, 9, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1978) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1979) and (dt.year <= 1995) and (dt >= __lastSun	(dt.year, 9, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1981) and (dt >= __lastSun	(dt.year, 3, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1996) and (dt >= __lastSun	(dt.year, 10, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Winn(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1916) and (dt >= datetime(dt.year, 4, 23, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1916) and (dt >= datetime(dt.year, 9, 17, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1918) and (dt >= datetime(dt.year, 4, 14, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1918) and (dt >= datetime(dt.year, 10, 27, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1937) and (dt >= datetime(dt.year, 5, 16, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1937) and (dt >= datetime(dt.year, 9, 26, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1942) and (dt >= datetime(dt.year, 2, 9, 2, 0)):
        l = 'W'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 8, 14, 23, 0)):
        l = 'P'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1945) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1946) and (dt >= datetime(dt.year, 5, 12, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1946) and (dt >= datetime(dt.year, 10, 13, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1947) and (dt.year <= 1949) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1947) and (dt.year <= 1949) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1950) and (dt >= datetime(dt.year, 5, 1, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1950) and (dt >= datetime(dt.year, 9, 30, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1951) and (dt.year <= 1960) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1951) and (dt.year <= 1958) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1959) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1960) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1963) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1963) and (dt >= datetime(dt.year, 9, 22, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1966) and (dt.year <= 1986) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1966) and (dt.year <= 2005) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1987) and (dt.year <= 2005) and (dt >= __SunGtEq(dt.year, 4, 1, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    return (s, l)
def _Salv(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1987) and (dt.year <= 1988) and (dt >= __SunGtEq(dt.year, 5, 1, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1987) and (dt.year <= 1988) and (dt >= __lastSun(dt.year, 9, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Pakistan(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 2002) and (dt >= __SunGtEq(dt.year, 4, 2, 0, 1)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2002) and (dt >= __SunGtEq(dt.year, 10, 2, 0, 1)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2008) and (dt >= datetime(dt.year, 6, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2008) and (dt >= datetime(dt.year, 11, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2009) and (dt >= datetime(dt.year, 4, 15, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2009) and (dt >= datetime(dt.year, 11, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Albania(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1940) and (dt >= datetime(dt.year, 6, 16, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1942) and (dt >= datetime(dt.year, 11, 2, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1943) and (dt >= datetime(dt.year, 3, 29, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1943) and (dt >= datetime(dt.year, 4, 10, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1974) and (dt >= datetime(dt.year, 5, 4, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1974) and (dt >= datetime(dt.year, 10, 2, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1975) and (dt >= datetime(dt.year, 5, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1975) and (dt >= datetime(dt.year, 10, 2, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1976) and (dt >= datetime(dt.year, 5, 2, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1976) and (dt >= datetime(dt.year, 10, 3, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1977) and (dt >= datetime(dt.year, 5, 8, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1977) and (dt >= datetime(dt.year, 10, 2, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1978) and (dt >= datetime(dt.year, 5, 6, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1978) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1979) and (dt >= datetime(dt.year, 5, 5, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1979) and (dt >= datetime(dt.year, 9, 30, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1980) and (dt >= datetime(dt.year, 5, 3, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1980) and (dt >= datetime(dt.year, 10, 4, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1981) and (dt >= datetime(dt.year, 4, 26, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1981) and (dt >= datetime(dt.year, 9, 27, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1982) and (dt >= datetime(dt.year, 5, 2, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1982) and (dt >= datetime(dt.year, 10, 3, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1983) and (dt >= datetime(dt.year, 4, 18, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1983) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1984) and (dt >= datetime(dt.year, 4, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    return (s, l)
def _Macau(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1961) and (dt.year <= 1962) and (dt >= __SunGtEq(dt.year, 3, 16, 3, 30)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1961) and (dt.year <= 1964) and (dt >= __SunGtEq(dt.year, 11, 1, 3, 30)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1963) and (dt >= __SunGtEq(dt.year, 3, 16, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1964) and (dt >= __SunGtEq(dt.year, 3, 16, 3, 30)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1965) and (dt >= __SunGtEq(dt.year, 3, 16, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1965) and (dt >= datetime(dt.year, 10, 31, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1966) and (dt.year <= 1971) and (dt >= __SunGtEq(dt.year, 4, 16, 3, 30)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1966) and (dt.year <= 1971) and (dt >= __SunGtEq(dt.year, 10, 16, 3, 30)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1972) and (dt.year <= 1974) and (dt >= __SunGtEq(dt.year, 4, 15, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1972) and (dt.year <= 1973) and (dt >= __SunGtEq(dt.year, 10, 15, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1974) and (dt.year <= 1977) and (dt >= __SunGtEq(dt.year, 10, 15, 3, 30)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1975) and (dt.year <= 1977) and (dt >= __SunGtEq(dt.year, 4, 15, 3, 30)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1978) and (dt.year <= 1980) and (dt >= __SunGtEq(dt.year, 4, 15, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1978) and (dt.year <= 1980) and (dt >= __SunGtEq(dt.year, 10, 15, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Neth(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1916) and (dt >= datetime(dt.year, 5, 1, 0, 0)):
        l = 'NST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1916) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = 'AMT'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1917) and (dt >= datetime(dt.year, 4, 16, 2, 0)):
        l = 'NST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1917) and (dt >= datetime(dt.year, 9, 17, 2, 0)):
        l = 'AMT'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1918) and (dt.year <= 1921) and (dt >= __MonGtEq(dt.year, 4, 1, 2, 0)):
        l = 'NST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1918) and (dt.year <= 1921) and (dt >= __lastMon(dt.year, 9, 2, 0)):
        l = 'AMT'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1922) and (dt >= __lastSun(dt.year, 3, 2, 0)):
        l = 'NST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1922) and (dt.year <= 1936) and (dt >= __SunGtEq(dt.year, 10, 2, 2, 0)):
        l = 'AMT'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1923) and (dt >= __FriGtEq(dt.year, 6, 1, 2, 0)):
        l = 'NST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1924) and (dt >= __lastSun(dt.year, 3, 2, 0)):
        l = 'NST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1925) and (dt >= __FriGtEq(dt.year, 6, 1, 2, 0)):
        l = 'NST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1926) and (dt.year <= 1931) and (dt >= datetime(dt.year, 5, 15, 2, 0)):
        l = 'NST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1932) and (dt >= datetime(dt.year, 5, 22, 2, 0)):
        l = 'NST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1933) and (dt.year <= 1936) and (dt >= datetime(dt.year, 5, 15, 2, 0)):
        l = 'NST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1937) and (dt >= datetime(dt.year, 5, 22, 2, 0)):
        l = 'NST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1937) and (dt >= datetime(dt.year, 7, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1937) and (dt.year <= 1939) and (dt >= __SunGtEq(dt.year, 10, 2, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1938) and (dt.year <= 1939) and (dt >= datetime(dt.year, 5, 15, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 4, 2, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 9, 16, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Bulg(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1979) and (dt >= datetime(dt.year, 3, 31, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1979) and (dt >= datetime(dt.year, 10, 1, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1980) and (dt.year <= 1982) and (dt >= __SatGtEq(dt.year, 4, 1, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1980) and (dt >= datetime(dt.year, 9, 29, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1981) and (dt >= datetime(dt.year, 9, 27, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Louisville(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1921) and (dt >= datetime(dt.year, 5, 1, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1921) and (dt >= datetime(dt.year, 9, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1941) and (dt.year <= 1961) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1941) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1946) and (dt >= datetime(dt.year, 6, 2, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1950) and (dt.year <= 1955) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1956) and (dt.year <= 1960) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Guat(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1973) and (dt >= datetime(dt.year, 11, 25, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1974) and (dt >= datetime(dt.year, 2, 24, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1983) and (dt >= datetime(dt.year, 5, 21, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1983) and (dt >= datetime(dt.year, 9, 22, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1991) and (dt >= datetime(dt.year, 3, 23, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1991) and (dt >= datetime(dt.year, 9, 7, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2006) and (dt >= datetime(dt.year, 4, 30, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2006) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Arg(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1930) and (dt >= datetime(dt.year, 12, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1931) and (dt >= datetime(dt.year, 4, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1931) and (dt >= datetime(dt.year, 10, 15, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1932) and (dt.year <= 1940) and (dt >= datetime(dt.year, 3, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1932) and (dt.year <= 1939) and (dt >= datetime(dt.year, 11, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1940) and (dt >= datetime(dt.year, 7, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1941) and (dt >= datetime(dt.year, 6, 15, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1941) and (dt >= datetime(dt.year, 10, 15, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1943) and (dt >= datetime(dt.year, 8, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1943) and (dt >= datetime(dt.year, 10, 15, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1946) and (dt >= datetime(dt.year, 3, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1946) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1963) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1963) and (dt >= datetime(dt.year, 12, 15, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1964) and (dt.year <= 1966) and (dt >= datetime(dt.year, 3, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1964) and (dt.year <= 1966) and (dt >= datetime(dt.year, 10, 15, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1967) and (dt >= datetime(dt.year, 4, 2, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1967) and (dt.year <= 1968) and (dt >= __SunGtEq(dt.year, 10, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1968) and (dt.year <= 1969) and (dt >= __SunGtEq(dt.year, 4, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1974) and (dt >= datetime(dt.year, 1, 23, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1974) and (dt >= datetime(dt.year, 5, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1988) and (dt >= datetime(dt.year, 12, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1989) and (dt.year <= 1993) and (dt >= __SunGtEq(dt.year, 3, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1989) and (dt.year <= 1992) and (dt >= __SunGtEq(dt.year, 10, 15, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1999) and (dt >= __SunGtEq(dt.year, 10, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2000) and (dt >= datetime(dt.year, 3, 3, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2007) and (dt >= datetime(dt.year, 12, 30, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2008) and (dt.year <= 2009) and (dt >= __SunGtEq(dt.year, 3, 15, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2008) and (dt >= __SunGtEq(dt.year, 10, 15, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    return (s, l)
def _Turkey(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1916) and (dt >= datetime(dt.year, 5, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1916) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1920) and (dt >= datetime(dt.year, 3, 28, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1920) and (dt >= datetime(dt.year, 10, 25, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1921) and (dt >= datetime(dt.year, 4, 3, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1921) and (dt >= datetime(dt.year, 10, 3, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1922) and (dt >= datetime(dt.year, 3, 26, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1922) and (dt >= datetime(dt.year, 10, 8, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1924) and (dt >= datetime(dt.year, 5, 13, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1924) and (dt.year <= 1925) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1925) and (dt >= datetime(dt.year, 5, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1940) and (dt >= datetime(dt.year, 6, 30, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1940) and (dt >= datetime(dt.year, 10, 5, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1940) and (dt >= datetime(dt.year, 12, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1941) and (dt >= datetime(dt.year, 9, 21, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1942) and (dt >= datetime(dt.year, 4, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1942) and (dt >= datetime(dt.year, 11, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 4, 2, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 10, 8, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1946) and (dt >= datetime(dt.year, 6, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1946) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1947) and (dt.year <= 1948) and (dt >= __SunGtEq(dt.year, 4, 16, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1947) and (dt.year <= 1950) and (dt >= __SunGtEq(dt.year, 10, 2, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1949) and (dt >= datetime(dt.year, 4, 10, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1950) and (dt >= datetime(dt.year, 4, 19, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1951) and (dt >= datetime(dt.year, 4, 22, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1951) and (dt >= datetime(dt.year, 10, 8, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1962) and (dt >= datetime(dt.year, 7, 15, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1962) and (dt >= datetime(dt.year, 10, 8, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1964) and (dt >= datetime(dt.year, 5, 15, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1964) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1970) and (dt.year <= 1972) and (dt >= __SunGtEq(dt.year, 5, 2, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1970) and (dt.year <= 1972) and (dt >= __SunGtEq(dt.year, 10, 2, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1973) and (dt >= datetime(dt.year, 6, 3, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1973) and (dt >= datetime(dt.year, 11, 4, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1974) and (dt >= datetime(dt.year, 3, 31, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1974) and (dt >= datetime(dt.year, 11, 3, 5, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1975) and (dt >= datetime(dt.year, 3, 30, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1975) and (dt.year <= 1976) and (dt >= __lastSun(dt.year, 10, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1976) and (dt >= datetime(dt.year, 6, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1977) and (dt.year <= 1978) and (dt >= __SunGtEq(dt.year, 4, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1977) and (dt >= datetime(dt.year, 10, 16, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1979) and (dt.year <= 1980) and (dt >= __SunGtEq(dt.year, 4, 1, 3, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1979) and (dt.year <= 1982) and (dt >= __MonGtEq(dt.year, 10, 11, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1981) and (dt.year <= 1982) and (dt >= __lastSun(dt.year, 3, 3, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1983) and (dt >= datetime(dt.year, 7, 31, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1983) and (dt >= datetime(dt.year, 10, 2, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1985) and (dt >= datetime(dt.year, 4, 20, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1985) and (dt >= datetime(dt.year, 9, 28, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1986) and (dt.year <= 1990) and (dt >= __lastSun(dt.year, 3, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1986) and (dt.year <= 1990) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1991) and (dt.year <= 2006) and (dt >= __lastSun(dt.year, 3, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1991) and (dt.year <= 1995) and (dt >= __lastSun(dt.year, 9, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1996) and (dt.year <= 2006) and (dt >= __lastSun(dt.year, 10, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Perry(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1946) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1946) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1953) and (dt.year <= 1954) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1953) and (dt.year <= 1959) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1955) and (dt >= datetime(dt.year, 5, 1, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1956) and (dt.year <= 1963) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1960) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1961) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1962) and (dt.year <= 1963) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Lux(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1916) and (dt >= datetime(dt.year, 5, 14, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1916) and (dt >= datetime(dt.year, 10, 1, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1917) and (dt >= datetime(dt.year, 4, 28, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1917) and (dt >= datetime(dt.year, 9, 17, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1918) and (dt >= __MonGtEq(dt.year, 4, 15, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1918) and (dt >= __MonGtEq(dt.year, 9, 15, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1919) and (dt >= datetime(dt.year, 3, 1, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1919) and (dt >= datetime(dt.year, 10, 5, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1920) and (dt >= datetime(dt.year, 2, 14, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1920) and (dt >= datetime(dt.year, 10, 24, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1921) and (dt >= datetime(dt.year, 3, 14, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1921) and (dt >= datetime(dt.year, 10, 26, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1922) and (dt >= datetime(dt.year, 3, 25, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1922) and (dt >= __SunGtEq(dt.year, 10, 2, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1923) and (dt >= datetime(dt.year, 4, 21, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1923) and (dt >= __SunGtEq(dt.year, 10, 2, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1924) and (dt >= datetime(dt.year, 3, 29, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1924) and (dt.year <= 1928) and (dt >= __SunGtEq(dt.year, 10, 2, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1925) and (dt >= datetime(dt.year, 4, 5, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1926) and (dt >= datetime(dt.year, 4, 17, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1927) and (dt >= datetime(dt.year, 4, 9, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1928) and (dt >= datetime(dt.year, 4, 14, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1929) and (dt >= datetime(dt.year, 4, 20, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    return (s, l)
def _Lebanon(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1920) and (dt >= datetime(dt.year, 3, 28, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1920) and (dt >= datetime(dt.year, 10, 25, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1921) and (dt >= datetime(dt.year, 4, 3, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1921) and (dt >= datetime(dt.year, 10, 3, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1922) and (dt >= datetime(dt.year, 3, 26, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1922) and (dt >= datetime(dt.year, 10, 8, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1923) and (dt >= datetime(dt.year, 4, 22, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1923) and (dt >= datetime(dt.year, 9, 16, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1957) and (dt.year <= 1961) and (dt >= datetime(dt.year, 5, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1957) and (dt.year <= 1961) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1972) and (dt >= datetime(dt.year, 6, 22, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1972) and (dt.year <= 1977) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1973) and (dt.year <= 1977) and (dt >= datetime(dt.year, 5, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1978) and (dt >= datetime(dt.year, 4, 30, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1978) and (dt >= datetime(dt.year, 9, 30, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1984) and (dt.year <= 1987) and (dt >= datetime(dt.year, 5, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1984) and (dt.year <= 1991) and (dt >= datetime(dt.year, 10, 16, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1988) and (dt >= datetime(dt.year, 6, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1989) and (dt >= datetime(dt.year, 5, 10, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1990) and (dt.year <= 1992) and (dt >= datetime(dt.year, 5, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1992) and (dt >= datetime(dt.year, 10, 4, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1993) and (dt >= __lastSun(dt.year, 3, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1993) and (dt.year <= 1998) and (dt >= __lastSun(dt.year, 9, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1999) and (dt >= __lastSun(dt.year, 10, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Denver(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1920) and (dt.year <= 1921) and (dt >= __lastSun(dt.year, 3, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1920) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1921) and (dt >= datetime(dt.year, 5, 22, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1965) and (dt.year <= 1966) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1965) and (dt.year <= 1966) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _France(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1916) and (dt >= datetime(dt.year, 6, 14, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1916) and (dt.year <= 1919) and (dt >= __SunGtEq(dt.year, 10, 1, 23, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1917) and (dt >= datetime(dt.year, 3, 24, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1918) and (dt >= datetime(dt.year, 3, 9, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1919) and (dt >= datetime(dt.year, 3, 1, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1920) and (dt >= datetime(dt.year, 2, 14, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1920) and (dt >= datetime(dt.year, 10, 23, 23, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1921) and (dt >= datetime(dt.year, 3, 14, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1921) and (dt >= datetime(dt.year, 10, 25, 23, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1922) and (dt >= datetime(dt.year, 3, 25, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1922) and (dt.year <= 1938) and (dt >= __SatGtEq(dt.year, 10, 1, 23, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1923) and (dt >= datetime(dt.year, 5, 26, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1924) and (dt >= datetime(dt.year, 3, 29, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1925) and (dt >= datetime(dt.year, 4, 4, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1926) and (dt >= datetime(dt.year, 4, 17, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1927) and (dt >= datetime(dt.year, 4, 9, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1928) and (dt >= datetime(dt.year, 4, 14, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1929) and (dt >= datetime(dt.year, 4, 20, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1930) and (dt >= datetime(dt.year, 4, 12, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1931) and (dt >= datetime(dt.year, 4, 18, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1932) and (dt >= datetime(dt.year, 4, 2, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1933) and (dt >= datetime(dt.year, 3, 25, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1934) and (dt >= datetime(dt.year, 4, 7, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1935) and (dt >= datetime(dt.year, 3, 30, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1936) and (dt >= datetime(dt.year, 4, 18, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1937) and (dt >= datetime(dt.year, 4, 3, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1938) and (dt >= datetime(dt.year, 3, 26, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1939) and (dt >= datetime(dt.year, 4, 15, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1939) and (dt >= datetime(dt.year, 11, 18, 23, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1940) and (dt >= datetime(dt.year, 2, 25, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1941) and (dt >= datetime(dt.year, 5, 5, 0, 0)):
        l = 'M'
        s = timedelta(seconds=0, hours=2, minutes=0)
    if (dt.year == 1941) and (dt >= datetime(dt.year, 10, 6, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1942) and (dt >= datetime(dt.year, 3, 9, 0, 0)):
        l = 'M'
        s = timedelta(seconds=0, hours=2, minutes=0)
    if (dt.year == 1942) and (dt >= datetime(dt.year, 11, 2, 3, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1943) and (dt >= datetime(dt.year, 3, 29, 2, 0)):
        l = 'M'
        s = timedelta(seconds=0, hours=2, minutes=0)
    if (dt.year == 1943) and (dt >= datetime(dt.year, 10, 4, 3, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1944) and (dt >= datetime(dt.year, 4, 3, 2, 0)):
        l = 'M'
        s = timedelta(seconds=0, hours=2, minutes=0)
    if (dt.year == 1944) and (dt >= datetime(dt.year, 10, 8, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 4, 2, 2, 0)):
        l = 'M'
        s = timedelta(seconds=0, hours=2, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 9, 16, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1976) and (dt >= datetime(dt.year, 3, 28, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1976) and (dt >= datetime(dt.year, 9, 26, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _HK(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1941) and (dt >= datetime(dt.year, 4, 1, 3, 30)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1941) and (dt >= datetime(dt.year, 9, 30, 3, 30)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1946) and (dt >= datetime(dt.year, 4, 20, 3, 30)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1946) and (dt >= datetime(dt.year, 12, 1, 3, 30)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1947) and (dt >= datetime(dt.year, 4, 13, 3, 30)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1947) and (dt >= datetime(dt.year, 12, 30, 3, 30)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1948) and (dt >= datetime(dt.year, 5, 2, 3, 30)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1948) and (dt.year <= 1951) and (dt >= __lastSun(dt.year, 10, 3, 30)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1952) and (dt >= datetime(dt.year, 10, 25, 3, 30)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1949) and (dt.year <= 1953) and (dt >= __SunGtEq(dt.year, 4, 1, 3, 30)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1953) and (dt >= datetime(dt.year, 11, 1, 3, 30)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1954) and (dt.year <= 1964) and (dt >= __SunGtEq(dt.year, 3, 18, 3, 30)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1954) and (dt >= datetime(dt.year, 10, 31, 3, 30)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1955) and (dt.year <= 1964) and (dt >= __SunGtEq(dt.year, 11, 1, 3, 30)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1965) and (dt.year <= 1976) and (dt >= __SunGtEq(dt.year, 4, 16, 3, 30)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1965) and (dt.year <= 1976) and (dt >= __SunGtEq(dt.year, 10, 16, 3, 30)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1973) and (dt >= datetime(dt.year, 12, 30, 3, 30)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1979) and (dt >= __SunGtEq(dt.year, 5, 8, 3, 30)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1979) and (dt >= __SunGtEq(dt.year, 10, 16, 3, 30)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Peru(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1938) and (dt >= datetime(dt.year, 1, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1938) and (dt >= datetime(dt.year, 4, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1938) and (dt.year <= 1939) and (dt >= __lastSun(dt.year, 9, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1939) and (dt.year <= 1940) and (dt >= __SunGtEq(dt.year, 3, 24, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1986) and (dt.year <= 1987) and (dt >= datetime(dt.year, 1, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1986) and (dt.year <= 1987) and (dt >= datetime(dt.year, 4, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1990) and (dt >= datetime(dt.year, 1, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1990) and (dt >= datetime(dt.year, 4, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1994) and (dt >= datetime(dt.year, 1, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1994) and (dt >= datetime(dt.year, 4, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Vanuatu(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1983) and (dt >= datetime(dt.year, 9, 25, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1984) and (dt.year <= 1991) and (dt >= __SunGtEq(dt.year, 3, 23, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1984) and (dt >= datetime(dt.year, 10, 23, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1985) and (dt.year <= 1991) and (dt >= __SunGtEq(dt.year, 9, 23, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1992) and (dt.year <= 1993) and (dt >= __SunGtEq(dt.year, 1, 23, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1992) and (dt >= __SunGtEq(dt.year, 10, 23, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    return (s, l)
def _Norway(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1916) and (dt >= datetime(dt.year, 5, 22, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1916) and (dt >= datetime(dt.year, 9, 30, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 4, 2, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 10, 1, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1959) and (dt.year <= 1964) and (dt >= __SunGtEq(dt.year, 3, 15, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1959) and (dt.year <= 1965) and (dt >= __SunGtEq(dt.year, 9, 15, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1965) and (dt >= datetime(dt.year, 4, 25, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    return (s, l)
def _ROK(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1960) and (dt >= datetime(dt.year, 5, 15, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1960) and (dt >= datetime(dt.year, 9, 13, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1987) and (dt.year <= 1988) and (dt >= __SunGtEq(dt.year, 5, 8, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1987) and (dt.year <= 1988) and (dt >= __SunGtEq(dt.year, 10, 8, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Zion(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1940) and (dt >= datetime(dt.year, 6, 1, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1942) and (dt.year <= 1944) and (dt >= datetime(dt.year, 11, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1943) and (dt >= datetime(dt.year, 4, 1, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1944) and (dt >= datetime(dt.year, 4, 1, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 4, 16, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 11, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1946) and (dt >= datetime(dt.year, 4, 16, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1946) and (dt >= datetime(dt.year, 11, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1948) and (dt >= datetime(dt.year, 5, 23, 0, 0)):
        l = 'DD'
        s = timedelta(seconds=0, hours=2, minutes=0)
    if (dt.year == 1948) and (dt >= datetime(dt.year, 9, 1, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1948) and (dt.year <= 1949) and (dt >= datetime(dt.year, 11, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1949) and (dt >= datetime(dt.year, 5, 1, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1950) and (dt >= datetime(dt.year, 4, 16, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1950) and (dt >= datetime(dt.year, 9, 15, 3, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1951) and (dt >= datetime(dt.year, 4, 1, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1951) and (dt >= datetime(dt.year, 11, 11, 3, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1952) and (dt >= datetime(dt.year, 4, 20, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1952) and (dt >= datetime(dt.year, 10, 19, 3, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1953) and (dt >= datetime(dt.year, 4, 12, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1953) and (dt >= datetime(dt.year, 9, 13, 3, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1954) and (dt >= datetime(dt.year, 6, 13, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1954) and (dt >= datetime(dt.year, 9, 12, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1955) and (dt >= datetime(dt.year, 6, 11, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1955) and (dt >= datetime(dt.year, 9, 11, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1956) and (dt >= datetime(dt.year, 6, 3, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1956) and (dt >= datetime(dt.year, 9, 30, 3, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1957) and (dt >= datetime(dt.year, 4, 29, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1957) and (dt >= datetime(dt.year, 9, 22, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1974) and (dt >= datetime(dt.year, 7, 7, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1974) and (dt >= datetime(dt.year, 10, 13, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1975) and (dt >= datetime(dt.year, 4, 20, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1975) and (dt >= datetime(dt.year, 8, 31, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1985) and (dt >= datetime(dt.year, 4, 14, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1985) and (dt >= datetime(dt.year, 9, 15, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1986) and (dt >= datetime(dt.year, 5, 18, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1986) and (dt >= datetime(dt.year, 9, 7, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1987) and (dt >= datetime(dt.year, 4, 15, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1987) and (dt >= datetime(dt.year, 9, 13, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1988) and (dt >= datetime(dt.year, 4, 10, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1988) and (dt >= datetime(dt.year, 9, 4, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1989) and (dt >= datetime(dt.year, 4, 30, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1989) and (dt >= datetime(dt.year, 9, 3, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1990) and (dt >= datetime(dt.year, 3, 25, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1990) and (dt >= datetime(dt.year, 8, 26, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1991) and (dt >= datetime(dt.year, 3, 24, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1991) and (dt >= datetime(dt.year, 9, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1992) and (dt >= datetime(dt.year, 3, 29, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1992) and (dt >= datetime(dt.year, 9, 6, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1993) and (dt >= datetime(dt.year, 4, 2, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1993) and (dt >= datetime(dt.year, 9, 5, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1994) and (dt >= datetime(dt.year, 4, 1, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1994) and (dt >= datetime(dt.year, 8, 28, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1995) and (dt >= datetime(dt.year, 3, 31, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1995) and (dt >= datetime(dt.year, 9, 3, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1996) and (dt >= datetime(dt.year, 3, 15, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1996) and (dt >= datetime(dt.year, 9, 16, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1997) and (dt >= datetime(dt.year, 3, 21, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1997) and (dt >= datetime(dt.year, 9, 14, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1998) and (dt >= datetime(dt.year, 3, 20, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1998) and (dt >= datetime(dt.year, 9, 6, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1999) and (dt >= datetime(dt.year, 4, 2, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1999) and (dt >= datetime(dt.year, 9, 3, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2000) and (dt >= datetime(dt.year, 4, 14, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2000) and (dt >= datetime(dt.year, 10, 6, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2001) and (dt >= datetime(dt.year, 4, 9, 1, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2001) and (dt >= datetime(dt.year, 9, 24, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2002) and (dt >= datetime(dt.year, 3, 29, 1, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2002) and (dt >= datetime(dt.year, 10, 7, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2003) and (dt >= datetime(dt.year, 3, 28, 1, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2003) and (dt >= datetime(dt.year, 10, 3, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2004) and (dt >= datetime(dt.year, 4, 7, 1, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2004) and (dt >= datetime(dt.year, 9, 22, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2005) and (dt >= datetime(dt.year, 4, 1, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2005) and (dt >= datetime(dt.year, 10, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2006) and (dt.year <= 2010) and (dt >= __FriGtEq(dt.year, 3, 26, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2006) and (dt >= datetime(dt.year, 10, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2007) and (dt >= datetime(dt.year, 9, 16, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2008) and (dt >= datetime(dt.year, 10, 5, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2009) and (dt >= datetime(dt.year, 9, 27, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2010) and (dt >= datetime(dt.year, 9, 12, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2011) and (dt >= datetime(dt.year, 4, 1, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2011) and (dt >= datetime(dt.year, 10, 2, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2012) and (dt >= __FriGtEq(dt.year, 3, 26, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2012) and (dt >= datetime(dt.year, 9, 23, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2013) and (dt >= __FriGtEq(dt.year, 3, 23, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2013) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Para(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1975) and (dt.year <= 1988) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1975) and (dt.year <= 1978) and (dt >= datetime(dt.year, 3, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1979) and (dt.year <= 1991) and (dt >= datetime(dt.year, 4, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1989) and (dt >= datetime(dt.year, 10, 22, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1990) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1991) and (dt >= datetime(dt.year, 10, 6, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1992) and (dt >= datetime(dt.year, 3, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1992) and (dt >= datetime(dt.year, 10, 5, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1993) and (dt >= datetime(dt.year, 3, 31, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1993) and (dt.year <= 1995) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1994) and (dt.year <= 1995) and (dt >= __lastSun(dt.year, 2, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1996) and (dt >= datetime(dt.year, 3, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1996) and (dt.year <= 2001) and (dt >= __SunGtEq(dt.year, 10, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1997) and (dt >= __lastSun(dt.year, 2, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1998) and (dt.year <= 2001) and (dt >= __SunGtEq(dt.year, 3, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2002) and (dt.year <= 2004) and (dt >= __SunGtEq(dt.year, 4, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2002) and (dt.year <= 2003) and (dt >= __SunGtEq(dt.year, 9, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2004) and (dt.year <= 2009) and (dt >= __SunGtEq(dt.year, 10, 15, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2005) and (dt.year <= 2009) and (dt >= __SunGtEq(dt.year, 3, 8, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2010) and (dt >= __SunGtEq(dt.year, 10, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2010) and (dt.year <= 2012) and (dt >= __SunGtEq(dt.year, 4, 8, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2013) and (dt >= __SunGtEq(dt.year, 3, 22, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Cuba(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1928) and (dt >= datetime(dt.year, 6, 10, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1928) and (dt >= datetime(dt.year, 10, 10, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1940) and (dt.year <= 1942) and (dt >= __SunGtEq(dt.year, 6, 1, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1940) and (dt.year <= 1942) and (dt >= __SunGtEq(dt.year, 9, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1945) and (dt.year <= 1946) and (dt >= __SunGtEq(dt.year, 6, 1, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1945) and (dt.year <= 1946) and (dt >= __SunGtEq(dt.year, 9, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1965) and (dt >= datetime(dt.year, 6, 1, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1965) and (dt >= datetime(dt.year, 9, 30, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1966) and (dt >= datetime(dt.year, 5, 29, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1966) and (dt >= datetime(dt.year, 10, 2, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1967) and (dt >= datetime(dt.year, 4, 8, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1967) and (dt.year <= 1968) and (dt >= __SunGtEq(dt.year, 9, 8, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1968) and (dt >= datetime(dt.year, 4, 14, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1969) and (dt.year <= 1977) and (dt >= __lastSun(dt.year, 4, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1969) and (dt.year <= 1971) and (dt >= __lastSun(dt.year, 10, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1972) and (dt.year <= 1974) and (dt >= datetime(dt.year, 10, 8, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1975) and (dt.year <= 1977) and (dt >= __lastSun(dt.year, 10, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1978) and (dt >= datetime(dt.year, 5, 7, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1978) and (dt.year <= 1990) and (dt >= __SunGtEq(dt.year, 10, 8, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1979) and (dt.year <= 1980) and (dt >= __SunGtEq(dt.year, 3, 15, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1981) and (dt.year <= 1985) and (dt >= __SunGtEq(dt.year, 5, 5, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1986) and (dt.year <= 1989) and (dt >= __SunGtEq(dt.year, 3, 14, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1990) and (dt.year <= 1997) and (dt >= __SunGtEq(dt.year, 4, 1, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1991) and (dt.year <= 1995) and (dt >= __SunGtEq(dt.year, 10, 8, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1996) and (dt >= datetime(dt.year, 10, 6, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1997) and (dt >= datetime(dt.year, 10, 12, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1998) and (dt.year <= 1999) and (dt >= __lastSun(dt.year, 3, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1998) and (dt.year <= 2003) and (dt >= __lastSun(dt.year, 10, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2000) and (dt.year <= 2003) and (dt >= __SunGtEq(dt.year, 4, 1, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2004) and (dt >= __lastSun(dt.year, 3, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2006) and (dt.year <= 2010) and (dt >= __lastSun(dt.year, 10, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2007) and (dt >= __SunGtEq(dt.year, 3, 8, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2008) and (dt >= __SunGtEq(dt.year, 3, 15, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2009) and (dt.year <= 2010) and (dt >= __SunGtEq(dt.year, 3, 8, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2011) and (dt >= __SunGtEq(dt.year, 3, 15, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2011) and (dt >= datetime(dt.year, 11, 13, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2012) and (dt >= datetime(dt.year, 4, 1, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2012) and (dt >= __SunGtEq(dt.year, 11, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2013) and (dt >= __SunGtEq(dt.year, 3, 8, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    return (s, l)
def _StJohns(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1917) and (dt >= datetime(dt.year, 4, 8, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1917) and (dt >= datetime(dt.year, 9, 17, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1919) and (dt >= datetime(dt.year, 5, 5, 23, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1919) and (dt >= datetime(dt.year, 8, 12, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1920) and (dt.year <= 1935) and (dt >= __SunGtEq(dt.year, 5, 1, 23, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1920) and (dt.year <= 1935) and (dt >= __lastSun(dt.year, 10, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1936) and (dt.year <= 1941) and (dt >= __MonGtEq(dt.year, 5, 9, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1936) and (dt.year <= 1941) and (dt >= __MonGtEq(dt.year, 10, 2, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1946) and (dt.year <= 1950) and (dt >= __SunGtEq(dt.year, 5, 8, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1946) and (dt.year <= 1950) and (dt >= __SunGtEq(dt.year, 10, 2, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1951) and (dt.year <= 1986) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1951) and (dt.year <= 1959) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1960) and (dt.year <= 1986) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1987) and (dt >= __SunGtEq(dt.year, 4, 1, 0, 1)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1987) and (dt.year <= 2006) and (dt >= __lastSun(dt.year, 10, 0, 1)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1988) and (dt >= __SunGtEq(dt.year, 4, 1, 0, 1)):
        l = 'DD'
        s = timedelta(seconds=0, hours=2, minutes=0)
    if (dt.year >= 1989) and (dt.year <= 2006) and (dt >= __SunGtEq(dt.year, 4, 1, 0, 1)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2007) and (dt.year <= 2011) and (dt >= __SunGtEq(dt.year, 3, 8, 0, 1)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2007) and (dt.year <= 2010) and (dt >= __SunGtEq(dt.year, 11, 1, 0, 1)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Cook(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1978) and (dt >= datetime(dt.year, 11, 12, 0, 0)):
        l = 'HS'
        s = timedelta(seconds=0, hours=0, minutes=30)
    if (dt.year >= 1979) and (dt.year <= 1991) and (dt >= __SunGtEq(dt.year, 3, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1979) and (dt.year <= 1990) and (dt >= __lastSun(dt.year, 10, 0, 0)):
        l = 'HS'
        s = timedelta(seconds=0, hours=0, minutes=30)
    return (s, l)
def _Chatham(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1974) and (dt >= __SunGtEq(dt.year, 11, 1, 2, 45)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1975) and (dt >= __lastSun(dt.year, 2, 2, 45)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1975) and (dt.year <= 1988) and (dt >= __lastSun(dt.year, 10, 2, 45)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1976) and (dt.year <= 1989) and (dt >= __SunGtEq(dt.year, 3, 1, 2, 45)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1989) and (dt >= __SunGtEq(dt.year, 10, 8, 2, 45)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1990) and (dt.year <= 2006) and (dt >= __SunGtEq(dt.year, 10, 1, 2, 45)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1990) and (dt.year <= 2007) and (dt >= __SunGtEq(dt.year, 3, 15, 2, 45)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2007) and (dt >= __lastSun(dt.year, 9, 2, 45)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2008) and (dt >= __SunGtEq(dt.year, 4, 1, 2, 45)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Swift(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1957) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1957) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1959) and (dt.year <= 1961) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1959) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1960) and (dt.year <= 1961) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Tonga(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1999) and (dt >= datetime(dt.year, 10, 7, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2000) and (dt >= datetime(dt.year, 3, 19, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2000) and (dt.year <= 2001) and (dt >= __SunGtEq(dt.year, 11, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2001) and (dt.year <= 2002) and (dt >= __lastSun(dt.year, 1, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Finland(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1942) and (dt >= datetime(dt.year, 4, 2, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1942) and (dt >= datetime(dt.year, 10, 4, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1981) and (dt.year <= 1982) and (dt >= __lastSun(dt.year, 3, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1981) and (dt.year <= 1982) and (dt >= __lastSun(dt.year, 9, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Libya(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1951) and (dt >= datetime(dt.year, 10, 14, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1952) and (dt >= datetime(dt.year, 1, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1953) and (dt >= datetime(dt.year, 10, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1954) and (dt >= datetime(dt.year, 1, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1955) and (dt >= datetime(dt.year, 9, 30, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1956) and (dt >= datetime(dt.year, 1, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1982) and (dt.year <= 1984) and (dt >= datetime(dt.year, 4, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1982) and (dt.year <= 1985) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1985) and (dt >= datetime(dt.year, 4, 6, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1986) and (dt >= datetime(dt.year, 4, 4, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1986) and (dt >= datetime(dt.year, 10, 3, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1987) and (dt.year <= 1989) and (dt >= datetime(dt.year, 4, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1987) and (dt.year <= 1989) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1997) and (dt >= datetime(dt.year, 4, 4, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1997) and (dt >= datetime(dt.year, 10, 4, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2013) and (dt >= __lastFri(dt.year, 3, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2013) and (dt >= __lastFri(dt.year, 10, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _RussiaAsia(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1981) and (dt.year <= 1984) and (dt >= datetime(dt.year, 4, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1981) and (dt.year <= 1983) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1984) and (dt.year <= 1991) and (dt >= __lastSun	(dt.year, 9, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1985) and (dt.year <= 1991) and (dt >= __lastSun	(dt.year, 3, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1992) and (dt >= __lastSat(dt.year, 3, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1992) and (dt >= __lastSat(dt.year, 9, 23, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1993) and (dt >= __lastSun	(dt.year, 3, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1993) and (dt.year <= 1995) and (dt >= __lastSun	(dt.year, 9, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1996) and (dt >= __lastSun	(dt.year, 10, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Mauritius(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1982) and (dt >= datetime(dt.year, 10, 10, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1983) and (dt >= datetime(dt.year, 3, 21, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2008) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2009) and (dt >= __lastSun(dt.year, 3, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _EU(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1977) and (dt.year <= 1980) and (dt >= __SunGtEq(dt.year, 4, 1, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1977) and (dt >= __lastSun	(dt.year, 9, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1978) and (dt >= datetime(dt.year, 10, 1, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1979) and (dt.year <= 1995) and (dt >= __lastSun	(dt.year, 9, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1981) and (dt >= __lastSun	(dt.year, 3, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1996) and (dt >= __lastSun	(dt.year, 10, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _GB_Eire(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1916) and (dt >= datetime(dt.year, 5, 21, 2, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1916) and (dt >= datetime(dt.year, 10, 1, 2, 0)):
        l = 'GMT'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1917) and (dt >= datetime(dt.year, 4, 8, 2, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1917) and (dt >= datetime(dt.year, 9, 17, 2, 0)):
        l = 'GMT'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1918) and (dt >= datetime(dt.year, 3, 24, 2, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1918) and (dt >= datetime(dt.year, 9, 30, 2, 0)):
        l = 'GMT'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1919) and (dt >= datetime(dt.year, 3, 30, 2, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1919) and (dt >= datetime(dt.year, 9, 29, 2, 0)):
        l = 'GMT'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1920) and (dt >= datetime(dt.year, 3, 28, 2, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1920) and (dt >= datetime(dt.year, 10, 25, 2, 0)):
        l = 'GMT'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1921) and (dt >= datetime(dt.year, 4, 3, 2, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1921) and (dt >= datetime(dt.year, 10, 3, 2, 0)):
        l = 'GMT'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1922) and (dt >= datetime(dt.year, 3, 26, 2, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1922) and (dt >= datetime(dt.year, 10, 8, 2, 0)):
        l = 'GMT'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1923) and (dt >= __SunGtEq(dt.year, 4, 16, 2, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1923) and (dt.year <= 1924) and (dt >= __SunGtEq(dt.year, 9, 16, 2, 0)):
        l = 'GMT'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1924) and (dt >= __SunGtEq(dt.year, 4, 9, 2, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1925) and (dt.year <= 1926) and (dt >= __SunGtEq(dt.year, 4, 16, 2, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1925) and (dt.year <= 1938) and (dt >= __SunGtEq(dt.year, 10, 2, 2, 0)):
        l = 'GMT'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1927) and (dt >= __SunGtEq(dt.year, 4, 9, 2, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1928) and (dt.year <= 1929) and (dt >= __SunGtEq(dt.year, 4, 16, 2, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1930) and (dt >= __SunGtEq(dt.year, 4, 9, 2, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1931) and (dt.year <= 1932) and (dt >= __SunGtEq(dt.year, 4, 16, 2, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1933) and (dt >= __SunGtEq(dt.year, 4, 9, 2, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1934) and (dt >= __SunGtEq(dt.year, 4, 16, 2, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1935) and (dt >= __SunGtEq(dt.year, 4, 9, 2, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1936) and (dt.year <= 1937) and (dt >= __SunGtEq(dt.year, 4, 16, 2, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1938) and (dt >= __SunGtEq(dt.year, 4, 9, 2, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1939) and (dt >= __SunGtEq(dt.year, 4, 16, 2, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1939) and (dt >= __SunGtEq(dt.year, 11, 16, 2, 0)):
        l = 'GMT'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1940) and (dt >= __SunGtEq(dt.year, 2, 23, 2, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1941) and (dt >= __SunGtEq(dt.year, 5, 2, 1, 0)):
        l = 'BDST'
        s = timedelta(seconds=0, hours=2, minutes=0)
    if (dt.year >= 1941) and (dt.year <= 1943) and (dt >= __SunGtEq(dt.year, 8, 9, 1, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1942) and (dt.year <= 1944) and (dt >= __SunGtEq(dt.year, 4, 2, 1, 0)):
        l = 'BDST'
        s = timedelta(seconds=0, hours=2, minutes=0)
    if (dt.year == 1944) and (dt >= __SunGtEq(dt.year, 9, 16, 1, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1945) and (dt >= __MonGtEq(dt.year, 4, 2, 1, 0)):
        l = 'BDST'
        s = timedelta(seconds=0, hours=2, minutes=0)
    if (dt.year == 1945) and (dt >= __SunGtEq(dt.year, 7, 9, 1, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1945) and (dt.year <= 1946) and (dt >= __SunGtEq(dt.year, 10, 2, 2, 0)):
        l = 'GMT'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1946) and (dt >= __SunGtEq(dt.year, 4, 9, 2, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1947) and (dt >= datetime(dt.year, 3, 16, 2, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1947) and (dt >= datetime(dt.year, 4, 13, 1, 0)):
        l = 'BDST'
        s = timedelta(seconds=0, hours=2, minutes=0)
    if (dt.year == 1947) and (dt >= datetime(dt.year, 8, 10, 1, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1947) and (dt >= datetime(dt.year, 11, 2, 2, 0)):
        l = 'GMT'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1948) and (dt >= datetime(dt.year, 3, 14, 2, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1948) and (dt >= datetime(dt.year, 10, 31, 2, 0)):
        l = 'GMT'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1949) and (dt >= datetime(dt.year, 4, 3, 2, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1949) and (dt >= datetime(dt.year, 10, 30, 2, 0)):
        l = 'GMT'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1950) and (dt.year <= 1952) and (dt >= __SunGtEq(dt.year, 4, 14, 2, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1950) and (dt.year <= 1952) and (dt >= __SunGtEq(dt.year, 10, 21, 2, 0)):
        l = 'GMT'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1953) and (dt >= __SunGtEq(dt.year, 4, 16, 2, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1953) and (dt.year <= 1960) and (dt >= __SunGtEq(dt.year, 10, 2, 2, 0)):
        l = 'GMT'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1954) and (dt >= __SunGtEq(dt.year, 4, 9, 2, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1955) and (dt.year <= 1956) and (dt >= __SunGtEq(dt.year, 4, 16, 2, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1957) and (dt >= __SunGtEq(dt.year, 4, 9, 2, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1958) and (dt.year <= 1959) and (dt >= __SunGtEq(dt.year, 4, 16, 2, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1960) and (dt >= __SunGtEq(dt.year, 4, 9, 2, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1961) and (dt.year <= 1963) and (dt >= __lastSun(dt.year, 3, 2, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1961) and (dt.year <= 1968) and (dt >= __SunGtEq(dt.year, 10, 23, 2, 0)):
        l = 'GMT'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1964) and (dt.year <= 1967) and (dt >= __SunGtEq(dt.year, 3, 19, 2, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1968) and (dt >= datetime(dt.year, 2, 18, 2, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1972) and (dt.year <= 1980) and (dt >= __SunGtEq(dt.year, 3, 16, 2, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1972) and (dt.year <= 1980) and (dt >= __SunGtEq(dt.year, 10, 23, 2, 0)):
        l = 'GMT'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1981) and (dt.year <= 1995) and (dt >= __lastSun(dt.year, 3, 1, 0)):
        l = 'BST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1981) and (dt.year <= 1989) and (dt >= __SunGtEq(dt.year, 10, 23, 1, 0)):
        l = 'GMT'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1990) and (dt.year <= 1995) and (dt >= __SunGtEq(dt.year, 10, 22, 1, 0)):
        l = 'GMT'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Poland(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1918) and (dt.year <= 1919) and (dt >= datetime(dt.year, 9, 16, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1919) and (dt >= datetime(dt.year, 4, 15, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1944) and (dt >= datetime(dt.year, 4, 3, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1944) and (dt >= datetime(dt.year, 10, 4, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 4, 29, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 11, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1946) and (dt >= datetime(dt.year, 4, 14, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1946) and (dt >= datetime(dt.year, 10, 7, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1947) and (dt >= datetime(dt.year, 5, 4, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1947) and (dt.year <= 1949) and (dt >= __SunGtEq(dt.year, 10, 1, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1948) and (dt >= datetime(dt.year, 4, 18, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1949) and (dt >= datetime(dt.year, 4, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1957) and (dt >= datetime(dt.year, 6, 2, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1957) and (dt.year <= 1958) and (dt >= __lastSun(dt.year, 9, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1958) and (dt >= datetime(dt.year, 3, 30, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1959) and (dt >= datetime(dt.year, 5, 31, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1959) and (dt.year <= 1961) and (dt >= __SunGtEq(dt.year, 10, 1, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1960) and (dt >= datetime(dt.year, 4, 3, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1961) and (dt.year <= 1964) and (dt >= __lastSun(dt.year, 5, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1962) and (dt.year <= 1964) and (dt >= __lastSun(dt.year, 9, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Russia(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1917) and (dt >= datetime(dt.year, 7, 1, 23, 0)):
        l = 'MST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1917) and (dt >= datetime(dt.year, 12, 28, 0, 0)):
        l = 'MMT'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1918) and (dt >= datetime(dt.year, 5, 31, 22, 0)):
        l = 'MDST'
        s = timedelta(seconds=0, hours=2, minutes=0)
    if (dt.year == 1918) and (dt >= datetime(dt.year, 9, 16, 1, 0)):
        l = 'MST'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1919) and (dt >= datetime(dt.year, 5, 31, 23, 0)):
        l = 'MDST'
        s = timedelta(seconds=0, hours=2, minutes=0)
    if (dt.year == 1919) and (dt >= datetime(dt.year, 7, 1, 2, 0)):
        l = 'MSD'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1919) and (dt >= datetime(dt.year, 8, 16, 0, 0)):
        l = 'MSK'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1921) and (dt >= datetime(dt.year, 2, 14, 23, 0)):
        l = 'MSD'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1921) and (dt >= datetime(dt.year, 3, 20, 23, 0)):
        l = 'MSM'
        s = timedelta(seconds=0, hours=2, minutes=0)
    if (dt.year == 1921) and (dt >= datetime(dt.year, 9, 1, 0, 0)):
        l = 'MSD'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1921) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1981) and (dt.year <= 1984) and (dt >= datetime(dt.year, 4, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1981) and (dt.year <= 1983) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1984) and (dt.year <= 1991) and (dt >= __lastSun	(dt.year, 9, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1985) and (dt.year <= 1991) and (dt >= __lastSun	(dt.year, 3, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1992) and (dt >= __lastSat	(dt.year, 3, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1992) and (dt >= __lastSat	(dt.year, 9, 23, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1993) and (dt.year <= 2010) and (dt >= __lastSun	(dt.year, 3, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1993) and (dt.year <= 1995) and (dt >= __lastSun	(dt.year, 9, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1996) and (dt.year <= 2010) and (dt >= __lastSun	(dt.year, 10, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Romania(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1932) and (dt >= datetime(dt.year, 5, 21, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1932) and (dt.year <= 1939) and (dt >= __SunGtEq(dt.year, 10, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1933) and (dt.year <= 1939) and (dt >= __SunGtEq(dt.year, 4, 2, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1979) and (dt >= datetime(dt.year, 5, 27, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1979) and (dt >= __lastSun	(dt.year, 9, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1980) and (dt >= datetime(dt.year, 4, 5, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1980) and (dt >= __lastSun	(dt.year, 9, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1991) and (dt.year <= 1993) and (dt >= __lastSun	(dt.year, 3, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1991) and (dt.year <= 1993) and (dt >= __lastSun	(dt.year, 9, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Fiji(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1998) and (dt.year <= 1999) and (dt >= __SunGtEq(dt.year, 11, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1999) and (dt.year <= 2000) and (dt >= __lastSun(dt.year, 2, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2009) and (dt >= datetime(dt.year, 11, 29, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2010) and (dt >= __lastSun(dt.year, 3, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2010) and (dt >= __SunGtEq(dt.year, 10, 21, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2011) and (dt >= __SunGtEq(dt.year, 3, 1, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2012) and (dt.year <= 2013) and (dt >= __SunGtEq(dt.year, 1, 18, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2014) and (dt >= __SunGtEq(dt.year, 1, 18, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _US(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1918) and (dt.year <= 1919) and (dt >= __lastSun(dt.year, 3, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1918) and (dt.year <= 1919) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1942) and (dt >= datetime(dt.year, 2, 9, 2, 0)):
        l = 'W'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 8, 14, 23, 0)):
        l = 'P'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 9, 30, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1967) and (dt.year <= 2006) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1967) and (dt.year <= 1973) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1974) and (dt >= datetime(dt.year, 1, 6, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1975) and (dt >= datetime(dt.year, 2, 23, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1976) and (dt.year <= 1986) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1987) and (dt.year <= 2006) and (dt >= __SunGtEq(dt.year, 4, 1, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2007) and (dt >= __SunGtEq(dt.year, 3, 8, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2007) and (dt >= __SunGtEq(dt.year, 11, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Austria(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1920) and (dt >= datetime(dt.year, 4, 5, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1920) and (dt >= datetime(dt.year, 9, 13, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1946) and (dt >= datetime(dt.year, 4, 14, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1946) and (dt.year <= 1948) and (dt >= __SunGtEq(dt.year, 10, 1, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1947) and (dt >= datetime(dt.year, 4, 6, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1948) and (dt >= datetime(dt.year, 4, 18, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1980) and (dt >= datetime(dt.year, 4, 6, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1980) and (dt >= datetime(dt.year, 9, 28, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Barb(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1977) and (dt >= datetime(dt.year, 6, 12, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1977) and (dt.year <= 1978) and (dt >= __SunGtEq(dt.year, 10, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1978) and (dt.year <= 1980) and (dt >= __SunGtEq(dt.year, 4, 15, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1979) and (dt >= datetime(dt.year, 9, 30, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1980) and (dt >= datetime(dt.year, 9, 25, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Hungary(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1918) and (dt >= datetime(dt.year, 4, 1, 3, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1918) and (dt >= datetime(dt.year, 9, 16, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1919) and (dt >= datetime(dt.year, 4, 15, 3, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1919) and (dt >= datetime(dt.year, 11, 24, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 5, 1, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 11, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1946) and (dt >= datetime(dt.year, 3, 31, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1946) and (dt.year <= 1949) and (dt >= __SunGtEq(dt.year, 10, 1, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1947) and (dt.year <= 1949) and (dt >= __SunGtEq(dt.year, 4, 4, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1950) and (dt >= datetime(dt.year, 4, 17, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1950) and (dt >= datetime(dt.year, 10, 23, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1954) and (dt.year <= 1955) and (dt >= datetime(dt.year, 5, 23, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1954) and (dt.year <= 1955) and (dt >= datetime(dt.year, 10, 3, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1956) and (dt >= __SunGtEq(dt.year, 6, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1956) and (dt >= __lastSun	(dt.year, 9, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1957) and (dt >= __SunGtEq(dt.year, 6, 1, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1957) and (dt >= __lastSun	(dt.year, 9, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1980) and (dt >= datetime(dt.year, 4, 6, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    return (s, l)
def _Brazil(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1931) and (dt >= datetime(dt.year, 10, 3, 11, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1932) and (dt.year <= 1933) and (dt >= datetime(dt.year, 4, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1932) and (dt >= datetime(dt.year, 10, 3, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1949) and (dt.year <= 1952) and (dt >= datetime(dt.year, 12, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1950) and (dt >= datetime(dt.year, 4, 16, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1951) and (dt.year <= 1952) and (dt >= datetime(dt.year, 4, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1953) and (dt >= datetime(dt.year, 3, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1963) and (dt >= datetime(dt.year, 12, 9, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1964) and (dt >= datetime(dt.year, 3, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1965) and (dt >= datetime(dt.year, 1, 31, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1965) and (dt >= datetime(dt.year, 3, 31, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1965) and (dt >= datetime(dt.year, 12, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1966) and (dt.year <= 1968) and (dt >= datetime(dt.year, 3, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1966) and (dt.year <= 1967) and (dt >= datetime(dt.year, 11, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1985) and (dt >= datetime(dt.year, 11, 2, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1986) and (dt >= datetime(dt.year, 3, 15, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1986) and (dt >= datetime(dt.year, 10, 25, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1987) and (dt >= datetime(dt.year, 2, 14, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1987) and (dt >= datetime(dt.year, 10, 25, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1988) and (dt >= datetime(dt.year, 2, 7, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1988) and (dt >= datetime(dt.year, 10, 16, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1989) and (dt >= datetime(dt.year, 1, 29, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1989) and (dt >= datetime(dt.year, 10, 15, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1990) and (dt >= datetime(dt.year, 2, 11, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1990) and (dt >= datetime(dt.year, 10, 21, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1991) and (dt >= datetime(dt.year, 2, 17, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1991) and (dt >= datetime(dt.year, 10, 20, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1992) and (dt >= datetime(dt.year, 2, 9, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1992) and (dt >= datetime(dt.year, 10, 25, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1993) and (dt >= datetime(dt.year, 1, 31, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1993) and (dt.year <= 1995) and (dt >= __SunGtEq(dt.year, 10, 11, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1994) and (dt.year <= 1995) and (dt >= __SunGtEq(dt.year, 2, 15, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1996) and (dt >= datetime(dt.year, 2, 11, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1996) and (dt >= datetime(dt.year, 10, 6, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1997) and (dt >= datetime(dt.year, 2, 16, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1997) and (dt >= datetime(dt.year, 10, 6, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1998) and (dt >= datetime(dt.year, 3, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1998) and (dt >= datetime(dt.year, 10, 11, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1999) and (dt >= datetime(dt.year, 2, 21, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1999) and (dt >= datetime(dt.year, 10, 3, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2000) and (dt >= datetime(dt.year, 2, 27, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2000) and (dt.year <= 2001) and (dt >= __SunGtEq(dt.year, 10, 8, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2001) and (dt.year <= 2006) and (dt >= __SunGtEq(dt.year, 2, 15, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2002) and (dt >= datetime(dt.year, 11, 3, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2003) and (dt >= datetime(dt.year, 10, 19, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2004) and (dt >= datetime(dt.year, 11, 2, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2005) and (dt >= datetime(dt.year, 10, 16, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2006) and (dt >= datetime(dt.year, 11, 5, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2007) and (dt >= datetime(dt.year, 2, 25, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2007) and (dt >= __SunGtEq(dt.year, 10, 8, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2008) and (dt >= __SunGtEq(dt.year, 10, 15, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2008) and (dt.year <= 2011) and (dt >= __SunGtEq(dt.year, 2, 15, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2012) and (dt >= __SunGtEq(dt.year, 2, 22, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2013) and (dt.year <= 2014) and (dt >= __SunGtEq(dt.year, 2, 15, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2015) and (dt >= __SunGtEq(dt.year, 2, 22, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2016) and (dt.year <= 2022) and (dt >= __SunGtEq(dt.year, 2, 15, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2023) and (dt >= __SunGtEq(dt.year, 2, 22, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2024) and (dt.year <= 2025) and (dt >= __SunGtEq(dt.year, 2, 15, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2026) and (dt >= __SunGtEq(dt.year, 2, 22, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2027) and (dt.year <= 2033) and (dt >= __SunGtEq(dt.year, 2, 15, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2034) and (dt >= __SunGtEq(dt.year, 2, 22, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2035) and (dt.year <= 2036) and (dt >= __SunGtEq(dt.year, 2, 15, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2037) and (dt >= __SunGtEq(dt.year, 2, 22, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2038) and (dt >= __SunGtEq(dt.year, 2, 15, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Hond(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1987) and (dt.year <= 1988) and (dt >= __SunGtEq(dt.year, 5, 1, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1987) and (dt.year <= 1988) and (dt >= __lastSun(dt.year, 9, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2006) and (dt >= __SunGtEq(dt.year, 5, 1, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2006) and (dt >= __MonGtEq(dt.year, 8, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _AV(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1971) and (dt.year <= 1985) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1972) and (dt >= __lastSun(dt.year, 2, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1973) and (dt.year <= 1985) and (dt >= __SunGtEq(dt.year, 3, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1986) and (dt.year <= 1990) and (dt >= __SunGtEq(dt.year, 3, 15, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1986) and (dt.year <= 1987) and (dt >= __SunGtEq(dt.year, 10, 15, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1988) and (dt.year <= 1999) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1991) and (dt.year <= 1994) and (dt >= __SunGtEq(dt.year, 3, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1995) and (dt.year <= 2005) and (dt >= __lastSun(dt.year, 3, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2000) and (dt >= __lastSun(dt.year, 8, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2001) and (dt.year <= 2007) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2006) and (dt >= __SunGtEq(dt.year, 4, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2007) and (dt >= __lastSun(dt.year, 3, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2008) and (dt >= __SunGtEq(dt.year, 4, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2008) and (dt >= __SunGtEq(dt.year, 10, 1, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    return (s, l)
def _Bahamas(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1964) and (dt.year <= 1975) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1964) and (dt.year <= 1975) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    return (s, l)
def _Aus(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1917) and (dt >= datetime(dt.year, 1, 1, 0, 1)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1917) and (dt >= datetime(dt.year, 3, 25, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1942) and (dt >= datetime(dt.year, 1, 1, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1942) and (dt >= datetime(dt.year, 3, 29, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1942) and (dt >= datetime(dt.year, 9, 27, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1943) and (dt.year <= 1944) and (dt >= __lastSun(dt.year, 3, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1943) and (dt >= datetime(dt.year, 10, 3, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    return (s, l)
def _Holiday(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1992) and (dt.year <= 1993) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1993) and (dt.year <= 1994) and (dt >= __SunGtEq(dt.year, 3, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Indianapolis(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1941) and (dt >= datetime(dt.year, 6, 22, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1941) and (dt.year <= 1954) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1946) and (dt.year <= 1954) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    return (s, l)
def _Iran(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1978) and (dt.year <= 1980) and (dt >= datetime(dt.year, 3, 21, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1978) and (dt >= datetime(dt.year, 10, 21, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1979) and (dt >= datetime(dt.year, 9, 19, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1980) and (dt >= datetime(dt.year, 9, 23, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1991) and (dt >= datetime(dt.year, 5, 3, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1992) and (dt.year <= 1995) and (dt >= datetime(dt.year, 3, 22, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1991) and (dt.year <= 1995) and (dt >= datetime(dt.year, 9, 22, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1996) and (dt >= datetime(dt.year, 3, 21, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1996) and (dt >= datetime(dt.year, 9, 21, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1997) and (dt.year <= 1999) and (dt >= datetime(dt.year, 3, 22, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1997) and (dt.year <= 1999) and (dt >= datetime(dt.year, 9, 22, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2000) and (dt >= datetime(dt.year, 3, 21, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2000) and (dt >= datetime(dt.year, 9, 21, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2001) and (dt.year <= 2003) and (dt >= datetime(dt.year, 3, 22, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2001) and (dt.year <= 2003) and (dt >= datetime(dt.year, 9, 22, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2004) and (dt >= datetime(dt.year, 3, 21, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2004) and (dt >= datetime(dt.year, 9, 21, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2005) and (dt >= datetime(dt.year, 3, 22, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2005) and (dt >= datetime(dt.year, 9, 22, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2008) and (dt >= datetime(dt.year, 3, 21, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2008) and (dt >= datetime(dt.year, 9, 21, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2009) and (dt.year <= 2011) and (dt >= datetime(dt.year, 3, 22, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2009) and (dt.year <= 2011) and (dt >= datetime(dt.year, 9, 22, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2012) and (dt >= datetime(dt.year, 3, 21, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2012) and (dt >= datetime(dt.year, 9, 21, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2013) and (dt.year <= 2015) and (dt >= datetime(dt.year, 3, 22, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2013) and (dt.year <= 2015) and (dt >= datetime(dt.year, 9, 22, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2016) and (dt >= datetime(dt.year, 3, 21, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2016) and (dt >= datetime(dt.year, 9, 21, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2017) and (dt.year <= 2019) and (dt >= datetime(dt.year, 3, 22, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2017) and (dt.year <= 2019) and (dt >= datetime(dt.year, 9, 22, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2020) and (dt >= datetime(dt.year, 3, 21, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2020) and (dt >= datetime(dt.year, 9, 21, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2021) and (dt.year <= 2023) and (dt >= datetime(dt.year, 3, 22, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2021) and (dt.year <= 2023) and (dt >= datetime(dt.year, 9, 22, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2024) and (dt >= datetime(dt.year, 3, 21, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2024) and (dt >= datetime(dt.year, 9, 21, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2025) and (dt.year <= 2027) and (dt >= datetime(dt.year, 3, 22, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2025) and (dt.year <= 2027) and (dt >= datetime(dt.year, 9, 22, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2028) and (dt.year <= 2029) and (dt >= datetime(dt.year, 3, 21, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2028) and (dt.year <= 2029) and (dt >= datetime(dt.year, 9, 21, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2030) and (dt.year <= 2031) and (dt >= datetime(dt.year, 3, 22, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2030) and (dt.year <= 2031) and (dt >= datetime(dt.year, 9, 22, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2032) and (dt.year <= 2033) and (dt >= datetime(dt.year, 3, 21, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2032) and (dt.year <= 2033) and (dt >= datetime(dt.year, 9, 21, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2034) and (dt.year <= 2035) and (dt >= datetime(dt.year, 3, 22, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2034) and (dt.year <= 2035) and (dt >= datetime(dt.year, 9, 22, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2036) and (dt.year <= 2037) and (dt >= datetime(dt.year, 3, 21, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2036) and (dt.year <= 2037) and (dt >= datetime(dt.year, 9, 21, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Algeria(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1916) and (dt >= datetime(dt.year, 6, 14, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1916) and (dt.year <= 1919) and (dt >= __SunGtEq(dt.year, 10, 1, 23, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1917) and (dt >= datetime(dt.year, 3, 24, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1918) and (dt >= datetime(dt.year, 3, 9, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1919) and (dt >= datetime(dt.year, 3, 1, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1920) and (dt >= datetime(dt.year, 2, 14, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1920) and (dt >= datetime(dt.year, 10, 23, 23, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1921) and (dt >= datetime(dt.year, 3, 14, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1921) and (dt >= datetime(dt.year, 6, 21, 23, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1939) and (dt >= datetime(dt.year, 9, 11, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1939) and (dt >= datetime(dt.year, 11, 19, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1944) and (dt.year <= 1945) and (dt >= __MonGtEq(dt.year, 4, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1944) and (dt >= datetime(dt.year, 10, 8, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 9, 16, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1971) and (dt >= datetime(dt.year, 4, 25, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1971) and (dt >= datetime(dt.year, 9, 26, 23, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1977) and (dt >= datetime(dt.year, 5, 6, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1977) and (dt >= datetime(dt.year, 10, 21, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1978) and (dt >= datetime(dt.year, 3, 24, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1978) and (dt >= datetime(dt.year, 9, 22, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1980) and (dt >= datetime(dt.year, 4, 25, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1980) and (dt >= datetime(dt.year, 10, 31, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Shang(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1940) and (dt >= datetime(dt.year, 6, 3, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1940) and (dt.year <= 1941) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1941) and (dt >= datetime(dt.year, 3, 16, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    return (s, l)
def _NC(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1977) and (dt.year <= 1978) and (dt >= __SunGtEq(dt.year, 12, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1978) and (dt.year <= 1979) and (dt >= datetime(dt.year, 2, 27, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1996) and (dt >= datetime(dt.year, 12, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1997) and (dt >= datetime(dt.year, 3, 2, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _NZ(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1927) and (dt >= datetime(dt.year, 11, 6, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1928) and (dt >= datetime(dt.year, 3, 4, 2, 0)):
        l = 'M'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1928) and (dt.year <= 1933) and (dt >= __SunGtEq(dt.year, 10, 8, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=30)
    if (dt.year >= 1929) and (dt.year <= 1933) and (dt >= __SunGtEq(dt.year, 3, 15, 2, 0)):
        l = 'M'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1934) and (dt.year <= 1940) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'M'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1934) and (dt.year <= 1940) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=30)
    if (dt.year == 1946) and (dt >= datetime(dt.year, 1, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1974) and (dt >= __SunGtEq(dt.year, 11, 1, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1975) and (dt >= __lastSun(dt.year, 2, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1975) and (dt.year <= 1988) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1976) and (dt.year <= 1989) and (dt >= __SunGtEq(dt.year, 3, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1989) and (dt >= __SunGtEq(dt.year, 10, 8, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1990) and (dt.year <= 2006) and (dt >= __SunGtEq(dt.year, 10, 1, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1990) and (dt.year <= 2007) and (dt >= __SunGtEq(dt.year, 3, 15, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2007) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2008) and (dt >= __SunGtEq(dt.year, 4, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Chile(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1927) and (dt.year <= 1932) and (dt >= datetime(dt.year, 9, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1928) and (dt.year <= 1932) and (dt >= datetime(dt.year, 4, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1942) and (dt >= datetime(dt.year, 6, 1, 4, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1942) and (dt >= datetime(dt.year, 8, 1, 5, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1946) and (dt >= datetime(dt.year, 7, 15, 4, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1946) and (dt >= datetime(dt.year, 9, 1, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1947) and (dt >= datetime(dt.year, 4, 1, 4, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1968) and (dt >= datetime(dt.year, 11, 3, 4, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1969) and (dt >= datetime(dt.year, 3, 30, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1969) and (dt >= datetime(dt.year, 11, 23, 4, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1970) and (dt >= datetime(dt.year, 3, 29, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1971) and (dt >= datetime(dt.year, 3, 14, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1970) and (dt.year <= 1972) and (dt >= __SunGtEq(dt.year, 10, 9, 4, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1972) and (dt.year <= 1986) and (dt >= __SunGtEq(dt.year, 3, 9, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1973) and (dt >= datetime(dt.year, 9, 30, 4, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1974) and (dt.year <= 1987) and (dt >= __SunGtEq(dt.year, 10, 9, 4, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1987) and (dt >= datetime(dt.year, 4, 12, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1988) and (dt.year <= 1989) and (dt >= __SunGtEq(dt.year, 3, 9, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1988) and (dt >= __SunGtEq(dt.year, 10, 1, 4, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1989) and (dt >= __SunGtEq(dt.year, 10, 9, 4, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1990) and (dt >= datetime(dt.year, 3, 18, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1990) and (dt >= datetime(dt.year, 9, 16, 4, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1991) and (dt.year <= 1996) and (dt >= __SunGtEq(dt.year, 3, 9, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1991) and (dt.year <= 1997) and (dt >= __SunGtEq(dt.year, 10, 9, 4, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1997) and (dt >= datetime(dt.year, 3, 30, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1998) and (dt >= __SunGtEq(dt.year, 3, 9, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1998) and (dt >= datetime(dt.year, 9, 27, 4, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1999) and (dt >= datetime(dt.year, 4, 4, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1999) and (dt.year <= 2010) and (dt >= __SunGtEq(dt.year, 10, 9, 4, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2000) and (dt.year <= 2007) and (dt >= __SunGtEq(dt.year, 3, 9, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2008) and (dt >= datetime(dt.year, 3, 30, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2009) and (dt >= __SunGtEq(dt.year, 3, 9, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2010) and (dt >= __SunGtEq(dt.year, 4, 1, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2011) and (dt >= __SunGtEq(dt.year, 5, 2, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2011) and (dt >= __SunGtEq(dt.year, 8, 16, 4, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2012) and (dt >= __SunGtEq(dt.year, 4, 23, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2012) and (dt >= __SunGtEq(dt.year, 9, 2, 4, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    return (s, l)
def _Moncton(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1933) and (dt.year <= 1935) and (dt >= __SunGtEq(dt.year, 6, 8, 1, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1933) and (dt.year <= 1935) and (dt >= __SunGtEq(dt.year, 9, 8, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1936) and (dt.year <= 1938) and (dt >= __SunGtEq(dt.year, 6, 1, 1, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1936) and (dt.year <= 1938) and (dt >= __SunGtEq(dt.year, 9, 1, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1939) and (dt >= datetime(dt.year, 5, 27, 1, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1939) and (dt.year <= 1941) and (dt >= __SatGtEq(dt.year, 9, 21, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1940) and (dt >= datetime(dt.year, 5, 19, 1, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1941) and (dt >= datetime(dt.year, 5, 4, 1, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1946) and (dt.year <= 1972) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1946) and (dt.year <= 1956) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1957) and (dt.year <= 1972) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1993) and (dt.year <= 2006) and (dt >= __SunGtEq(dt.year, 4, 1, 0, 1)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1993) and (dt.year <= 2006) and (dt >= __lastSun(dt.year, 10, 0, 1)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Belgium(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1918) and (dt >= datetime(dt.year, 3, 9, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1918) and (dt.year <= 1919) and (dt >= __SatGtEq(dt.year, 10, 1, 23, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1919) and (dt >= datetime(dt.year, 3, 1, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1920) and (dt >= datetime(dt.year, 2, 14, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1920) and (dt >= datetime(dt.year, 10, 23, 23, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1921) and (dt >= datetime(dt.year, 3, 14, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1921) and (dt >= datetime(dt.year, 10, 25, 23, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1922) and (dt >= datetime(dt.year, 3, 25, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1922) and (dt.year <= 1927) and (dt >= __SatGtEq(dt.year, 10, 1, 23, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1923) and (dt >= datetime(dt.year, 4, 21, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1924) and (dt >= datetime(dt.year, 3, 29, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1925) and (dt >= datetime(dt.year, 4, 4, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1926) and (dt >= datetime(dt.year, 4, 17, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1927) and (dt >= datetime(dt.year, 4, 9, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1928) and (dt >= datetime(dt.year, 4, 14, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1928) and (dt.year <= 1938) and (dt >= __SunGtEq(dt.year, 10, 2, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1929) and (dt >= datetime(dt.year, 4, 21, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1930) and (dt >= datetime(dt.year, 4, 13, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1931) and (dt >= datetime(dt.year, 4, 19, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1932) and (dt >= datetime(dt.year, 4, 3, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1933) and (dt >= datetime(dt.year, 3, 26, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1934) and (dt >= datetime(dt.year, 4, 8, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1935) and (dt >= datetime(dt.year, 3, 31, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1936) and (dt >= datetime(dt.year, 4, 19, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1937) and (dt >= datetime(dt.year, 4, 4, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1938) and (dt >= datetime(dt.year, 3, 27, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1939) and (dt >= datetime(dt.year, 4, 16, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1939) and (dt >= datetime(dt.year, 11, 19, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1940) and (dt >= datetime(dt.year, 2, 25, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1944) and (dt >= datetime(dt.year, 9, 17, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 4, 2, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 9, 16, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1946) and (dt >= datetime(dt.year, 5, 19, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1946) and (dt >= datetime(dt.year, 10, 7, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Haiti(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1983) and (dt >= datetime(dt.year, 5, 8, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1984) and (dt.year <= 1987) and (dt >= __lastSun(dt.year, 4, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1983) and (dt.year <= 1987) and (dt >= __lastSun(dt.year, 10, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1988) and (dt.year <= 1997) and (dt >= __SunGtEq(dt.year, 4, 1, 1, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1988) and (dt.year <= 1997) and (dt >= __lastSun(dt.year, 10, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2005) and (dt.year <= 2006) and (dt >= __SunGtEq(dt.year, 4, 1, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2005) and (dt.year <= 2006) and (dt >= __lastSun(dt.year, 10, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2012) and (dt >= __SunGtEq(dt.year, 3, 8, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2012) and (dt >= __SunGtEq(dt.year, 11, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Iraq(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1982) and (dt >= datetime(dt.year, 5, 1, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1982) and (dt.year <= 1984) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1983) and (dt >= datetime(dt.year, 3, 31, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1984) and (dt.year <= 1985) and (dt >= datetime(dt.year, 4, 1, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1985) and (dt.year <= 1990) and (dt >= __lastSun(dt.year, 9, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1986) and (dt.year <= 1990) and (dt >= __lastSun(dt.year, 3, 1, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1991) and (dt.year <= 2007) and (dt >= datetime(dt.year, 4, 1, 3, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1991) and (dt.year <= 2007) and (dt >= datetime(dt.year, 10, 1, 3, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Toronto(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1919) and (dt >= datetime(dt.year, 3, 30, 23, 30)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1919) and (dt >= datetime(dt.year, 10, 26, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1920) and (dt >= datetime(dt.year, 5, 2, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1920) and (dt >= datetime(dt.year, 9, 26, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1921) and (dt >= datetime(dt.year, 5, 15, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1921) and (dt >= datetime(dt.year, 9, 15, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1922) and (dt.year <= 1923) and (dt >= __SunGtEq(dt.year, 5, 8, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1922) and (dt.year <= 1926) and (dt >= __SunGtEq(dt.year, 9, 15, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1924) and (dt.year <= 1927) and (dt >= __SunGtEq(dt.year, 5, 1, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1927) and (dt.year <= 1932) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1928) and (dt.year <= 1931) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1932) and (dt >= datetime(dt.year, 5, 1, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1933) and (dt.year <= 1940) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1933) and (dt >= datetime(dt.year, 10, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1934) and (dt.year <= 1939) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1945) and (dt.year <= 1946) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1946) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1947) and (dt.year <= 1949) and (dt >= __lastSun(dt.year, 4, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1947) and (dt.year <= 1948) and (dt >= __lastSun(dt.year, 9, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1949) and (dt >= __lastSun(dt.year, 11, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1950) and (dt.year <= 1973) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1950) and (dt >= __lastSun(dt.year, 11, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1951) and (dt.year <= 1956) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1957) and (dt.year <= 1973) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Pike(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1955) and (dt >= datetime(dt.year, 5, 1, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1955) and (dt.year <= 1960) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1956) and (dt.year <= 1964) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1961) and (dt.year <= 1964) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _CO(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1992) and (dt >= datetime(dt.year, 5, 3, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1993) and (dt >= datetime(dt.year, 4, 4, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Denmark(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1916) and (dt >= datetime(dt.year, 5, 14, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1916) and (dt >= datetime(dt.year, 9, 30, 23, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1940) and (dt >= datetime(dt.year, 5, 15, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 4, 2, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 8, 15, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1946) and (dt >= datetime(dt.year, 5, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1946) and (dt >= datetime(dt.year, 9, 1, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1947) and (dt >= datetime(dt.year, 5, 4, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1947) and (dt >= datetime(dt.year, 8, 10, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1948) and (dt >= datetime(dt.year, 5, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1948) and (dt >= datetime(dt.year, 8, 8, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _CA(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1948) and (dt >= datetime(dt.year, 3, 14, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1949) and (dt >= datetime(dt.year, 1, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1950) and (dt.year <= 1966) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1950) and (dt.year <= 1961) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1962) and (dt.year <= 1966) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Phil(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1936) and (dt >= datetime(dt.year, 11, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1937) and (dt >= datetime(dt.year, 2, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1954) and (dt >= datetime(dt.year, 4, 12, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1954) and (dt >= datetime(dt.year, 7, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1978) and (dt >= datetime(dt.year, 3, 22, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1978) and (dt >= datetime(dt.year, 9, 21, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Detroit(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1948) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1948) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1967) and (dt >= datetime(dt.year, 6, 14, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1967) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Morocco(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1939) and (dt >= datetime(dt.year, 9, 12, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1939) and (dt >= datetime(dt.year, 11, 19, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1940) and (dt >= datetime(dt.year, 2, 25, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 11, 18, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1950) and (dt >= datetime(dt.year, 6, 11, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1950) and (dt >= datetime(dt.year, 10, 29, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1967) and (dt >= datetime(dt.year, 6, 3, 12, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1967) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1974) and (dt >= datetime(dt.year, 6, 24, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1974) and (dt >= datetime(dt.year, 9, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1976) and (dt.year <= 1977) and (dt >= datetime(dt.year, 5, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1976) and (dt >= datetime(dt.year, 8, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1977) and (dt >= datetime(dt.year, 9, 28, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1978) and (dt >= datetime(dt.year, 6, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1978) and (dt >= datetime(dt.year, 8, 4, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2008) and (dt >= datetime(dt.year, 6, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2008) and (dt >= datetime(dt.year, 9, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2009) and (dt >= datetime(dt.year, 6, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2009) and (dt >= datetime(dt.year, 8, 21, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2010) and (dt >= datetime(dt.year, 5, 2, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2010) and (dt >= datetime(dt.year, 8, 8, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2011) and (dt >= datetime(dt.year, 4, 3, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2011) and (dt >= datetime(dt.year, 7, 31, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2012) and (dt.year <= 2013) and (dt >= __lastSun	(dt.year, 4, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2012) and (dt >= datetime(dt.year, 9, 30, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2012) and (dt >= datetime(dt.year, 7, 20, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2012) and (dt >= datetime(dt.year, 8, 20, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2013) and (dt >= datetime(dt.year, 7, 7, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2013) and (dt >= datetime(dt.year, 8, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2013) and (dt >= __lastSun	(dt.year, 10, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2014) and (dt.year <= 2022) and (dt >= __lastSun	(dt.year, 3, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2014) and (dt >= datetime(dt.year, 6, 28, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2014) and (dt >= datetime(dt.year, 8, 2, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2015) and (dt >= datetime(dt.year, 6, 13, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2015) and (dt >= datetime(dt.year, 7, 18, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2016) and (dt >= datetime(dt.year, 6, 4, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2016) and (dt >= datetime(dt.year, 7, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2017) and (dt >= datetime(dt.year, 5, 20, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2017) and (dt >= datetime(dt.year, 7, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2018) and (dt >= datetime(dt.year, 5, 12, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2018) and (dt >= datetime(dt.year, 6, 16, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2019) and (dt >= datetime(dt.year, 5, 4, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2019) and (dt >= datetime(dt.year, 6, 8, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2020) and (dt >= datetime(dt.year, 4, 18, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2020) and (dt >= datetime(dt.year, 5, 30, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2021) and (dt >= datetime(dt.year, 4, 10, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2021) and (dt >= datetime(dt.year, 5, 15, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2022) and (dt >= datetime(dt.year, 4, 2, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2022) and (dt >= datetime(dt.year, 5, 7, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2023) and (dt >= datetime(dt.year, 4, 22, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2024) and (dt >= datetime(dt.year, 4, 13, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2025) and (dt >= datetime(dt.year, 4, 5, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2026) and (dt >= __lastSun	(dt.year, 3, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2035) and (dt >= datetime(dt.year, 10, 27, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2036) and (dt >= datetime(dt.year, 10, 18, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2037) and (dt >= datetime(dt.year, 10, 10, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Namibia(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1994) and (dt >= __SunGtEq(dt.year, 9, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1995) and (dt >= __SunGtEq(dt.year, 4, 1, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _CR(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1979) and (dt.year <= 1980) and (dt >= __lastSun(dt.year, 2, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1979) and (dt.year <= 1980) and (dt >= __SunGtEq(dt.year, 6, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1991) and (dt.year <= 1992) and (dt >= __SatGtEq(dt.year, 1, 15, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1991) and (dt >= datetime(dt.year, 7, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1992) and (dt >= datetime(dt.year, 3, 15, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Belize(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1918) and (dt.year <= 1942) and (dt >= __SunGtEq(dt.year, 10, 2, 0, 0)):
        l = 'HD'
        s = timedelta(seconds=0, hours=0, minutes=30)
    if (dt.year >= 1919) and (dt.year <= 1943) and (dt >= __SunGtEq(dt.year, 2, 9, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1973) and (dt >= datetime(dt.year, 12, 5, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1974) and (dt >= datetime(dt.year, 2, 9, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1982) and (dt >= datetime(dt.year, 12, 18, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1983) and (dt >= datetime(dt.year, 2, 12, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Uruguay(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1923) and (dt >= datetime(dt.year, 10, 2, 0, 0)):
        l = 'HS'
        s = timedelta(seconds=0, hours=0, minutes=30)
    if (dt.year >= 1924) and (dt.year <= 1926) and (dt >= datetime(dt.year, 4, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1924) and (dt.year <= 1925) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = 'HS'
        s = timedelta(seconds=0, hours=0, minutes=30)
    if (dt.year >= 1933) and (dt.year <= 1935) and (dt >= __lastSun	(dt.year, 10, 0, 0)):
        l = 'HS'
        s = timedelta(seconds=0, hours=0, minutes=30)
    if (dt.year >= 1934) and (dt.year <= 1936) and (dt >= __SatGtEq(dt.year, 3, 25, 23, 30)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1936) and (dt >= datetime(dt.year, 11, 1, 0, 0)):
        l = 'HS'
        s = timedelta(seconds=0, hours=0, minutes=30)
    if (dt.year >= 1937) and (dt.year <= 1941) and (dt >= __lastSun	(dt.year, 3, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1937) and (dt.year <= 1940) and (dt >= __lastSun	(dt.year, 10, 0, 0)):
        l = 'HS'
        s = timedelta(seconds=0, hours=0, minutes=30)
    if (dt.year == 1941) and (dt >= datetime(dt.year, 8, 1, 0, 0)):
        l = 'HS'
        s = timedelta(seconds=0, hours=0, minutes=30)
    if (dt.year == 1942) and (dt >= datetime(dt.year, 1, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1942) and (dt >= datetime(dt.year, 12, 14, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1943) and (dt >= datetime(dt.year, 3, 14, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1959) and (dt >= datetime(dt.year, 5, 24, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1959) and (dt >= datetime(dt.year, 11, 15, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1960) and (dt >= datetime(dt.year, 1, 17, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1960) and (dt >= datetime(dt.year, 3, 6, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1965) and (dt.year <= 1967) and (dt >= __SunGtEq(dt.year, 4, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1965) and (dt >= datetime(dt.year, 9, 26, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1966) and (dt.year <= 1967) and (dt >= datetime(dt.year, 10, 31, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1968) and (dt.year <= 1970) and (dt >= datetime(dt.year, 5, 27, 0, 0)):
        l = 'HS'
        s = timedelta(seconds=0, hours=0, minutes=30)
    if (dt.year >= 1968) and (dt.year <= 1970) and (dt >= datetime(dt.year, 12, 2, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1972) and (dt >= datetime(dt.year, 4, 24, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1972) and (dt >= datetime(dt.year, 8, 15, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1974) and (dt >= datetime(dt.year, 3, 10, 0, 0)):
        l = 'HS'
        s = timedelta(seconds=0, hours=0, minutes=30)
    if (dt.year == 1974) and (dt >= datetime(dt.year, 12, 22, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1976) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1977) and (dt >= datetime(dt.year, 12, 4, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1978) and (dt >= datetime(dt.year, 4, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1979) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1980) and (dt >= datetime(dt.year, 5, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1987) and (dt >= datetime(dt.year, 12, 14, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1988) and (dt >= datetime(dt.year, 3, 14, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1988) and (dt >= datetime(dt.year, 12, 11, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1989) and (dt >= datetime(dt.year, 3, 12, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1989) and (dt >= datetime(dt.year, 10, 29, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1990) and (dt.year <= 1992) and (dt >= __SunGtEq(dt.year, 3, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1990) and (dt.year <= 1991) and (dt >= __SunGtEq(dt.year, 10, 21, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1992) and (dt >= datetime(dt.year, 10, 18, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1993) and (dt >= datetime(dt.year, 2, 28, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2004) and (dt >= datetime(dt.year, 9, 19, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2005) and (dt >= datetime(dt.year, 3, 27, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2005) and (dt >= datetime(dt.year, 10, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2006) and (dt >= datetime(dt.year, 3, 12, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2006) and (dt >= __SunGtEq(dt.year, 10, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2007) and (dt >= __SunGtEq(dt.year, 3, 8, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Czech(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1945) and (dt >= datetime(dt.year, 4, 8, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 11, 18, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1946) and (dt >= datetime(dt.year, 5, 6, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1946) and (dt.year <= 1949) and (dt >= __SunGtEq(dt.year, 10, 1, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1947) and (dt >= datetime(dt.year, 4, 20, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1948) and (dt >= datetime(dt.year, 4, 18, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1949) and (dt >= datetime(dt.year, 4, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    return (s, l)
def _NT_YK(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1918) and (dt >= datetime(dt.year, 4, 14, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1918) and (dt >= datetime(dt.year, 10, 27, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1919) and (dt >= datetime(dt.year, 5, 25, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1919) and (dt >= datetime(dt.year, 11, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1942) and (dt >= datetime(dt.year, 2, 9, 2, 0)):
        l = 'W'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 8, 14, 23, 0)):
        l = 'P'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 9, 30, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1965) and (dt >= __lastSun(dt.year, 4, 0, 0)):
        l = 'DD'
        s = timedelta(seconds=0, hours=2, minutes=0)
    if (dt.year == 1965) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1980) and (dt.year <= 1986) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1980) and (dt.year <= 2006) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1987) and (dt.year <= 2006) and (dt >= __SunGtEq(dt.year, 4, 1, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    return (s, l)
def _Egypt(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1940) and (dt >= datetime(dt.year, 7, 15, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1940) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1941) and (dt >= datetime(dt.year, 4, 15, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1941) and (dt >= datetime(dt.year, 9, 16, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1942) and (dt.year <= 1944) and (dt >= datetime(dt.year, 4, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1942) and (dt >= datetime(dt.year, 10, 27, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1943) and (dt.year <= 1945) and (dt >= datetime(dt.year, 11, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 4, 16, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1957) and (dt >= datetime(dt.year, 5, 10, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1957) and (dt.year <= 1958) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1958) and (dt >= datetime(dt.year, 5, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1959) and (dt.year <= 1981) and (dt >= datetime(dt.year, 5, 1, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1959) and (dt.year <= 1965) and (dt >= datetime(dt.year, 9, 30, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1966) and (dt.year <= 1994) and (dt >= datetime(dt.year, 10, 1, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1982) and (dt >= datetime(dt.year, 7, 25, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1983) and (dt >= datetime(dt.year, 7, 12, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1984) and (dt.year <= 1988) and (dt >= datetime(dt.year, 5, 1, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1989) and (dt >= datetime(dt.year, 5, 6, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1990) and (dt.year <= 1994) and (dt >= datetime(dt.year, 5, 1, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1995) and (dt.year <= 2010) and (dt >= __lastFri	(dt.year, 4, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1995) and (dt.year <= 2005) and (dt >= __lastThu(dt.year, 9, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2006) and (dt >= datetime(dt.year, 9, 21, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2007) and (dt >= __ThuGtEq(dt.year, 9, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2008) and (dt >= __lastThu(dt.year, 8, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2009) and (dt >= datetime(dt.year, 8, 20, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2010) and (dt >= datetime(dt.year, 8, 10, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2010) and (dt >= datetime(dt.year, 9, 9, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2010) and (dt >= __lastThu(dt.year, 9, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2014) and (dt >= datetime(dt.year, 5, 15, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2014) and (dt >= datetime(dt.year, 6, 26, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2014) and (dt >= datetime(dt.year, 7, 31, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2014) and (dt >= __lastThu(dt.year, 9, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2015) and (dt.year <= 2019) and (dt >= __lastFri	(dt.year, 4, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2015) and (dt >= datetime(dt.year, 6, 11, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2015) and (dt >= datetime(dt.year, 7, 23, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2016) and (dt >= datetime(dt.year, 6, 2, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2016) and (dt >= datetime(dt.year, 7, 7, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2017) and (dt >= datetime(dt.year, 5, 25, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2017) and (dt >= datetime(dt.year, 6, 29, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2018) and (dt >= datetime(dt.year, 5, 10, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2018) and (dt >= datetime(dt.year, 6, 14, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2019) and (dt >= datetime(dt.year, 5, 2, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2019) and (dt >= datetime(dt.year, 6, 6, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2020) and (dt >= datetime(dt.year, 5, 28, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2021) and (dt >= datetime(dt.year, 5, 13, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2022) and (dt >= datetime(dt.year, 5, 5, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2023) and (dt >= __lastFri	(dt.year, 4, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    return (s, l)
def _Halifax(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1916) and (dt >= datetime(dt.year, 4, 1, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1916) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1920) and (dt >= datetime(dt.year, 5, 9, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1920) and (dt >= datetime(dt.year, 8, 29, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1921) and (dt >= datetime(dt.year, 5, 6, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1921) and (dt.year <= 1922) and (dt >= datetime(dt.year, 9, 5, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1922) and (dt >= datetime(dt.year, 4, 30, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1923) and (dt.year <= 1925) and (dt >= __SunGtEq(dt.year, 5, 1, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1923) and (dt >= datetime(dt.year, 9, 4, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1924) and (dt >= datetime(dt.year, 9, 15, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1925) and (dt >= datetime(dt.year, 9, 28, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1926) and (dt >= datetime(dt.year, 5, 16, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1926) and (dt >= datetime(dt.year, 9, 13, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1927) and (dt >= datetime(dt.year, 5, 1, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1927) and (dt >= datetime(dt.year, 9, 26, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1928) and (dt.year <= 1931) and (dt >= __SunGtEq(dt.year, 5, 8, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1928) and (dt >= datetime(dt.year, 9, 9, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1929) and (dt >= datetime(dt.year, 9, 3, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1930) and (dt >= datetime(dt.year, 9, 15, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1931) and (dt.year <= 1932) and (dt >= __MonGtEq(dt.year, 9, 24, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1932) and (dt >= datetime(dt.year, 5, 1, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1933) and (dt >= datetime(dt.year, 4, 30, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1933) and (dt >= datetime(dt.year, 10, 2, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1934) and (dt >= datetime(dt.year, 5, 20, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1934) and (dt >= datetime(dt.year, 9, 16, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1935) and (dt >= datetime(dt.year, 6, 2, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1935) and (dt >= datetime(dt.year, 9, 30, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1936) and (dt >= datetime(dt.year, 6, 1, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1936) and (dt >= datetime(dt.year, 9, 14, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1937) and (dt.year <= 1938) and (dt >= __SunGtEq(dt.year, 5, 1, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1937) and (dt.year <= 1941) and (dt >= __MonGtEq(dt.year, 9, 24, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1939) and (dt >= datetime(dt.year, 5, 28, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1940) and (dt.year <= 1941) and (dt >= __SunGtEq(dt.year, 5, 1, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1946) and (dt.year <= 1949) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1946) and (dt.year <= 1949) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1951) and (dt.year <= 1954) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1951) and (dt.year <= 1954) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1956) and (dt.year <= 1959) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1956) and (dt.year <= 1959) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1962) and (dt.year <= 1973) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1962) and (dt.year <= 1973) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Cyprus(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1975) and (dt >= datetime(dt.year, 4, 13, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1975) and (dt >= datetime(dt.year, 10, 12, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1976) and (dt >= datetime(dt.year, 5, 15, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1976) and (dt >= datetime(dt.year, 10, 11, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1977) and (dt.year <= 1980) and (dt >= __SunGtEq(dt.year, 4, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1977) and (dt >= datetime(dt.year, 9, 25, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1978) and (dt >= datetime(dt.year, 10, 2, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1979) and (dt.year <= 1997) and (dt >= __lastSun(dt.year, 9, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1981) and (dt.year <= 1998) and (dt >= __lastSun(dt.year, 3, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    return (s, l)
def _EUAsia(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1981) and (dt >= __lastSun	(dt.year, 3, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1979) and (dt.year <= 1995) and (dt >= __lastSun	(dt.year, 9, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1996) and (dt >= __lastSun	(dt.year, 10, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Starke(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1947) and (dt.year <= 1961) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1947) and (dt.year <= 1954) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1955) and (dt.year <= 1956) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1957) and (dt.year <= 1958) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1959) and (dt.year <= 1961) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Italy(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1916) and (dt >= datetime(dt.year, 6, 3, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1916) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1917) and (dt >= datetime(dt.year, 4, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1917) and (dt >= datetime(dt.year, 9, 30, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1918) and (dt >= datetime(dt.year, 3, 10, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1918) and (dt.year <= 1919) and (dt >= __SunGtEq(dt.year, 10, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1919) and (dt >= datetime(dt.year, 3, 2, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1920) and (dt >= datetime(dt.year, 3, 21, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1920) and (dt >= datetime(dt.year, 9, 19, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1940) and (dt >= datetime(dt.year, 6, 15, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1944) and (dt >= datetime(dt.year, 9, 17, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 4, 2, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 9, 15, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1946) and (dt >= datetime(dt.year, 3, 17, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1946) and (dt >= datetime(dt.year, 10, 6, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1947) and (dt >= datetime(dt.year, 3, 16, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1947) and (dt >= datetime(dt.year, 10, 5, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1948) and (dt >= datetime(dt.year, 2, 29, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1948) and (dt >= datetime(dt.year, 10, 3, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1966) and (dt.year <= 1968) and (dt >= __SunGtEq(dt.year, 5, 22, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1966) and (dt.year <= 1969) and (dt >= __SunGtEq(dt.year, 9, 22, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1969) and (dt >= datetime(dt.year, 6, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1970) and (dt >= datetime(dt.year, 5, 31, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1970) and (dt >= __lastSun(dt.year, 9, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1971) and (dt.year <= 1972) and (dt >= __SunGtEq(dt.year, 5, 22, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1971) and (dt >= __lastSun(dt.year, 9, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1972) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1973) and (dt >= datetime(dt.year, 6, 3, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1973) and (dt.year <= 1974) and (dt >= __lastSun(dt.year, 9, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1974) and (dt >= datetime(dt.year, 5, 26, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1975) and (dt >= datetime(dt.year, 6, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1975) and (dt.year <= 1977) and (dt >= __lastSun(dt.year, 9, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1976) and (dt >= datetime(dt.year, 5, 30, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1977) and (dt.year <= 1979) and (dt >= __SunGtEq(dt.year, 5, 22, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1978) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1979) and (dt >= datetime(dt.year, 9, 30, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Chicago(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1920) and (dt >= datetime(dt.year, 6, 13, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1920) and (dt.year <= 1921) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1921) and (dt >= __lastSun(dt.year, 3, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1922) and (dt.year <= 1966) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1922) and (dt.year <= 1954) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1955) and (dt.year <= 1966) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Sudan(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1970) and (dt >= datetime(dt.year, 5, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1970) and (dt.year <= 1985) and (dt >= datetime(dt.year, 10, 15, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1971) and (dt >= datetime(dt.year, 4, 30, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1972) and (dt.year <= 1985) and (dt >= __lastSun(dt.year, 4, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    return (s, l)
def _Malta(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1973) and (dt >= datetime(dt.year, 3, 31, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1973) and (dt >= datetime(dt.year, 9, 29, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1974) and (dt >= datetime(dt.year, 4, 21, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1974) and (dt >= datetime(dt.year, 9, 16, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1975) and (dt.year <= 1979) and (dt >= __SunGtEq(dt.year, 4, 15, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1975) and (dt.year <= 1980) and (dt >= __SunGtEq(dt.year, 9, 15, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1980) and (dt >= datetime(dt.year, 3, 31, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    return (s, l)
def _Pulaski(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1946) and (dt.year <= 1960) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1946) and (dt.year <= 1954) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1955) and (dt.year <= 1956) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1957) and (dt.year <= 1960) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _DR(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1966) and (dt >= datetime(dt.year, 10, 30, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1967) and (dt >= datetime(dt.year, 2, 28, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1969) and (dt.year <= 1973) and (dt >= __lastSun(dt.year, 10, 0, 0)):
        l = 'HD'
        s = timedelta(seconds=0, hours=0, minutes=30)
    if (dt.year == 1970) and (dt >= datetime(dt.year, 2, 21, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1971) and (dt >= datetime(dt.year, 1, 20, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1972) and (dt.year <= 1974) and (dt >= datetime(dt.year, 1, 21, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _C_Eur(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1916) and (dt >= datetime(dt.year, 4, 30, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1916) and (dt >= datetime(dt.year, 10, 1, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1917) and (dt.year <= 1918) and (dt >= __MonGtEq(dt.year, 4, 15, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1917) and (dt.year <= 1918) and (dt >= __MonGtEq(dt.year, 9, 15, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1940) and (dt >= datetime(dt.year, 4, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1942) and (dt >= datetime(dt.year, 11, 2, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1943) and (dt >= datetime(dt.year, 3, 29, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1943) and (dt >= datetime(dt.year, 10, 4, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1944) and (dt.year <= 1945) and (dt >= __MonGtEq(dt.year, 4, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1944) and (dt >= datetime(dt.year, 10, 2, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 9, 16, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1977) and (dt.year <= 1980) and (dt >= __SunGtEq(dt.year, 4, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1977) and (dt >= __lastSun	(dt.year, 9, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1978) and (dt >= datetime(dt.year, 10, 1, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1979) and (dt.year <= 1995) and (dt >= __lastSun	(dt.year, 9, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1981) and (dt >= __lastSun	(dt.year, 3, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1996) and (dt >= __lastSun	(dt.year, 10, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Marengo(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1951) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1951) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1954) and (dt.year <= 1960) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1954) and (dt.year <= 1960) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Nic(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1979) and (dt.year <= 1980) and (dt >= __SunGtEq(dt.year, 3, 16, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1979) and (dt.year <= 1980) and (dt >= __MonGtEq(dt.year, 6, 23, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2005) and (dt >= datetime(dt.year, 4, 10, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2005) and (dt >= __SunGtEq(dt.year, 10, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2006) and (dt >= datetime(dt.year, 4, 30, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2006) and (dt >= __SunGtEq(dt.year, 10, 1, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Vincennes(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1946) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1946) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1953) and (dt.year <= 1954) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1953) and (dt.year <= 1959) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1955) and (dt >= datetime(dt.year, 5, 1, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1956) and (dt.year <= 1963) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1960) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1961) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1962) and (dt.year <= 1963) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _E_EurAsia(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1981) and (dt >= __lastSun	(dt.year, 3, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1979) and (dt.year <= 1995) and (dt >= __lastSun	(dt.year, 9, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1996) and (dt >= __lastSun	(dt.year, 10, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _LH(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1981) and (dt.year <= 1984) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1982) and (dt.year <= 1985) and (dt >= __SunGtEq(dt.year, 3, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1985) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=0, minutes=30)
    if (dt.year >= 1986) and (dt.year <= 1989) and (dt >= __SunGtEq(dt.year, 3, 15, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1986) and (dt >= datetime(dt.year, 10, 19, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=0, minutes=30)
    if (dt.year >= 1987) and (dt.year <= 1999) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=0, minutes=30)
    if (dt.year >= 1990) and (dt.year <= 1995) and (dt >= __SunGtEq(dt.year, 3, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1996) and (dt.year <= 2005) and (dt >= __lastSun(dt.year, 3, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2000) and (dt >= __lastSun(dt.year, 8, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=0, minutes=30)
    if (dt.year >= 2001) and (dt.year <= 2007) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=0, minutes=30)
    if (dt.year == 2006) and (dt >= __SunGtEq(dt.year, 4, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2007) and (dt >= __lastSun(dt.year, 3, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2008) and (dt >= __SunGtEq(dt.year, 4, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2008) and (dt >= __SunGtEq(dt.year, 10, 1, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=0, minutes=30)
    return (s, l)
def _Falk(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1937) and (dt.year <= 1938) and (dt >= __lastSun(dt.year, 9, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1938) and (dt.year <= 1942) and (dt >= __SunGtEq(dt.year, 3, 19, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1939) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1940) and (dt.year <= 1942) and (dt >= __lastSun(dt.year, 9, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1943) and (dt >= datetime(dt.year, 1, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1983) and (dt >= __lastSun(dt.year, 9, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1984) and (dt.year <= 1985) and (dt >= __lastSun(dt.year, 4, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1984) and (dt >= datetime(dt.year, 9, 16, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1985) and (dt.year <= 2000) and (dt >= __SunGtEq(dt.year, 9, 9, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1986) and (dt.year <= 2000) and (dt >= __SunGtEq(dt.year, 4, 16, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2001) and (dt.year <= 2010) and (dt >= __SunGtEq(dt.year, 4, 15, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2001) and (dt.year <= 2010) and (dt >= __SunGtEq(dt.year, 9, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    return (s, l)
def _W_Eur(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1977) and (dt.year <= 1980) and (dt >= __SunGtEq(dt.year, 4, 1, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1977) and (dt >= __lastSun	(dt.year, 9, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1978) and (dt >= datetime(dt.year, 10, 1, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1979) and (dt.year <= 1995) and (dt >= __lastSun	(dt.year, 9, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1981) and (dt >= __lastSun	(dt.year, 3, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1996) and (dt >= __lastSun	(dt.year, 10, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Vanc(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1918) and (dt >= datetime(dt.year, 4, 14, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1918) and (dt >= datetime(dt.year, 10, 27, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1942) and (dt >= datetime(dt.year, 2, 9, 2, 0)):
        l = 'W'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 8, 14, 23, 0)):
        l = 'P'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 9, 30, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1946) and (dt.year <= 1986) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1946) and (dt >= datetime(dt.year, 10, 13, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1947) and (dt.year <= 1961) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1962) and (dt.year <= 2006) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Germany(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1946) and (dt >= datetime(dt.year, 4, 14, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1946) and (dt >= datetime(dt.year, 10, 7, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1947) and (dt.year <= 1949) and (dt >= __SunGtEq(dt.year, 10, 1, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1947) and (dt >= datetime(dt.year, 4, 6, 3, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1947) and (dt >= datetime(dt.year, 5, 11, 2, 0)):
        l = 'M'
        s = timedelta(seconds=0, hours=2, minutes=0)
    if (dt.year == 1947) and (dt >= datetime(dt.year, 6, 29, 3, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1948) and (dt >= datetime(dt.year, 4, 18, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1949) and (dt >= datetime(dt.year, 4, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    return (s, l)
def _EgyptAsia(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1957) and (dt >= datetime(dt.year, 5, 10, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1957) and (dt.year <= 1958) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1958) and (dt >= datetime(dt.year, 5, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1959) and (dt.year <= 1967) and (dt >= datetime(dt.year, 5, 1, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1959) and (dt.year <= 1965) and (dt >= datetime(dt.year, 9, 30, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1966) and (dt >= datetime(dt.year, 10, 1, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _TC(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1979) and (dt.year <= 1986) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1979) and (dt.year <= 2006) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1987) and (dt.year <= 2006) and (dt >= __SunGtEq(dt.year, 4, 1, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2007) and (dt >= __SunGtEq(dt.year, 3, 8, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2007) and (dt >= __SunGtEq(dt.year, 11, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Dhaka(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 2009) and (dt >= datetime(dt.year, 6, 19, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2009) and (dt >= datetime(dt.year, 12, 31, 23, 59)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Thule(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1991) and (dt.year <= 1992) and (dt >= __lastSun(dt.year, 3, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1991) and (dt.year <= 1992) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1993) and (dt.year <= 2006) and (dt >= __SunGtEq(dt.year, 4, 1, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1993) and (dt.year <= 2006) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2007) and (dt >= __SunGtEq(dt.year, 3, 8, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2007) and (dt >= __SunGtEq(dt.year, 11, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Greece(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1932) and (dt >= datetime(dt.year, 7, 7, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1932) and (dt >= datetime(dt.year, 9, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1941) and (dt >= datetime(dt.year, 4, 7, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1942) and (dt >= datetime(dt.year, 11, 2, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1943) and (dt >= datetime(dt.year, 3, 30, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1943) and (dt >= datetime(dt.year, 10, 4, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1952) and (dt >= datetime(dt.year, 7, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1952) and (dt >= datetime(dt.year, 11, 2, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1975) and (dt >= datetime(dt.year, 4, 12, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1975) and (dt >= datetime(dt.year, 11, 26, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1976) and (dt >= datetime(dt.year, 4, 11, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1976) and (dt >= datetime(dt.year, 10, 10, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1977) and (dt.year <= 1978) and (dt >= __SunGtEq(dt.year, 4, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1977) and (dt >= datetime(dt.year, 9, 26, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1978) and (dt >= datetime(dt.year, 9, 24, 4, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1979) and (dt >= datetime(dt.year, 4, 1, 9, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1979) and (dt >= datetime(dt.year, 9, 29, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1980) and (dt >= datetime(dt.year, 4, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1980) and (dt >= datetime(dt.year, 9, 28, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _AN(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1971) and (dt.year <= 1985) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1972) and (dt >= datetime(dt.year, 2, 27, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1973) and (dt.year <= 1981) and (dt >= __SunGtEq(dt.year, 3, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1982) and (dt >= __SunGtEq(dt.year, 4, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1983) and (dt.year <= 1985) and (dt >= __SunGtEq(dt.year, 3, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1986) and (dt.year <= 1989) and (dt >= __SunGtEq(dt.year, 3, 15, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1986) and (dt >= datetime(dt.year, 10, 19, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1987) and (dt.year <= 1999) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1990) and (dt.year <= 1995) and (dt >= __SunGtEq(dt.year, 3, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1996) and (dt.year <= 2005) and (dt >= __lastSun(dt.year, 3, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2000) and (dt >= __lastSun(dt.year, 8, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2001) and (dt.year <= 2007) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2006) and (dt >= __SunGtEq(dt.year, 4, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2007) and (dt >= __lastSun(dt.year, 3, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2008) and (dt >= __SunGtEq(dt.year, 4, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2008) and (dt >= __SunGtEq(dt.year, 10, 1, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    return (s, l)
def _AQ(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1971) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1972) and (dt >= __lastSun(dt.year, 2, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1989) and (dt.year <= 1991) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1990) and (dt.year <= 1992) and (dt >= __SunGtEq(dt.year, 3, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _AS(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1971) and (dt.year <= 1985) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1986) and (dt >= datetime(dt.year, 10, 19, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1987) and (dt.year <= 2007) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1972) and (dt >= datetime(dt.year, 2, 27, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1973) and (dt.year <= 1985) and (dt >= __SunGtEq(dt.year, 3, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1986) and (dt.year <= 1990) and (dt >= __SunGtEq(dt.year, 3, 15, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1991) and (dt >= datetime(dt.year, 3, 3, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1992) and (dt >= datetime(dt.year, 3, 22, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1993) and (dt >= datetime(dt.year, 3, 7, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1994) and (dt >= datetime(dt.year, 3, 20, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1995) and (dt.year <= 2005) and (dt >= __lastSun(dt.year, 3, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2006) and (dt >= datetime(dt.year, 4, 2, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2007) and (dt >= __lastSun(dt.year, 3, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2008) and (dt >= __SunGtEq(dt.year, 4, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2008) and (dt >= __SunGtEq(dt.year, 10, 1, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    return (s, l)
def _Latvia(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1989) and (dt.year <= 1996) and (dt >= __lastSun	(dt.year, 3, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1989) and (dt.year <= 1996) and (dt >= __lastSun	(dt.year, 9, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _AT(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1967) and (dt >= __SunGtEq(dt.year, 10, 1, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1968) and (dt >= __lastSun(dt.year, 3, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1968) and (dt.year <= 1985) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1969) and (dt.year <= 1971) and (dt >= __SunGtEq(dt.year, 3, 8, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1972) and (dt >= __lastSun(dt.year, 2, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1973) and (dt.year <= 1981) and (dt >= __SunGtEq(dt.year, 3, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1982) and (dt.year <= 1983) and (dt >= __lastSun(dt.year, 3, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1984) and (dt.year <= 1986) and (dt >= __SunGtEq(dt.year, 3, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1986) and (dt >= __SunGtEq(dt.year, 10, 15, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1987) and (dt.year <= 1990) and (dt >= __SunGtEq(dt.year, 3, 15, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1987) and (dt >= __SunGtEq(dt.year, 10, 22, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1988) and (dt.year <= 1990) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1991) and (dt.year <= 1999) and (dt >= __SunGtEq(dt.year, 10, 1, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1991) and (dt.year <= 2005) and (dt >= __lastSun(dt.year, 3, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2000) and (dt >= __lastSun(dt.year, 8, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2001) and (dt >= __SunGtEq(dt.year, 10, 1, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2006) and (dt >= __SunGtEq(dt.year, 4, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2007) and (dt >= __lastSun(dt.year, 3, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2008) and (dt >= __SunGtEq(dt.year, 4, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _AW(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1974) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1975) and (dt >= __SunGtEq(dt.year, 3, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1983) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1984) and (dt >= __SunGtEq(dt.year, 3, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1991) and (dt >= datetime(dt.year, 11, 17, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1992) and (dt >= __SunGtEq(dt.year, 3, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2006) and (dt >= datetime(dt.year, 12, 3, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2007) and (dt.year <= 2009) and (dt >= __lastSun(dt.year, 3, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2007) and (dt.year <= 2008) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    return (s, l)
def _Japan(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1948) and (dt >= __SunGtEq(dt.year, 5, 1, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1948) and (dt.year <= 1951) and (dt >= __SatGtEq(dt.year, 9, 8, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1949) and (dt >= __SunGtEq(dt.year, 4, 1, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1950) and (dt.year <= 1951) and (dt >= __SunGtEq(dt.year, 5, 1, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    return (s, l)
def _Swiss(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1941) and (dt.year <= 1942) and (dt >= __MonGtEq(dt.year, 5, 1, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1941) and (dt.year <= 1942) and (dt >= __MonGtEq(dt.year, 10, 1, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Syria(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1920) and (dt.year <= 1923) and (dt >= __SunGtEq(dt.year, 4, 15, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1920) and (dt.year <= 1923) and (dt >= __SunGtEq(dt.year, 10, 1, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1962) and (dt >= datetime(dt.year, 4, 29, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1962) and (dt >= datetime(dt.year, 10, 1, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1963) and (dt.year <= 1965) and (dt >= datetime(dt.year, 5, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1963) and (dt >= datetime(dt.year, 9, 30, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1964) and (dt >= datetime(dt.year, 10, 1, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1965) and (dt >= datetime(dt.year, 9, 30, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1966) and (dt >= datetime(dt.year, 4, 24, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1966) and (dt.year <= 1976) and (dt >= datetime(dt.year, 10, 1, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1967) and (dt.year <= 1978) and (dt >= datetime(dt.year, 5, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1977) and (dt.year <= 1978) and (dt >= datetime(dt.year, 9, 1, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1983) and (dt.year <= 1984) and (dt >= datetime(dt.year, 4, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1983) and (dt.year <= 1984) and (dt >= datetime(dt.year, 10, 1, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1986) and (dt >= datetime(dt.year, 2, 16, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1986) and (dt >= datetime(dt.year, 10, 9, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1987) and (dt >= datetime(dt.year, 3, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1987) and (dt.year <= 1988) and (dt >= datetime(dt.year, 10, 31, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1988) and (dt >= datetime(dt.year, 3, 15, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1989) and (dt >= datetime(dt.year, 3, 31, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1989) and (dt >= datetime(dt.year, 10, 1, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1990) and (dt >= datetime(dt.year, 4, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1990) and (dt >= datetime(dt.year, 9, 30, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1991) and (dt >= datetime(dt.year, 4, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1991) and (dt.year <= 1992) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1992) and (dt >= datetime(dt.year, 4, 8, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1993) and (dt >= datetime(dt.year, 3, 26, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1993) and (dt >= datetime(dt.year, 9, 25, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1994) and (dt.year <= 1996) and (dt >= datetime(dt.year, 4, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1994) and (dt.year <= 2005) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1997) and (dt.year <= 1998) and (dt >= __lastMon(dt.year, 3, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1999) and (dt.year <= 2006) and (dt >= datetime(dt.year, 4, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2006) and (dt >= datetime(dt.year, 9, 22, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2007) and (dt >= __lastFri(dt.year, 3, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2007) and (dt >= __FriGtEq(dt.year, 11, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2008) and (dt >= __FriGtEq(dt.year, 4, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2008) and (dt >= datetime(dt.year, 11, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2009) and (dt >= __lastFri(dt.year, 3, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2010) and (dt.year <= 2011) and (dt >= __FriGtEq(dt.year, 4, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2012) and (dt >= __lastFri(dt.year, 3, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2009) and (dt >= __lastFri(dt.year, 10, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _SA(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1942) and (dt.year <= 1943) and (dt >= __SunGtEq(dt.year, 9, 15, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1943) and (dt.year <= 1944) and (dt >= __SunGtEq(dt.year, 3, 15, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Mexico(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1939) and (dt >= datetime(dt.year, 2, 5, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1939) and (dt >= datetime(dt.year, 6, 25, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1940) and (dt >= datetime(dt.year, 12, 9, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1941) and (dt >= datetime(dt.year, 4, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1943) and (dt >= datetime(dt.year, 12, 16, 0, 0)):
        l = 'W'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1944) and (dt >= datetime(dt.year, 5, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1950) and (dt >= datetime(dt.year, 2, 12, 0, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1950) and (dt >= datetime(dt.year, 7, 30, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1996) and (dt.year <= 2000) and (dt >= __SunGtEq(dt.year, 4, 1, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1996) and (dt.year <= 2000) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 2001) and (dt >= __SunGtEq(dt.year, 5, 1, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2001) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2002) and (dt >= __SunGtEq(dt.year, 4, 1, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2002) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Tunisia(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1939) and (dt >= datetime(dt.year, 4, 15, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1939) and (dt >= datetime(dt.year, 11, 18, 23, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1940) and (dt >= datetime(dt.year, 2, 25, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1941) and (dt >= datetime(dt.year, 10, 6, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1942) and (dt >= datetime(dt.year, 3, 9, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1942) and (dt >= datetime(dt.year, 11, 2, 3, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1943) and (dt >= datetime(dt.year, 3, 29, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1943) and (dt >= datetime(dt.year, 4, 17, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1943) and (dt >= datetime(dt.year, 4, 25, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1943) and (dt >= datetime(dt.year, 10, 4, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1944) and (dt.year <= 1945) and (dt >= __MonGtEq(dt.year, 4, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1944) and (dt >= datetime(dt.year, 10, 8, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 9, 16, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1977) and (dt >= datetime(dt.year, 4, 30, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1977) and (dt >= datetime(dt.year, 9, 24, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1978) and (dt >= datetime(dt.year, 5, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1978) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1988) and (dt >= datetime(dt.year, 6, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1988) and (dt.year <= 1990) and (dt >= __lastSun	(dt.year, 9, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1989) and (dt >= datetime(dt.year, 3, 26, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1990) and (dt >= datetime(dt.year, 5, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2005) and (dt >= datetime(dt.year, 5, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 2005) and (dt >= datetime(dt.year, 9, 30, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2006) and (dt.year <= 2008) and (dt >= __lastSun	(dt.year, 3, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 2006) and (dt.year <= 2008) and (dt >= __lastSun	(dt.year, 10, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _SovietZone(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1945) and (dt >= datetime(dt.year, 5, 24, 2, 0)):
        l = 'M'
        s = timedelta(seconds=0, hours=2, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 9, 24, 3, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 11, 18, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Edm(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1918) and (dt.year <= 1919) and (dt >= __SunGtEq(dt.year, 4, 8, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1918) and (dt >= datetime(dt.year, 10, 27, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1919) and (dt >= datetime(dt.year, 5, 27, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1920) and (dt.year <= 1923) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1920) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1921) and (dt.year <= 1923) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1942) and (dt >= datetime(dt.year, 2, 9, 2, 0)):
        l = 'W'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1945) and (dt >= datetime(dt.year, 8, 14, 23, 0)):
        l = 'P'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1945) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1947) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1947) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1967) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1967) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1969) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1969) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1972) and (dt.year <= 1986) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1972) and (dt.year <= 2006) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Iceland(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 1917) and (dt.year <= 1918) and (dt >= datetime(dt.year, 2, 19, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1917) and (dt >= datetime(dt.year, 10, 21, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1918) and (dt >= datetime(dt.year, 11, 16, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1939) and (dt >= datetime(dt.year, 4, 29, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1939) and (dt >= datetime(dt.year, 11, 29, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1940) and (dt >= datetime(dt.year, 2, 25, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1940) and (dt >= datetime(dt.year, 11, 3, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1941) and (dt >= datetime(dt.year, 3, 2, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1941) and (dt >= datetime(dt.year, 11, 2, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1942) and (dt >= datetime(dt.year, 3, 8, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1942) and (dt >= datetime(dt.year, 10, 25, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1943) and (dt.year <= 1946) and (dt >= __SunGtEq(dt.year, 3, 1, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1943) and (dt.year <= 1948) and (dt >= __SunGtEq(dt.year, 10, 22, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1947) and (dt.year <= 1967) and (dt >= __SunGtEq(dt.year, 4, 1, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1949) and (dt >= datetime(dt.year, 10, 30, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1950) and (dt.year <= 1966) and (dt >= __SunGtEq(dt.year, 10, 22, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1967) and (dt >= datetime(dt.year, 10, 29, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _SanLuis(dt):
    s = timedelta()
    l = 'S'
    if (dt.year >= 2008) and (dt.year <= 2009) and (dt >= __SunGtEq(dt.year, 3, 8, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 2007) and (dt.year <= 2008) and (dt >= __SunGtEq(dt.year, 10, 8, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    return (s, l)
def _Menominee(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1946) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1946) and (dt >= __lastSun(dt.year, 9, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1966) and (dt >= __lastSun(dt.year, 4, 2, 0)):
        l = 'D'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1966) and (dt >= __lastSun(dt.year, 10, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=0, minutes=0)
    return (s, l)
def _Port(dt):
    s = timedelta()
    l = 'S'
    if (dt.year == 1916) and (dt >= datetime(dt.year, 6, 17, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1916) and (dt >= datetime(dt.year, 11, 1, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1917) and (dt >= datetime(dt.year, 2, 28, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1917) and (dt.year <= 1921) and (dt >= datetime(dt.year, 10, 14, 23, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1918) and (dt >= datetime(dt.year, 3, 1, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1919) and (dt >= datetime(dt.year, 2, 28, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1920) and (dt >= datetime(dt.year, 2, 29, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1921) and (dt >= datetime(dt.year, 2, 28, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1924) and (dt >= datetime(dt.year, 4, 16, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1924) and (dt >= datetime(dt.year, 10, 14, 23, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1926) and (dt >= datetime(dt.year, 4, 17, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1926) and (dt.year <= 1929) and (dt >= __SatGtEq(dt.year, 10, 1, 23, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1927) and (dt >= datetime(dt.year, 4, 9, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1928) and (dt >= datetime(dt.year, 4, 14, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1929) and (dt >= datetime(dt.year, 4, 20, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1931) and (dt >= datetime(dt.year, 4, 18, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1931) and (dt.year <= 1932) and (dt >= __SatGtEq(dt.year, 10, 1, 23, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1932) and (dt >= datetime(dt.year, 4, 2, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1934) and (dt >= datetime(dt.year, 4, 7, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1934) and (dt.year <= 1938) and (dt >= __SatGtEq(dt.year, 10, 1, 23, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1935) and (dt >= datetime(dt.year, 3, 30, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1936) and (dt >= datetime(dt.year, 4, 18, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1937) and (dt >= datetime(dt.year, 4, 3, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1938) and (dt >= datetime(dt.year, 3, 26, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1939) and (dt >= datetime(dt.year, 4, 15, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1939) and (dt >= datetime(dt.year, 11, 18, 23, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1940) and (dt >= datetime(dt.year, 2, 24, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1940) and (dt.year <= 1941) and (dt >= datetime(dt.year, 10, 5, 23, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1941) and (dt >= datetime(dt.year, 4, 5, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1942) and (dt.year <= 1945) and (dt >= __SatGtEq(dt.year, 3, 8, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1942) and (dt >= datetime(dt.year, 4, 25, 22, 0)):
        l = 'M'
        s = timedelta(seconds=0, hours=2, minutes=0)
    if (dt.year == 1942) and (dt >= datetime(dt.year, 8, 15, 22, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1942) and (dt.year <= 1945) and (dt >= __SatGtEq(dt.year, 10, 24, 23, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1943) and (dt >= datetime(dt.year, 4, 17, 22, 0)):
        l = 'M'
        s = timedelta(seconds=0, hours=2, minutes=0)
    if (dt.year >= 1943) and (dt.year <= 1945) and (dt >= __SatGtEq(dt.year, 8, 25, 22, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1944) and (dt.year <= 1945) and (dt >= __SatGtEq(dt.year, 4, 21, 22, 0)):
        l = 'M'
        s = timedelta(seconds=0, hours=2, minutes=0)
    if (dt.year == 1946) and (dt >= __SatGtEq(dt.year, 4, 1, 23, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1946) and (dt >= __SatGtEq(dt.year, 10, 1, 23, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1947) and (dt.year <= 1949) and (dt >= __SunGtEq(dt.year, 4, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1947) and (dt.year <= 1949) and (dt >= __SunGtEq(dt.year, 10, 1, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1951) and (dt.year <= 1965) and (dt >= __SunGtEq(dt.year, 4, 1, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1951) and (dt.year <= 1965) and (dt >= __SunGtEq(dt.year, 10, 1, 2, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1977) and (dt >= datetime(dt.year, 3, 27, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1977) and (dt >= datetime(dt.year, 9, 25, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1978) and (dt.year <= 1979) and (dt >= __SunGtEq(dt.year, 4, 1, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1978) and (dt >= datetime(dt.year, 10, 1, 0, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year >= 1979) and (dt.year <= 1982) and (dt >= __lastSun	(dt.year, 9, 1, 0)):
        l = '-'
        s = timedelta(seconds=0, hours=0, minutes=0)
    if (dt.year == 1980) and (dt >= __lastSun	(dt.year, 3, 0, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year >= 1981) and (dt.year <= 1982) and (dt >= __lastSun	(dt.year, 3, 1, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    if (dt.year == 1983) and (dt >= __lastSun	(dt.year, 3, 2, 0)):
        l = 'S'
        s = timedelta(seconds=0, hours=1, minutes=0)
    return (s, l)
# Zones sets
class Atlantic_Canary(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1922,3,1,0,0)):
            offset = timedelta(seconds=0, hours=-1, minutes=-1)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1946,9,30,1,0)):
            offset = timedelta(seconds=0, hours=-1, minutes=0)
            rule = None
            format = 'CANT'
        elif(dt < datetime(1980,4,1,6,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = None
            format = 'WET'
        elif(dt < datetime(1980,9,28,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = _rule_constant_1hour
            format = 'WEST'
        else:
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = _EU
            format = 'WE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Australia_Melbourne(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1895,2,1,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=39)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1971,1,1,0,0)):
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = _Aus
            format = 'AE%sT'
        else:
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = _AV
            format = 'AE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Etc_GMTplus9(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=-9, minutes=0)
        rule = None
        format = 'GMT+9'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Etc_GMTplus8(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=-8, minutes=0)
        rule = None
        format = 'GMT+8'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Lisbon(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1884,1,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=-36)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1912,1,1,1,0)):
            offset = timedelta(seconds=0, hours=0, minutes=-36)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1966,4,1,3,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = _Port
            format = 'WE%sT'
        elif(dt < datetime(1976,9,26,1,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = None
            format = 'CET'
        elif(dt < datetime(1983,9,25,1,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = _Port
            format = 'WE%sT'
        elif(dt < datetime(1992,9,27,1,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = _W_Eur
            format = 'WE%sT'
        elif(dt < datetime(1996,3,31,1,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _EU
            format = 'CE%sT'
        else:
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = _EU
            format = 'WE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Etc_GMTplus3(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=-3, minutes=0)
        rule = None
        format = 'GMT+3'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Etc_GMTplus2(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=-2, minutes=0)
        rule = None
        format = 'GMT+2'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Etc_GMTplus1(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=-1, minutes=0)
        rule = None
        format = 'GMT+1'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Nipigon(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1895,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=-53)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1940,9,29,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _Canada
            format = 'E%sT'
        elif(dt < datetime(1942,2,1,9,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _rule_constant_1hour
            format = 'EDT'
        else:
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _Canada
            format = 'E%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Etc_GMTplus6(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=-6, minutes=0)
        rule = None
        format = 'GMT+6'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Etc_GMTplus5(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=-5, minutes=0)
        rule = None
        format = 'GMT+5'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Etc_GMTplus4(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=-4, minutes=0)
        rule = None
        format = 'GMT+4'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Indian_Reunion(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1911,6,1,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=41)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = None
            format = 'RET'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Dhaka(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1890,1,1,0,0)):
            offset = timedelta(seconds=0, hours=6, minutes=1)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1941,10,1,0,0)):
            offset = timedelta(seconds=0, hours=5, minutes=53)
            rule = None
            format = 'HMT'
        elif(dt < datetime(1942,5,15,0,0)):
            offset = timedelta(seconds=0, hours=6, minutes=30)
            rule = None
            format = 'BURT'
        elif(dt < datetime(1942,9,1,0,0)):
            offset = timedelta(seconds=0, hours=5, minutes=30)
            rule = None
            format = 'IST'
        elif(dt < datetime(1951,9,30,0,0)):
            offset = timedelta(seconds=0, hours=6, minutes=30)
            rule = None
            format = 'BURT'
        elif(dt < datetime(1971,3,26,0,0)):
            offset = timedelta(seconds=0, hours=6, minutes=0)
            rule = None
            format = 'DACT'
        elif(dt < datetime(2009,1,1,0,0)):
            offset = timedelta(seconds=0, hours=6, minutes=0)
            rule = None
            format = 'BDT'
        else:
            offset = timedelta(seconds=0, hours=6, minutes=0)
            rule = _Dhaka
            format = 'BD%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Phoenix(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1883,11,18,11,31)):
            offset = timedelta(seconds=0, hours=-7, minutes=-28)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1944,1,1,1,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = _US
            format = 'M%sT'
        elif(dt < datetime(1944,4,1,1,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = None
            format = 'MST'
        elif(dt < datetime(1944,10,1,1,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = _US
            format = 'M%sT'
        elif(dt < datetime(1967,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = None
            format = 'MST'
        elif(dt < datetime(1968,3,21,0,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = _US
            format = 'M%sT'
        else:
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = None
            format = 'MST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Kaliningrad(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1893,4,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=22)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1945,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _C_Eur
            format = 'CE%sT'
        elif(dt < datetime(1946,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _Poland
            format = 'CE%sT'
        elif(dt < datetime(1991,3,31,2,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = _Russia
            format = 'MSK/MSD'
        elif(dt < datetime(2011,3,27,2,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _Russia
            format = 'EE%sT'
        elif(dt < datetime(2014,10,26,2,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'FET'
        else:
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'EET'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Etc_GMTplus7(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=-7, minutes=0)
        rule = None
        format = 'GMT+7'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Mazatlan(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1921,12,31,23,54)):
            offset = timedelta(seconds=0, hours=-7, minutes=-5)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1927,6,10,23,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = None
            format = 'MST'
        elif(dt < datetime(1930,11,15,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = None
            format = 'CST'
        elif(dt < datetime(1931,5,1,1,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = None
            format = 'MST'
        elif(dt < datetime(1931,10,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = None
            format = 'CST'
        elif(dt < datetime(1932,4,1,1,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = None
            format = 'MST'
        elif(dt < datetime(1942,4,24,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = None
            format = 'CST'
        elif(dt < datetime(1949,1,14,0,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = None
            format = 'MST'
        elif(dt < datetime(1970,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = None
            format = 'PST'
        else:
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = _Mexico
            format = 'M%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Paris(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1891,3,15,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=9)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1911,3,11,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=9)
            rule = None
            format = 'PMT'
        elif(dt < datetime(1940,6,14,23,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = _France
            format = 'WE%sT'
        elif(dt < datetime(1944,8,25,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _C_Eur
            format = 'CE%sT'
        elif(dt < datetime(1945,9,16,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = _France
            format = 'WE%sT'
        elif(dt < datetime(1977,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _France
            format = 'CE%sT'
        else:
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _EU
            format = 'CE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Stockholm(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1879,1,1,1,0)):
            offset = timedelta(seconds=0, hours=1, minutes=12)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1900,1,1,1,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = None
            format = 'SET'
        elif(dt < datetime(1916,5,14,23,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = None
            format = 'CET'
        elif(dt < datetime(1916,10,1,1,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _rule_constant_1hour
            format = 'CEST'
        elif(dt < datetime(1980,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = None
            format = 'CET'
        else:
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _EU
            format = 'CE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Pacific_Fiji(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1915,10,26,0,0)):
            offset = timedelta(seconds=0, hours=11, minutes=55)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=12, minutes=0)
            rule = _Fiji
            format = 'FJ%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Pacific_Apia(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1879,7,1,5,0)):
            offset = timedelta(seconds=0, hours=12, minutes=33)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1911,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-11, minutes=-26)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1950,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-11, minutes=-30)
            rule = None
            format = 'WSST'
        elif(dt < datetime(2011,12,29,24,0)):
            offset = timedelta(seconds=0, hours=-11, minutes=0)
            rule = _WS
            format = 'S%sT'
        else:
            offset = timedelta(seconds=0, hours=13, minutes=0)
            rule = _WS
            format = 'WS%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Miquelon(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1911,5,15,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-44)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1980,5,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'AST'
        elif(dt < datetime(1987,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'PMST'
        else:
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Canada
            format = 'PM%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Pacific_Pago_Pago(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1879,7,1,5,0)):
            offset = timedelta(seconds=0, hours=12, minutes=37)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1911,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-11, minutes=-22)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1967,4,1,0,0)):
            offset = timedelta(seconds=0, hours=-11, minutes=0)
            rule = None
            format = 'NST'
        elif(dt < datetime(1983,11,30,0,0)):
            offset = timedelta(seconds=0, hours=-11, minutes=0)
            rule = None
            format = 'BST'
        else:
            offset = timedelta(seconds=0, hours=-11, minutes=0)
            rule = None
            format = 'SST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Rangoon(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1880,1,1,0,0)):
            offset = timedelta(seconds=0, hours=6, minutes=24)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1920,1,1,0,0)):
            offset = timedelta(seconds=0, hours=6, minutes=24)
            rule = None
            format = 'RMT'
        elif(dt < datetime(1942,5,1,0,0)):
            offset = timedelta(seconds=0, hours=6, minutes=30)
            rule = None
            format = 'BURT'
        elif(dt < datetime(1945,5,3,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = None
            format = 'JST'
        else:
            offset = timedelta(seconds=0, hours=6, minutes=30)
            rule = None
            format = 'MMT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Mexico_City(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1922,1,1,1,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=-36)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1927,6,10,23,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = None
            format = 'MST'
        elif(dt < datetime(1930,11,15,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = None
            format = 'CST'
        elif(dt < datetime(1931,5,1,1,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = None
            format = 'MST'
        elif(dt < datetime(1931,10,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = None
            format = 'CST'
        elif(dt < datetime(1932,4,1,1,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = None
            format = 'MST'
        elif(dt < datetime(2001,9,30,2,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Mexico
            format = 'C%sT'
        elif(dt < datetime(2002,2,20,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = None
            format = 'CST'
        else:
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Mexico
            format = 'C%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Puerto_Rico(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1899,3,28,12,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-24)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1942,5,1,3,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'AST'
        elif(dt < datetime(1946,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _US
            format = 'A%sT'
        else:
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'AST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Indian_Mauritius(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1907,1,1,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=50)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = _Mauritius
            format = 'MU%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Berlin(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1893,4,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=53)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1945,5,24,2,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _C_Eur
            format = 'CE%sT'
        elif(dt < datetime(1946,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _SovietZone
            format = 'CE%sT'
        elif(dt < datetime(1980,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _Germany
            format = 'CE%sT'
        else:
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _EU
            format = 'CE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Zurich(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1853,7,16,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=34)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1894,6,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=29)
            rule = None
            format = 'BMT'
        elif(dt < datetime(1981,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _Swiss
            format = 'CE%sT'
        else:
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _EU
            format = 'CE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Casablanca(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1913,10,26,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=-30)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1984,3,16,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = _Morocco
            format = 'WE%sT'
        elif(dt < datetime(1986,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = None
            format = 'CET'
        else:
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = _Morocco
            format = 'WE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Antarctica_Macquarie(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1899,11,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = None
            format = 'zzz'
        elif(dt < datetime(1916,10,1,2,0)):
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = None
            format = 'AEST'
        elif(dt < datetime(1917,2,1,0,0)):
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = _rule_constant_1hour
            format = 'AEDT'
        elif(dt < datetime(1919,4,1,0,0)):
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = _Aus
            format = 'AE%sT'
        elif(dt < datetime(1948,3,25,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = None
            format = 'zzz'
        elif(dt < datetime(1967,1,1,0,0)):
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = _Aus
            format = 'AE%sT'
        elif(dt < datetime(2010,4,4,3,0)):
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = _AT
            format = 'AE%sT'
        else:
            offset = timedelta(seconds=0, hours=11, minutes=0)
            rule = None
            format = 'MIST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Krasnoyarsk(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1920,1,1,6,0)):
            offset = timedelta(seconds=0, hours=6, minutes=11)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1930,6,21,0,0)):
            offset = timedelta(seconds=0, hours=6, minutes=0)
            rule = None
            format = 'KRAT'
        elif(dt < datetime(1991,3,31,2,0)):
            offset = timedelta(seconds=0, hours=7, minutes=0)
            rule = _Russia
            format = 'KRA%sT'
        elif(dt < datetime(1992,1,19,2,0)):
            offset = timedelta(seconds=0, hours=6, minutes=0)
            rule = _Russia
            format = 'KRA%sT'
        elif(dt < datetime(2011,3,27,2,0)):
            offset = timedelta(seconds=0, hours=7, minutes=0)
            rule = _Russia
            format = 'KRA%sT'
        elif(dt < datetime(2014,10,26,2,0)):
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = None
            format = 'KRAT'
        else:
            offset = timedelta(seconds=0, hours=7, minutes=0)
            rule = None
            format = 'KRAT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Atlantic_Bermuda(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1930,1,1,1,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-19)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1974,4,28,2,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'AST'
        elif(dt < datetime(1976,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Canada
            format = 'A%sT'
        else:
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _US
            format = 'A%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Australia_Currie(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1895,9,1,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=35)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1916,10,1,2,0)):
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = None
            format = 'AEST'
        elif(dt < datetime(1917,2,1,0,0)):
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = _rule_constant_1hour
            format = 'AEDT'
        elif(dt < datetime(1971,7,1,0,0)):
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = _Aus
            format = 'AE%sT'
        else:
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = _AT
            format = 'AE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Tehran(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1916,1,1,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=25)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1946,1,1,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=25)
            rule = None
            format = 'TMT'
        elif(dt < datetime(1977,11,1,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=30)
            rule = None
            format = 'IRST'
        elif(dt < datetime(1979,1,1,0,0)):
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = _Iran
            format = 'IR%sT'
        else:
            offset = timedelta(seconds=0, hours=3, minutes=30)
            rule = _Iran
            format = 'IR%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Baku(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1924,5,1,2,0)):
            offset = timedelta(seconds=0, hours=3, minutes=19)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1957,3,1,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'BAKT'
        elif(dt < datetime(1991,3,31,2,0)):
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = _RussiaAsia
            format = 'BAK%sT'
        elif(dt < datetime(1991,8,30,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = _rule_constant_1hour
            format = 'BAKST'
        elif(dt < datetime(1992,9,1,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = _RussiaAsia
            format = 'AZ%sT'
        elif(dt < datetime(1996,1,1,0,0)):
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = None
            format = 'AZT'
        elif(dt < datetime(1997,1,1,0,0)):
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = _EUAsia
            format = 'AZ%sT'
        else:
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = _Azer
            format = 'AZ%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Santarem(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1914,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-38)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1988,9,12,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Brazil
            format = 'AM%sT'
        elif(dt < datetime(2008,6,24,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'AMT'
        else:
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'BRT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Danmarkshavn(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1916,7,28,0,0)):
            offset = timedelta(seconds=0, hours=-1, minutes=-14)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1980,4,1,6,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'WGT'
        elif(dt < datetime(1996,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _EU
            format = 'WG%sT'
        else:
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = None
            format = 'GMT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Scoresbysund(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1916,7,28,0,0)):
            offset = timedelta(seconds=0, hours=-1, minutes=-27)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1980,4,1,6,0)):
            offset = timedelta(seconds=0, hours=-2, minutes=0)
            rule = None
            format = 'CGT'
        elif(dt < datetime(1981,3,29,0,0)):
            offset = timedelta(seconds=0, hours=-2, minutes=0)
            rule = _C_Eur
            format = 'CG%sT'
        else:
            offset = timedelta(seconds=0, hours=-1, minutes=0)
            rule = _EU
            format = 'EG%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Eirunepe(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1914,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-39)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1988,9,12,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _Brazil
            format = 'AC%sT'
        elif(dt < datetime(1993,9,28,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'ACT'
        elif(dt < datetime(1994,9,22,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _Brazil
            format = 'AC%sT'
        elif(dt < datetime(2008,6,24,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'ACT'
        elif(dt < datetime(2013,11,10,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'AMT'
        else:
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'ACT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Baghdad(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1890,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=57)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1918,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=57)
            rule = None
            format = 'BMT'
        elif(dt < datetime(1982,5,1,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'AST'
        else:
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = _Iraq
            format = 'A%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Monrovia(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1882,1,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=-43)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1919,3,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=-43)
            rule = None
            format = 'MMT'
        elif(dt < datetime(1972,5,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=-44)
            rule = None
            format = 'LRT'
        else:
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = None
            format = 'GMT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Vancouver(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1884,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=-12)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1987,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _Vanc
            format = 'P%sT'
        else:
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _Canada
            format = 'P%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Ho_Chi_Minh(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1906,6,1,9,0)):
            offset = timedelta(seconds=0, hours=7, minutes=6)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1911,3,11,0,1)):
            offset = timedelta(seconds=0, hours=7, minutes=6)
            rule = None
            format = 'SMT'
        elif(dt < datetime(1912,5,1,0,0)):
            offset = timedelta(seconds=0, hours=7, minutes=0)
            rule = None
            format = 'ICT'
        elif(dt < datetime(1931,5,1,0,0)):
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = None
            format = 'ICT'
        else:
            offset = timedelta(seconds=0, hours=7, minutes=0)
            rule = None
            format = 'ICT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Thimphu(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1947,8,15,0,0)):
            offset = timedelta(seconds=0, hours=5, minutes=58)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1987,10,1,0,0)):
            offset = timedelta(seconds=0, hours=5, minutes=30)
            rule = None
            format = 'IST'
        else:
            offset = timedelta(seconds=0, hours=6, minutes=0)
            rule = None
            format = 'BTT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Accra(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1918,1,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = _Ghana
            format = '%s'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Belize(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1912,4,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=-52)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Belize
            format = 'C%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Port_of_Spain(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1912,3,2,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-6)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'AST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Tashkent(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1924,5,1,2,0)):
            offset = timedelta(seconds=0, hours=4, minutes=37)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1930,6,21,0,0)):
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = None
            format = 'TAST'
        elif(dt < datetime(1991,3,31,2,0)):
            offset = timedelta(seconds=0, hours=6, minutes=0)
            rule = _RussiaAsia
            format = 'TAS%sT'
        elif(dt < datetime(1991,9,1,1,0)):
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = _RussiaAsia
            format = 'TAS%sT'
        elif(dt < datetime(1992,1,1,0,0)):
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = _RussiaAsia
            format = 'UZ%sT'
        else:
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = None
            format = 'UZT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Tokyo(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1887,12,31,15,0)):
            offset = timedelta(seconds=0, hours=9, minutes=18)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1896,1,1,1,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = None
            format = 'JST'
        elif(dt < datetime(1937,10,1,1,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = None
            format = 'JCST'
        else:
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = _Japan
            format = 'J%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Pacific_Kiritimati(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1901,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-10, minutes=-29)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1979,10,1,0,0)):
            offset = timedelta(seconds=0, hours=-10, minutes=-40)
            rule = None
            format = 'LINT'
        elif(dt < datetime(1995,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-10, minutes=0)
            rule = None
            format = 'LINT'
        else:
            offset = timedelta(seconds=0, hours=14, minutes=0)
            rule = None
            format = 'LINT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Australia_Sydney(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1895,2,1,0,0)):
            offset = timedelta(seconds=0, hours=10, minutes=4)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1971,1,1,0,0)):
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = _Aus
            format = 'AE%sT'
        else:
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = _AN
            format = 'AE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Riga(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1880,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=36)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1918,4,15,2,0)):
            offset = timedelta(seconds=0, hours=1, minutes=36)
            rule = None
            format = 'RMT'
        elif(dt < datetime(1918,9,16,3,0)):
            offset = timedelta(seconds=0, hours=1, minutes=36)
            rule = _rule_constant_1hour
            format = 'LST'
        elif(dt < datetime(1919,4,1,1,0)):
            offset = timedelta(seconds=0, hours=1, minutes=36)
            rule = None
            format = 'RMT'
        elif(dt < datetime(1919,5,22,3,0)):
            offset = timedelta(seconds=0, hours=1, minutes=36)
            rule = _rule_constant_1hour
            format = 'LST'
        elif(dt < datetime(1926,5,11,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=36)
            rule = None
            format = 'RMT'
        elif(dt < datetime(1940,8,1,5,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'EET'
        elif(dt < datetime(1941,7,1,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'MSK'
        elif(dt < datetime(1944,10,13,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _C_Eur
            format = 'CE%sT'
        elif(dt < datetime(1989,3,1,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = _Russia
            format = 'MSK/MSD'
        elif(dt < datetime(1989,9,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _rule_constant_1hour
            format = 'EEST'
        elif(dt < datetime(1997,1,21,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _Latvia
            format = 'EE%sT'
        elif(dt < datetime(2000,2,29,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _EU
            format = 'EE%sT'
        elif(dt < datetime(2001,1,1,2,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'EET'
        else:
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _EU
            format = 'EE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Dili(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1912,1,1,0,0)):
            offset = timedelta(seconds=0, hours=8, minutes=22)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1942,2,21,23,0)):
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = None
            format = 'TLT'
        elif(dt < datetime(1945,9,23,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = None
            format = 'JST'
        elif(dt < datetime(1976,5,1,3,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = None
            format = 'TLT'
        elif(dt < datetime(2000,9,17,0,0)):
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = None
            format = 'WITA'
        else:
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = None
            format = 'TLT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Mbabane(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1903,3,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=4)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'SAST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Oral(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1924,5,1,2,0)):
            offset = timedelta(seconds=0, hours=3, minutes=25)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1930,6,21,0,0)):
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = None
            format = 'URAT'
        elif(dt < datetime(1981,4,1,1,0)):
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = None
            format = 'URAT'
        elif(dt < datetime(1981,10,1,1,0)):
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = _rule_constant_1hour
            format = 'URAST'
        elif(dt < datetime(1982,4,1,1,0)):
            offset = timedelta(seconds=0, hours=6, minutes=0)
            rule = None
            format = 'URAT'
        elif(dt < datetime(1989,3,26,2,0)):
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = _RussiaAsia
            format = 'URA%sT'
        elif(dt < datetime(1991,1,1,0,0)):
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = _RussiaAsia
            format = 'URA%sT'
        elif(dt < datetime(1991,12,16,0,0)):
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = None
            format = 'URAT'
        elif(dt < datetime(2005,3,15,0,0)):
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = _RussiaAsia
            format = 'ORA%sT'
        else:
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = None
            format = 'ORAT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Aden(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1950,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=59)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'AST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class MST7MDT(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=-7, minutes=0)
        rule = _US
        format = 'M%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Istanbul(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1880,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=55)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1910,10,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=56)
            rule = None
            format = 'IMT'
        elif(dt < datetime(1978,10,15,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _Turkey
            format = 'EE%sT'
        elif(dt < datetime(1985,4,20,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = _Turkey
            format = 'TR%sT'
        elif(dt < datetime(2007,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _Turkey
            format = 'EE%sT'
        elif(dt < datetime(2011,3,27,1,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _EU
            format = 'EE%sT'
        elif(dt < datetime(2011,3,28,1,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'EET'
        elif(dt < datetime(2014,3,30,1,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _EU
            format = 'EE%sT'
        elif(dt < datetime(2014,3,31,1,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'EET'
        else:
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _EU
            format = 'EE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Abidjan(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1912,1,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=-16)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = None
            format = 'GMT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Australia_Lindeman(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1895,1,1,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=55)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1971,1,1,0,0)):
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = _Aus
            format = 'AE%sT'
        elif(dt < datetime(1992,7,1,0,0)):
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = _AQ
            format = 'AE%sT'
        else:
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = _Holiday
            format = 'AE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Pacific_Galapagos(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1931,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=-58)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1986,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'ECT'
        else:
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = None
            format = 'GALT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Bogota(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1884,3,13,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-56)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1914,11,23,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-56)
            rule = None
            format = 'BMT'
        else:
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _CO
            format = 'CO%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Asmara(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1870,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=35)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1890,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=35)
            rule = None
            format = 'AMT'
        elif(dt < datetime(1936,5,5,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=35)
            rule = None
            format = 'ADMT'
        else:
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'EAT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Chicago(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1883,11,18,12,9)):
            offset = timedelta(seconds=0, hours=-5, minutes=-50)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1920,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _US
            format = 'C%sT'
        elif(dt < datetime(1936,3,1,1,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Chicago
            format = 'C%sT'
        elif(dt < datetime(1936,11,15,2,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        elif(dt < datetime(1942,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Chicago
            format = 'C%sT'
        elif(dt < datetime(1946,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _US
            format = 'C%sT'
        elif(dt < datetime(1967,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Chicago
            format = 'C%sT'
        else:
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _US
            format = 'C%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Pacific_Kwajalein(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1901,1,1,0,0)):
            offset = timedelta(seconds=0, hours=11, minutes=9)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1969,10,1,0,0)):
            offset = timedelta(seconds=0, hours=11, minutes=0)
            rule = None
            format = 'MHT'
        elif(dt < datetime(1993,8,20,0,0)):
            offset = timedelta(seconds=0, hours=-12, minutes=0)
            rule = None
            format = 'KWAT'
        else:
            offset = timedelta(seconds=0, hours=12, minutes=0)
            rule = None
            format = 'MHT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Australia_Broken_Hill(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1895,2,1,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=25)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1896,8,23,0,0)):
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = None
            format = 'AEST'
        elif(dt < datetime(1899,5,1,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = None
            format = 'ACST'
        elif(dt < datetime(1971,1,1,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=30)
            rule = _Aus
            format = 'AC%sT'
        elif(dt < datetime(2000,1,1,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=30)
            rule = _AN
            format = 'AC%sT'
        else:
            offset = timedelta(seconds=0, hours=9, minutes=30)
            rule = _AS
            format = 'AC%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Cuiaba(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1914,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-44)
            rule = None
            format = 'LMT'
        elif(dt < datetime(2003,9,24,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Brazil
            format = 'AM%sT'
        elif(dt < datetime(2004,10,1,1,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'AMT'
        else:
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Brazil
            format = 'AM%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Indian_Christmas(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1895,2,1,0,0)):
            offset = timedelta(seconds=0, hours=7, minutes=2)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=7, minutes=0)
            rule = None
            format = 'CXT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Jayapura(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1932,11,1,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=22)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1944,9,1,1,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = None
            format = 'WIT'
        elif(dt < datetime(1964,1,1,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=30)
            rule = None
            format = 'ACST'
        else:
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = None
            format = 'WIT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Brussels(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1880,1,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=17)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1892,5,1,1,0)):
            offset = timedelta(seconds=0, hours=0, minutes=17)
            rule = None
            format = 'BMT'
        elif(dt < datetime(1914,11,1,8,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = None
            format = 'WET'
        elif(dt < datetime(1916,5,1,1,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = None
            format = 'CET'
        elif(dt < datetime(1918,11,11,11,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _C_Eur
            format = 'CE%sT'
        elif(dt < datetime(1940,5,20,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = _Belgium
            format = 'WE%sT'
        elif(dt < datetime(1944,9,1,3,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _C_Eur
            format = 'CE%sT'
        elif(dt < datetime(1977,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _Belgium
            format = 'CE%sT'
        else:
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _EU
            format = 'CE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Argentina_Cordoba(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1894,10,31,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-16)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1920,5,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-16)
            rule = None
            format = 'CMT'
        elif(dt < datetime(1930,12,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'ART'
        elif(dt < datetime(1969,10,1,5,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(1991,3,1,3,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(1991,10,20,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'WART'
        elif(dt < datetime(1999,10,1,3,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(2000,3,1,3,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        else:
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Noronha(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1914,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-2, minutes=-9)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1990,9,17,0,0)):
            offset = timedelta(seconds=0, hours=-2, minutes=0)
            rule = _Brazil
            format = 'FN%sT'
        elif(dt < datetime(1999,9,30,0,0)):
            offset = timedelta(seconds=0, hours=-2, minutes=0)
            rule = None
            format = 'FNT'
        elif(dt < datetime(2000,10,15,0,0)):
            offset = timedelta(seconds=0, hours=-2, minutes=0)
            rule = _Brazil
            format = 'FN%sT'
        elif(dt < datetime(2001,9,13,0,0)):
            offset = timedelta(seconds=0, hours=-2, minutes=0)
            rule = None
            format = 'FNT'
        elif(dt < datetime(2002,10,1,1,0)):
            offset = timedelta(seconds=0, hours=-2, minutes=0)
            rule = _Brazil
            format = 'FN%sT'
        else:
            offset = timedelta(seconds=0, hours=-2, minutes=0)
            rule = None
            format = 'FNT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Algiers(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1891,3,15,0,1)):
            offset = timedelta(seconds=0, hours=0, minutes=12)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1911,3,11,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=9)
            rule = None
            format = 'PMT'
        elif(dt < datetime(1940,2,25,2,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = _Algeria
            format = 'WE%sT'
        elif(dt < datetime(1946,10,1,7,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _Algeria
            format = 'CE%sT'
        elif(dt < datetime(1956,1,29,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = None
            format = 'WET'
        elif(dt < datetime(1963,4,14,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = None
            format = 'CET'
        elif(dt < datetime(1977,10,21,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = _Algeria
            format = 'WE%sT'
        elif(dt < datetime(1979,10,26,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _Algeria
            format = 'CE%sT'
        elif(dt < datetime(1981,5,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = _Algeria
            format = 'WE%sT'
        else:
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = None
            format = 'CET'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Harare(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1903,3,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=4)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'CAT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Ndjamena(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1912,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1979,10,14,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = None
            format = 'WAT'
        elif(dt < datetime(1980,3,1,8,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _rule_constant_1hour
            format = 'WAST'
        else:
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = None
            format = 'WAT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Costa_Rica(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1890,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=-36)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1921,1,15,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=-36)
            rule = None
            format = 'SJMT'
        else:
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _CR
            format = 'C%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Indian_Mayotte(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1911,7,1,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'EAT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Phnom_Penh(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1906,6,1,9,0)):
            offset = timedelta(seconds=0, hours=6, minutes=59)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1911,3,11,0,1)):
            offset = timedelta(seconds=0, hours=7, minutes=6)
            rule = None
            format = 'SMT'
        elif(dt < datetime(1912,5,1,0,0)):
            offset = timedelta(seconds=0, hours=7, minutes=0)
            rule = None
            format = 'ICT'
        elif(dt < datetime(1931,5,1,0,0)):
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = None
            format = 'ICT'
        else:
            offset = timedelta(seconds=0, hours=7, minutes=0)
            rule = None
            format = 'ICT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Managua(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1890,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=-45)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1934,6,23,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=-45)
            rule = None
            format = 'MMT'
        elif(dt < datetime(1973,5,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = None
            format = 'CST'
        elif(dt < datetime(1975,2,16,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        elif(dt < datetime(1992,1,1,1,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Nic
            format = 'C%sT'
        elif(dt < datetime(1992,9,24,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        elif(dt < datetime(1993,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = None
            format = 'CST'
        elif(dt < datetime(1997,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        else:
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Nic
            format = 'C%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Pangnirtung(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1921,1,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = None
            format = 'zzz'
        elif(dt < datetime(1995,4,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _NT_YK
            format = 'A%sT'
        elif(dt < datetime(1999,10,31,2,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _Canada
            format = 'E%sT'
        elif(dt < datetime(2000,10,29,2,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Canada
            format = 'C%sT'
        else:
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _Canada
            format = 'E%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Nicosia(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1921,11,14,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=13)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1998,9,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _Cyprus
            format = 'EE%sT'
        else:
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _EUAsia
            format = 'EE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Tijuana(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1922,1,1,1,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=-48)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1924,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = None
            format = 'MST'
        elif(dt < datetime(1927,6,10,23,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = None
            format = 'PST'
        elif(dt < datetime(1930,11,15,0,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = None
            format = 'MST'
        elif(dt < datetime(1931,4,1,1,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = None
            format = 'PST'
        elif(dt < datetime(1931,9,30,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _rule_constant_1hour
            format = 'PDT'
        elif(dt < datetime(1942,4,24,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = None
            format = 'PST'
        elif(dt < datetime(1945,8,14,23,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _rule_constant_1hour
            format = 'PWT'
        elif(dt < datetime(1945,11,12,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _rule_constant_1hour
            format = 'PPT'
        elif(dt < datetime(1948,4,1,5,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = None
            format = 'PST'
        elif(dt < datetime(1949,1,14,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _rule_constant_1hour
            format = 'PDT'
        elif(dt < datetime(1954,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = None
            format = 'PST'
        elif(dt < datetime(1961,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _CA
            format = 'P%sT'
        elif(dt < datetime(1976,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = None
            format = 'PST'
        elif(dt < datetime(1996,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _US
            format = 'P%sT'
        elif(dt < datetime(2001,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _Mexico
            format = 'P%sT'
        elif(dt < datetime(2002,2,20,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _US
            format = 'P%sT'
        elif(dt < datetime(2010,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _Mexico
            format = 'P%sT'
        else:
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _US
            format = 'P%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Pacific_Fakaofo(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1901,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-11, minutes=-24)
            rule = None
            format = 'LMT'
        elif(dt < datetime(2011,12,30,0,0)):
            offset = timedelta(seconds=0, hours=-11, minutes=0)
            rule = None
            format = 'TKT'
        else:
            offset = timedelta(seconds=0, hours=13, minutes=0)
            rule = None
            format = 'TKT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Martinique(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1890,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-4)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1911,5,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-4)
            rule = None
            format = 'FFMT'
        elif(dt < datetime(1980,4,1,6,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'AST'
        elif(dt < datetime(1980,9,28,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _rule_constant_1hour
            format = 'ADT'
        else:
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'AST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Antigua(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1912,3,2,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-7)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1951,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        else:
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'AST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Indiana_Indianapolis(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1883,11,18,12,15)):
            offset = timedelta(seconds=0, hours=-5, minutes=-44)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1920,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _US
            format = 'C%sT'
        elif(dt < datetime(1942,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Indianapolis
            format = 'C%sT'
        elif(dt < datetime(1946,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _US
            format = 'C%sT'
        elif(dt < datetime(1955,4,24,2,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Indianapolis
            format = 'C%sT'
        elif(dt < datetime(1957,9,29,2,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        elif(dt < datetime(1958,4,27,2,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = None
            format = 'CST'
        elif(dt < datetime(1969,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        elif(dt < datetime(1971,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _US
            format = 'E%sT'
        elif(dt < datetime(2006,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        else:
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _US
            format = 'E%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Argentina_La_Rioja(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1894,10,31,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-27)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1920,5,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-16)
            rule = None
            format = 'CMT'
        elif(dt < datetime(1930,12,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'ART'
        elif(dt < datetime(1969,10,1,5,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(1991,3,1,1,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(1991,5,1,7,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'WART'
        elif(dt < datetime(1999,10,1,3,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(2000,3,1,3,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(2004,6,1,1,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'ART'
        elif(dt < datetime(2004,6,20,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'WART'
        elif(dt < datetime(2008,10,18,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        else:
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'ART'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Pacific_Tahiti(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1912,10,1,0,0)):
            offset = timedelta(seconds=0, hours=-9, minutes=-58)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=-10, minutes=0)
            rule = None
            format = 'TAHT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Brunei(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1926,3,1,0,0)):
            offset = timedelta(seconds=0, hours=7, minutes=39)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1933,1,1,0,0)):
            offset = timedelta(seconds=0, hours=7, minutes=30)
            rule = None
            format = 'BNT'
        else:
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = None
            format = 'BNT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Asuncion(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1890,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-50)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1931,10,10,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-50)
            rule = None
            format = 'AMT'
        elif(dt < datetime(1972,10,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'PYT'
        elif(dt < datetime(1974,4,1,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'PYT'
        else:
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Para
            format = 'PY%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Vienna(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1893,4,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=5)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1920,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _C_Eur
            format = 'CE%sT'
        elif(dt < datetime(1940,4,1,1,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _Austria
            format = 'CE%sT'
        elif(dt < datetime(1945,4,1,2,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _C_Eur
            format = 'CE%sT'
        elif(dt < datetime(1945,4,12,2,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _rule_constant_1hour
            format = 'CEST'
        elif(dt < datetime(1946,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = None
            format = 'CET'
        elif(dt < datetime(1981,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _Austria
            format = 'CE%sT'
        else:
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _EU
            format = 'CE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Australia_Hobart(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1895,9,1,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=49)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1916,10,1,2,0)):
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = None
            format = 'AEST'
        elif(dt < datetime(1917,2,1,0,0)):
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = _rule_constant_1hour
            format = 'AEDT'
        elif(dt < datetime(1967,1,1,0,0)):
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = _Aus
            format = 'AE%sT'
        else:
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = _AT
            format = 'AE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Juneau(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1867,10,18,0,0)):
            offset = timedelta(seconds=0, hours=15, minutes=2)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1900,8,20,12,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=-57)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1942,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = None
            format = 'PST'
        elif(dt < datetime(1946,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _US
            format = 'P%sT'
        elif(dt < datetime(1969,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = None
            format = 'PST'
        elif(dt < datetime(1980,4,27,2,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _US
            format = 'P%sT'
        elif(dt < datetime(1980,10,26,2,0)):
            offset = timedelta(seconds=0, hours=-9, minutes=0)
            rule = _US
            format = 'Y%sT'
        elif(dt < datetime(1983,10,30,2,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _US
            format = 'P%sT'
        elif(dt < datetime(1983,11,30,0,0)):
            offset = timedelta(seconds=0, hours=-9, minutes=0)
            rule = _US
            format = 'Y%sT'
        else:
            offset = timedelta(seconds=0, hours=-9, minutes=0)
            rule = _US
            format = 'AK%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Inuvik(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1953,1,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = None
            format = 'zzz'
        elif(dt < datetime(1979,4,1,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _NT_YK
            format = 'P%sT'
        elif(dt < datetime(1980,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = _NT_YK
            format = 'M%sT'
        else:
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = _Canada
            format = 'M%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Ojinaga(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1922,1,1,0,2)):
            offset = timedelta(seconds=0, hours=-6, minutes=-57)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1927,6,10,23,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = None
            format = 'MST'
        elif(dt < datetime(1930,11,15,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = None
            format = 'CST'
        elif(dt < datetime(1931,5,1,1,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = None
            format = 'MST'
        elif(dt < datetime(1931,10,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = None
            format = 'CST'
        elif(dt < datetime(1932,4,1,1,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = None
            format = 'MST'
        elif(dt < datetime(1996,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = None
            format = 'CST'
        elif(dt < datetime(1998,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Mexico
            format = 'C%sT'
        elif(dt < datetime(1998,4,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = None
            format = 'CST'
        elif(dt < datetime(2010,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = _Mexico
            format = 'M%sT'
        else:
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = _US
            format = 'M%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Montreal(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1884,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-54)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1918,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _Mont
            format = 'E%sT'
        elif(dt < datetime(1919,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _Canada
            format = 'E%sT'
        elif(dt < datetime(1942,2,1,9,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _Mont
            format = 'E%sT'
        elif(dt < datetime(1946,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _Canada
            format = 'E%sT'
        elif(dt < datetime(1974,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _Mont
            format = 'E%sT'
        else:
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _Canada
            format = 'E%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Seoul(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1890,1,1,0,0)):
            offset = timedelta(seconds=0, hours=8, minutes=27)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1904,12,1,0,0)):
            offset = timedelta(seconds=0, hours=8, minutes=30)
            rule = None
            format = 'KST'
        elif(dt < datetime(1928,1,1,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = None
            format = 'JCST'
        elif(dt < datetime(1932,1,1,0,0)):
            offset = timedelta(seconds=0, hours=8, minutes=30)
            rule = None
            format = 'KST'
        elif(dt < datetime(1937,10,1,1,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = None
            format = 'JCST'
        elif(dt < datetime(1945,9,1,8,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = None
            format = 'JST'
        elif(dt < datetime(1954,3,21,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = None
            format = 'KST'
        elif(dt < datetime(1961,8,10,0,0)):
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = _ROK
            format = 'K%sT'
        elif(dt < datetime(1968,10,1,0,0)):
            offset = timedelta(seconds=0, hours=8, minutes=30)
            rule = None
            format = 'KST'
        else:
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = _ROK
            format = 'K%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Indian_Comoro(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1911,7,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=53)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'EAT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Tallinn(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1880,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=39)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1918,2,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=39)
            rule = None
            format = 'TMT'
        elif(dt < datetime(1919,7,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _C_Eur
            format = 'CE%sT'
        elif(dt < datetime(1921,5,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=39)
            rule = None
            format = 'TMT'
        elif(dt < datetime(1940,8,1,6,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'EET'
        elif(dt < datetime(1941,9,15,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'MSK'
        elif(dt < datetime(1944,9,22,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _C_Eur
            format = 'CE%sT'
        elif(dt < datetime(1989,3,26,2,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = _Russia
            format = 'MSK/MSD'
        elif(dt < datetime(1989,9,24,2,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _rule_constant_1hour
            format = 'EEST'
        elif(dt < datetime(1998,9,22,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _C_Eur
            format = 'EE%sT'
        elif(dt < datetime(1999,11,1,1,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _EU
            format = 'EE%sT'
        elif(dt < datetime(2002,2,21,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'EET'
        else:
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _EU
            format = 'EE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Indian_Mahe(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1906,6,1,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=41)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = None
            format = 'SCT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Argentina_Jujuy(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1894,10,31,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-21)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1920,5,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-16)
            rule = None
            format = 'CMT'
        elif(dt < datetime(1930,12,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'ART'
        elif(dt < datetime(1969,10,1,5,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(1990,3,1,4,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(1990,10,28,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'WART'
        elif(dt < datetime(1991,3,17,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _rule_constant_1hour
            format = 'WARST'
        elif(dt < datetime(1991,10,1,6,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'WART'
        elif(dt < datetime(1992,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _rule_constant_1hour
            format = 'ARST'
        elif(dt < datetime(1999,10,1,3,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(2000,3,1,3,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(2008,10,18,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        else:
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'ART'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Creston(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1884,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=-46)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1916,10,1,0,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = None
            format = 'MST'
        elif(dt < datetime(1918,6,2,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = None
            format = 'PST'
        else:
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = None
            format = 'MST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Adak(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1867,10,18,0,0)):
            offset = timedelta(seconds=0, hours=12, minutes=13)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1900,8,20,12,0)):
            offset = timedelta(seconds=0, hours=-11, minutes=-46)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1942,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-11, minutes=0)
            rule = None
            format = 'NST'
        elif(dt < datetime(1946,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-11, minutes=0)
            rule = _US
            format = 'N%sT'
        elif(dt < datetime(1967,4,1,0,0)):
            offset = timedelta(seconds=0, hours=-11, minutes=0)
            rule = None
            format = 'NST'
        elif(dt < datetime(1969,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-11, minutes=0)
            rule = None
            format = 'BST'
        elif(dt < datetime(1983,10,30,2,0)):
            offset = timedelta(seconds=0, hours=-11, minutes=0)
            rule = _US
            format = 'B%sT'
        elif(dt < datetime(1983,11,30,0,0)):
            offset = timedelta(seconds=0, hours=-10, minutes=0)
            rule = _US
            format = 'AH%sT'
        else:
            offset = timedelta(seconds=0, hours=-10, minutes=0)
            rule = _US
            format = 'HA%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Singapore(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1901,1,1,1,0)):
            offset = timedelta(seconds=0, hours=6, minutes=55)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1905,6,1,1,0)):
            offset = timedelta(seconds=0, hours=6, minutes=55)
            rule = None
            format = 'SMT'
        elif(dt < datetime(1933,1,1,1,0)):
            offset = timedelta(seconds=0, hours=7, minutes=0)
            rule = None
            format = 'MALT'
        elif(dt < datetime(1936,1,1,1,0)):
            offset = timedelta(seconds=0, hours=7, minutes=0)
            rule = _rule_constant_20min
            format = 'MALST'
        elif(dt < datetime(1941,9,1,1,0)):
            offset = timedelta(seconds=0, hours=7, minutes=20)
            rule = None
            format = 'MALT'
        elif(dt < datetime(1942,2,16,0,0)):
            offset = timedelta(seconds=0, hours=7, minutes=30)
            rule = None
            format = 'MALT'
        elif(dt < datetime(1945,9,12,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = None
            format = 'JST'
        elif(dt < datetime(1965,8,1,9,0)):
            offset = timedelta(seconds=0, hours=7, minutes=30)
            rule = None
            format = 'MALT'
        elif(dt < datetime(1982,1,1,1,0)):
            offset = timedelta(seconds=0, hours=7, minutes=30)
            rule = None
            format = 'SGT'
        else:
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = None
            format = 'SGT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Nairobi(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1928,7,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=27)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1930,1,1,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'EAT'
        elif(dt < datetime(1940,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=30)
            rule = None
            format = 'BEAT'
        elif(dt < datetime(1960,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=45)
            rule = None
            format = 'BEAUT'
        else:
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'EAT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Pacific_Noumea(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1912,1,13,0,0)):
            offset = timedelta(seconds=0, hours=11, minutes=5)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=11, minutes=0)
            rule = _NC
            format = 'NC%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Cairo(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1900,10,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=5)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _Egypt
            format = 'EE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Moscow(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1880,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=30)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1916,7,1,3,0)):
            offset = timedelta(seconds=0, hours=2, minutes=30)
            rule = None
            format = 'MMT'
        elif(dt < datetime(1919,7,1,1,0)):
            offset = timedelta(seconds=0, hours=2, minutes=31)
            rule = _Russia
            format = '%s'
        elif(dt < datetime(1921,10,1,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = _Russia
            format = '%s'
        elif(dt < datetime(1922,10,1,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = _Russia
            format = 'MSK/MSD'
        elif(dt < datetime(1930,6,21,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'EET'
        elif(dt < datetime(1991,3,31,2,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = _Russia
            format = 'MSK/MSD'
        elif(dt < datetime(1992,1,19,2,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _Russia
            format = 'EE%sT'
        elif(dt < datetime(2011,3,27,2,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = _Russia
            format = 'MSK/MSD'
        elif(dt < datetime(2014,10,26,2,0)):
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = None
            format = 'MSK'
        else:
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'MSK'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Ulaanbaatar(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1905,8,1,0,0)):
            offset = timedelta(seconds=0, hours=7, minutes=7)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1978,1,1,0,0)):
            offset = timedelta(seconds=0, hours=7, minutes=0)
            rule = None
            format = 'ULAT'
        else:
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = _Mongol
            format = 'ULA%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Rainy_River(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1895,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=-18)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1940,9,29,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Canada
            format = 'C%sT'
        elif(dt < datetime(1942,2,1,9,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _rule_constant_1hour
            format = 'CDT'
        else:
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Canada
            format = 'C%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Kampala(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1928,7,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=9)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1930,1,1,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'EAT'
        elif(dt < datetime(1948,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=30)
            rule = None
            format = 'BEAT'
        elif(dt < datetime(1957,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=45)
            rule = None
            format = 'BEAUT'
        else:
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'EAT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Colombo(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1880,1,1,0,0)):
            offset = timedelta(seconds=0, hours=5, minutes=19)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1906,1,1,0,0)):
            offset = timedelta(seconds=0, hours=5, minutes=19)
            rule = None
            format = 'MMT'
        elif(dt < datetime(1942,1,1,5,0)):
            offset = timedelta(seconds=0, hours=5, minutes=30)
            rule = None
            format = 'IST'
        elif(dt < datetime(1942,9,1,0,0)):
            offset = timedelta(seconds=0, hours=5, minutes=30)
            rule = _rule_constant_30min
            format = 'IHST'
        elif(dt < datetime(1945,10,16,2,0)):
            offset = timedelta(seconds=0, hours=5, minutes=30)
            rule = _rule_constant_1hour
            format = 'IST'
        elif(dt < datetime(1996,5,25,0,0)):
            offset = timedelta(seconds=0, hours=5, minutes=30)
            rule = None
            format = 'IST'
        elif(dt < datetime(1996,10,26,0,30)):
            offset = timedelta(seconds=0, hours=6, minutes=30)
            rule = None
            format = 'LKT'
        elif(dt < datetime(2006,4,15,0,30)):
            offset = timedelta(seconds=0, hours=6, minutes=0)
            rule = None
            format = 'LKT'
        else:
            offset = timedelta(seconds=0, hours=5, minutes=30)
            rule = None
            format = 'IST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Australia_Adelaide(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1895,2,1,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=14)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1899,5,1,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = None
            format = 'ACST'
        elif(dt < datetime(1971,1,1,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=30)
            rule = _Aus
            format = 'AC%sT'
        else:
            offset = timedelta(seconds=0, hours=9, minutes=30)
            rule = _AS
            format = 'AC%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Cambridge_Bay(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1920,1,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = None
            format = 'zzz'
        elif(dt < datetime(1999,10,31,2,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = _NT_YK
            format = 'M%sT'
        elif(dt < datetime(2000,10,29,2,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Canada
            format = 'C%sT'
        elif(dt < datetime(2000,11,1,5,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        elif(dt < datetime(2001,4,1,1,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = None
            format = 'CST'
        else:
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = _Canada
            format = 'M%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Luanda(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1892,1,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=52)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1911,5,26,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=52)
            rule = None
            format = 'AOT'
        else:
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = None
            format = 'WAT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Pacific_Chatham(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1868,11,1,2,0)):
            offset = timedelta(seconds=0, hours=12, minutes=13)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1946,1,1,1,0)):
            offset = timedelta(seconds=0, hours=12, minutes=15)
            rule = None
            format = 'CHAST'
        else:
            offset = timedelta(seconds=0, hours=12, minutes=45)
            rule = _Chatham
            format = 'CHA%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Indiana_Winamac(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1883,11,18,12,13)):
            offset = timedelta(seconds=0, hours=-5, minutes=-46)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1946,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _US
            format = 'C%sT'
        elif(dt < datetime(1961,4,30,2,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Pulaski
            format = 'C%sT'
        elif(dt < datetime(1969,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        elif(dt < datetime(1971,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _US
            format = 'E%sT'
        elif(dt < datetime(2006,4,1,2,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        elif(dt < datetime(2007,3,11,2,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _US
            format = 'C%sT'
        else:
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _US
            format = 'E%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Tbilisi(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1880,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=59)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1924,5,1,2,0)):
            offset = timedelta(seconds=0, hours=2, minutes=59)
            rule = None
            format = 'TBMT'
        elif(dt < datetime(1957,3,1,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'TBIT'
        elif(dt < datetime(1991,3,31,2,0)):
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = _RussiaAsia
            format = 'TBI%sT'
        elif(dt < datetime(1991,4,1,9,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = _rule_constant_1hour
            format = 'TBIST'
        elif(dt < datetime(1992,1,1,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = _RussiaAsia
            format = 'GE%sT'
        elif(dt < datetime(1994,9,1,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = _E_EurAsia
            format = 'GE%sT'
        elif(dt < datetime(1996,10,1,0,0)):
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = _E_EurAsia
            format = 'GE%sT'
        elif(dt < datetime(1997,3,1,0,0)):
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = _rule_constant_1hour
            format = 'GEST'
        elif(dt < datetime(2004,6,27,0,0)):
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = _E_EurAsia
            format = 'GE%sT'
        elif(dt < datetime(2005,3,1,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = _RussiaAsia
            format = 'GE%sT'
        else:
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = None
            format = 'GET'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Gibraltar(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1880,8,1,2,0)):
            offset = timedelta(seconds=0, hours=0, minutes=-21)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1957,4,14,2,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = _GB_Eire
            format = '%s'
        elif(dt < datetime(1982,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = None
            format = 'CET'
        else:
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _EU
            format = 'CE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Karachi(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1907,1,1,0,0)):
            offset = timedelta(seconds=0, hours=4, minutes=28)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1942,9,1,0,0)):
            offset = timedelta(seconds=0, hours=5, minutes=30)
            rule = None
            format = 'IST'
        elif(dt < datetime(1945,10,15,0,0)):
            offset = timedelta(seconds=0, hours=5, minutes=30)
            rule = _rule_constant_1hour
            format = 'IST'
        elif(dt < datetime(1951,9,30,0,0)):
            offset = timedelta(seconds=0, hours=5, minutes=30)
            rule = None
            format = 'IST'
        elif(dt < datetime(1971,3,26,0,0)):
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = None
            format = 'KART'
        else:
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = _Pakistan
            format = 'PK%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Australia_Lord_Howe(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1895,2,1,0,0)):
            offset = timedelta(seconds=0, hours=10, minutes=36)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1981,3,1,0,0)):
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = None
            format = 'AEST'
        else:
            offset = timedelta(seconds=0, hours=10, minutes=30)
            rule = _LH
            format = 'LH%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Etc_GMT_9(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=9, minutes=0)
        rule = None
        format = 'GMT-9'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Etc_GMT_8(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=8, minutes=0)
        rule = None
        format = 'GMT-8'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Bahia_Banderas(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1921,12,31,23,59)):
            offset = timedelta(seconds=0, hours=-7, minutes=-1)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1927,6,10,23,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = None
            format = 'MST'
        elif(dt < datetime(1930,11,15,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = None
            format = 'CST'
        elif(dt < datetime(1931,5,1,1,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = None
            format = 'MST'
        elif(dt < datetime(1931,10,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = None
            format = 'CST'
        elif(dt < datetime(1932,4,1,1,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = None
            format = 'MST'
        elif(dt < datetime(1942,4,24,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = None
            format = 'CST'
        elif(dt < datetime(1949,1,14,0,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = None
            format = 'MST'
        elif(dt < datetime(1970,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = None
            format = 'PST'
        elif(dt < datetime(2010,4,4,2,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = _Mexico
            format = 'M%sT'
        else:
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Mexico
            format = 'C%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Etc_GMT_1(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=1, minutes=0)
        rule = None
        format = 'GMT-1'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Etc_GMT_3(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=3, minutes=0)
        rule = None
        format = 'GMT-3'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Etc_GMT_2(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=2, minutes=0)
        rule = None
        format = 'GMT-2'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Etc_GMT_5(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=5, minutes=0)
        rule = None
        format = 'GMT-5'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Etc_GMT_4(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=4, minutes=0)
        rule = None
        format = 'GMT-4'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Etc_GMT_7(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=7, minutes=0)
        rule = None
        format = 'GMT-7'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Etc_GMT_6(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=6, minutes=0)
        rule = None
        format = 'GMT-6'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Boa_Vista(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1914,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-2)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1988,9,12,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Brazil
            format = 'AM%sT'
        elif(dt < datetime(1999,9,30,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'AMT'
        elif(dt < datetime(2000,10,15,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Brazil
            format = 'AM%sT'
        else:
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'AMT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Tripoli(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1920,1,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=52)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1959,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _Libya
            format = 'CE%sT'
        elif(dt < datetime(1982,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'EET'
        elif(dt < datetime(1990,5,1,4,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _Libya
            format = 'CE%sT'
        elif(dt < datetime(1996,9,30,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'EET'
        elif(dt < datetime(1997,10,1,4,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _Libya
            format = 'CE%sT'
        elif(dt < datetime(2012,11,10,2,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'EET'
        elif(dt < datetime(2013,10,25,2,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _Libya
            format = 'CE%sT'
        else:
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'EET'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Pacific_Wallis(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1901,1,1,0,0)):
            offset = timedelta(seconds=0, hours=12, minutes=15)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=12, minutes=0)
            rule = None
            format = 'WFT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Atlantic_Stanley(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1890,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-51)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1912,3,12,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-51)
            rule = None
            format = 'SMT'
        elif(dt < datetime(1983,5,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Falk
            format = 'FK%sT'
        elif(dt < datetime(1985,9,15,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Falk
            format = 'FK%sT'
        elif(dt < datetime(2010,9,5,2,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Falk
            format = 'FK%sT'
        else:
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'FKST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Srednekolymsk(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1924,5,1,2,0)):
            offset = timedelta(seconds=0, hours=10, minutes=14)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1930,6,21,0,0)):
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = None
            format = 'MAGT'
        elif(dt < datetime(1991,3,31,2,0)):
            offset = timedelta(seconds=0, hours=11, minutes=0)
            rule = _Russia
            format = 'MAG%sT'
        elif(dt < datetime(1992,1,19,2,0)):
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = _Russia
            format = 'MAG%sT'
        elif(dt < datetime(2011,3,27,2,0)):
            offset = timedelta(seconds=0, hours=11, minutes=0)
            rule = _Russia
            format = 'MAG%sT'
        elif(dt < datetime(2014,10,26,2,0)):
            offset = timedelta(seconds=0, hours=12, minutes=0)
            rule = None
            format = 'MAGT'
        else:
            offset = timedelta(seconds=0, hours=11, minutes=0)
            rule = None
            format = 'SRET'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class CET(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=1, minutes=0)
        rule = _C_Eur
        format = 'CE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Lubumbashi(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1897,11,9,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=49)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'CAT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Blanc_Sablon(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1884,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-48)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1970,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Canada
            format = 'A%sT'
        else:
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'AST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Jamaica(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1890,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=-7)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1912,2,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=-7)
            rule = None
            format = 'KMT'
        elif(dt < datetime(1974,4,28,2,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        elif(dt < datetime(1984,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _US
            format = 'E%sT'
        else:
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Kiev(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1880,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=2)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1924,5,1,2,0)):
            offset = timedelta(seconds=0, hours=2, minutes=2)
            rule = None
            format = 'KMT'
        elif(dt < datetime(1930,6,21,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'EET'
        elif(dt < datetime(1941,9,20,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'MSK'
        elif(dt < datetime(1943,11,1,6,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _C_Eur
            format = 'CE%sT'
        elif(dt < datetime(1990,7,1,1,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = _Russia
            format = 'MSK/MSD'
        elif(dt < datetime(1991,9,29,3,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _rule_constant_1hour
            format = 'EEST'
        elif(dt < datetime(1995,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _E_Eur
            format = 'EE%sT'
        else:
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _EU
            format = 'EE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Budapest(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1890,10,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=16)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1918,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _C_Eur
            format = 'CE%sT'
        elif(dt < datetime(1941,4,1,8,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _Hungary
            format = 'CE%sT'
        elif(dt < datetime(1945,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _C_Eur
            format = 'CE%sT'
        elif(dt < datetime(1980,9,28,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _Hungary
            format = 'CE%sT'
        else:
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _EU
            format = 'CE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Pacific_Midway(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1901,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-11, minutes=-49)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1956,6,1,3,0)):
            offset = timedelta(seconds=0, hours=-11, minutes=0)
            rule = None
            format = 'NST'
        elif(dt < datetime(1956,9,1,2,0)):
            offset = timedelta(seconds=0, hours=-11, minutes=0)
            rule = _rule_constant_1hour
            format = 'NDT'
        elif(dt < datetime(1967,4,1,0,0)):
            offset = timedelta(seconds=0, hours=-11, minutes=0)
            rule = None
            format = 'NST'
        elif(dt < datetime(1983,11,30,0,0)):
            offset = timedelta(seconds=0, hours=-11, minutes=0)
            rule = None
            format = 'BST'
        else:
            offset = timedelta(seconds=0, hours=-11, minutes=0)
            rule = None
            format = 'SST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Goose_Bay(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1884,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-1)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1918,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-30)
            rule = None
            format = 'NST'
        elif(dt < datetime(1919,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-30)
            rule = _Canada
            format = 'N%sT'
        elif(dt < datetime(1935,3,30,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-30)
            rule = None
            format = 'NST'
        elif(dt < datetime(1936,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-30)
            rule = None
            format = 'NST'
        elif(dt < datetime(1942,5,11,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-30)
            rule = _StJohns
            format = 'N%sT'
        elif(dt < datetime(1946,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-30)
            rule = _Canada
            format = 'N%sT'
        elif(dt < datetime(1966,3,15,2,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-30)
            rule = _StJohns
            format = 'N%sT'
        elif(dt < datetime(2011,11,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _StJohns
            format = 'A%sT'
        else:
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Canada
            format = 'A%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Amman(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1931,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=23)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _Jordan
            format = 'EE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Sakhalin(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1905,8,23,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=30)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1937,10,1,1,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = None
            format = 'JCST'
        elif(dt < datetime(1945,8,25,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = None
            format = 'JST'
        elif(dt < datetime(1991,3,31,2,0)):
            offset = timedelta(seconds=0, hours=11, minutes=0)
            rule = _Russia
            format = 'SAK%sT'
        elif(dt < datetime(1992,1,19,2,0)):
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = _Russia
            format = 'SAK%sT'
        elif(dt < datetime(1997,3,1,0,0)):
            offset = timedelta(seconds=0, hours=11, minutes=0)
            rule = _Russia
            format = 'SAK%sT'
        elif(dt < datetime(2011,3,27,2,0)):
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = _Russia
            format = 'SAK%sT'
        elif(dt < datetime(2014,10,26,2,0)):
            offset = timedelta(seconds=0, hours=11, minutes=0)
            rule = None
            format = 'SAKT'
        else:
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = None
            format = 'SAKT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Windhoek(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1892,2,8,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=8)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1903,3,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=30)
            rule = None
            format = 'SWAT'
        elif(dt < datetime(1942,9,20,2,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'SAST'
        elif(dt < datetime(1943,3,21,2,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _rule_constant_1hour
            format = 'SAST'
        elif(dt < datetime(1990,3,21,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'SAST'
        elif(dt < datetime(1994,4,1,3,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'CAT'
        else:
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _Namibia
            format = 'WA%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Sitka(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1867,10,18,0,0)):
            offset = timedelta(seconds=0, hours=14, minutes=58)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1900,8,20,12,0)):
            offset = timedelta(seconds=0, hours=-9, minutes=-1)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1942,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = None
            format = 'PST'
        elif(dt < datetime(1946,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _US
            format = 'P%sT'
        elif(dt < datetime(1969,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = None
            format = 'PST'
        elif(dt < datetime(1983,10,30,2,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _US
            format = 'P%sT'
        elif(dt < datetime(1983,11,30,0,0)):
            offset = timedelta(seconds=0, hours=-9, minutes=0)
            rule = _US
            format = 'Y%sT'
        else:
            offset = timedelta(seconds=0, hours=-9, minutes=0)
            rule = _US
            format = 'AK%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Guyana(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1915,3,1,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-52)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1966,5,26,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-45)
            rule = None
            format = 'GBGT'
        elif(dt < datetime(1975,7,31,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-45)
            rule = None
            format = 'GYT'
        elif(dt < datetime(1991,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'GYT'
        else:
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'GYT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Pacific_Pohnpei(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1901,1,1,0,0)):
            offset = timedelta(seconds=0, hours=10, minutes=32)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=11, minutes=0)
            rule = None
            format = 'PONT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Sao_Paulo(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1914,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-6)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1963,10,23,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Brazil
            format = 'BR%sT'
        elif(dt < datetime(1964,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _rule_constant_1hour
            format = 'BRST'
        else:
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Brazil
            format = 'BR%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Australia_Perth(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1895,12,1,0,0)):
            offset = timedelta(seconds=0, hours=7, minutes=43)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1943,7,1,0,0)):
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = _Aus
            format = 'AW%sT'
        else:
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = _AW
            format = 'AW%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Djibouti(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1911,7,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=52)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'EAT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Jakarta(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1867,8,10,0,0)):
            offset = timedelta(seconds=0, hours=7, minutes=7)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1923,12,31,23,47)):
            offset = timedelta(seconds=0, hours=7, minutes=7)
            rule = None
            format = 'BMT'
        elif(dt < datetime(1932,11,1,0,0)):
            offset = timedelta(seconds=0, hours=7, minutes=20)
            rule = None
            format = 'JAVT'
        elif(dt < datetime(1942,3,23,0,0)):
            offset = timedelta(seconds=0, hours=7, minutes=30)
            rule = None
            format = 'WIB'
        elif(dt < datetime(1945,9,23,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = None
            format = 'JST'
        elif(dt < datetime(1948,5,1,0,0)):
            offset = timedelta(seconds=0, hours=7, minutes=30)
            rule = None
            format = 'WIB'
        elif(dt < datetime(1950,5,1,0,0)):
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = None
            format = 'WIB'
        elif(dt < datetime(1964,1,1,0,0)):
            offset = timedelta(seconds=0, hours=7, minutes=30)
            rule = None
            format = 'WIB'
        else:
            offset = timedelta(seconds=0, hours=7, minutes=0)
            rule = None
            format = 'WIB'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Pyongyang(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1890,1,1,0,0)):
            offset = timedelta(seconds=0, hours=8, minutes=23)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1904,12,1,0,0)):
            offset = timedelta(seconds=0, hours=8, minutes=30)
            rule = None
            format = 'KST'
        elif(dt < datetime(1928,1,1,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = None
            format = 'JCST'
        elif(dt < datetime(1932,1,1,0,0)):
            offset = timedelta(seconds=0, hours=8, minutes=30)
            rule = None
            format = 'KST'
        elif(dt < datetime(1937,10,1,1,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = None
            format = 'JCST'
        elif(dt < datetime(1945,8,24,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = None
            format = 'JST'
        elif(dt < datetime(1954,3,21,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = None
            format = 'KST'
        elif(dt < datetime(1961,8,10,0,0)):
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = None
            format = 'KST'
        else:
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = None
            format = 'KST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class EST5EDT(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=-5, minutes=0)
        rule = _US
        format = 'E%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Johannesburg(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1892,2,8,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=52)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1903,3,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=30)
            rule = None
            format = 'SAST'
        else:
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _SA
            format = 'SAST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Irkutsk(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1880,1,1,0,0)):
            offset = timedelta(seconds=0, hours=6, minutes=57)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1920,1,25,0,0)):
            offset = timedelta(seconds=0, hours=6, minutes=57)
            rule = None
            format = 'IMT'
        elif(dt < datetime(1930,6,21,0,0)):
            offset = timedelta(seconds=0, hours=7, minutes=0)
            rule = None
            format = 'IRKT'
        elif(dt < datetime(1991,3,31,2,0)):
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = _Russia
            format = 'IRK%sT'
        elif(dt < datetime(1992,1,19,2,0)):
            offset = timedelta(seconds=0, hours=7, minutes=0)
            rule = _Russia
            format = 'IRK%sT'
        elif(dt < datetime(2011,3,27,2,0)):
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = _Russia
            format = 'IRK%sT'
        elif(dt < datetime(2014,10,26,2,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = None
            format = 'IRKT'
        else:
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = None
            format = 'IRKT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Niamey(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1912,1,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=8)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1934,2,26,0,0)):
            offset = timedelta(seconds=0, hours=-1, minutes=0)
            rule = None
            format = 'WAT'
        elif(dt < datetime(1960,1,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = None
            format = 'GMT'
        else:
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = None
            format = 'WAT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Belem(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1914,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-13)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1988,9,12,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Brazil
            format = 'BR%sT'
        else:
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'BRT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Indiana_Marengo(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1883,11,18,12,14)):
            offset = timedelta(seconds=0, hours=-5, minutes=-45)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1951,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _US
            format = 'C%sT'
        elif(dt < datetime(1961,4,30,2,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Marengo
            format = 'C%sT'
        elif(dt < datetime(1969,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        elif(dt < datetime(1974,1,1,6,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _US
            format = 'E%sT'
        elif(dt < datetime(1974,10,27,2,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _rule_constant_1hour
            format = 'CDT'
        elif(dt < datetime(1976,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _US
            format = 'E%sT'
        elif(dt < datetime(2006,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        else:
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _US
            format = 'E%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Vilnius(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1880,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=41)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1917,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=24)
            rule = None
            format = 'WMT'
        elif(dt < datetime(1919,10,10,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=35)
            rule = None
            format = 'KMT'
        elif(dt < datetime(1920,7,12,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = None
            format = 'CET'
        elif(dt < datetime(1920,10,1,9,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'EET'
        elif(dt < datetime(1940,8,1,3,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = None
            format = 'CET'
        elif(dt < datetime(1941,6,24,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'MSK'
        elif(dt < datetime(1944,8,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _C_Eur
            format = 'CE%sT'
        elif(dt < datetime(1991,3,31,2,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = _Russia
            format = 'MSK/MSD'
        elif(dt < datetime(1991,9,29,2,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _rule_constant_1hour
            format = 'EEST'
        elif(dt < datetime(1998,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _C_Eur
            format = 'EE%sT'
        elif(dt < datetime(1998,3,29,1,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'EET'
        elif(dt < datetime(1999,10,31,1,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _EU
            format = 'CE%sT'
        elif(dt < datetime(2003,1,1,1,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'EET'
        else:
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _EU
            format = 'EE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Cayenne(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1911,7,1,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-29)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1967,10,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'GFT'
        else:
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'GFT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Mogadishu(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1893,11,1,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=1)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1931,1,1,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'EAT'
        elif(dt < datetime(1957,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=30)
            rule = None
            format = 'BEAT'
        else:
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'EAT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Kentucky_Monticello(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1883,11,18,12,20)):
            offset = timedelta(seconds=0, hours=-5, minutes=-39)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1946,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _US
            format = 'C%sT'
        elif(dt < datetime(1968,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = None
            format = 'CST'
        elif(dt < datetime(2000,10,29,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _US
            format = 'C%sT'
        else:
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _US
            format = 'E%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Rio_Branco(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1914,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-31)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1988,9,12,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _Brazil
            format = 'AC%sT'
        elif(dt < datetime(2008,6,24,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'ACT'
        elif(dt < datetime(2013,11,10,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'AMT'
        else:
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'ACT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Cancun(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1922,1,1,1,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=-47)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1981,12,23,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = None
            format = 'CST'
        elif(dt < datetime(1998,8,1,2,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _Mexico
            format = 'E%sT'
        else:
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Mexico
            format = 'C%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Havana(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1890,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=-29)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1925,7,19,12,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=-29)
            rule = None
            format = 'HMT'
        else:
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _Cuba
            format = 'C%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Pacific_Guam(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1844,12,31,0,0)):
            offset = timedelta(seconds=0, hours=-14, minutes=-21)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1901,1,1,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=39)
            rule = None
            format = 'LMT'
        elif(dt < datetime(2000,12,23,0,0)):
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = None
            format = 'GST'
        else:
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = None
            format = 'ChST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Pacific_Kosrae(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1901,1,1,0,0)):
            offset = timedelta(seconds=0, hours=10, minutes=51)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1969,10,1,0,0)):
            offset = timedelta(seconds=0, hours=11, minutes=0)
            rule = None
            format = 'KOST'
        elif(dt < datetime(1999,1,1,0,0)):
            offset = timedelta(seconds=0, hours=12, minutes=0)
            rule = None
            format = 'KOST'
        else:
            offset = timedelta(seconds=0, hours=11, minutes=0)
            rule = None
            format = 'KOST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Atlantic_Azores(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1884,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-1, minutes=-42)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1911,5,24,0,0)):
            offset = timedelta(seconds=0, hours=-1, minutes=-54)
            rule = None
            format = 'HMT'
        elif(dt < datetime(1966,4,1,3,0)):
            offset = timedelta(seconds=0, hours=-2, minutes=0)
            rule = _Port
            format = 'AZO%sT'
        elif(dt < datetime(1983,9,25,1,0)):
            offset = timedelta(seconds=0, hours=-1, minutes=0)
            rule = _Port
            format = 'AZO%sT'
        elif(dt < datetime(1992,9,27,1,0)):
            offset = timedelta(seconds=0, hours=-1, minutes=0)
            rule = _W_Eur
            format = 'AZO%sT'
        elif(dt < datetime(1993,3,28,1,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = _EU
            format = 'WE%sT'
        else:
            offset = timedelta(seconds=0, hours=-1, minutes=0)
            rule = _EU
            format = 'AZO%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Australia_Eucla(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1895,12,1,0,0)):
            offset = timedelta(seconds=0, hours=8, minutes=35)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1943,7,1,0,0)):
            offset = timedelta(seconds=0, hours=8, minutes=45)
            rule = _Aus
            format = 'ACW%sT'
        else:
            offset = timedelta(seconds=0, hours=8, minutes=45)
            rule = _AW
            format = 'ACW%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Shanghai(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1901,1,1,0,0)):
            offset = timedelta(seconds=0, hours=8, minutes=5)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1949,1,1,0,0)):
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = _Shang
            format = 'C%sT'
        else:
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = _PRC
            format = 'C%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Rankin_Inlet(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1957,1,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = None
            format = 'zzz'
        elif(dt < datetime(2000,10,29,2,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _NT_YK
            format = 'C%sT'
        elif(dt < datetime(2001,4,1,1,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        else:
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Canada
            format = 'C%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Beirut(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1880,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=22)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _Lebanon
            format = 'EE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Maputo(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1903,3,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=10)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'CAT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Bahrain(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1920,1,1,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=22)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1972,6,1,0,0)):
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = None
            format = 'GST'
        else:
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'AST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Ashgabat(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1924,5,1,2,0)):
            offset = timedelta(seconds=0, hours=3, minutes=53)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1930,6,21,0,0)):
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = None
            format = 'ASHT'
        elif(dt < datetime(1991,3,31,2,0)):
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = _RussiaAsia
            format = 'ASH%sT'
        elif(dt < datetime(1991,10,27,0,0)):
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = _RussiaAsia
            format = 'ASH%sT'
        elif(dt < datetime(1992,1,19,2,0)):
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = _RussiaAsia
            format = 'TM%sT'
        else:
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = None
            format = 'TMT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Riyadh(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1947,3,14,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=6)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'AST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_London(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1847,12,1,1,0)):
            offset = timedelta(seconds=0, hours=0, minutes=-1)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1968,10,27,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = _GB_Eire
            format = '%s'
        elif(dt < datetime(1971,10,31,2,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = None
            format = 'BST'
        elif(dt < datetime(1996,1,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = _GB_Eire
            format = '%s'
        else:
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = _EU
            format = 'GMT/BST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Warsaw(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1880,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=24)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1915,8,1,5,0)):
            offset = timedelta(seconds=0, hours=1, minutes=24)
            rule = None
            format = 'WMT'
        elif(dt < datetime(1918,9,16,3,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _C_Eur
            format = 'CE%sT'
        elif(dt < datetime(1922,6,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _Poland
            format = 'EE%sT'
        elif(dt < datetime(1940,6,23,2,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _Poland
            format = 'CE%sT'
        elif(dt < datetime(1944,10,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _C_Eur
            format = 'CE%sT'
        elif(dt < datetime(1977,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _Poland
            format = 'CE%sT'
        elif(dt < datetime(1988,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _W_Eur
            format = 'CE%sT'
        else:
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _EU
            format = 'CE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Damascus(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1920,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=25)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _Syria
            format = 'EE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_North_Dakota_Center(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1883,11,18,12,14)):
            offset = timedelta(seconds=0, hours=-6, minutes=-45)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1992,10,25,2,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = _US
            format = 'M%sT'
        else:
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _US
            format = 'C%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Indiana_Vevay(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1883,11,18,12,19)):
            offset = timedelta(seconds=0, hours=-5, minutes=-40)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1954,4,25,2,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _US
            format = 'C%sT'
        elif(dt < datetime(1969,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        elif(dt < datetime(1973,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _US
            format = 'E%sT'
        elif(dt < datetime(2006,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        else:
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _US
            format = 'E%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Barbados(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1924,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-58)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1932,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-58)
            rule = None
            format = 'BMT'
        else:
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Barb
            format = 'A%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Atlantic_Faroe(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1908,1,11,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=-27)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1981,1,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = None
            format = 'WET'
        else:
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = _EU
            format = 'WE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Almaty(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1924,5,1,2,0)):
            offset = timedelta(seconds=0, hours=5, minutes=7)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1930,6,21,0,0)):
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = None
            format = 'ALMT'
        elif(dt < datetime(1991,1,1,0,0)):
            offset = timedelta(seconds=0, hours=6, minutes=0)
            rule = _RussiaAsia
            format = 'ALM%sT'
        elif(dt < datetime(1992,1,1,0,0)):
            offset = timedelta(seconds=0, hours=6, minutes=0)
            rule = None
            format = 'ALMT'
        elif(dt < datetime(2005,3,15,0,0)):
            offset = timedelta(seconds=0, hours=6, minutes=0)
            rule = _RussiaAsia
            format = 'ALM%sT'
        else:
            offset = timedelta(seconds=0, hours=6, minutes=0)
            rule = None
            format = 'ALMT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Santo_Domingo(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1890,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-39)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1933,4,1,1,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-40)
            rule = None
            format = 'SDMT'
        elif(dt < datetime(1974,10,27,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _DR
            format = 'E%sT'
        elif(dt < datetime(2000,10,29,2,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'AST'
        elif(dt < datetime(2000,12,1,3,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _US
            format = 'E%sT'
        else:
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'AST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Brazzaville(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1912,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=1)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = None
            format = 'WAT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Nome(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1867,10,18,0,0)):
            offset = timedelta(seconds=0, hours=12, minutes=58)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1900,8,20,12,0)):
            offset = timedelta(seconds=0, hours=-11, minutes=-1)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1942,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-11, minutes=0)
            rule = None
            format = 'NST'
        elif(dt < datetime(1946,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-11, minutes=0)
            rule = _US
            format = 'N%sT'
        elif(dt < datetime(1967,4,1,0,0)):
            offset = timedelta(seconds=0, hours=-11, minutes=0)
            rule = None
            format = 'NST'
        elif(dt < datetime(1969,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-11, minutes=0)
            rule = None
            format = 'BST'
        elif(dt < datetime(1983,10,30,2,0)):
            offset = timedelta(seconds=0, hours=-11, minutes=0)
            rule = _US
            format = 'B%sT'
        elif(dt < datetime(1983,11,30,0,0)):
            offset = timedelta(seconds=0, hours=-9, minutes=0)
            rule = _US
            format = 'Y%sT'
        else:
            offset = timedelta(seconds=0, hours=-9, minutes=0)
            rule = _US
            format = 'AK%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Dublin(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1880,8,1,2,0)):
            offset = timedelta(seconds=0, hours=0, minutes=-25)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1916,5,21,2,0)):
            offset = timedelta(seconds=0, hours=0, minutes=-25)
            rule = None
            format = 'DMT'
        elif(dt < datetime(1916,10,1,1,0)):
            offset = timedelta(seconds=0, hours=0, minutes=-25)
            rule = _rule_constant_1hour
            format = 'IST'
        elif(dt < datetime(1921,12,1,6,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = _GB_Eire
            format = '%s'
        elif(dt < datetime(1940,2,25,2,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = _GB_Eire
            format = 'GMT/IST'
        elif(dt < datetime(1946,10,1,6,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = _rule_constant_1hour
            format = 'IST'
        elif(dt < datetime(1947,3,16,2,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = None
            format = 'GMT'
        elif(dt < datetime(1947,11,1,2,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = _rule_constant_1hour
            format = 'IST'
        elif(dt < datetime(1948,4,18,2,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = None
            format = 'GMT'
        elif(dt < datetime(1968,10,27,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = _GB_Eire
            format = 'GMT/IST'
        elif(dt < datetime(1971,10,31,2,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = None
            format = 'IST'
        elif(dt < datetime(1996,1,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = _GB_Eire
            format = 'GMT/IST'
        else:
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = _EU
            format = 'GMT/IST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Yakutat(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1867,10,18,0,0)):
            offset = timedelta(seconds=0, hours=14, minutes=41)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1900,8,20,12,0)):
            offset = timedelta(seconds=0, hours=-9, minutes=-18)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1942,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-9, minutes=0)
            rule = None
            format = 'YST'
        elif(dt < datetime(1946,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-9, minutes=0)
            rule = _US
            format = 'Y%sT'
        elif(dt < datetime(1969,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-9, minutes=0)
            rule = None
            format = 'YST'
        elif(dt < datetime(1983,11,30,0,0)):
            offset = timedelta(seconds=0, hours=-9, minutes=0)
            rule = _US
            format = 'Y%sT'
        else:
            offset = timedelta(seconds=0, hours=-9, minutes=0)
            rule = _US
            format = 'AK%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Argentina_Mendoza(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1894,10,31,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-35)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1920,5,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-16)
            rule = None
            format = 'CMT'
        elif(dt < datetime(1930,12,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'ART'
        elif(dt < datetime(1969,10,1,5,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(1990,3,1,4,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(1990,10,15,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'WART'
        elif(dt < datetime(1991,3,1,1,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _rule_constant_1hour
            format = 'WARST'
        elif(dt < datetime(1991,10,15,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'WART'
        elif(dt < datetime(1992,3,1,1,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _rule_constant_1hour
            format = 'WARST'
        elif(dt < datetime(1992,10,18,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'WART'
        elif(dt < datetime(1999,10,1,3,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(2000,3,1,3,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(2004,5,23,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'ART'
        elif(dt < datetime(2004,9,26,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'WART'
        elif(dt < datetime(2008,10,18,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        else:
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'ART'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Araguaina(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1914,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-12)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1990,9,17,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Brazil
            format = 'BR%sT'
        elif(dt < datetime(1995,9,14,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'BRT'
        elif(dt < datetime(2003,9,24,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Brazil
            format = 'BR%sT'
        elif(dt < datetime(2012,10,21,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'BRT'
        elif(dt < datetime(2013,9,1,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Brazil
            format = 'BR%sT'
        else:
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'BRT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Etc_UTC(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=0, minutes=0)
        rule = None
        format = 'UTC'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Minsk(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1880,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=50)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1924,5,2,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=50)
            rule = None
            format = 'MMT'
        elif(dt < datetime(1930,6,21,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'EET'
        elif(dt < datetime(1941,6,28,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'MSK'
        elif(dt < datetime(1944,7,1,3,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _C_Eur
            format = 'CE%sT'
        elif(dt < datetime(1990,1,1,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = _Russia
            format = 'MSK/MSD'
        elif(dt < datetime(1991,3,31,2,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'MSK'
        elif(dt < datetime(1991,9,29,2,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _rule_constant_1hour
            format = 'EEST'
        elif(dt < datetime(1992,3,29,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'EET'
        elif(dt < datetime(1992,9,27,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _rule_constant_1hour
            format = 'EEST'
        elif(dt < datetime(2011,3,27,2,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _Russia
            format = 'EE%sT'
        else:
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'FET'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Kolkata(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1880,1,1,0,0)):
            offset = timedelta(seconds=0, hours=5, minutes=53)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1941,10,1,0,0)):
            offset = timedelta(seconds=0, hours=5, minutes=53)
            rule = None
            format = 'HMT'
        elif(dt < datetime(1942,5,15,0,0)):
            offset = timedelta(seconds=0, hours=6, minutes=30)
            rule = None
            format = 'BURT'
        elif(dt < datetime(1942,9,1,0,0)):
            offset = timedelta(seconds=0, hours=5, minutes=30)
            rule = None
            format = 'IST'
        elif(dt < datetime(1945,10,15,0,0)):
            offset = timedelta(seconds=0, hours=5, minutes=30)
            rule = _rule_constant_1hour
            format = 'IST'
        else:
            offset = timedelta(seconds=0, hours=5, minutes=30)
            rule = None
            format = 'IST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Maseru(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1903,3,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=50)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1943,9,19,2,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'SAST'
        elif(dt < datetime(1944,3,19,2,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _rule_constant_1hour
            format = 'SAST'
        else:
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'SAST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Atikokan(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1895,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=-6)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1940,9,29,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Canada
            format = 'C%sT'
        elif(dt < datetime(1942,2,1,9,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _rule_constant_1hour
            format = 'CDT'
        elif(dt < datetime(1945,9,30,2,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Canada
            format = 'C%sT'
        else:
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Santa_Isabel(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1922,1,1,1,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=-39)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1924,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = None
            format = 'MST'
        elif(dt < datetime(1927,6,10,23,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = None
            format = 'PST'
        elif(dt < datetime(1930,11,15,0,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = None
            format = 'MST'
        elif(dt < datetime(1931,4,1,1,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = None
            format = 'PST'
        elif(dt < datetime(1931,9,30,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _rule_constant_1hour
            format = 'PDT'
        elif(dt < datetime(1942,4,24,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = None
            format = 'PST'
        elif(dt < datetime(1945,8,14,23,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _rule_constant_1hour
            format = 'PWT'
        elif(dt < datetime(1945,11,12,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _rule_constant_1hour
            format = 'PPT'
        elif(dt < datetime(1948,4,1,5,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = None
            format = 'PST'
        elif(dt < datetime(1949,1,14,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _rule_constant_1hour
            format = 'PDT'
        elif(dt < datetime(1954,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = None
            format = 'PST'
        elif(dt < datetime(1961,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _CA
            format = 'P%sT'
        elif(dt < datetime(1976,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = None
            format = 'PST'
        elif(dt < datetime(1996,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _US
            format = 'P%sT'
        elif(dt < datetime(2001,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _Mexico
            format = 'P%sT'
        elif(dt < datetime(2002,2,20,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _US
            format = 'P%sT'
        else:
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _Mexico
            format = 'P%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Kuching(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1926,3,1,0,0)):
            offset = timedelta(seconds=0, hours=7, minutes=21)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1933,1,1,0,0)):
            offset = timedelta(seconds=0, hours=7, minutes=30)
            rule = None
            format = 'BORT'
        elif(dt < datetime(1942,2,16,0,0)):
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = _NBorneo
            format = 'BOR%sT'
        elif(dt < datetime(1945,9,12,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = None
            format = 'JST'
        elif(dt < datetime(1982,1,1,1,0)):
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = None
            format = 'BORT'
        else:
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = None
            format = 'MYT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Libreville(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1912,1,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=37)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = None
            format = 'WAT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Bissau(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1911,5,26,0,0)):
            offset = timedelta(seconds=0, hours=-1, minutes=-2)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1975,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-1, minutes=0)
            rule = None
            format = 'WAT'
        else:
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = None
            format = 'GMT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Samara(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1919,7,1,1,0)):
            offset = timedelta(seconds=0, hours=3, minutes=20)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1930,6,21,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'SAMT'
        elif(dt < datetime(1935,1,27,0,0)):
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = None
            format = 'SAMT'
        elif(dt < datetime(1989,3,26,2,0)):
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = _Russia
            format = 'KUY%sT'
        elif(dt < datetime(1991,3,31,2,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = _Russia
            format = 'MSK/MSD'
        elif(dt < datetime(1991,9,29,2,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _Russia
            format = 'EE%sT'
        elif(dt < datetime(1991,10,20,3,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'KUYT'
        elif(dt < datetime(2010,3,28,2,0)):
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = _Russia
            format = 'SAM%sT'
        elif(dt < datetime(2011,3,27,2,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = _Russia
            format = 'SAM%sT'
        else:
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = None
            format = 'SAMT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Amsterdam(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1835,1,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=19)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1937,7,1,1,0)):
            offset = timedelta(seconds=0, hours=0, minutes=19)
            rule = _Neth
            format = '%s'
        elif(dt < datetime(1940,5,16,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=20)
            rule = _Neth
            format = 'NE%sT'
        elif(dt < datetime(1945,4,1,2,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _C_Eur
            format = 'CE%sT'
        elif(dt < datetime(1977,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _Neth
            format = 'CE%sT'
        else:
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _EU
            format = 'CE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Tirane(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1914,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=19)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1940,6,16,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = None
            format = 'CET'
        elif(dt < datetime(1984,7,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _Albania
            format = 'CE%sT'
        else:
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _EU
            format = 'CE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Pacific_Saipan(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1844,12,31,0,0)):
            offset = timedelta(seconds=0, hours=-14, minutes=-17)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1901,1,1,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=43)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1969,10,1,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = None
            format = 'MPT'
        elif(dt < datetime(2000,12,23,0,0)):
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = None
            format = 'MPT'
        else:
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = None
            format = 'ChST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Magadan(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1924,5,1,2,0)):
            offset = timedelta(seconds=0, hours=10, minutes=3)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1930,6,21,0,0)):
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = None
            format = 'MAGT'
        elif(dt < datetime(1991,3,31,2,0)):
            offset = timedelta(seconds=0, hours=11, minutes=0)
            rule = _Russia
            format = 'MAG%sT'
        elif(dt < datetime(1992,1,19,2,0)):
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = _Russia
            format = 'MAG%sT'
        elif(dt < datetime(2011,3,27,2,0)):
            offset = timedelta(seconds=0, hours=11, minutes=0)
            rule = _Russia
            format = 'MAG%sT'
        elif(dt < datetime(2014,10,26,2,0)):
            offset = timedelta(seconds=0, hours=12, minutes=0)
            rule = None
            format = 'MAGT'
        else:
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = None
            format = 'MAGT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Zaporozhye(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1880,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=20)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1924,5,1,2,0)):
            offset = timedelta(seconds=0, hours=2, minutes=20)
            rule = None
            format = 'CUT'
        elif(dt < datetime(1930,6,21,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'EET'
        elif(dt < datetime(1941,8,25,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'MSK'
        elif(dt < datetime(1943,10,25,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _C_Eur
            format = 'CE%sT'
        elif(dt < datetime(1991,3,31,2,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = _Russia
            format = 'MSK/MSD'
        elif(dt < datetime(1995,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _E_Eur
            format = 'EE%sT'
        else:
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _EU
            format = 'EE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class HST(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=-10, minutes=0)
        rule = None
        format = 'HST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_El_Salvador(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1921,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=-56)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Salv
            format = 'C%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Madrid(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1901,1,1,1,0)):
            offset = timedelta(seconds=0, hours=0, minutes=-14)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1946,9,30,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = _Spain
            format = 'WE%sT'
        elif(dt < datetime(1979,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _Spain
            format = 'CE%sT'
        else:
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _EU
            format = 'CE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Santiago(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1890,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-42)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1910,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-42)
            rule = None
            format = 'SMT'
        elif(dt < datetime(1916,7,1,1,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'CLT'
        elif(dt < datetime(1918,9,1,1,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-42)
            rule = None
            format = 'SMT'
        elif(dt < datetime(1919,7,1,1,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'CLT'
        elif(dt < datetime(1927,9,1,1,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-42)
            rule = None
            format = 'SMT'
        elif(dt < datetime(1947,5,22,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _Chile
            format = 'CL%sT'
        else:
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Chile
            format = 'CL%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Argentina_Buenos_Aires(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1894,10,31,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-53)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1920,5,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-16)
            rule = None
            format = 'CMT'
        elif(dt < datetime(1930,12,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'ART'
        elif(dt < datetime(1969,10,1,5,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(1999,10,1,3,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(2000,3,1,3,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        else:
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Argentina_San_Luis(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1894,10,31,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-25)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1920,5,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-16)
            rule = None
            format = 'CMT'
        elif(dt < datetime(1930,12,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'ART'
        elif(dt < datetime(1969,10,1,5,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(1990,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(1990,3,14,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _rule_constant_1hour
            format = 'ARST'
        elif(dt < datetime(1990,10,15,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'WART'
        elif(dt < datetime(1991,3,1,1,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _rule_constant_1hour
            format = 'WARST'
        elif(dt < datetime(1991,6,1,1,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'WART'
        elif(dt < datetime(1999,10,1,3,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'ART'
        elif(dt < datetime(2000,3,1,3,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _rule_constant_1hour
            format = 'WARST'
        elif(dt < datetime(2004,5,31,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'ART'
        elif(dt < datetime(2004,7,25,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'WART'
        elif(dt < datetime(2008,1,21,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(2009,10,11,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _SanLuis
            format = 'WAR%sT'
        else:
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'ART'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class WET(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=0, minutes=0)
        rule = _EU
        format = 'WE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Regina(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1905,9,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=-58)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1960,4,1,0,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = _Regina
            format = 'M%sT'
        else:
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = None
            format = 'CST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Pacific_Chuuk(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1901,1,1,0,0)):
            offset = timedelta(seconds=0, hours=10, minutes=7)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = None
            format = 'CHUT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Khandyga(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1919,12,15,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=2)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1930,6,21,0,0)):
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = None
            format = 'YAKT'
        elif(dt < datetime(1991,3,31,2,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = _Russia
            format = 'YAK%sT'
        elif(dt < datetime(1992,1,19,2,0)):
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = _Russia
            format = 'YAK%sT'
        elif(dt < datetime(2004,1,1,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = _Russia
            format = 'YAK%sT'
        elif(dt < datetime(2011,3,27,2,0)):
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = _Russia
            format = 'VLA%sT'
        elif(dt < datetime(2011,9,13,0,0)):
            offset = timedelta(seconds=0, hours=11, minutes=0)
            rule = None
            format = 'VLAT'
        elif(dt < datetime(2014,10,26,2,0)):
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = None
            format = 'YAKT'
        else:
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = None
            format = 'YAKT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Pacific_Funafuti(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1901,1,1,0,0)):
            offset = timedelta(seconds=0, hours=11, minutes=56)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=12, minutes=0)
            rule = None
            format = 'TVT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Merida(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1922,1,1,1,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=-58)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1981,12,23,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = None
            format = 'CST'
        elif(dt < datetime(1982,12,1,2,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        else:
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Mexico
            format = 'C%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Guatemala(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1918,10,5,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=-2)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Guat
            format = 'C%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Makassar(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1920,1,1,0,0)):
            offset = timedelta(seconds=0, hours=7, minutes=57)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1932,11,1,0,0)):
            offset = timedelta(seconds=0, hours=7, minutes=57)
            rule = None
            format = 'MMT'
        elif(dt < datetime(1942,2,1,9,0)):
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = None
            format = 'WITA'
        elif(dt < datetime(1945,9,23,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = None
            format = 'JST'
        else:
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = None
            format = 'WITA'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Bujumbura(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1890,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=57)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'CAT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Chisinau(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1880,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=55)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1918,2,15,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=55)
            rule = None
            format = 'CMT'
        elif(dt < datetime(1931,7,24,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=44)
            rule = None
            format = 'BMT'
        elif(dt < datetime(1940,8,15,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _Romania
            format = 'EE%sT'
        elif(dt < datetime(1941,7,17,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _rule_constant_1hour
            format = 'EEST'
        elif(dt < datetime(1944,8,24,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _C_Eur
            format = 'CE%sT'
        elif(dt < datetime(1990,1,1,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = _Russia
            format = 'MSK/MSD'
        elif(dt < datetime(1990,5,6,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'MSK'
        elif(dt < datetime(1991,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'EET'
        elif(dt < datetime(1992,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _Russia
            format = 'EE%sT'
        elif(dt < datetime(1997,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _E_Eur
            format = 'EE%sT'
        else:
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _EU
            format = 'EE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Monterrey(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1921,12,31,23,18)):
            offset = timedelta(seconds=0, hours=-6, minutes=-41)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1988,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = None
            format = 'CST'
        elif(dt < datetime(1989,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _US
            format = 'C%sT'
        else:
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Mexico
            format = 'C%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Yekaterinburg(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1919,7,15,4,0)):
            offset = timedelta(seconds=0, hours=4, minutes=2)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1930,6,21,0,0)):
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = None
            format = 'SVET'
        elif(dt < datetime(1991,3,31,2,0)):
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = _Russia
            format = 'SVE%sT'
        elif(dt < datetime(1992,1,19,2,0)):
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = _Russia
            format = 'SVE%sT'
        elif(dt < datetime(2011,3,27,2,0)):
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = _Russia
            format = 'YEK%sT'
        elif(dt < datetime(2014,10,26,2,0)):
            offset = timedelta(seconds=0, hours=6, minutes=0)
            rule = None
            format = 'YEKT'
        else:
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = None
            format = 'YEKT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Pacific_Enderbury(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1901,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-11, minutes=-24)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1979,10,1,0,0)):
            offset = timedelta(seconds=0, hours=-12, minutes=0)
            rule = None
            format = 'PHOT'
        elif(dt < datetime(1995,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-11, minutes=0)
            rule = None
            format = 'PHOT'
        else:
            offset = timedelta(seconds=0, hours=13, minutes=0)
            rule = None
            format = 'PHOT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Thule(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1916,7,28,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-35)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Thule
            format = 'A%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_St_Johns(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1884,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-30)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1918,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-30)
            rule = _StJohns
            format = 'N%sT'
        elif(dt < datetime(1919,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-30)
            rule = _Canada
            format = 'N%sT'
        elif(dt < datetime(1935,3,30,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-30)
            rule = _StJohns
            format = 'N%sT'
        elif(dt < datetime(1942,5,11,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-30)
            rule = _StJohns
            format = 'N%sT'
        elif(dt < datetime(1946,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-30)
            rule = _Canada
            format = 'N%sT'
        elif(dt < datetime(2011,11,1,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-30)
            rule = _StJohns
            format = 'N%sT'
        else:
            offset = timedelta(seconds=0, hours=-3, minutes=-30)
            rule = _Canada
            format = 'N%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Moncton(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1883,12,1,9,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-19)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1902,6,15,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        elif(dt < datetime(1933,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Canada
            format = 'A%sT'
        elif(dt < datetime(1942,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Moncton
            format = 'A%sT'
        elif(dt < datetime(1946,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Canada
            format = 'A%sT'
        elif(dt < datetime(1973,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Moncton
            format = 'A%sT'
        elif(dt < datetime(1993,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Canada
            format = 'A%sT'
        elif(dt < datetime(2007,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Moncton
            format = 'A%sT'
        else:
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Canada
            format = 'A%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Helsinki(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1878,5,31,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=39)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1921,5,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=39)
            rule = None
            format = 'HMT'
        elif(dt < datetime(1983,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _Finland
            format = 'EE%sT'
        else:
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _EU
            format = 'EE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Atlantic_Cape_Verde(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1907,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-1, minutes=-34)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1942,9,1,0,0)):
            offset = timedelta(seconds=0, hours=-2, minutes=0)
            rule = None
            format = 'CVT'
        elif(dt < datetime(1945,10,15,0,0)):
            offset = timedelta(seconds=0, hours=-2, minutes=0)
            rule = _rule_constant_1hour
            format = 'CVST'
        elif(dt < datetime(1975,11,25,2,0)):
            offset = timedelta(seconds=0, hours=-2, minutes=0)
            rule = None
            format = 'CVT'
        else:
            offset = timedelta(seconds=0, hours=-1, minutes=0)
            rule = None
            format = 'CVT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Tegucigalpa(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1921,4,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=-48)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Hond
            format = 'C%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Indian_Cocos(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1900,1,1,0,0)):
            offset = timedelta(seconds=0, hours=6, minutes=27)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=6, minutes=30)
            rule = None
            format = 'CCT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Boise(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1883,11,18,12,15)):
            offset = timedelta(seconds=0, hours=-7, minutes=-44)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1923,5,13,2,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _US
            format = 'P%sT'
        elif(dt < datetime(1974,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = _US
            format = 'M%sT'
        elif(dt < datetime(1974,2,1,3,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = None
            format = 'MST'
        else:
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = _US
            format = 'M%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Nassau(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1912,3,2,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=-9)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1976,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _Bahamas
            format = 'E%sT'
        else:
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _US
            format = 'E%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Prague(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1850,1,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=57)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1891,10,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=57)
            rule = None
            format = 'PMT'
        elif(dt < datetime(1944,9,17,2,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _C_Eur
            format = 'CE%sT'
        elif(dt < datetime(1979,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _Czech
            format = 'CE%sT'
        else:
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _EU
            format = 'CE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Halifax(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1902,6,15,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-14)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1918,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Halifax
            format = 'A%sT'
        elif(dt < datetime(1919,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Canada
            format = 'A%sT'
        elif(dt < datetime(1942,2,1,9,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Halifax
            format = 'A%sT'
        elif(dt < datetime(1946,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Canada
            format = 'A%sT'
        elif(dt < datetime(1974,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Halifax
            format = 'A%sT'
        else:
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Canada
            format = 'A%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Hovd(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1905,8,1,0,0)):
            offset = timedelta(seconds=0, hours=6, minutes=6)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1978,1,1,0,0)):
            offset = timedelta(seconds=0, hours=6, minutes=0)
            rule = None
            format = 'HOVT'
        else:
            offset = timedelta(seconds=0, hours=7, minutes=0)
            rule = _Mongol
            format = 'HOV%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Manaus(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1914,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1988,9,12,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Brazil
            format = 'AM%sT'
        elif(dt < datetime(1993,9,28,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'AMT'
        elif(dt < datetime(1994,9,22,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Brazil
            format = 'AM%sT'
        else:
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'AMT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Godthab(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1916,7,28,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-26)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1980,4,1,6,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'WGT'
        else:
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _EU
            format = 'WG%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Etc_UCT(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=0, minutes=0)
        rule = None
        format = 'UCT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_North_Dakota_Beulah(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1883,11,18,12,12)):
            offset = timedelta(seconds=0, hours=-6, minutes=-47)
            rule = None
            format = 'LMT'
        elif(dt < datetime(2010,11,1,7,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = _US
            format = 'M%sT'
        else:
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _US
            format = 'C%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Chihuahua(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1921,12,31,23,55)):
            offset = timedelta(seconds=0, hours=-7, minutes=-4)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1927,6,10,23,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = None
            format = 'MST'
        elif(dt < datetime(1930,11,15,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = None
            format = 'CST'
        elif(dt < datetime(1931,5,1,1,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = None
            format = 'MST'
        elif(dt < datetime(1931,10,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = None
            format = 'CST'
        elif(dt < datetime(1932,4,1,1,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = None
            format = 'MST'
        elif(dt < datetime(1996,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = None
            format = 'CST'
        elif(dt < datetime(1998,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Mexico
            format = 'C%sT'
        elif(dt < datetime(1998,4,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = None
            format = 'CST'
        else:
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = _Mexico
            format = 'M%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Iqaluit(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1942,8,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = None
            format = 'zzz'
        elif(dt < datetime(1999,10,31,2,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _NT_YK
            format = 'E%sT'
        elif(dt < datetime(2000,10,29,2,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Canada
            format = 'C%sT'
        else:
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _Canada
            format = 'E%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Argentina_Rio_Gallegos(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1894,10,31,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-36)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1920,5,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-16)
            rule = None
            format = 'CMT'
        elif(dt < datetime(1930,12,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'ART'
        elif(dt < datetime(1969,10,1,5,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(1999,10,1,3,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(2000,3,1,3,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(2004,6,1,1,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'ART'
        elif(dt < datetime(2004,6,20,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'WART'
        elif(dt < datetime(2008,10,18,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        else:
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'ART'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Pacific_Gambier(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1912,10,1,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=-59)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=-9, minutes=0)
            rule = None
            format = 'GAMT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Volgograd(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1920,1,1,3,0)):
            offset = timedelta(seconds=0, hours=2, minutes=57)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1925,4,1,6,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'TSAT'
        elif(dt < datetime(1930,6,21,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'STAT'
        elif(dt < datetime(1961,11,11,0,0)):
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = None
            format = 'STAT'
        elif(dt < datetime(1989,3,26,2,0)):
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = _Russia
            format = 'VOL%sT'
        elif(dt < datetime(1991,3,31,2,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = _Russia
            format = 'VOL%sT'
        elif(dt < datetime(1992,3,29,2,0)):
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = None
            format = 'VOLT'
        elif(dt < datetime(2011,3,27,2,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = _Russia
            format = 'MSK'
        elif(dt < datetime(2014,10,26,2,0)):
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = None
            format = 'MSK'
        else:
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'MSK'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Novokuznetsk(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1920,1,1,6,0)):
            offset = timedelta(seconds=0, hours=5, minutes=48)
            rule = None
            format = 'NMT'
        elif(dt < datetime(1930,6,21,0,0)):
            offset = timedelta(seconds=0, hours=6, minutes=0)
            rule = None
            format = 'KRAT'
        elif(dt < datetime(1991,3,31,2,0)):
            offset = timedelta(seconds=0, hours=7, minutes=0)
            rule = _Russia
            format = 'KRA%sT'
        elif(dt < datetime(1992,1,19,2,0)):
            offset = timedelta(seconds=0, hours=6, minutes=0)
            rule = _Russia
            format = 'KRA%sT'
        elif(dt < datetime(2010,3,28,2,0)):
            offset = timedelta(seconds=0, hours=7, minutes=0)
            rule = _Russia
            format = 'KRA%sT'
        elif(dt < datetime(2011,3,27,2,0)):
            offset = timedelta(seconds=0, hours=6, minutes=0)
            rule = _Russia
            format = 'NOV%sT'
        elif(dt < datetime(2014,10,26,2,0)):
            offset = timedelta(seconds=0, hours=7, minutes=0)
            rule = None
            format = 'NOVT'
        else:
            offset = timedelta(seconds=0, hours=7, minutes=0)
            rule = None
            format = 'KRAT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Uzhgorod(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1890,10,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=29)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1940,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = None
            format = 'CET'
        elif(dt < datetime(1944,10,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _C_Eur
            format = 'CE%sT'
        elif(dt < datetime(1944,10,26,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _rule_constant_1hour
            format = 'CEST'
        elif(dt < datetime(1945,6,29,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = None
            format = 'CET'
        elif(dt < datetime(1990,1,1,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = _Russia
            format = 'MSK/MSD'
        elif(dt < datetime(1990,7,1,1,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'MSK'
        elif(dt < datetime(1991,3,31,3,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = None
            format = 'CET'
        elif(dt < datetime(1992,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'EET'
        elif(dt < datetime(1995,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _E_Eur
            format = 'EE%sT'
        else:
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _EU
            format = 'EE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Aqtau(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1924,5,1,2,0)):
            offset = timedelta(seconds=0, hours=3, minutes=21)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1930,6,21,0,0)):
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = None
            format = 'FORT'
        elif(dt < datetime(1963,1,1,0,0)):
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = None
            format = 'FORT'
        elif(dt < datetime(1981,10,1,1,0)):
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = None
            format = 'SHET'
        elif(dt < datetime(1982,4,1,1,0)):
            offset = timedelta(seconds=0, hours=6, minutes=0)
            rule = None
            format = 'SHET'
        elif(dt < datetime(1991,1,1,0,0)):
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = _RussiaAsia
            format = 'SHE%sT'
        elif(dt < datetime(1991,12,16,0,0)):
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = None
            format = 'SHET'
        elif(dt < datetime(1995,3,1,0,0)):
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = _RussiaAsia
            format = 'AQT%sT'
        elif(dt < datetime(2005,3,15,0,0)):
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = _RussiaAsia
            format = 'AQT%sT'
        else:
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = None
            format = 'AQTT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Pacific_Palau(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1901,1,1,0,0)):
            offset = timedelta(seconds=0, hours=8, minutes=57)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = None
            format = 'PWT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Malabo(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1912,1,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=35)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1963,12,15,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = None
            format = 'GMT'
        else:
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = None
            format = 'WAT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class PST8PDT(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=-8, minutes=0)
        rule = _US
        format = 'P%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Atlantic_Madeira(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1884,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-1, minutes=-7)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1911,5,24,0,0)):
            offset = timedelta(seconds=0, hours=-1, minutes=-7)
            rule = None
            format = 'FMT'
        elif(dt < datetime(1966,4,1,3,0)):
            offset = timedelta(seconds=0, hours=-1, minutes=0)
            rule = _Port
            format = 'MAD%sT'
        elif(dt < datetime(1983,9,25,1,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = _Port
            format = 'WE%sT'
        else:
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = _EU
            format = 'WE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Maceio(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1914,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-2, minutes=-22)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1990,9,17,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Brazil
            format = 'BR%sT'
        elif(dt < datetime(1995,10,13,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'BRT'
        elif(dt < datetime(1996,9,1,4,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Brazil
            format = 'BR%sT'
        elif(dt < datetime(1999,9,30,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'BRT'
        elif(dt < datetime(2000,10,22,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Brazil
            format = 'BR%sT'
        elif(dt < datetime(2001,9,13,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'BRT'
        elif(dt < datetime(2002,10,1,1,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Brazil
            format = 'BR%sT'
        else:
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'BRT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Kinshasa(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1897,11,9,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=1)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = None
            format = 'WAT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Malta(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1893,11,1,2,0)):
            offset = timedelta(seconds=0, hours=0, minutes=58)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1942,11,1,2,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _Italy
            format = 'CE%sT'
        elif(dt < datetime(1945,4,1,2,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _C_Eur
            format = 'CE%sT'
        elif(dt < datetime(1973,3,31,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _Italy
            format = 'CE%sT'
        elif(dt < datetime(1981,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _Malta
            format = 'CE%sT'
        else:
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _EU
            format = 'CE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Argentina_Ushuaia(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1894,10,31,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-33)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1920,5,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-16)
            rule = None
            format = 'CMT'
        elif(dt < datetime(1930,12,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'ART'
        elif(dt < datetime(1969,10,1,5,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(1999,10,1,3,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(2000,3,1,3,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(2004,5,30,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'ART'
        elif(dt < datetime(2004,6,20,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'WART'
        elif(dt < datetime(2008,10,18,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        else:
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'ART'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Bangkok(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1880,1,1,0,0)):
            offset = timedelta(seconds=0, hours=6, minutes=42)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1920,4,1,0,0)):
            offset = timedelta(seconds=0, hours=6, minutes=42)
            rule = None
            format = 'BMT'
        else:
            offset = timedelta(seconds=0, hours=7, minutes=0)
            rule = None
            format = 'ICT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Pacific_Niue(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1901,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-11, minutes=-19)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1951,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-11, minutes=-20)
            rule = None
            format = 'NUT'
        elif(dt < datetime(1978,10,1,0,0)):
            offset = timedelta(seconds=0, hours=-11, minutes=-30)
            rule = None
            format = 'NUT'
        else:
            offset = timedelta(seconds=0, hours=-11, minutes=0)
            rule = None
            format = 'NUT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Australia_Brisbane(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1895,1,1,0,0)):
            offset = timedelta(seconds=0, hours=10, minutes=12)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1971,1,1,0,0)):
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = _Aus
            format = 'AE%sT'
        else:
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = _AQ
            format = 'AE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Recife(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1914,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-2, minutes=-19)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1990,9,17,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Brazil
            format = 'BR%sT'
        elif(dt < datetime(1999,9,30,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'BRT'
        elif(dt < datetime(2000,10,15,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Brazil
            format = 'BR%sT'
        elif(dt < datetime(2001,9,13,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'BRT'
        elif(dt < datetime(2002,10,1,1,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Brazil
            format = 'BR%sT'
        else:
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'BRT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Glace_Bay(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1902,6,15,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-59)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1953,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Canada
            format = 'A%sT'
        elif(dt < datetime(1954,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Halifax
            format = 'A%sT'
        elif(dt < datetime(1972,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'AST'
        elif(dt < datetime(1974,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Halifax
            format = 'A%sT'
        else:
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Canada
            format = 'A%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Yerevan(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1924,5,1,2,0)):
            offset = timedelta(seconds=0, hours=2, minutes=58)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1957,3,1,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'YERT'
        elif(dt < datetime(1991,3,31,2,0)):
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = _RussiaAsia
            format = 'YER%sT'
        elif(dt < datetime(1991,9,23,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = _rule_constant_1hour
            format = 'YERST'
        elif(dt < datetime(1995,9,24,2,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = _RussiaAsia
            format = 'AM%sT'
        elif(dt < datetime(1997,1,1,0,0)):
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = None
            format = 'AMT'
        elif(dt < datetime(2012,3,25,2,0)):
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = _RussiaAsia
            format = 'AM%sT'
        else:
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = None
            format = 'AMT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_La_Paz(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1890,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-32)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1931,10,15,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-32)
            rule = None
            format = 'CMT'
        elif(dt < datetime(1932,3,21,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-32)
            rule = _rule_constant_1hour
            format = 'BOST'
        else:
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'BOT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Urumqi(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1928,1,1,0,0)):
            offset = timedelta(seconds=0, hours=5, minutes=50)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=6, minutes=0)
            rule = None
            format = 'XJT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Lusaka(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1903,3,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=53)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'CAT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Pacific_Guadalcanal(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1912,10,1,0,0)):
            offset = timedelta(seconds=0, hours=10, minutes=39)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=11, minutes=0)
            rule = None
            format = 'SBT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Yellowknife(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1935,1,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = None
            format = 'zzz'
        elif(dt < datetime(1980,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = _NT_YK
            format = 'M%sT'
        else:
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = _Canada
            format = 'M%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Vientiane(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1906,6,1,9,0)):
            offset = timedelta(seconds=0, hours=6, minutes=50)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1911,3,11,0,1)):
            offset = timedelta(seconds=0, hours=7, minutes=6)
            rule = None
            format = 'SMT'
        elif(dt < datetime(1912,5,1,0,0)):
            offset = timedelta(seconds=0, hours=7, minutes=0)
            rule = None
            format = 'ICT'
        elif(dt < datetime(1931,5,1,0,0)):
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = None
            format = 'ICT'
        else:
            offset = timedelta(seconds=0, hours=7, minutes=0)
            rule = None
            format = 'ICT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Kuwait(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1950,1,1,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=11)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'AST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Argentina_Tucuman(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1894,10,31,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-20)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1920,5,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-16)
            rule = None
            format = 'CMT'
        elif(dt < datetime(1930,12,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'ART'
        elif(dt < datetime(1969,10,1,5,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(1991,3,1,3,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(1991,10,20,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'WART'
        elif(dt < datetime(1999,10,1,3,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(2000,3,1,3,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(2004,6,1,1,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'ART'
        elif(dt < datetime(2004,6,13,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'WART'
        else:
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Chita(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1919,12,15,0,0)):
            offset = timedelta(seconds=0, hours=7, minutes=33)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1930,6,21,0,0)):
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = None
            format = 'YAKT'
        elif(dt < datetime(1991,3,31,2,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = _Russia
            format = 'YAK%sT'
        elif(dt < datetime(1992,1,19,2,0)):
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = _Russia
            format = 'YAK%sT'
        elif(dt < datetime(2011,3,27,2,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = _Russia
            format = 'YAK%sT'
        elif(dt < datetime(2014,10,26,2,0)):
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = None
            format = 'YAKT'
        else:
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = None
            format = 'IRKT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Oslo(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1895,1,1,1,0)):
            offset = timedelta(seconds=0, hours=0, minutes=43)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1940,8,10,23,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _Norway
            format = 'CE%sT'
        elif(dt < datetime(1945,4,1,2,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _C_Eur
            format = 'CE%sT'
        elif(dt < datetime(1980,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _Norway
            format = 'CE%sT'
        else:
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _EU
            format = 'CE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Caracas(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1890,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-27)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1912,2,12,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-27)
            rule = None
            format = 'CMT'
        elif(dt < datetime(1965,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-30)
            rule = None
            format = 'VET'
        elif(dt < datetime(2007,12,1,9,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'VET'
        else:
            offset = timedelta(seconds=0, hours=-4, minutes=-30)
            rule = None
            format = 'VET'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Panama(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1890,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=-18)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1908,4,22,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=-19)
            rule = None
            format = 'CMT'
        else:
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Hermosillo(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1921,12,31,23,36)):
            offset = timedelta(seconds=0, hours=-7, minutes=-23)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1927,6,10,23,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = None
            format = 'MST'
        elif(dt < datetime(1930,11,15,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = None
            format = 'CST'
        elif(dt < datetime(1931,5,1,1,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = None
            format = 'MST'
        elif(dt < datetime(1931,10,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = None
            format = 'CST'
        elif(dt < datetime(1932,4,1,1,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = None
            format = 'MST'
        elif(dt < datetime(1942,4,24,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = None
            format = 'CST'
        elif(dt < datetime(1949,1,14,0,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = None
            format = 'MST'
        elif(dt < datetime(1970,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = None
            format = 'PST'
        elif(dt < datetime(1999,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = _Mexico
            format = 'M%sT'
        else:
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = None
            format = 'MST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Hebron(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1900,10,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=20)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1948,5,15,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _Zion
            format = 'EET'
        elif(dt < datetime(1967,6,1,5,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _EgyptAsia
            format = 'EE%sT'
        elif(dt < datetime(1996,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _Zion
            format = 'I%sT'
        elif(dt < datetime(1999,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _Jordan
            format = 'EE%sT'
        else:
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _Palestine
            format = 'EE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Guayaquil(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1890,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=-19)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1931,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=-14)
            rule = None
            format = 'QMT'
        else:
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'ECT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Kuala_Lumpur(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1901,1,1,1,0)):
            offset = timedelta(seconds=0, hours=6, minutes=46)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1905,6,1,1,0)):
            offset = timedelta(seconds=0, hours=6, minutes=55)
            rule = None
            format = 'SMT'
        elif(dt < datetime(1933,1,1,1,0)):
            offset = timedelta(seconds=0, hours=7, minutes=0)
            rule = None
            format = 'MALT'
        elif(dt < datetime(1936,1,1,1,0)):
            offset = timedelta(seconds=0, hours=7, minutes=0)
            rule = _rule_constant_20min
            format = 'MALST'
        elif(dt < datetime(1941,9,1,1,0)):
            offset = timedelta(seconds=0, hours=7, minutes=20)
            rule = None
            format = 'MALT'
        elif(dt < datetime(1942,2,16,0,0)):
            offset = timedelta(seconds=0, hours=7, minutes=30)
            rule = None
            format = 'MALT'
        elif(dt < datetime(1945,9,12,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = None
            format = 'JST'
        elif(dt < datetime(1982,1,1,1,0)):
            offset = timedelta(seconds=0, hours=7, minutes=30)
            rule = None
            format = 'MALT'
        else:
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = None
            format = 'MYT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Menominee(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1885,9,18,12,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=-50)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1946,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _US
            format = 'C%sT'
        elif(dt < datetime(1969,4,27,2,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Menominee
            format = 'C%sT'
        elif(dt < datetime(1973,4,29,2,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        else:
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _US
            format = 'C%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Kamchatka(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1922,11,10,0,0)):
            offset = timedelta(seconds=0, hours=10, minutes=34)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1930,6,21,0,0)):
            offset = timedelta(seconds=0, hours=11, minutes=0)
            rule = None
            format = 'PETT'
        elif(dt < datetime(1991,3,31,2,0)):
            offset = timedelta(seconds=0, hours=12, minutes=0)
            rule = _Russia
            format = 'PET%sT'
        elif(dt < datetime(1992,1,19,2,0)):
            offset = timedelta(seconds=0, hours=11, minutes=0)
            rule = _Russia
            format = 'PET%sT'
        elif(dt < datetime(2010,3,28,2,0)):
            offset = timedelta(seconds=0, hours=12, minutes=0)
            rule = _Russia
            format = 'PET%sT'
        elif(dt < datetime(2011,3,27,2,0)):
            offset = timedelta(seconds=0, hours=11, minutes=0)
            rule = _Russia
            format = 'PET%sT'
        else:
            offset = timedelta(seconds=0, hours=12, minutes=0)
            rule = None
            format = 'PETT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Factory(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=0, minutes=0)
        rule = None
        format = '"Local time zone must be set--see zic manual page"'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Vladivostok(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1922,11,15,0,0)):
            offset = timedelta(seconds=0, hours=8, minutes=47)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1930,6,21,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = None
            format = 'VLAT'
        elif(dt < datetime(1991,3,31,2,0)):
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = _Russia
            format = 'VLA%sT'
        elif(dt < datetime(1992,1,19,2,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = _Russia
            format = 'VLA%sT'
        elif(dt < datetime(2011,3,27,2,0)):
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = _Russia
            format = 'VLA%sT'
        elif(dt < datetime(2014,10,26,2,0)):
            offset = timedelta(seconds=0, hours=11, minutes=0)
            rule = None
            format = 'VLAT'
        else:
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = None
            format = 'VLAT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Matamoros(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1921,12,31,23,20)):
            offset = timedelta(seconds=0, hours=-6, minutes=-40)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1988,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = None
            format = 'CST'
        elif(dt < datetime(1989,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _US
            format = 'C%sT'
        elif(dt < datetime(2010,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Mexico
            format = 'C%sT'
        else:
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _US
            format = 'C%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Qatar(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1920,1,1,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=26)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1972,6,1,0,0)):
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = None
            format = 'GST'
        else:
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'AST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Dubai(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1920,1,1,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=41)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = None
            format = 'GST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Yakutsk(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1919,12,15,0,0)):
            offset = timedelta(seconds=0, hours=8, minutes=38)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1930,6,21,0,0)):
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = None
            format = 'YAKT'
        elif(dt < datetime(1991,3,31,2,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = _Russia
            format = 'YAK%sT'
        elif(dt < datetime(1992,1,19,2,0)):
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = _Russia
            format = 'YAK%sT'
        elif(dt < datetime(2011,3,27,2,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = _Russia
            format = 'YAK%sT'
        elif(dt < datetime(2014,10,26,2,0)):
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = None
            format = 'YAKT'
        else:
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = None
            format = 'YAKT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Omsk(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1919,11,14,0,0)):
            offset = timedelta(seconds=0, hours=4, minutes=53)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1930,6,21,0,0)):
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = None
            format = 'OMST'
        elif(dt < datetime(1991,3,31,2,0)):
            offset = timedelta(seconds=0, hours=6, minutes=0)
            rule = _Russia
            format = 'OMS%sT'
        elif(dt < datetime(1992,1,19,2,0)):
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = _Russia
            format = 'OMS%sT'
        elif(dt < datetime(2011,3,27,2,0)):
            offset = timedelta(seconds=0, hours=6, minutes=0)
            rule = _Russia
            format = 'OMS%sT'
        elif(dt < datetime(2014,10,26,2,0)):
            offset = timedelta(seconds=0, hours=7, minutes=0)
            rule = None
            format = 'OMST'
        else:
            offset = timedelta(seconds=0, hours=6, minutes=0)
            rule = None
            format = 'OMST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Bangui(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1912,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=14)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = None
            format = 'WAT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Paramaribo(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1911,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-40)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1935,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-40)
            rule = None
            format = 'PMT'
        elif(dt < datetime(1945,10,1,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-40)
            rule = None
            format = 'PMT'
        elif(dt < datetime(1975,11,20,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-30)
            rule = None
            format = 'NEGT'
        elif(dt < datetime(1984,10,1,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-30)
            rule = None
            format = 'SRT'
        else:
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'SRT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Etc_GMT_11(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=11, minutes=0)
        rule = None
        format = 'GMT-11'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Etc_GMT_10(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=10, minutes=0)
        rule = None
        format = 'GMT-10'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Etc_GMT_13(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=13, minutes=0)
        rule = None
        format = 'GMT-13'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Etc_GMT_12(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=12, minutes=0)
        rule = None
        format = 'GMT-12'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Etc_GMT_14(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=14, minutes=0)
        rule = None
        format = 'GMT-14'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Pacific_Marquesas(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1912,10,1,0,0)):
            offset = timedelta(seconds=0, hours=-9, minutes=-18)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=-9, minutes=-30)
            rule = None
            format = 'MART'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Anadyr(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1924,5,1,2,0)):
            offset = timedelta(seconds=0, hours=11, minutes=49)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1930,6,21,0,0)):
            offset = timedelta(seconds=0, hours=12, minutes=0)
            rule = None
            format = 'ANAT'
        elif(dt < datetime(1982,4,1,1,0)):
            offset = timedelta(seconds=0, hours=13, minutes=0)
            rule = _Russia
            format = 'ANA%sT'
        elif(dt < datetime(1991,3,31,2,0)):
            offset = timedelta(seconds=0, hours=12, minutes=0)
            rule = _Russia
            format = 'ANA%sT'
        elif(dt < datetime(1992,1,19,2,0)):
            offset = timedelta(seconds=0, hours=11, minutes=0)
            rule = _Russia
            format = 'ANA%sT'
        elif(dt < datetime(2010,3,28,2,0)):
            offset = timedelta(seconds=0, hours=12, minutes=0)
            rule = _Russia
            format = 'ANA%sT'
        elif(dt < datetime(2011,3,27,2,0)):
            offset = timedelta(seconds=0, hours=11, minutes=0)
            rule = _Russia
            format = 'ANA%sT'
        else:
            offset = timedelta(seconds=0, hours=12, minutes=0)
            rule = None
            format = 'ANAT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_New_York(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1883,11,18,12,3)):
            offset = timedelta(seconds=0, hours=-4, minutes=-56)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1920,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _US
            format = 'E%sT'
        elif(dt < datetime(1942,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _NYC
            format = 'E%sT'
        elif(dt < datetime(1946,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _US
            format = 'E%sT'
        elif(dt < datetime(1967,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _NYC
            format = 'E%sT'
        else:
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _US
            format = 'E%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Pacific_Norfolk(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1901,1,1,0,0)):
            offset = timedelta(seconds=0, hours=11, minutes=11)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1951,1,1,0,0)):
            offset = timedelta(seconds=0, hours=11, minutes=12)
            rule = None
            format = 'NMT'
        else:
            offset = timedelta(seconds=0, hours=11, minutes=30)
            rule = None
            format = 'NFT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class CST6CDT(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=-6, minutes=0)
        rule = _US
        format = 'C%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Pacific_Rarotonga(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1901,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-10, minutes=-39)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1978,11,12,0,0)):
            offset = timedelta(seconds=0, hours=-10, minutes=-30)
            rule = None
            format = 'CKT'
        else:
            offset = timedelta(seconds=0, hours=-10, minutes=0)
            rule = _Cook
            format = 'CK%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Porto_Novo(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1912,1,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=10)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1934,2,26,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = None
            format = 'GMT'
        else:
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = None
            format = 'WAT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Samarkand(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1924,5,1,2,0)):
            offset = timedelta(seconds=0, hours=4, minutes=27)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1930,6,21,0,0)):
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = None
            format = 'SAMT'
        elif(dt < datetime(1981,4,1,1,0)):
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = None
            format = 'SAMT'
        elif(dt < datetime(1981,10,1,1,0)):
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = _rule_constant_1hour
            format = 'SAMST'
        elif(dt < datetime(1982,4,1,1,0)):
            offset = timedelta(seconds=0, hours=6, minutes=0)
            rule = None
            format = 'TAST'
        elif(dt < datetime(1991,9,1,1,0)):
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = _RussiaAsia
            format = 'SAM%sT'
        elif(dt < datetime(1992,1,1,0,0)):
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = _RussiaAsia
            format = 'UZ%sT'
        else:
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = None
            format = 'UZT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Dushanbe(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1924,5,1,2,0)):
            offset = timedelta(seconds=0, hours=4, minutes=35)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1930,6,21,0,0)):
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = None
            format = 'DUST'
        elif(dt < datetime(1991,3,31,2,0)):
            offset = timedelta(seconds=0, hours=6, minutes=0)
            rule = _RussiaAsia
            format = 'DUS%sT'
        elif(dt < datetime(1991,9,1,9,0)):
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = _rule_constant_1hour
            format = 'DUSST'
        else:
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = None
            format = 'TJT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Kentucky_Louisville(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1883,11,18,12,16)):
            offset = timedelta(seconds=0, hours=-5, minutes=-43)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1921,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _US
            format = 'C%sT'
        elif(dt < datetime(1942,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Louisville
            format = 'C%sT'
        elif(dt < datetime(1946,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _US
            format = 'C%sT'
        elif(dt < datetime(1961,7,23,2,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Louisville
            format = 'C%sT'
        elif(dt < datetime(1968,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        elif(dt < datetime(1974,1,1,6,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _US
            format = 'E%sT'
        elif(dt < datetime(1974,10,27,2,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _rule_constant_1hour
            format = 'CDT'
        else:
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _US
            format = 'E%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Toronto(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1895,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=-17)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1919,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _Canada
            format = 'E%sT'
        elif(dt < datetime(1942,2,1,9,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _Toronto
            format = 'E%sT'
        elif(dt < datetime(1946,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _Canada
            format = 'E%sT'
        elif(dt < datetime(1974,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _Toronto
            format = 'E%sT'
        else:
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _Canada
            format = 'E%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Bahia(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1914,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-2, minutes=-34)
            rule = None
            format = 'LMT'
        elif(dt < datetime(2003,9,24,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Brazil
            format = 'BR%sT'
        elif(dt < datetime(2011,10,16,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'BRT'
        elif(dt < datetime(2012,10,21,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Brazil
            format = 'BR%sT'
        else:
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'BRT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Indian_Maldives(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1880,1,1,0,0)):
            offset = timedelta(seconds=0, hours=4, minutes=54)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1960,1,1,0,0)):
            offset = timedelta(seconds=0, hours=4, minutes=54)
            rule = None
            format = 'MMT'
        else:
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = None
            format = 'MVT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Muscat(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1920,1,1,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=54)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = None
            format = 'GST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Edmonton(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1906,9,1,0,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=-33)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1987,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = _Edm
            format = 'M%sT'
        else:
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = _Canada
            format = 'M%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Pacific_Wake(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1901,1,1,0,0)):
            offset = timedelta(seconds=0, hours=11, minutes=6)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=12, minutes=0)
            rule = None
            format = 'WAKT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Indiana_Tell_City(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1883,11,18,12,12)):
            offset = timedelta(seconds=0, hours=-5, minutes=-47)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1946,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _US
            format = 'C%sT'
        elif(dt < datetime(1964,4,26,2,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Perry
            format = 'C%sT'
        elif(dt < datetime(1969,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        elif(dt < datetime(1971,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _US
            format = 'E%sT'
        elif(dt < datetime(2006,4,1,2,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        else:
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _US
            format = 'C%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Australia_Darwin(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1895,2,1,0,0)):
            offset = timedelta(seconds=0, hours=8, minutes=43)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1899,5,1,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = None
            format = 'ACST'
        else:
            offset = timedelta(seconds=0, hours=9, minutes=30)
            rule = _Aus
            format = 'AC%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Whitehorse(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1900,8,20,0,0)):
            offset = timedelta(seconds=0, hours=-9, minutes=0)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1966,7,1,2,0)):
            offset = timedelta(seconds=0, hours=-9, minutes=0)
            rule = _NT_YK
            format = 'Y%sT'
        elif(dt < datetime(1980,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _NT_YK
            format = 'P%sT'
        else:
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _Canada
            format = 'P%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Swift_Current(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1905,9,1,0,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=-11)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1946,4,1,0,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = _Canada
            format = 'M%sT'
        elif(dt < datetime(1950,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = _Regina
            format = 'M%sT'
        elif(dt < datetime(1972,4,1,0,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = _Swift
            format = 'M%sT'
        else:
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = None
            format = 'CST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Copenhagen(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1890,1,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=50)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1894,1,1,1,0)):
            offset = timedelta(seconds=0, hours=0, minutes=50)
            rule = None
            format = 'CMT'
        elif(dt < datetime(1942,11,1,2,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _Denmark
            format = 'CE%sT'
        elif(dt < datetime(1945,4,1,2,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _C_Eur
            format = 'CE%sT'
        elif(dt < datetime(1980,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _Denmark
            format = 'CE%sT'
        else:
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _EU
            format = 'CE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Argentina_Salta(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1894,10,31,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-21)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1920,5,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-16)
            rule = None
            format = 'CMT'
        elif(dt < datetime(1930,12,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'ART'
        elif(dt < datetime(1969,10,1,5,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(1991,3,1,3,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(1991,10,20,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'WART'
        elif(dt < datetime(1999,10,1,3,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(2000,3,1,3,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(2008,10,18,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        else:
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'ART'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Simferopol(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1880,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=16)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1924,5,1,2,0)):
            offset = timedelta(seconds=0, hours=2, minutes=16)
            rule = None
            format = 'SMT'
        elif(dt < datetime(1930,6,21,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'EET'
        elif(dt < datetime(1941,11,1,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'MSK'
        elif(dt < datetime(1944,4,13,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _C_Eur
            format = 'CE%sT'
        elif(dt < datetime(1990,1,1,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = _Russia
            format = 'MSK/MSD'
        elif(dt < datetime(1990,7,1,1,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'MSK'
        elif(dt < datetime(1992,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'EET'
        elif(dt < datetime(1994,5,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _E_Eur
            format = 'EE%sT'
        elif(dt < datetime(1996,3,31,3,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = _E_Eur
            format = 'MSK/MSD'
        elif(dt < datetime(1996,10,27,3,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = _rule_constant_1hour
            format = 'MSD'
        elif(dt < datetime(1997,1,1,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = _Russia
            format = 'MSK/MSD'
        elif(dt < datetime(1997,3,1,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'MSK'
        elif(dt < datetime(2014,3,30,2,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _EU
            format = 'EE%sT'
        elif(dt < datetime(2014,10,26,2,0)):
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = None
            format = 'MSK'
        else:
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'MSK'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Blantyre(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1903,3,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=20)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'CAT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Detroit(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1905,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=-32)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1915,5,15,2,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = None
            format = 'CST'
        elif(dt < datetime(1942,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        elif(dt < datetime(1946,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _US
            format = 'E%sT'
        elif(dt < datetime(1973,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _Detroit
            format = 'E%sT'
        elif(dt < datetime(1975,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _US
            format = 'E%sT'
        elif(dt < datetime(1975,4,27,2,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        else:
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _US
            format = 'E%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Indiana_Vincennes(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1883,11,18,12,9)):
            offset = timedelta(seconds=0, hours=-5, minutes=-50)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1946,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _US
            format = 'C%sT'
        elif(dt < datetime(1964,4,26,2,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Vincennes
            format = 'C%sT'
        elif(dt < datetime(1969,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        elif(dt < datetime(1971,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _US
            format = 'E%sT'
        elif(dt < datetime(2006,4,1,2,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        elif(dt < datetime(2007,11,1,4,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _US
            format = 'C%sT'
        else:
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _US
            format = 'E%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Indiana_Petersburg(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1883,11,18,12,10)):
            offset = timedelta(seconds=0, hours=-5, minutes=-49)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1955,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _US
            format = 'C%sT'
        elif(dt < datetime(1965,4,25,2,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Pike
            format = 'C%sT'
        elif(dt < datetime(1966,10,30,2,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        elif(dt < datetime(1977,10,30,2,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _US
            format = 'C%sT'
        elif(dt < datetime(2006,4,1,2,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        elif(dt < datetime(2007,11,1,4,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _US
            format = 'C%sT'
        else:
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _US
            format = 'E%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Kathmandu(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1920,1,1,0,0)):
            offset = timedelta(seconds=0, hours=5, minutes=41)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1986,1,1,0,0)):
            offset = timedelta(seconds=0, hours=5, minutes=30)
            rule = None
            format = 'IST'
        else:
            offset = timedelta(seconds=0, hours=5, minutes=45)
            rule = None
            format = 'NPT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Pontianak(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1908,5,1,0,0)):
            offset = timedelta(seconds=0, hours=7, minutes=17)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1932,11,1,0,0)):
            offset = timedelta(seconds=0, hours=7, minutes=17)
            rule = None
            format = 'PMT'
        elif(dt < datetime(1942,1,29,0,0)):
            offset = timedelta(seconds=0, hours=7, minutes=30)
            rule = None
            format = 'WIB'
        elif(dt < datetime(1945,9,23,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = None
            format = 'JST'
        elif(dt < datetime(1948,5,1,0,0)):
            offset = timedelta(seconds=0, hours=7, minutes=30)
            rule = None
            format = 'WIB'
        elif(dt < datetime(1950,5,1,0,0)):
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = None
            format = 'WIB'
        elif(dt < datetime(1964,1,1,0,0)):
            offset = timedelta(seconds=0, hours=7, minutes=30)
            rule = None
            format = 'WIB'
        elif(dt < datetime(1988,1,1,1,0)):
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = None
            format = 'WITA'
        else:
            offset = timedelta(seconds=0, hours=7, minutes=0)
            rule = None
            format = 'WIB'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Athens(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1895,9,14,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=34)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1916,7,28,0,1)):
            offset = timedelta(seconds=0, hours=1, minutes=34)
            rule = None
            format = 'AMT'
        elif(dt < datetime(1941,4,30,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _Greece
            format = 'EE%sT'
        elif(dt < datetime(1944,4,1,4,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _Greece
            format = 'CE%sT'
        elif(dt < datetime(1981,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _Greece
            format = 'EE%sT'
        else:
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _EU
            format = 'EE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Port_au_Prince(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1890,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-49)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1917,1,24,12,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-49)
            rule = None
            format = 'PPMT'
        else:
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _Haiti
            format = 'E%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Cayman(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1890,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=-25)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1912,2,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=-7)
            rule = None
            format = 'KMT'
        else:
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Dar_es_Salaam(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1931,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=37)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1948,1,1,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'EAT'
        elif(dt < datetime(1961,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=45)
            rule = None
            format = 'BEAUT'
        else:
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'EAT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Curacao(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1912,2,12,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-35)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1965,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-30)
            rule = None
            format = 'ANT'
        else:
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'AST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Khartoum(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1931,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=10)
            rule = None
            format = 'LMT'
        elif(dt < datetime(2000,1,15,12,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _Sudan
            format = 'CA%sT'
        else:
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'EAT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Manila(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1844,12,31,0,0)):
            offset = timedelta(seconds=0, hours=-15, minutes=-56)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1899,5,11,0,0)):
            offset = timedelta(seconds=0, hours=8, minutes=4)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1942,5,1,0,0)):
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = _Phil
            format = 'PH%sT'
        elif(dt < datetime(1944,11,1,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = None
            format = 'JST'
        else:
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = _Phil
            format = 'PH%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Douala(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1912,1,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=38)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = None
            format = 'WAT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class EET(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=2, minutes=0)
        rule = _EU
        format = 'EE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Argentina_San_Juan(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1894,10,31,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-34)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1920,5,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-16)
            rule = None
            format = 'CMT'
        elif(dt < datetime(1930,12,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'ART'
        elif(dt < datetime(1969,10,1,5,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(1991,3,1,1,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(1991,5,1,7,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'WART'
        elif(dt < datetime(1999,10,1,3,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(2000,3,1,3,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(2004,5,31,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'ART'
        elif(dt < datetime(2004,7,25,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'WART'
        elif(dt < datetime(2008,10,18,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        else:
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'ART'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_North_Dakota_New_Salem(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1883,11,18,12,14)):
            offset = timedelta(seconds=0, hours=-6, minutes=-45)
            rule = None
            format = 'LMT'
        elif(dt < datetime(2003,10,26,2,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = _US
            format = 'M%sT'
        else:
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _US
            format = 'C%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Pacific_Port_Moresby(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1880,1,1,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=48)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1895,1,1,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=48)
            rule = None
            format = 'PMMT'
        else:
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = None
            format = 'PGT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Andorra(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1901,1,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=6)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1946,9,30,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = None
            format = 'WET'
        elif(dt < datetime(1985,3,31,2,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = None
            format = 'CET'
        else:
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _EU
            format = 'CE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Luxembourg(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1904,6,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=24)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1918,11,25,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _Lux
            format = 'CE%sT'
        elif(dt < datetime(1929,10,1,6,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = _Lux
            format = 'WE%sT'
        elif(dt < datetime(1940,5,14,3,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = _Belgium
            format = 'WE%sT'
        elif(dt < datetime(1944,9,18,3,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _C_Eur
            format = 'WE%sT'
        elif(dt < datetime(1977,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _Belgium
            format = 'CE%sT'
        else:
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _EU
            format = 'CE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Pacific_Honolulu(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1896,1,13,12,0)):
            offset = timedelta(seconds=0, hours=-10, minutes=-31)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1933,4,30,2,0)):
            offset = timedelta(seconds=0, hours=-10, minutes=-30)
            rule = None
            format = 'HST'
        elif(dt < datetime(1933,5,21,12,0)):
            offset = timedelta(seconds=0, hours=-10, minutes=-30)
            rule = _rule_constant_1hour
            format = 'HDT'
        elif(dt < datetime(1942,2,9,2,0)):
            offset = timedelta(seconds=0, hours=-10, minutes=-30)
            rule = None
            format = 'HST'
        elif(dt < datetime(1945,9,30,2,0)):
            offset = timedelta(seconds=0, hours=-10, minutes=-30)
            rule = _rule_constant_1hour
            format = 'HDT'
        elif(dt < datetime(1947,6,1,8,0)):
            offset = timedelta(seconds=0, hours=-10, minutes=-30)
            rule = None
            format = 'HST'
        else:
            offset = timedelta(seconds=0, hours=-10, minutes=0)
            rule = None
            format = 'HST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Pacific_Majuro(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1901,1,1,0,0)):
            offset = timedelta(seconds=0, hours=11, minutes=24)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1969,10,1,0,0)):
            offset = timedelta(seconds=0, hours=11, minutes=0)
            rule = None
            format = 'MHT'
        else:
            offset = timedelta(seconds=0, hours=12, minutes=0)
            rule = None
            format = 'MHT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Hong_Kong(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1904,10,30,0,0)):
            offset = timedelta(seconds=0, hours=7, minutes=36)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1941,12,25,0,0)):
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = _HK
            format = 'HK%sT'
        elif(dt < datetime(1945,9,15,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = None
            format = 'JST'
        else:
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = _HK
            format = 'HK%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Macau(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1912,1,1,0,0)):
            offset = timedelta(seconds=0, hours=7, minutes=34)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1999,12,20,0,0)):
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = _Macau
            format = 'MO%sT'
        else:
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = _PRC
            format = 'C%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Belgrade(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1884,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=22)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1941,4,18,23,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = None
            format = 'CET'
        elif(dt < datetime(1945,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _C_Eur
            format = 'CE%sT'
        elif(dt < datetime(1945,5,8,2,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = None
            format = 'CET'
        elif(dt < datetime(1945,9,16,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _rule_constant_1hour
            format = 'CEST'
        elif(dt < datetime(1982,11,27,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = None
            format = 'CET'
        else:
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _EU
            format = 'CE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Choibalsan(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1905,8,1,0,0)):
            offset = timedelta(seconds=0, hours=7, minutes=38)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1978,1,1,0,0)):
            offset = timedelta(seconds=0, hours=7, minutes=0)
            rule = None
            format = 'ULAT'
        elif(dt < datetime(1983,4,1,0,0)):
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = None
            format = 'ULAT'
        elif(dt < datetime(2008,3,31,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = _Mongol
            format = 'CHO%sT'
        else:
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = _Mongol
            format = 'CHO%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Thunder_Bay(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1895,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=-57)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1910,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = None
            format = 'CST'
        elif(dt < datetime(1942,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        elif(dt < datetime(1970,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _Canada
            format = 'E%sT'
        elif(dt < datetime(1973,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _Toronto
            format = 'E%sT'
        elif(dt < datetime(1974,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        else:
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _Canada
            format = 'E%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Los_Angeles(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1883,11,18,12,7)):
            offset = timedelta(seconds=0, hours=-7, minutes=-52)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1946,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _US
            format = 'P%sT'
        elif(dt < datetime(1967,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _CA
            format = 'P%sT'
        else:
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _US
            format = 'P%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Kabul(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1890,1,1,0,0)):
            offset = timedelta(seconds=0, hours=4, minutes=36)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1945,1,1,0,0)):
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = None
            format = 'AFT'
        else:
            offset = timedelta(seconds=0, hours=4, minutes=30)
            rule = None
            format = 'AFT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Indian_Antananarivo(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1911,7,1,0,0)):
            offset = timedelta(seconds=0, hours=3, minutes=10)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1954,2,27,23,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'EAT'
        elif(dt < datetime(1954,5,29,23,0)):
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = _rule_constant_1hour
            format = 'EAST'
        else:
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'EAT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Atlantic_Reykjavik(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1837,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-1, minutes=-27)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1908,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-1, minutes=-27)
            rule = None
            format = 'RMT'
        elif(dt < datetime(1968,4,7,1,0)):
            offset = timedelta(seconds=0, hours=-1, minutes=0)
            rule = _Iceland
            format = 'IS%sT'
        else:
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = None
            format = 'GMT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Etc_GMTplus12(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=-12, minutes=0)
        rule = None
        format = 'GMT+12'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Etc_GMTplus11(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=-11, minutes=0)
        rule = None
        format = 'GMT+11'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Etc_GMTplus10(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=-10, minutes=0)
        rule = None
        format = 'GMT+10'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Pacific_Tongatapu(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1901,1,1,0,0)):
            offset = timedelta(seconds=0, hours=12, minutes=19)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1941,1,1,0,0)):
            offset = timedelta(seconds=0, hours=12, minutes=20)
            rule = None
            format = 'TOT'
        elif(dt < datetime(1999,1,1,0,0)):
            offset = timedelta(seconds=0, hours=13, minutes=0)
            rule = None
            format = 'TOT'
        else:
            offset = timedelta(seconds=0, hours=13, minutes=0)
            rule = _Tonga
            format = 'TO%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Pacific_Pitcairn(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1901,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=-40)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1998,4,27,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=-30)
            rule = None
            format = 'PNT'
        else:
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = None
            format = 'PST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Pacific_Easter(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1890,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=-17)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1932,9,1,0,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=-17)
            rule = None
            format = 'EMT'
        elif(dt < datetime(1982,3,13,21,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = _Chile
            format = 'EAS%sT'
        else:
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Chile
            format = 'EAS%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Atlantic_South_Georgia(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1890,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-2, minutes=-26)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=-2, minutes=0)
            rule = None
            format = 'GST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_El_Aaiun(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1934,1,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=-52)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1976,4,14,0,0)):
            offset = timedelta(seconds=0, hours=-1, minutes=0)
            rule = None
            format = 'WAT'
        else:
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = _Morocco
            format = 'WE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Campo_Grande(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1914,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-38)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Brazil
            format = 'AM%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Dawson_Creek(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1884,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1947,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _Canada
            format = 'P%sT'
        elif(dt < datetime(1972,8,30,2,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _Vanc
            format = 'P%sT'
        else:
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = None
            format = 'MST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Bucharest(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1891,10,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=44)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1931,7,24,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=44)
            rule = None
            format = 'BMT'
        elif(dt < datetime(1981,3,29,2,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _Romania
            format = 'EE%sT'
        elif(dt < datetime(1991,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _C_Eur
            format = 'EE%sT'
        elif(dt < datetime(1994,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _Romania
            format = 'EE%sT'
        elif(dt < datetime(1997,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _E_Eur
            format = 'EE%sT'
        else:
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _EU
            format = 'EE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Porto_Velho(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1914,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-15)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1988,9,12,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Brazil
            format = 'AM%sT'
        else:
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'AMT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Monaco(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1891,3,15,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=29)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1911,3,11,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=9)
            rule = None
            format = 'PMT'
        elif(dt < datetime(1945,9,16,3,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = _France
            format = 'WE%sT'
        elif(dt < datetime(1977,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _France
            format = 'CE%sT'
        else:
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _EU
            format = 'CE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Bishkek(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1924,5,1,2,0)):
            offset = timedelta(seconds=0, hours=4, minutes=58)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1930,6,21,0,0)):
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = None
            format = 'FRUT'
        elif(dt < datetime(1991,3,31,2,0)):
            offset = timedelta(seconds=0, hours=6, minutes=0)
            rule = _RussiaAsia
            format = 'FRU%sT'
        elif(dt < datetime(1991,8,31,2,0)):
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = _rule_constant_1hour
            format = 'FRUST'
        elif(dt < datetime(2005,8,12,0,0)):
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = _Kyrgyz
            format = 'KG%sT'
        else:
            offset = timedelta(seconds=0, hours=6, minutes=0)
            rule = None
            format = 'KGT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Ceuta(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1901,1,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=-21)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1918,5,1,6,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = None
            format = 'WET'
        elif(dt < datetime(1918,10,1,7,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = _rule_constant_1hour
            format = 'WEST'
        elif(dt < datetime(1924,1,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = None
            format = 'WET'
        elif(dt < datetime(1929,1,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = _Spain
            format = 'WE%sT'
        elif(dt < datetime(1984,3,16,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = _SpainAfrica
            format = 'WE%sT'
        elif(dt < datetime(1986,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = None
            format = 'CET'
        else:
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _EU
            format = 'CE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Rome(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1866,9,22,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=49)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1893,11,1,1,0)):
            offset = timedelta(seconds=0, hours=0, minutes=49)
            rule = None
            format = 'RMT'
        elif(dt < datetime(1942,11,1,2,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _Italy
            format = 'CE%sT'
        elif(dt < datetime(1944,7,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _C_Eur
            format = 'CE%sT'
        elif(dt < datetime(1980,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _Italy
            format = 'CE%sT'
        else:
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _EU
            format = 'CE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Winnipeg(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1887,7,16,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=-28)
            rule = None
            format = 'LMT'
        elif(dt < datetime(2006,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Winn
            format = 'C%sT'
        else:
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Canada
            format = 'C%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Aqtobe(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1924,5,1,2,0)):
            offset = timedelta(seconds=0, hours=3, minutes=48)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1930,6,21,0,0)):
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = None
            format = 'AKTT'
        elif(dt < datetime(1981,4,1,1,0)):
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = None
            format = 'AKTT'
        elif(dt < datetime(1981,10,1,1,0)):
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = _rule_constant_1hour
            format = 'AKTST'
        elif(dt < datetime(1982,4,1,1,0)):
            offset = timedelta(seconds=0, hours=6, minutes=0)
            rule = None
            format = 'AKTT'
        elif(dt < datetime(1991,1,1,0,0)):
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = _RussiaAsia
            format = 'AKT%sT'
        elif(dt < datetime(1991,12,16,0,0)):
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = None
            format = 'AKTT'
        elif(dt < datetime(2005,3,15,0,0)):
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = _RussiaAsia
            format = 'AQT%sT'
        else:
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = None
            format = 'AQTT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Fortaleza(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1914,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-2, minutes=-34)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1990,9,17,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Brazil
            format = 'BR%sT'
        elif(dt < datetime(1999,9,30,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'BRT'
        elif(dt < datetime(2000,10,22,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Brazil
            format = 'BR%sT'
        elif(dt < datetime(2001,9,13,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'BRT'
        elif(dt < datetime(2002,10,1,1,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Brazil
            format = 'BR%sT'
        else:
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'BRT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Pacific_Tarawa(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1901,1,1,0,0)):
            offset = timedelta(seconds=0, hours=11, minutes=32)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=12, minutes=0)
            rule = None
            format = 'GILT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Dawson(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1900,8,20,0,0)):
            offset = timedelta(seconds=0, hours=-9, minutes=-17)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1973,10,28,0,0)):
            offset = timedelta(seconds=0, hours=-9, minutes=0)
            rule = _NT_YK
            format = 'Y%sT'
        elif(dt < datetime(1980,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _NT_YK
            format = 'P%sT'
        else:
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _Canada
            format = 'P%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Addis_Ababa(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1870,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=34)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1936,5,5,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=35)
            rule = None
            format = 'ADMT'
        else:
            offset = timedelta(seconds=0, hours=3, minutes=0)
            rule = None
            format = 'EAT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Pacific_Efate(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1912,1,13,0,0)):
            offset = timedelta(seconds=0, hours=11, minutes=13)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=11, minutes=0)
            rule = _Vanuatu
            format = 'VU%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Qyzylorda(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1924,5,1,2,0)):
            offset = timedelta(seconds=0, hours=4, minutes=21)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1930,6,21,0,0)):
            offset = timedelta(seconds=0, hours=4, minutes=0)
            rule = None
            format = 'KIZT'
        elif(dt < datetime(1981,4,1,1,0)):
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = None
            format = 'KIZT'
        elif(dt < datetime(1981,10,1,1,0)):
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = _rule_constant_1hour
            format = 'KIZST'
        elif(dt < datetime(1982,4,1,1,0)):
            offset = timedelta(seconds=0, hours=6, minutes=0)
            rule = None
            format = 'KIZT'
        elif(dt < datetime(1991,1,1,0,0)):
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = _RussiaAsia
            format = 'KIZ%sT'
        elif(dt < datetime(1991,12,16,0,0)):
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = None
            format = 'KIZT'
        elif(dt < datetime(1992,1,19,2,0)):
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = None
            format = 'QYZT'
        elif(dt < datetime(2005,3,15,0,0)):
            offset = timedelta(seconds=0, hours=6, minutes=0)
            rule = _RussiaAsia
            format = 'QYZ%sT'
        else:
            offset = timedelta(seconds=0, hours=6, minutes=0)
            rule = None
            format = 'QYZT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Jerusalem(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1880,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=20)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1918,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=20)
            rule = None
            format = 'JMT'
        else:
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _Zion
            format = 'I%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class MET(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=1, minutes=0)
        rule = _C_Eur
        format = 'ME%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Pacific_Auckland(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1868,11,1,2,0)):
            offset = timedelta(seconds=0, hours=11, minutes=39)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1946,1,1,1,0)):
            offset = timedelta(seconds=0, hours=11, minutes=30)
            rule = _NZ
            format = 'NZ%sT'
        else:
            offset = timedelta(seconds=0, hours=12, minutes=0)
            rule = _NZ
            format = 'NZ%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Metlakatla(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1867,10,18,0,0)):
            offset = timedelta(seconds=0, hours=15, minutes=13)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1900,8,20,12,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=-46)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1942,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = None
            format = 'PST'
        elif(dt < datetime(1946,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _US
            format = 'P%sT'
        elif(dt < datetime(1969,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = None
            format = 'PST'
        elif(dt < datetime(1983,10,30,2,0)):
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = _US
            format = 'P%sT'
        else:
            offset = timedelta(seconds=0, hours=-8, minutes=0)
            rule = None
            format = 'PST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Denver(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1883,11,18,12,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=-59)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1920,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = _US
            format = 'M%sT'
        elif(dt < datetime(1942,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = _Denver
            format = 'M%sT'
        elif(dt < datetime(1946,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = _US
            format = 'M%sT'
        elif(dt < datetime(1967,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = _Denver
            format = 'M%sT'
        else:
            offset = timedelta(seconds=0, hours=-7, minutes=0)
            rule = _US
            format = 'M%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Indian_Chagos(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1907,1,1,0,0)):
            offset = timedelta(seconds=0, hours=4, minutes=49)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1996,1,1,0,0)):
            offset = timedelta(seconds=0, hours=5, minutes=0)
            rule = None
            format = 'IOT'
        else:
            offset = timedelta(seconds=0, hours=6, minutes=0)
            rule = None
            format = 'IOT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class MST(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=-7, minutes=0)
        rule = None
        format = 'MST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Gaborone(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1885,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=43)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1903,3,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=30)
            rule = None
            format = 'SAST'
        elif(dt < datetime(1943,9,19,2,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'CAT'
        elif(dt < datetime(1944,3,19,2,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _rule_constant_1hour
            format = 'CAST'
        else:
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'CAT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Tunis(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1881,5,12,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=40)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1911,3,11,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=9)
            rule = None
            format = 'PMT'
        else:
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _Tunisia
            format = 'CE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Montevideo(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1898,6,28,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-44)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1920,5,1,1,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-44)
            rule = None
            format = 'MMT'
        elif(dt < datetime(1942,12,14,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=-30)
            rule = _Uruguay
            format = 'UY%sT'
        else:
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Uruguay
            format = 'UY%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Ust_Nera(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1919,12,15,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=32)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1930,6,21,0,0)):
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = None
            format = 'YAKT'
        elif(dt < datetime(1981,4,1,1,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = _Russia
            format = 'YAKT'
        elif(dt < datetime(1991,3,31,2,0)):
            offset = timedelta(seconds=0, hours=11, minutes=0)
            rule = _Russia
            format = 'MAG%sT'
        elif(dt < datetime(1992,1,19,2,0)):
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = _Russia
            format = 'MAG%sT'
        elif(dt < datetime(2011,3,27,2,0)):
            offset = timedelta(seconds=0, hours=11, minutes=0)
            rule = _Russia
            format = 'MAG%sT'
        elif(dt < datetime(2011,9,13,0,0)):
            offset = timedelta(seconds=0, hours=12, minutes=0)
            rule = None
            format = 'MAGT'
        elif(dt < datetime(2014,10,26,2,0)):
            offset = timedelta(seconds=0, hours=11, minutes=0)
            rule = None
            format = 'VLAT'
        else:
            offset = timedelta(seconds=0, hours=10, minutes=0)
            rule = None
            format = 'VLAT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Resolute(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1947,8,31,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=0)
            rule = None
            format = 'zzz'
        elif(dt < datetime(2000,10,29,2,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _NT_YK
            format = 'C%sT'
        elif(dt < datetime(2001,4,1,1,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        elif(dt < datetime(2006,10,29,2,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Canada
            format = 'C%sT'
        elif(dt < datetime(2007,3,11,3,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        else:
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Canada
            format = 'C%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Etc_GMT(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=0, minutes=0)
        rule = None
        format = 'GMT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Gaza(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1900,10,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=17)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1948,5,15,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _Zion
            format = 'EET'
        elif(dt < datetime(1967,6,1,5,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _EgyptAsia
            format = 'EE%sT'
        elif(dt < datetime(1996,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _Zion
            format = 'I%sT'
        elif(dt < datetime(1999,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _Jordan
            format = 'EE%sT'
        elif(dt < datetime(2008,8,29,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _Palestine
            format = 'EE%sT'
        elif(dt < datetime(2008,9,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'EET'
        elif(dt < datetime(2010,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _Palestine
            format = 'EE%sT'
        elif(dt < datetime(2010,3,27,0,1)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'EET'
        elif(dt < datetime(2011,8,1,1,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _Palestine
            format = 'EE%sT'
        elif(dt < datetime(2012,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'EET'
        else:
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _Palestine
            format = 'EE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Taipei(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1896,1,1,1,0)):
            offset = timedelta(seconds=0, hours=8, minutes=6)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1937,10,1,1,0)):
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = None
            format = 'JWST'
        elif(dt < datetime(1945,9,21,1,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = None
            format = 'JST'
        else:
            offset = timedelta(seconds=0, hours=8, minutes=0)
            rule = _Taiwan
            format = 'C%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Argentina_Catamarca(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1894,10,31,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-23)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1920,5,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-16)
            rule = None
            format = 'CMT'
        elif(dt < datetime(1930,12,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'ART'
        elif(dt < datetime(1969,10,1,5,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(1991,3,1,3,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(1991,10,20,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'WART'
        elif(dt < datetime(1999,10,1,3,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(2000,3,1,3,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        elif(dt < datetime(2004,6,1,1,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'ART'
        elif(dt < datetime(2004,6,20,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=0)
            rule = None
            format = 'WART'
        elif(dt < datetime(2008,10,18,0,0)):
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = _Arg
            format = 'AR%sT'
        else:
            offset = timedelta(seconds=0, hours=-3, minutes=0)
            rule = None
            format = 'ART'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Indiana_Knox(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1883,11,18,12,13)):
            offset = timedelta(seconds=0, hours=-5, minutes=-46)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1947,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _US
            format = 'C%sT'
        elif(dt < datetime(1962,4,29,2,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _Starke
            format = 'C%sT'
        elif(dt < datetime(1963,10,27,2,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        elif(dt < datetime(1991,10,27,2,0)):
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _US
            format = 'C%sT'
        elif(dt < datetime(2006,4,1,2,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = None
            format = 'EST'
        else:
            offset = timedelta(seconds=0, hours=-6, minutes=0)
            rule = _US
            format = 'C%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Asia_Novosibirsk(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1919,12,14,6,0)):
            offset = timedelta(seconds=0, hours=5, minutes=31)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1930,6,21,0,0)):
            offset = timedelta(seconds=0, hours=6, minutes=0)
            rule = None
            format = 'NOVT'
        elif(dt < datetime(1991,3,31,2,0)):
            offset = timedelta(seconds=0, hours=7, minutes=0)
            rule = _Russia
            format = 'NOV%sT'
        elif(dt < datetime(1992,1,19,2,0)):
            offset = timedelta(seconds=0, hours=6, minutes=0)
            rule = _Russia
            format = 'NOV%sT'
        elif(dt < datetime(1993,5,23,0,0)):
            offset = timedelta(seconds=0, hours=7, minutes=0)
            rule = _Russia
            format = 'NOV%sT'
        elif(dt < datetime(2011,3,27,2,0)):
            offset = timedelta(seconds=0, hours=6, minutes=0)
            rule = _Russia
            format = 'NOV%sT'
        elif(dt < datetime(2014,10,26,2,0)):
            offset = timedelta(seconds=0, hours=7, minutes=0)
            rule = None
            format = 'NOVT'
        else:
            offset = timedelta(seconds=0, hours=6, minutes=0)
            rule = None
            format = 'NOVT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class EST(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        offset = timedelta(seconds=0, hours=-5, minutes=0)
        rule = None
        format = 'EST'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Kigali(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1935,6,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'CAT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Grand_Turk(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1890,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-4, minutes=-44)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1912,2,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=-7)
            rule = None
            format = 'KMT'
        else:
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _TC
            format = 'E%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Africa_Lagos(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1919,9,1,0,0)):
            offset = timedelta(seconds=0, hours=0, minutes=13)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = None
            format = 'WAT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Europe_Sofia(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1880,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=33)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1894,11,30,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=56)
            rule = None
            format = 'IMT'
        elif(dt < datetime(1942,11,1,2,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'EET'
        elif(dt < datetime(1945,1,1,0,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = _C_Eur
            format = 'CE%sT'
        elif(dt < datetime(1945,4,2,3,0)):
            offset = timedelta(seconds=0, hours=1, minutes=0)
            rule = None
            format = 'CET'
        elif(dt < datetime(1979,3,31,23,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = None
            format = 'EET'
        elif(dt < datetime(1982,9,26,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _Bulg
            format = 'EE%sT'
        elif(dt < datetime(1991,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _C_Eur
            format = 'EE%sT'
        elif(dt < datetime(1997,1,1,0,0)):
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _E_Eur
            format = 'EE%sT'
        else:
            offset = timedelta(seconds=0, hours=2, minutes=0)
            rule = _EU
            format = 'EE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Lima(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1890,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=-8)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1908,7,28,0,0)):
            offset = timedelta(seconds=0, hours=-5, minutes=-8)
            rule = None
            format = 'LMT'
        else:
            offset = timedelta(seconds=0, hours=-5, minutes=0)
            rule = _Peru
            format = 'PE%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class America_Anchorage(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1867,10,18,0,0)):
            offset = timedelta(seconds=0, hours=14, minutes=0)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1900,8,20,12,0)):
            offset = timedelta(seconds=0, hours=-9, minutes=-59)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1942,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-10, minutes=0)
            rule = None
            format = 'CAT'
        elif(dt < datetime(1945,8,14,23,0)):
            offset = timedelta(seconds=0, hours=-10, minutes=0)
            rule = _US
            format = 'CAT/CAWT'
        elif(dt < datetime(1946,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-10, minutes=0)
            rule = _US
            format = 'CAT/CAPT'
        elif(dt < datetime(1967,4,1,0,0)):
            offset = timedelta(seconds=0, hours=-10, minutes=0)
            rule = None
            format = 'CAT'
        elif(dt < datetime(1969,1,1,0,0)):
            offset = timedelta(seconds=0, hours=-10, minutes=0)
            rule = None
            format = 'AHST'
        elif(dt < datetime(1983,10,30,2,0)):
            offset = timedelta(seconds=0, hours=-10, minutes=0)
            rule = _US
            format = 'AH%sT'
        elif(dt < datetime(1983,11,30,0,0)):
            offset = timedelta(seconds=0, hours=-9, minutes=0)
            rule = _US
            format = 'Y%sT'
        else:
            offset = timedelta(seconds=0, hours=-9, minutes=0)
            rule = _US
            format = 'AK%sT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
class Pacific_Nauru(tzinfo):
    def __from_rules(self, dt):
        rule = None
        format = None
        letter = None
        offset = timedelta()
        save = timedelta()
        if dt:
            dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            dt = datetime.now()
        if (dt < datetime(1921,1,15,0,0)):
            offset = timedelta(seconds=0, hours=11, minutes=7)
            rule = None
            format = 'LMT'
        elif(dt < datetime(1942,3,15,0,0)):
            offset = timedelta(seconds=0, hours=11, minutes=30)
            rule = None
            format = 'NRT'
        elif(dt < datetime(1944,8,15,0,0)):
            offset = timedelta(seconds=0, hours=9, minutes=0)
            rule = None
            format = 'JST'
        elif(dt < datetime(1979,5,1,0,0)):
            offset = timedelta(seconds=0, hours=11, minutes=30)
            rule = None
            format = 'NRT'
        else:
            offset = timedelta(seconds=0, hours=12, minutes=0)
            rule = None
            format = 'NRT'
        if rule is not None:
            save, letter = rule(dt)
        if offset is not None and save is not None:
            offset = offset - save
        if format is not None and letter is not None and '%' in format:
            format = format % letter
        return offset, save, format
    def utcoffset(self, dt):
        offset, _, _ = self.__from_rules(dt)
        return offset
    def dst(self, dt):
        _, save, _ = self.__from_rules(dt)
        return save
    def tzname(self, dt):
        _, _, format = self.__from_rules(dt)
        return format
# Links
America_Virgin = America_Port_of_Spain
America_Buenos_Aires = America_Argentina_Buenos_Aires
Hongkong = Asia_Hong_Kong
Etc_GMTplus0 = Etc_GMT
Asia_Calcutta = Asia_Kolkata
Australia_South = Australia_Adelaide
America_Atka = America_Adak
America_Coral_Harbour = America_Atikokan
Africa_Freetown = Africa_Abidjan
America_Fort_Wayne = America_Indiana_Indianapolis
Canada_Newfoundland = America_St_Johns
America_Montserrat = America_Port_of_Spain
PRC = Asia_Shanghai
US_Mountain = America_Denver
Asia_Thimbu = Asia_Thimphu
Africa_Timbuktu = Africa_Abidjan
Asia_Kashgar = Asia_Urumqi
America_Shiprock = America_Denver
America_Grenada = America_Port_of_Spain
Europe_Podgorica = Europe_Belgrade
Africa_Juba = Africa_Khartoum
Brazil_DeNoronha = America_Noronha
Etc_Universal = Etc_UTC
Arctic_Longyearbyen = Europe_Oslo
Europe_Guernsey = Europe_London
GB = Europe_London
America_Aruba = America_Curacao
Canada_Yukon = America_Whitehorse
Jamaica = America_Jamaica
America_Indianapolis = America_Indiana_Indianapolis
Pacific_Truk = Pacific_Chuuk
Pacific_Yap = Pacific_Chuuk
America_Ensenada = America_Tijuana
Europe_Sarajevo = Europe_Belgrade
Canada_Atlantic = America_Halifax
Turkey = Europe_Istanbul
America_Jujuy = America_Argentina_Jujuy
America_Cordoba = America_Argentina_Cordoba
Asia_Harbin = Asia_Shanghai
Africa_Sao_Tome = Africa_Abidjan
Europe_Skopje = Europe_Belgrade
America_Kralendijk = America_Curacao
Australia_Tasmania = Australia_Hobart
Europe_Jersey = Europe_London
Europe_Nicosia = Asia_Nicosia
Asia_Macao = Asia_Macau
Eire = Europe_Dublin
ROK = Asia_Seoul
US_Hawaii = Pacific_Honolulu
Asia_Ujung_Pandang = Asia_Makassar
Cuba = America_Havana
Asia_Saigon = Asia_Ho_Chi_Minh
ROC = Asia_Taipei
America_Louisville = America_Kentucky_Louisville
Canada_Mountain = America_Edmonton
America_St_Thomas = America_Port_of_Spain
America_Porto_Acre = America_Rio_Branco
Navajo = America_Denver
America_Guadeloupe = America_Port_of_Spain
Australia_West = Australia_Perth
Brazil_West = America_Manaus
Libya = Africa_Tripoli
America_St_Lucia = America_Port_of_Spain
Antarctica_McMurdo = Pacific_Auckland
Canada_Saskatchewan = America_Regina
Canada_Pacific = America_Vancouver
Canada_Eastern = America_Toronto
Australia_Victoria = Australia_Melbourne
GB_Eire = Europe_London
Etc_Greenwich = Etc_GMT
Atlantic_Jan_Mayen = Europe_Oslo
Mexico_BajaSur = America_Mazatlan
America_St_Vincent = America_Port_of_Spain
Australia_ACT = Australia_Sydney
Portugal = Europe_Lisbon
Europe_Tiraspol = Europe_Chisinau
Europe_Busingen = Europe_Zurich
Asia_Katmandu = Asia_Kathmandu
Africa_Bamako = Africa_Abidjan
Etc_GMT0 = Etc_GMT
Pacific_Ponape = Pacific_Pohnpei
Africa_Banjul = Africa_Abidjan
Japan = Asia_Tokyo
Asia_Ulan_Bator = Asia_Ulaanbaatar
Kwajalein = Pacific_Kwajalein
Australia_Yancowinna = Australia_Broken_Hill
America_Marigot = America_Port_of_Spain
America_Lower_Princes = America_Curacao
Greenwich = Etc_GMT
America_Mendoza = America_Argentina_Mendoza
Asia_Dacca = Asia_Dhaka
US_East_Indiana = America_Indiana_Indianapolis
America_Argentina_ComodRivadavia = America_Argentina_Catamarca
Africa_Nouakchott = Africa_Abidjan
Canada_East_Saskatchewan = America_Regina
US_Pacific_New = America_Los_Angeles
Chile_Continental = America_Santiago
Asia_Tel_Aviv = Asia_Jerusalem
Canada_Central = America_Winnipeg
Asia_Istanbul = Europe_Istanbul
America_Rosario = America_Argentina_Cordoba
GMT0 = Etc_GMT
Europe_Mariehamn = Europe_Helsinki
Iran = Asia_Tehran
US_Aleutian = America_Adak
US_Pacific = America_Los_Angeles
Australia_North = Australia_Darwin
US_Samoa = Pacific_Pago_Pago
US_Michigan = America_Detroit
Asia_Chungking = Asia_Shanghai
Europe_Isle_of_Man = Europe_London
NZ = Pacific_Auckland
Asia_Ashkhabad = Asia_Ashgabat
America_Knox_IN = America_Indiana_Knox
America_Catamarca = America_Argentina_Catamarca
Zulu = Etc_UTC
Africa_Dakar = Africa_Abidjan
GMTplus0 = Etc_GMT
Poland = Europe_Warsaw
Pacific_Samoa = Pacific_Pago_Pago
US_Indiana_Starke = America_Indiana_Knox
Australia_LHI = Australia_Lord_Howe
Pacific_Johnston = Pacific_Honolulu
GMT = Etc_GMT
Chile_EasterIsland = Pacific_Easter
Africa_Conakry = Africa_Abidjan
Universal = Etc_UTC
US_Arizona = America_Phoenix
Europe_San_Marino = Europe_Rome
Asia_Chongqing = Asia_Shanghai
Australia_NSW = Australia_Sydney
America_St_Kitts = America_Port_of_Spain
Brazil_East = America_Sao_Paulo
Etc_Zulu = Etc_UTC
Singapore = Asia_Singapore
Europe_Ljubljana = Europe_Belgrade
US_Alaska = America_Anchorage
Atlantic_Faeroe = Atlantic_Faroe
Etc_GMT_0 = Etc_GMT
America_Anguilla = America_Port_of_Spain
Israel = Asia_Jerusalem
UCT = Etc_UCT
NZ_CHAT = Pacific_Chatham
Atlantic_St_Helena = Africa_Abidjan
Iceland = Atlantic_Reykjavik
Brazil_Acre = America_Rio_Branco
Europe_Vatican = Europe_Rome
Australia_Queensland = Australia_Brisbane
Africa_Lome = Africa_Abidjan
UTC = Etc_UTC
Mexico_BajaNorte = America_Tijuana
Australia_Canberra = Australia_Sydney
Europe_Zagreb = Europe_Belgrade
Europe_Belfast = Europe_London
US_Eastern = America_New_York
America_St_Barthelemy = America_Port_of_Spain
US_Central = America_Chicago
Europe_Bratislava = Europe_Prague
Mexico_General = America_Mexico_City
GMT_0 = Etc_GMT
W_SU = Europe_Moscow
America_Dominica = America_Port_of_Spain
Egypt = Africa_Cairo
America_Tortola = America_Port_of_Spain
Europe_Vaduz = Europe_Zurich
Africa_Ouagadougou = Africa_Abidjan
Africa_Asmera = Africa_Asmara
Antarctica_South_Pole = Pacific_Auckland

timezones = {
        "Atlantic/Canary": Atlantic_Canary(),
        "Australia/Melbourne": Australia_Melbourne(),
        "Etc/GMT+9": Etc_GMTplus9(),
        "Etc/GMT+8": Etc_GMTplus8(),
        "Europe/Lisbon": Europe_Lisbon(),
        "Etc/GMT+3": Etc_GMTplus3(),
        "Etc/GMT+2": Etc_GMTplus2(),
        "Etc/GMT+1": Etc_GMTplus1(),
        "America/Nipigon": America_Nipigon(),
        "Etc/GMT+6": Etc_GMTplus6(),
        "Etc/GMT+5": Etc_GMTplus5(),
        "Etc/GMT+4": Etc_GMTplus4(),
        "Indian/Reunion": Indian_Reunion(),
        "Asia/Dhaka": Asia_Dhaka(),
        "America/Phoenix": America_Phoenix(),
        "Europe/Kaliningrad": Europe_Kaliningrad(),
        "Etc/GMT+7": Etc_GMTplus7(),
        "America/Mazatlan": America_Mazatlan(),
        "Europe/Paris": Europe_Paris(),
        "Europe/Stockholm": Europe_Stockholm(),
        "Pacific/Fiji": Pacific_Fiji(),
        "Pacific/Apia": Pacific_Apia(),
        "America/Miquelon": America_Miquelon(),
        "Pacific/Pago_Pago": Pacific_Pago_Pago(),
        "Asia/Rangoon": Asia_Rangoon(),
        "America/Mexico_City": America_Mexico_City(),
        "America/Puerto_Rico": America_Puerto_Rico(),
        "Indian/Mauritius": Indian_Mauritius(),
        "Europe/Berlin": Europe_Berlin(),
        "Europe/Zurich": Europe_Zurich(),
        "Africa/Casablanca": Africa_Casablanca(),
        "Antarctica/Macquarie": Antarctica_Macquarie(),
        "Asia/Krasnoyarsk": Asia_Krasnoyarsk(),
        "Atlantic/Bermuda": Atlantic_Bermuda(),
        "Australia/Currie": Australia_Currie(),
        "Asia/Tehran": Asia_Tehran(),
        "Asia/Baku": Asia_Baku(),
        "America/Santarem": America_Santarem(),
        "America/Danmarkshavn": America_Danmarkshavn(),
        "America/Scoresbysund": America_Scoresbysund(),
        "America/Eirunepe": America_Eirunepe(),
        "Asia/Baghdad": Asia_Baghdad(),
        "Africa/Monrovia": Africa_Monrovia(),
        "America/Vancouver": America_Vancouver(),
        "Asia/Ho_Chi_Minh": Asia_Ho_Chi_Minh(),
        "Asia/Thimphu": Asia_Thimphu(),
        "Africa/Accra": Africa_Accra(),
        "America/Belize": America_Belize(),
        "America/Port_of_Spain": America_Port_of_Spain(),
        "Asia/Tashkent": Asia_Tashkent(),
        "Asia/Tokyo": Asia_Tokyo(),
        "Pacific/Kiritimati": Pacific_Kiritimati(),
        "Australia/Sydney": Australia_Sydney(),
        "Europe/Riga": Europe_Riga(),
        "Asia/Dili": Asia_Dili(),
        "Africa/Mbabane": Africa_Mbabane(),
        "Asia/Oral": Asia_Oral(),
        "Asia/Aden": Asia_Aden(),
        "MST7MDT": MST7MDT(),
        "Europe/Istanbul": Europe_Istanbul(),
        "Africa/Abidjan": Africa_Abidjan(),
        "Australia/Lindeman": Australia_Lindeman(),
        "Pacific/Galapagos": Pacific_Galapagos(),
        "America/Bogota": America_Bogota(),
        "Africa/Asmara": Africa_Asmara(),
        "America/Chicago": America_Chicago(),
        "Pacific/Kwajalein": Pacific_Kwajalein(),
        "Australia/Broken_Hill": Australia_Broken_Hill(),
        "America/Cuiaba": America_Cuiaba(),
        "Indian/Christmas": Indian_Christmas(),
        "Asia/Jayapura": Asia_Jayapura(),
        "Europe/Brussels": Europe_Brussels(),
        "America/Argentina/Cordoba": America_Argentina_Cordoba(),
        "America/Noronha": America_Noronha(),
        "Africa/Algiers": Africa_Algiers(),
        "Africa/Harare": Africa_Harare(),
        "Africa/Ndjamena": Africa_Ndjamena(),
        "America/Costa_Rica": America_Costa_Rica(),
        "Indian/Mayotte": Indian_Mayotte(),
        "Asia/Phnom_Penh": Asia_Phnom_Penh(),
        "America/Managua": America_Managua(),
        "America/Pangnirtung": America_Pangnirtung(),
        "Asia/Nicosia": Asia_Nicosia(),
        "America/Tijuana": America_Tijuana(),
        "Pacific/Fakaofo": Pacific_Fakaofo(),
        "America/Martinique": America_Martinique(),
        "America/Antigua": America_Antigua(),
        "America/Indiana/Indianapolis": America_Indiana_Indianapolis(),
        "America/Argentina/La_Rioja": America_Argentina_La_Rioja(),
        "Pacific/Tahiti": Pacific_Tahiti(),
        "Asia/Brunei": Asia_Brunei(),
        "America/Asuncion": America_Asuncion(),
        "Europe/Vienna": Europe_Vienna(),
        "Australia/Hobart": Australia_Hobart(),
        "America/Juneau": America_Juneau(),
        "America/Inuvik": America_Inuvik(),
        "America/Ojinaga": America_Ojinaga(),
        "America/Montreal": America_Montreal(),
        "Asia/Seoul": Asia_Seoul(),
        "Indian/Comoro": Indian_Comoro(),
        "Europe/Tallinn": Europe_Tallinn(),
        "Indian/Mahe": Indian_Mahe(),
        "America/Argentina/Jujuy": America_Argentina_Jujuy(),
        "America/Creston": America_Creston(),
        "America/Adak": America_Adak(),
        "Asia/Singapore": Asia_Singapore(),
        "Africa/Nairobi": Africa_Nairobi(),
        "Pacific/Noumea": Pacific_Noumea(),
        "Africa/Cairo": Africa_Cairo(),
        "Europe/Moscow": Europe_Moscow(),
        "Asia/Ulaanbaatar": Asia_Ulaanbaatar(),
        "America/Rainy_River": America_Rainy_River(),
        "Africa/Kampala": Africa_Kampala(),
        "Asia/Colombo": Asia_Colombo(),
        "Australia/Adelaide": Australia_Adelaide(),
        "America/Cambridge_Bay": America_Cambridge_Bay(),
        "Africa/Luanda": Africa_Luanda(),
        "Pacific/Chatham": Pacific_Chatham(),
        "America/Indiana/Winamac": America_Indiana_Winamac(),
        "Asia/Tbilisi": Asia_Tbilisi(),
        "Europe/Gibraltar": Europe_Gibraltar(),
        "Asia/Karachi": Asia_Karachi(),
        "Australia/Lord_Howe": Australia_Lord_Howe(),
        "Etc/GMT-9": Etc_GMT_9(),
        "Etc/GMT-8": Etc_GMT_8(),
        "America/Bahia_Banderas": America_Bahia_Banderas(),
        "Etc/GMT-1": Etc_GMT_1(),
        "Etc/GMT-3": Etc_GMT_3(),
        "Etc/GMT-2": Etc_GMT_2(),
        "Etc/GMT-5": Etc_GMT_5(),
        "Etc/GMT-4": Etc_GMT_4(),
        "Etc/GMT-7": Etc_GMT_7(),
        "Etc/GMT-6": Etc_GMT_6(),
        "America/Boa_Vista": America_Boa_Vista(),
        "Africa/Tripoli": Africa_Tripoli(),
        "Pacific/Wallis": Pacific_Wallis(),
        "Atlantic/Stanley": Atlantic_Stanley(),
        "Asia/Srednekolymsk": Asia_Srednekolymsk(),
        "CET": CET(),
        "Africa/Lubumbashi": Africa_Lubumbashi(),
        "America/Blanc-Sablon": America_Blanc_Sablon(),
        "America/Jamaica": America_Jamaica(),
        "Europe/Kiev": Europe_Kiev(),
        "Europe/Budapest": Europe_Budapest(),
        "Pacific/Midway": Pacific_Midway(),
        "America/Goose_Bay": America_Goose_Bay(),
        "Asia/Amman": Asia_Amman(),
        "Asia/Sakhalin": Asia_Sakhalin(),
        "Africa/Windhoek": Africa_Windhoek(),
        "America/Sitka": America_Sitka(),
        "America/Guyana": America_Guyana(),
        "Pacific/Pohnpei": Pacific_Pohnpei(),
        "America/Sao_Paulo": America_Sao_Paulo(),
        "Australia/Perth": Australia_Perth(),
        "Africa/Djibouti": Africa_Djibouti(),
        "Asia/Jakarta": Asia_Jakarta(),
        "Asia/Pyongyang": Asia_Pyongyang(),
        "EST5EDT": EST5EDT(),
        "Africa/Johannesburg": Africa_Johannesburg(),
        "Asia/Irkutsk": Asia_Irkutsk(),
        "Africa/Niamey": Africa_Niamey(),
        "America/Belem": America_Belem(),
        "America/Indiana/Marengo": America_Indiana_Marengo(),
        "Europe/Vilnius": Europe_Vilnius(),
        "America/Cayenne": America_Cayenne(),
        "Africa/Mogadishu": Africa_Mogadishu(),
        "America/Kentucky/Monticello": America_Kentucky_Monticello(),
        "America/Rio_Branco": America_Rio_Branco(),
        "America/Cancun": America_Cancun(),
        "America/Havana": America_Havana(),
        "Pacific/Guam": Pacific_Guam(),
        "Pacific/Kosrae": Pacific_Kosrae(),
        "Atlantic/Azores": Atlantic_Azores(),
        "Australia/Eucla": Australia_Eucla(),
        "Asia/Shanghai": Asia_Shanghai(),
        "America/Rankin_Inlet": America_Rankin_Inlet(),
        "Asia/Beirut": Asia_Beirut(),
        "Africa/Maputo": Africa_Maputo(),
        "Asia/Bahrain": Asia_Bahrain(),
        "Asia/Ashgabat": Asia_Ashgabat(),
        "Asia/Riyadh": Asia_Riyadh(),
        "Europe/London": Europe_London(),
        "Europe/Warsaw": Europe_Warsaw(),
        "Asia/Damascus": Asia_Damascus(),
        "America/North_Dakota/Center": America_North_Dakota_Center(),
        "America/Indiana/Vevay": America_Indiana_Vevay(),
        "America/Barbados": America_Barbados(),
        "Atlantic/Faroe": Atlantic_Faroe(),
        "Asia/Almaty": Asia_Almaty(),
        "America/Santo_Domingo": America_Santo_Domingo(),
        "Africa/Brazzaville": Africa_Brazzaville(),
        "America/Nome": America_Nome(),
        "Europe/Dublin": Europe_Dublin(),
        "America/Yakutat": America_Yakutat(),
        "America/Argentina/Mendoza": America_Argentina_Mendoza(),
        "America/Araguaina": America_Araguaina(),
        "Etc/UTC": Etc_UTC(),
        "Europe/Minsk": Europe_Minsk(),
        "Asia/Kolkata": Asia_Kolkata(),
        "Africa/Maseru": Africa_Maseru(),
        "America/Atikokan": America_Atikokan(),
        "America/Santa_Isabel": America_Santa_Isabel(),
        "Asia/Kuching": Asia_Kuching(),
        "Africa/Libreville": Africa_Libreville(),
        "Africa/Bissau": Africa_Bissau(),
        "Europe/Samara": Europe_Samara(),
        "Europe/Amsterdam": Europe_Amsterdam(),
        "Europe/Tirane": Europe_Tirane(),
        "Pacific/Saipan": Pacific_Saipan(),
        "Asia/Magadan": Asia_Magadan(),
        "Europe/Zaporozhye": Europe_Zaporozhye(),
        "HST": HST(),
        "America/El_Salvador": America_El_Salvador(),
        "Europe/Madrid": Europe_Madrid(),
        "America/Santiago": America_Santiago(),
        "America/Argentina/Buenos_Aires": America_Argentina_Buenos_Aires(),
        "America/Argentina/San_Luis": America_Argentina_San_Luis(),
        "WET": WET(),
        "America/Regina": America_Regina(),
        "Pacific/Chuuk": Pacific_Chuuk(),
        "Asia/Khandyga": Asia_Khandyga(),
        "Pacific/Funafuti": Pacific_Funafuti(),
        "America/Merida": America_Merida(),
        "America/Guatemala": America_Guatemala(),
        "Asia/Makassar": Asia_Makassar(),
        "Africa/Bujumbura": Africa_Bujumbura(),
        "Europe/Chisinau": Europe_Chisinau(),
        "America/Monterrey": America_Monterrey(),
        "Asia/Yekaterinburg": Asia_Yekaterinburg(),
        "Pacific/Enderbury": Pacific_Enderbury(),
        "America/Thule": America_Thule(),
        "America/St_Johns": America_St_Johns(),
        "America/Moncton": America_Moncton(),
        "Europe/Helsinki": Europe_Helsinki(),
        "Atlantic/Cape_Verde": Atlantic_Cape_Verde(),
        "America/Tegucigalpa": America_Tegucigalpa(),
        "Indian/Cocos": Indian_Cocos(),
        "America/Boise": America_Boise(),
        "America/Nassau": America_Nassau(),
        "Europe/Prague": Europe_Prague(),
        "America/Halifax": America_Halifax(),
        "Asia/Hovd": Asia_Hovd(),
        "America/Manaus": America_Manaus(),
        "America/Godthab": America_Godthab(),
        "Etc/UCT": Etc_UCT(),
        "America/North_Dakota/Beulah": America_North_Dakota_Beulah(),
        "America/Chihuahua": America_Chihuahua(),
        "America/Iqaluit": America_Iqaluit(),
        "America/Argentina/Rio_Gallegos": America_Argentina_Rio_Gallegos(),
        "Pacific/Gambier": Pacific_Gambier(),
        "Europe/Volgograd": Europe_Volgograd(),
        "Asia/Novokuznetsk": Asia_Novokuznetsk(),
        "Europe/Uzhgorod": Europe_Uzhgorod(),
        "Asia/Aqtau": Asia_Aqtau(),
        "Pacific/Palau": Pacific_Palau(),
        "Africa/Malabo": Africa_Malabo(),
        "PST8PDT": PST8PDT(),
        "Atlantic/Madeira": Atlantic_Madeira(),
        "America/Maceio": America_Maceio(),
        "Africa/Kinshasa": Africa_Kinshasa(),
        "Europe/Malta": Europe_Malta(),
        "America/Argentina/Ushuaia": America_Argentina_Ushuaia(),
        "Asia/Bangkok": Asia_Bangkok(),
        "Pacific/Niue": Pacific_Niue(),
        "Australia/Brisbane": Australia_Brisbane(),
        "America/Recife": America_Recife(),
        "America/Glace_Bay": America_Glace_Bay(),
        "Asia/Yerevan": Asia_Yerevan(),
        "America/La_Paz": America_La_Paz(),
        "Asia/Urumqi": Asia_Urumqi(),
        "Africa/Lusaka": Africa_Lusaka(),
        "Pacific/Guadalcanal": Pacific_Guadalcanal(),
        "America/Yellowknife": America_Yellowknife(),
        "Asia/Vientiane": Asia_Vientiane(),
        "Asia/Kuwait": Asia_Kuwait(),
        "America/Argentina/Tucuman": America_Argentina_Tucuman(),
        "Asia/Chita": Asia_Chita(),
        "Europe/Oslo": Europe_Oslo(),
        "America/Caracas": America_Caracas(),
        "America/Panama": America_Panama(),
        "America/Hermosillo": America_Hermosillo(),
        "Asia/Hebron": Asia_Hebron(),
        "America/Guayaquil": America_Guayaquil(),
        "Asia/Kuala_Lumpur": Asia_Kuala_Lumpur(),
        "America/Menominee": America_Menominee(),
        "Asia/Kamchatka": Asia_Kamchatka(),
        "Factory": Factory(),
        "Asia/Vladivostok": Asia_Vladivostok(),
        "America/Matamoros": America_Matamoros(),
        "Asia/Qatar": Asia_Qatar(),
        "Asia/Dubai": Asia_Dubai(),
        "Asia/Yakutsk": Asia_Yakutsk(),
        "Asia/Omsk": Asia_Omsk(),
        "Africa/Bangui": Africa_Bangui(),
        "America/Paramaribo": America_Paramaribo(),
        "Etc/GMT-11": Etc_GMT_11(),
        "Etc/GMT-10": Etc_GMT_10(),
        "Etc/GMT-13": Etc_GMT_13(),
        "Etc/GMT-12": Etc_GMT_12(),
        "Etc/GMT-14": Etc_GMT_14(),
        "Pacific/Marquesas": Pacific_Marquesas(),
        "Asia/Anadyr": Asia_Anadyr(),
        "America/New_York": America_New_York(),
        "Pacific/Norfolk": Pacific_Norfolk(),
        "CST6CDT": CST6CDT(),
        "Pacific/Rarotonga": Pacific_Rarotonga(),
        "Africa/Porto-Novo": Africa_Porto_Novo(),
        "Asia/Samarkand": Asia_Samarkand(),
        "Asia/Dushanbe": Asia_Dushanbe(),
        "America/Kentucky/Louisville": America_Kentucky_Louisville(),
        "America/Toronto": America_Toronto(),
        "America/Bahia": America_Bahia(),
        "Indian/Maldives": Indian_Maldives(),
        "Asia/Muscat": Asia_Muscat(),
        "America/Edmonton": America_Edmonton(),
        "Pacific/Wake": Pacific_Wake(),
        "America/Indiana/Tell_City": America_Indiana_Tell_City(),
        "Australia/Darwin": Australia_Darwin(),
        "America/Whitehorse": America_Whitehorse(),
        "America/Swift_Current": America_Swift_Current(),
        "Europe/Copenhagen": Europe_Copenhagen(),
        "America/Argentina/Salta": America_Argentina_Salta(),
        "Europe/Simferopol": Europe_Simferopol(),
        "Africa/Blantyre": Africa_Blantyre(),
        "America/Detroit": America_Detroit(),
        "America/Indiana/Vincennes": America_Indiana_Vincennes(),
        "America/Indiana/Petersburg": America_Indiana_Petersburg(),
        "Asia/Kathmandu": Asia_Kathmandu(),
        "Asia/Pontianak": Asia_Pontianak(),
        "Europe/Athens": Europe_Athens(),
        "America/Port-au-Prince": America_Port_au_Prince(),
        "America/Cayman": America_Cayman(),
        "Africa/Dar_es_Salaam": Africa_Dar_es_Salaam(),
        "America/Curacao": America_Curacao(),
        "Africa/Khartoum": Africa_Khartoum(),
        "Asia/Manila": Asia_Manila(),
        "Africa/Douala": Africa_Douala(),
        "EET": EET(),
        "America/Argentina/San_Juan": America_Argentina_San_Juan(),
        "America/North_Dakota/New_Salem": America_North_Dakota_New_Salem(),
        "Pacific/Port_Moresby": Pacific_Port_Moresby(),
        "Europe/Andorra": Europe_Andorra(),
        "Europe/Luxembourg": Europe_Luxembourg(),
        "Pacific/Honolulu": Pacific_Honolulu(),
        "Pacific/Majuro": Pacific_Majuro(),
        "Asia/Hong_Kong": Asia_Hong_Kong(),
        "Asia/Macau": Asia_Macau(),
        "Europe/Belgrade": Europe_Belgrade(),
        "Asia/Choibalsan": Asia_Choibalsan(),
        "America/Thunder_Bay": America_Thunder_Bay(),
        "America/Los_Angeles": America_Los_Angeles(),
        "Asia/Kabul": Asia_Kabul(),
        "Indian/Antananarivo": Indian_Antananarivo(),
        "Atlantic/Reykjavik": Atlantic_Reykjavik(),
        "Etc/GMT+12": Etc_GMTplus12(),
        "Etc/GMT+11": Etc_GMTplus11(),
        "Etc/GMT+10": Etc_GMTplus10(),
        "Pacific/Tongatapu": Pacific_Tongatapu(),
        "Pacific/Pitcairn": Pacific_Pitcairn(),
        "Pacific/Easter": Pacific_Easter(),
        "Atlantic/South_Georgia": Atlantic_South_Georgia(),
        "Africa/El_Aaiun": Africa_El_Aaiun(),
        "America/Campo_Grande": America_Campo_Grande(),
        "America/Dawson_Creek": America_Dawson_Creek(),
        "Europe/Bucharest": Europe_Bucharest(),
        "America/Porto_Velho": America_Porto_Velho(),
        "Europe/Monaco": Europe_Monaco(),
        "Asia/Bishkek": Asia_Bishkek(),
        "Africa/Ceuta": Africa_Ceuta(),
        "Europe/Rome": Europe_Rome(),
        "America/Winnipeg": America_Winnipeg(),
        "Asia/Aqtobe": Asia_Aqtobe(),
        "America/Fortaleza": America_Fortaleza(),
        "Pacific/Tarawa": Pacific_Tarawa(),
        "America/Dawson": America_Dawson(),
        "Africa/Addis_Ababa": Africa_Addis_Ababa(),
        "Pacific/Efate": Pacific_Efate(),
        "Asia/Qyzylorda": Asia_Qyzylorda(),
        "Asia/Jerusalem": Asia_Jerusalem(),
        "MET": MET(),
        "Pacific/Auckland": Pacific_Auckland(),
        "America/Metlakatla": America_Metlakatla(),
        "America/Denver": America_Denver(),
        "Indian/Chagos": Indian_Chagos(),
        "MST": MST(),
        "Africa/Gaborone": Africa_Gaborone(),
        "Africa/Tunis": Africa_Tunis(),
        "America/Montevideo": America_Montevideo(),
        "Asia/Ust-Nera": Asia_Ust_Nera(),
        "America/Resolute": America_Resolute(),
        "Etc/GMT": Etc_GMT(),
        "Asia/Gaza": Asia_Gaza(),
        "Asia/Taipei": Asia_Taipei(),
        "America/Argentina/Catamarca": America_Argentina_Catamarca(),
        "America/Indiana/Knox": America_Indiana_Knox(),
        "Asia/Novosibirsk": Asia_Novosibirsk(),
        "EST": EST(),
        "Africa/Kigali": Africa_Kigali(),
        "America/Grand_Turk": America_Grand_Turk(),
        "Africa/Lagos": Africa_Lagos(),
        "Europe/Sofia": Europe_Sofia(),
        "America/Lima": America_Lima(),
        "America/Anchorage": America_Anchorage(),
        "Pacific/Nauru": Pacific_Nauru(),
        "America/Virgin": America_Virgin(),
        "America/Buenos_Aires": America_Buenos_Aires(),
        "Hongkong": Hongkong(),
        "Etc/GMT+0": Etc_GMTplus0(),
        "Asia/Calcutta": Asia_Calcutta(),
        "Australia/South": Australia_South(),
        "America/Atka": America_Atka(),
        "America/Coral_Harbour": America_Coral_Harbour(),
        "Africa/Freetown": Africa_Freetown(),
        "America/Fort_Wayne": America_Fort_Wayne(),
        "Canada/Newfoundland": Canada_Newfoundland(),
        "America/Montserrat": America_Montserrat(),
        "PRC": PRC(),
        "US/Mountain": US_Mountain(),
        "Asia/Thimbu": Asia_Thimbu(),
        "Africa/Timbuktu": Africa_Timbuktu(),
        "Asia/Kashgar": Asia_Kashgar(),
        "America/Shiprock": America_Shiprock(),
        "America/Grenada": America_Grenada(),
        "Europe/Podgorica": Europe_Podgorica(),
        "Africa/Juba": Africa_Juba(),
        "Brazil/DeNoronha": Brazil_DeNoronha(),
        "Etc/Universal": Etc_Universal(),
        "Arctic/Longyearbyen": Arctic_Longyearbyen(),
        "Europe/Guernsey": Europe_Guernsey(),
        "GB": GB(),
        "America/Aruba": America_Aruba(),
        "Canada/Yukon": Canada_Yukon(),
        "Jamaica": Jamaica(),
        "America/Indianapolis": America_Indianapolis(),
        "Pacific/Truk": Pacific_Truk(),
        "Pacific/Yap": Pacific_Yap(),
        "America/Ensenada": America_Ensenada(),
        "Europe/Sarajevo": Europe_Sarajevo(),
        "Canada/Atlantic": Canada_Atlantic(),
        "Turkey": Turkey(),
        "America/Jujuy": America_Jujuy(),
        "America/Cordoba": America_Cordoba(),
        "Asia/Harbin": Asia_Harbin(),
        "Africa/Sao_Tome": Africa_Sao_Tome(),
        "Europe/Skopje": Europe_Skopje(),
        "America/Kralendijk": America_Kralendijk(),
        "Australia/Tasmania": Australia_Tasmania(),
        "Europe/Jersey": Europe_Jersey(),
        "Europe/Nicosia": Europe_Nicosia(),
        "Asia/Macao": Asia_Macao(),
        "Eire": Eire(),
        "ROK": ROK(),
        "US/Hawaii": US_Hawaii(),
        "Asia/Ujung_Pandang": Asia_Ujung_Pandang(),
        "Cuba": Cuba(),
        "Asia/Saigon": Asia_Saigon(),
        "ROC": ROC(),
        "America/Louisville": America_Louisville(),
        "Canada/Mountain": Canada_Mountain(),
        "America/St_Thomas": America_St_Thomas(),
        "America/Porto_Acre": America_Porto_Acre(),
        "Navajo": Navajo(),
        "America/Guadeloupe": America_Guadeloupe(),
        "Australia/West": Australia_West(),
        "Brazil/West": Brazil_West(),
        "Libya": Libya(),
        "America/St_Lucia": America_St_Lucia(),
        "Antarctica/McMurdo": Antarctica_McMurdo(),
        "Canada/Saskatchewan": Canada_Saskatchewan(),
        "Canada/Pacific": Canada_Pacific(),
        "Canada/Eastern": Canada_Eastern(),
        "Australia/Victoria": Australia_Victoria(),
        "GB-Eire": GB_Eire(),
        "Etc/Greenwich": Etc_Greenwich(),
        "Atlantic/Jan_Mayen": Atlantic_Jan_Mayen(),
        "Mexico/BajaSur": Mexico_BajaSur(),
        "America/St_Vincent": America_St_Vincent(),
        "Australia/ACT": Australia_ACT(),
        "Portugal": Portugal(),
        "Europe/Tiraspol": Europe_Tiraspol(),
        "Europe/Busingen": Europe_Busingen(),
        "Asia/Katmandu": Asia_Katmandu(),
        "Africa/Bamako": Africa_Bamako(),
        "Etc/GMT0": Etc_GMT0(),
        "Pacific/Ponape": Pacific_Ponape(),
        "Africa/Banjul": Africa_Banjul(),
        "Japan": Japan(),
        "Asia/Ulan_Bator": Asia_Ulan_Bator(),
        "Kwajalein": Kwajalein(),
        "Australia/Yancowinna": Australia_Yancowinna(),
        "America/Marigot": America_Marigot(),
        "America/Lower_Princes": America_Lower_Princes(),
        "Greenwich": Greenwich(),
        "America/Mendoza": America_Mendoza(),
        "Asia/Dacca": Asia_Dacca(),
        "US/East-Indiana": US_East_Indiana(),
        "America/Argentina/ComodRivadavia": America_Argentina_ComodRivadavia(),
        "Africa/Nouakchott": Africa_Nouakchott(),
        "Canada/East-Saskatchewan": Canada_East_Saskatchewan(),
        "US/Pacific-New": US_Pacific_New(),
        "Chile/Continental": Chile_Continental(),
        "Asia/Tel_Aviv": Asia_Tel_Aviv(),
        "Canada/Central": Canada_Central(),
        "Asia/Istanbul": Asia_Istanbul(),
        "America/Rosario": America_Rosario(),
        "GMT0": GMT0(),
        "Europe/Mariehamn": Europe_Mariehamn(),
        "Iran": Iran(),
        "US/Aleutian": US_Aleutian(),
        "US/Pacific": US_Pacific(),
        "Australia/North": Australia_North(),
        "US/Samoa": US_Samoa(),
        "US/Michigan": US_Michigan(),
        "Asia/Chungking": Asia_Chungking(),
        "Europe/Isle_of_Man": Europe_Isle_of_Man(),
        "NZ": NZ(),
        "Asia/Ashkhabad": Asia_Ashkhabad(),
        "America/Knox_IN": America_Knox_IN(),
        "America/Catamarca": America_Catamarca(),
        "Zulu": Zulu(),
        "Africa/Dakar": Africa_Dakar(),
        "GMT+0": GMTplus0(),
        "Poland": Poland(),
        "Pacific/Samoa": Pacific_Samoa(),
        "US/Indiana-Starke": US_Indiana_Starke(),
        "Australia/LHI": Australia_LHI(),
        "Pacific/Johnston": Pacific_Johnston(),
        "GMT": GMT(),
        "Chile/EasterIsland": Chile_EasterIsland(),
        "Africa/Conakry": Africa_Conakry(),
        "Universal": Universal(),
        "US/Arizona": US_Arizona(),
        "Europe/San_Marino": Europe_San_Marino(),
        "Asia/Chongqing": Asia_Chongqing(),
        "Australia/NSW": Australia_NSW(),
        "America/St_Kitts": America_St_Kitts(),
        "Brazil/East": Brazil_East(),
        "Etc/Zulu": Etc_Zulu(),
        "Singapore": Singapore(),
        "Europe/Ljubljana": Europe_Ljubljana(),
        "US/Alaska": US_Alaska(),
        "Atlantic/Faeroe": Atlantic_Faeroe(),
        "Etc/GMT-0": Etc_GMT_0(),
        "America/Anguilla": America_Anguilla(),
        "Israel": Israel(),
        "UCT": UCT(),
        "NZ-CHAT": NZ_CHAT(),
        "Atlantic/St_Helena": Atlantic_St_Helena(),
        "Iceland": Iceland(),
        "Brazil/Acre": Brazil_Acre(),
        "Europe/Vatican": Europe_Vatican(),
        "Australia/Queensland": Australia_Queensland(),
        "Africa/Lome": Africa_Lome(),
        "UTC": UTC(),
        "Mexico/BajaNorte": Mexico_BajaNorte(),
        "Australia/Canberra": Australia_Canberra(),
        "Europe/Zagreb": Europe_Zagreb(),
        "Europe/Belfast": Europe_Belfast(),
        "US/Eastern": US_Eastern(),
        "America/St_Barthelemy": America_St_Barthelemy(),
        "US/Central": US_Central(),
        "Europe/Bratislava": Europe_Bratislava(),
        "Mexico/General": Mexico_General(),
        "GMT-0": GMT_0(),
        "W-SU": W_SU(),
        "America/Dominica": America_Dominica(),
        "Egypt": Egypt(),
        "America/Tortola": America_Tortola(),
        "Europe/Vaduz": Europe_Vaduz(),
        "Africa/Ouagadougou": Africa_Ouagadougou(),
        "Africa/Asmera": Africa_Asmera(),
        "Antarctica/South_Pole": Antarctica_South_Pole(),
}
