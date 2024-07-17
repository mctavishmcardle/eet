use clap::Parser;
use patharg::{InputArg, OutputArg};
use std::io;
use std::io::{Write};

/// Write from INPUTS to OUTPUT
#[derive(Parser)]
struct Arguments {
    /// Files (or standard input) to read from
    #[arg(default_values_t = [InputArg::Stdin])]
    inputs: Vec<InputArg>,

    /// File (or standard output) to write to
    #[arg(short = 'o', long, default_value_t)]
    output: OutputArg,
}

fn main() -> io::Result<()> {
    let args = Arguments::parse();

    let mut output = args.output.create()?;

    for input in args.inputs.iter() {
        io::copy(&mut input.open()?, &mut output)?;
    }

    output.flush()?;
    Ok(())
}
