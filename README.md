# usersettings v1.0.7

## 2020 Note

After years of neglect, I'm going to try to get this package back into shape. If you use this package in your software, PLEASE open an issue with a link to your project. I need to write some tests and I want to make sure I'm capturing your use case. BTW if you're a good test writer, I'd love your help.

## Portable Local Settings Storage for Python

- Automatic storage of settings information in a simple flat text file ([ConfigParser][] format)
- Automatically stored in an OS-appropriate location (via [appdirs][]). For example, the settings for an app with the chosen identifier `com.example.apps.UserSettingsTest` would be stored in:
    - `~/Library/Application Support/com.example.apps.UserSettingsTest/settings.cfg` on OS X
    - `~/.config/com.example.apps.UserSettingsTest/settings.cfg` on Linux
    - `C:\Documents and Settings\<User>\Application Data\com.example.apps.UserSettingsTest\com.example.apps.UserSettingsTest\settings.cfg` (or an equivalent location depending on various factors) on Windows
- Interface modeled on the [argparse][] module.

## Example:

The following example code shows the entire interface. This program will change its output each time it is run.

    #!/usr/bin/python
    from usersettings import Settings
    import time
    
    # Identify for your app, specify what settings you have then
    # load em', use em', save em'
    
    s = Settings('com.example.apps.UserSettingsTest')    
    s.add_setting("counter", int, default=0)
    s.add_setting("animal", str, default="turtles")
    s.add_setting("runtimes", list, [])
    s.load_settings() # loads anything that might be saved
    
    s.counter += 1
    if s.counter > 2:
        # Tired of turtles?
        s.animal = "the Rabbit of Caerbannog"
    s.runtimes.append(time.time())
    s.save_settings()
    
    print "I've run {0.counter} time(s). I like {0.animal}!".format(s)
    print "I've been launched at these times: ",
    print ", ".join([str(x) for x in s.runtimes])

Running this example produces:

    $ python ./example.py 
    I've run 1 time(s). I like turtles!
    I've been launched at these times:  1370046713.82
    $ python ./example.py 
    I've run 2 time(s). I like turtles!
    I've been launched at these times:  1370046713.82, 1370046716.99
    $ python ./example.py 
    I've run 3 time(s). I like the Rabbit of Caerbannog!
    I've been launched at these times:  1370046713.82, 1370046716.99, 1370046719.49
    $ 

## License

This module is licensed under a BSD-style licence. See LICENSE.txt for details.

## Notes

- Uses the [appdirs][] module from pypi. 
- Created after asking this [question on stack overflow](http://stackoverflow.com/questions/16275031/portable-settings-and-app-data-storage-in-python)
- usersettings not your cup of tea? Have a look at [configmgr](https://bitbucket.org/grantor61/configmgr), an earlier project which also leverages appdirs (which I helpfully discovered only *after* creating this module)

[ConfigParser]: http://docs.python.org/2/library/configparser.html
[argparse]: http://docs.python.org/2/library/argparse.html
[appdirs]: https://pypi.python.org/pypi/appdirs
