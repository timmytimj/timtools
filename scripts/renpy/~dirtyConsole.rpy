init +999 python:
    config.console = True

init +999 python in _console:

    def AONquickOverview( l ):
        return str( sorted( renpy.python.store_dicts["store"].ever_been_changed ) )

    config.console_commands["vv"] = AONquickOverview
    config.console_commands["vv"].help = "vv: will return the list of all the variables which have been their value changed at least once since the start of the game."



init +999 python in _console:
    
    def reload_game_content():
        renpy.reload_script()
        renpy.restart_interaction()

    config.console_commands["reload"] = reload_game_content
    config.console_commands["reload"].help = "reload: Reload game content and restart the current interaction."

init +999 python in _console:

    def execute_code(code):
        try:
            exec(code)
        except Exception as e:
            return str(e)
        return "Code executed successfully."

    config.console_commands["exec"] = execute_code
    config.console_commands["exec"].help = "exec <code>: Execute arbitrary Python code."


init +999 python in _console:

    def get_current_scene_name():
        return str(renpy.get_scene_list()[-1])

    config.console_commands["scene"] = get_current_scene_name
    config.console_commands["scene"].help = "scene: Get the name of the current scene."
    
    
init +999 python in _console:

    def list_active_variables():
        variables = sorted(renpy.game.variables.keys())
        return str(variables)

    config.console_commands["variables"] = list_active_variables
    config.console_commands["variables"].help = "variables: List all active variables in the game."
    

init +999 python in _console:

    def grep_list(input_list, search_term):
        filtered_list = [item for item in input_list if search_term.lower() in str(item).lower()]
        return str(filtered_list)

    config.console_commands["grep"] = grep_list
    config.console_commands["grep"].help = "grep <search_term>: Filter and print a list based on the search term."

init +999 python in _console:

    def grep_dir(search_term):
        variables = dir()
        filtered_list = [var for var in variables if search_term.lower() in var.lower()]
        return str(filtered_list)

    config.console_commands["grepdir"] = grep_dir
    config.console_commands["grepdir"].help = "grepdir <search_term>: Filter and print the output of dir() based on the search term."

init +999 python in _console:

    import os

    def list_screenshots():
        screenshot_dir = os.path.join(renpy.config.screenshot_directory, "")
        screenshots = os.listdir(screenshot_dir)
        return str(screenshots)

    config.console_commands["screenshots"] = list_screenshots
    config.console_commands["screenshots"].help = "screenshots: List all screenshots in the default directory."

init +999 python in _console:

    def change_screenshot_location(new_directory):
        renpy.config.screenshot_directory = new_directory

    config.console_commands["set_screenshot_dir"] = change_screenshot_location
    config.console_commands["set_screenshot_dir"].help = "set_screenshot_dir <directory>: Change the default screenshot directory to the specified directory."

init +999 python in _console:

    import os

    def watch_and_log(output_dir, filename, expr, watchlog_func):
        log_filepath = os.path.join(output_dir, filename)

        try:
            with open(log_filepath, "a") as log_file:
                log_file.write(watchlog_func(expr) + "\n")
        except Exception as e:
            return str(e)

        return f"Results logged to '{log_filepath}'."

    config.console_commands["watchlog"] = watch_and_log
    config.console_commands["watchlog"].help = "watchlog <output_dir> <filename> <expr> <function_to_watchlog>: Watch an expression and log the results to a file."


init +999 python in _console:

    import sys

    def dump_console_output(output_dir, filename):
        try:
            log_filepath = os.path.join(output_dir, filename)
            sys.stdout = open(log_filepath, "a")
        except Exception as e:
            return str(e)

        return f"Console output is being dumped to '{log_filepath}'."

    config.console_commands["dumpoutput"] = dump_console_output
    config.console_commands["dumpoutput"].help = "dumpoutput <output_dir> <filename>: Dump the console output to a file."


