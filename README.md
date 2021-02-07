# `eet`

    Usage: eet [OPTIONS] [SOURCE]...

      Accept input either from `stdin` or SOURCE(s).

      Reverses `tee`.

      Intended as a convenience in pipe shell scripts, to be used as in the
      example:

          tee $@ | [COMMAND]...

      Input from `stdin` and argument filenames cannot both be accepted at the
      same time; argument filenames will be given priority in such cases, and
      input from `stdin` will be ignored. In circumstances where both are
      required, mixing together the input would better be accomplished with:

          cat - $@ | [COMMAND]...

    Options:
      --help  Show this message and exit.
