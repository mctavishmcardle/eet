import io
import typing

import click


@click.command(
    help="""
    Accept input either from `stdin` or SOURCE(s).

    Reverses `tee`.

    Intended as a convenience in pipe shell scripts, to be used as in the example:

        tee $@ | [COMMAND]...

    Input from `stdin` and argument filenames cannot both be accepted at the
    same time; argument filenames will be given priority in such cases, and
    input from `stdin` will be ignored. In circumstances where both are required,
    mixing together the input would better be accomplished with:

        cat - $@ | [COMMAND]...
    """
)
# pseudo-option to provide access to stdin
@click.option("--stdin", type=click.File(), default="-", hidden=True)
@click.argument(
    "source",
    type=click.File(),
    nargs=-1,
)
def eet(stdin: io.TextIOBase, source: typing.Tuple[io.TextIOBase]) -> None:
    if source:
        for individual_source in source:
            click.echo(individual_source.read(), nl=False)
    else:
        click.echo(stdin.read(), nl=False)
