#!/usr/bin/python
""" test usersettings """
import time
import usersettings

# Identify for your app
s = usersettings.Settings("com.example.apps.demo")

# specify what settings you have
s.add_setting("counter", int, default=0)
s.add_setting("animal", str, default="turtles")
s.add_setting("runtimes", list, [])

# load any previously-saved values for those
s.load_settings()

# use those values
s.counter += 1
if s.counter > 2:
    # Tired of turtles?
    s.animal = "the Rabbit of Caerbannog"
s.runtimes.append(time.time())

# save your changes
s.save_settings()

print(
    (
        "I've run {0.counter} time(s). "
        "I like {0.animal}! "
        "I've been launched at these times: {0.runtimes!s}"
    ).format(s)
)
