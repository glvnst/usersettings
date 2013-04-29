#!/usr/bin/python
""" Quick test of UserSettings module """

import UserSettings

CONF = UserSettings.UserSettings('com.example.apps.UserSettingsTest')
CONF.add_setting("counter", int, default=0)
CONF.add_setting("floatie", float, default=3.14159)
CONF.add_setting("stringie", str, default="s")
CONF.add_setting("boolie", bool, default=True)
CONF.load_settings()

print "Counter:",  CONF.counter
print "Floatie:",  CONF.floatie
print "Stringie:", CONF.stringie
print "Boolie:",   CONF.boolie

CONF.counter += 1
CONF.floatie *= 2
CONF.stringie = CONF.stringie + str(CONF.counter)
CONF.boolie = not CONF.boolie

CONF.save_settings()

