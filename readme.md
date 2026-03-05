**list_fasta_names**

A command-line utility to extract sequence names from a FASTA file. Names can be written to a plain text file (one per line), printed to stdout as a quoted space-separated string, or both at once.

------------------------------------------------------------------------

## **Requirements**

-   Python 3.10+

-   No third-party dependencies

------------------------------------------------------------------------

## **Usage**

```bash
`python list_fasta_names.py -i <input.fasta> [-o <output.txt>] [-s]`
```

## **Arguments**

| **Argument** | **Short** | **Required** | **Description** |
|:---|:---|:---|:---|
| `--input` | `-i` | Yes | Input FASTA file |
| `--output` | `-o` | No | Output `.txt` file to write sequence names to (one per line) |
| `--string` | `-s` | No | Print sequence names to stdout as a quoted space-separated string |

At least one of `--output` or `--string` should be provided.

------------------------------------------------------------------------

## **Output Formats**

## **File output (`-o`)**

Writes each sequence name on its own line:

```text
`sequence_1
sequence_2
sequence_3`
```

## **String output (`-s`)**

Prints all sequence names to stdout as double-quoted, space-separated tokens:

```text
`"sequence_1" "sequence_2" "sequence_3"`
```

This format is useful for embedding directly into shell commands or pipelines.

------------------------------------------------------------------------

## **Examples**

**Write names to a text file:**

```bash
`python list_fasta_names.py -i sequences.fasta -o names.txt`
```

**Print names as a quoted string:**

```         
bash
```

`python list_fasta_names.py -i sequences.fasta -s`

**Both at once:**

```bash
`python list_fasta_names.py -i sequences.fasta -o names.txt -s`
```

**Use string output directly in a pipeline:**

```bash
`seqkit grep -n sequences.fasta -p $(python list_fasta_names.py -i sequences.fasta -s)`
```