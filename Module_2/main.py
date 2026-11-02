
import sys #use for sys.argv command line argument
import argparse #parase commandline options
import json #data store in json formated
import logging #Recorde error  in log file 

from pathlib import Path

from datakit import (
    read_rows,
    clean_rows,
    summary,
    InvalidFileError,
    EmptyDatasetError
)


logging.basicConfig(
    filename="datakit.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def positive_int(value):
    number = int(value)
    if number <= 0:
        raise argparse.ArgumentTypeError(
            "N must be a positive integer"
        )
    return number


def main():
    parser = argparse.ArgumentParser(
        description="Analyze a CSV dataset"
    )

    parser.add_argument(
        "file",
        nargs="?",
        default="sample.csv",
        help="CSV file path (default: sample.csv)"
    )

    parser.add_argument(
        "--top",
        type=positive_int,
        default=None,
        help="Show top N rows by first numeric column"
    )

    args = parser.parse_args()

    try:
        path = Path(args.file)

        if path.suffix.lower() != ".csv":
            raise InvalidFileError(
                "Please provide a CSV file"
            )

        if not path.is_file():
            raise FileNotFoundError(
                f"File not found: {path}"
            )

        # Read and clean
        rows = list(read_rows(path))
        cleaned = clean_rows(rows)

        if not cleaned:
            raise EmptyDatasetError(
                "No valid rows remain after cleaning"
            )

        # Analyze cleaned dataset
        result = summary(cleaned)

        # Save JSON
        with open(
            "summary.json", "w", encoding="utf-8"
        ) as file:
            json.dump(result, file, indent=4)

        # Save TXT
        with open(
            "summary.txt", "w", encoding="utf-8"
        ) as file:
            file.write("DATAKIT - DATA SUMMARY\n")
            file.write("=" * 35 + "\n")
            file.write(f"File: {path}\n")
            file.write(f"Rows analyzed: {result['row_count']}\n")
            file.write(f"Columns: {', '.join(result['columns'])}\n")
            file.write("\nNUMERIC COLUMN STATISTICS\n")
            file.write("-" * 35 + "\n")

            for col, stats in result["numeric_summary"].items():
                file.write(f"\n{col}\n")
                file.write(f"  Minimum : {stats['min']}\n")
                file.write(f"  Maximum : {stats['max']}\n")
                file.write(f"  Mean    : {stats['mean']:.2f}\n")

        print("Analysis completed successfully!")
        print(f"Original rows: {len(rows)}")
        print(f"Cleaned rows: {len(cleaned)}")
        print(f"Removed rows: {len(rows) - len(cleaned)}")
        print("\nSummary:")
        print(json.dumps(result, indent=4))

        # Bonus: top N rows
        if args.top is not None:
            numeric_cols = list(
                result["numeric_summary"].keys()
            )

            if not numeric_cols:
                print("\nNo numeric column available for --top")
            else:
                col = numeric_cols[0]

                top_rows = sorted(
                    cleaned,
                    key=lambda row: row[col],
                    reverse=True
                )[:args.top]

                print(f"\nTop {args.top} rows by {col}:")
                for row in top_rows:
                    print(row)

    except FileNotFoundError as exc:
        logging.exception("File not found")
        print(f"Error: {exc}")

    except (InvalidFileError, EmptyDatasetError) as exc:
        logging.exception("DataKit processing failed")
        print(f"Error: {exc}")

    except OSError as exc:
        logging.exception("File operation failed")
        print(f"File error: {exc}")

    except Exception:
        logging.exception("Unexpected application error")
        print("Unexpected error. Check datakit.log")

    else:
        print("\nReports saved: summary.json and summary.txt")

    finally:
        print("\nDataKit execution finished.")


if __name__ == "__main__":
    main()
