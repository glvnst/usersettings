#!/usr/bin/python
"""
usersettings example: counter

This simple example exposes almost the entire functionality of the module.
Each time the script is run, it loads a saved counter "setting", displays it,
increments it, and saves the incremented value to an OS appropriate location
on disk.

Note that after the import, you must specify your unique
reverse-domain-name-style identifier for this app. This influences the on-disk
location of the saved settings file.

Next you identify the names of the settings that will be stored, what type of
variable they are (e.g.: string, int, bool, float), and what the initial or
default value is. (You can use your own type, but it must seamlessly normalize
to and from a string. Also it would ideally be plain-text and user editable)

The call to load_settings loads the stored values for the settings you have
previously identified if they exist. (Don't bother checking first, just always
call this method.)

The previously-named settings can be accessed and changed as attributes of the
Settings object.

The save_settings call saves any changes to disk.
"""

from usersettings import Settings

CONF = Settings("com.example.apps.UserSettingsExample")
CONF.add_setting("counter", int, default=0)
CONF.load_settings()

print("Counter:", CONF.counter)
CONF.counter += 1

CONF.save_settings()
