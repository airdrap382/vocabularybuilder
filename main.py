#!/usr/bin/env python3
"""Entry point for the vocabularybuilder data pipeline."""

import argparse
import sys

from vocabularybuilder.pipeline import run_pipeline
from vocabularybuilder import __version__


def main(argv=None):
 parser = argparse.ArgumentParser(description="VocabularyBuilder")
 parser.add_argument("source", help="input file (json, csv or txt)")
 parser.add_argument("target", help="output file")
 parser.add_argument("--version", action="version", version=__version__)
 args = parser.parse_args(argv)

 count = run_pipeline(args.source, args.target)
 print(f"processed {count} records")
 return 0


if __name__ == "__main__":
 sys.exit(main())