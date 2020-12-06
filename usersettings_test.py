#!/usr/bin/python
""" pytest test for usersettings.py """
import time
import usersettings


def test_store_load_int():
    """ tests storing an integer settings and loading back that same value """
    testvalue = int(time.time())
    app_id = "com.example.apps.UserSettingsExample"
    # save a value
    pre = usersettings.Settings(app_id)
    pre.add_setting("testint", int, default=0)
    pre.load_settings()
    pre.testint = testvalue
    pre.save_settings()
    # load it again
    post = usersettings.Settings(app_id)
    post.add_setting("testint", int, default=0)
    post.load_settings()
    # compare
    assert pre.testint == post.testint
