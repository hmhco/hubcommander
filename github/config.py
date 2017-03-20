from hubcommander.auth_plugins.enabled_plugins import AUTH_PLUGINS

# Define the organizations that this Bot will examine.
ORGS = {
    "hmhco": {
        "aliases": [
        ]
    }
}

# github API Version
GITHUB_VERSION = "application/vnd.github.v3+json"   # Is this still needed?

# GITHUB API PATH:
GITHUB_URL = "https://api.github.com/"

# You can use this to add/replace fields from the command_plugins dictionary:
USER_COMMAND_DICT = {
    # This is an example for enabling Duo 2FA support for the "!SetDefaultBranch" command:
    # "!SetDefaultBranch": {
        # "auth": {
        #    "plugin": AUTH_PLUGINS["duo"],
        #    "kwargs": {}
        # }
    #}
}
