
# This is the configuration file for your powerline-shell prompt
# Every time you make a change to this file, run install.py to apply changes
#
# For instructions on how to use the powerline-shell.py script, see the README

# Add, remove or rearrange these segments to customize what you see on the shell
# prompt. Any segment you add must be present in the segments/ directory

SEGMENTS = [
  # Set the terminal window title to user@host:dir
  'set_term_title',

  # Show the last command's exit code if it was non-zero
  'exit_code',

  # Show a padlock when ssh-ing from another machine
  'ssh',

  # Show the current directory. If the path is too long, the middle part is
  # replaced with ellipsis ('...')
  'cwd',

  # Show the current git branch and status
  'git',

  # Show a padlock if the current user has no write access to the current
  # directory
  'read_only',

  # Show number of running jobs
  'jobs',

  # Shows a '#' if the current user is root, '$' otherwise
  # Also, changes color if the last command exited with a non-zero error code
  'root',
  'ruby_version',
]

# Change the colors used to draw individual segments in your prompt
THEME = 'default'