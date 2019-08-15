# tmux-resurrect-ext

Status line extensions for tmux-resurrect and tmux-continuum

## Features

- `#{resurrect_last}` placeholder for the status line. Displays the
  humanized relative date of the last save (e.g. "18 minutes ago").

## Dependencies

- python3
- [humanize](https://pypi.org/project/humanize/)
- [tmux-resurrect](https://github.com/tmux-plugins/tmux-resurrect)

## Installation

Clone the repo:

    $ git clone https://github.com/fxg42/tmux-resurrect-ext ~/clone/path

Add this line to .tmux.conf:

    run-shell ~/clone/path/resurrect-ext.tmux

## License

[MIT](https://github.com/fxg42/tmux-resurrect-ext/blob/master/LICENSE)
