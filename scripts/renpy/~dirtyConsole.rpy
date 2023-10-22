init +999 python:
    config.console = True

init +999 python in _console:

    def AONquickOverview( l ):
        return str( sorted( renpy.python.store_dicts["store"].ever_been_changed ) )

    config.console_commands["vv"] = AONquickOverview
    config.console_commands["vv"].help = "vv: will return the list of all the variables which have been their value changed at least once since the start of the game."
