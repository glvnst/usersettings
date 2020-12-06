# usersettings

## Portable Local Settings Storage for Python

- Automatic storage of settings information in a simple flat text file ([ConfigParser][] format)
- Automatically stored in an OS-appropriate location (via [appdirs][]). For example, with the chosen app identifier `com.example.apps.demo`:

    |     OS    | Settings File Location                                                                                       |
    | :-------: | ------------------------------------------------------------------------------------------------------------ |
    | macOS     | `~/Library/Application Support/com.example.apps.demo/settings.cfg`                                           |
    | GNU/Linux | `~/.config/com.example.apps.demo/settings.cfg`                                                               |
    | Windows   | `C:\Documents and Settings\<User>\Application Data\com.example.apps.demo\com.example.apps.demo\settings.cfg` |

- Interface modeled on the [argparse][] module.

## Installation 

To install this package, run: `pip install usersettings`

You can also download builds of [usersettings on the Python Package Index](https://pypi.org/project/usersettings/).

## Example:

The following example code shows the entire interface. This program will change its output each time it is run.

```python
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
```

Running this demo on a mac:

```
$ python examples/demo.py 
I've run 1 time(s). I like turtles! I've been launched at these times: [1607277627.5897138]

$ python examples/demo.py 
I've run 2 time(s). I like turtles! I've been launched at these times: [1607277627.5897138, 1607277630.170041]

$ python examples/demo.py 
I've run 3 time(s). I like the Rabbit of Caerbannog! I've been launched at these times: [1607277627.5897138, 1607277630.170041, 1607277631.320534]

$ cat ~/Library/Application\ Support/com.example.apps.demo/settings.cfg 
[settings]
counter = 3
animal = the Rabbit of Caerbannog
runtimes = [1607277627.5897138, 1607277630.170041, 1607277631.320534]
```

## License

This module is licensed under a BSD-style licence. See [LICENSE.txt](LICENSE.txt) for details.

## Notes

- Uses the [appdirs][] module from pypi. 
- Created after asking this [question on stack overflow](http://stackoverflow.com/questions/16275031/portable-settings-and-app-data-storage-in-python)
- `usersettings` not your cup of tea? Have a look at [configmgr](https://bitbucket.org/grantor61/configmgr), an earlier project which also leverages appdirs

[ConfigParser]: http://docs.python.org/2/library/configparser.html
[argparse]: http://docs.python.org/2/library/argparse.html
[appdirs]: https://pypi.python.org/pypi/appdirs
