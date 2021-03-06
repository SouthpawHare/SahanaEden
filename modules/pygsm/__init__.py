#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4i encoding=utf-8


from gsmmodem import GsmModem
from autogsmmodem import AutoGsmModem
__doc__ = GsmModem.__doc__

def get_version():
    try:
        # do we have a static version set from an install?
        from __version__ import VERSION as version
    except ImportError:
        # if not, can we figure it out from the git tag?
        import commands
        try:
            # see http://stackoverflow.com/questions/62264/#72874
            version = commands.getoutput("git describe --tags --always")
        except:
            # otherwise, give up!
            version = "unknown"
    return version
