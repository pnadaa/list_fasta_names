import argparse
from pathlib import Path
from typing import Iterator, Sequence


def parse_args(argv=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="list_fasta_names",
        description=(
            "Extract the list of sequence names from a multifasta and store into a txt file"
        ),
    )
    parser.add_argument(
        "-i", "--input",
        required=True,
        type=Path,
        help="Input FASTA file, or a directory containing FASTA files",
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default=None,
        help="Output location of the fasta names list",
    )
    parser.add_argument(
        "-s", "--string",
        action="store_true",
        default=False,
        help=(
            'Print sequence names to stdout as a quoted space-separated string, \n'
            'e.g. "seq1" "seq2" "seq3". Can be combined with -o.'
        ),
    )
    return parser.parse_args(argv)


def iterate_fasta_records(path: Path) -> Iterator[str]:
    """
    Stream the list of sequence names from a fasta file.
    """
    with path.open("r", encoding="utf-8") as handle:
        for raw_line in handle:
            line = raw_line.strip()
            if not line:
                continue
            if line.startswith(">"):
                yield line[1:].strip()


def writefile(input_file: Path, output_file: Path) -> None:
    headers = iterate_fasta_records(input_file)
    with output_file.open("w", encoding="utf-8") as out:
        for header in headers:
            out.write(f"{header}\n")


def print_string_format(input_file: Path) -> None:
    """
    Print sequence names to stdout as a quoted space-separated string.
    Example output:  "seq1" "seq2" "seq3"
    """
    quoted = [f'"{name}"' for name in iterate_fasta_records(input_file)]
    print(" ".join(quoted))


def main(argv: Sequence[str] | None = None) -> None:
    args = parse_args(argv)

    if args.output is not None:
        writefile(args.input, args.output)

    if args.string:
        print_string_format(args.input)

    if args.output is None and not args.string:
        print("Warning: no output action specified. Use -o to write a file or -s for string output.")


if __name__ == "__main__":
    main()
