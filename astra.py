# astra.py
# Astra: Custom Wordlist Generator for Cybersecurity Tools

import argparse
import itertools
import os


def combine_elements(base_words, symbols, years, custom_words):
    combinations = set()
    for word in base_words:
        for s in symbols:
            for y in years:
                combinations.add(f"{word}{s}{y}")
                combinations.add(f"{y}{s}{word}")
                combinations.add(f"{word}{y}{s}")
        for cw in custom_words:
            combinations.add(f"{word}{cw}")
            combinations.add(f"{cw}{word}")
    return combinations


def filter_by_length(wordlist, min_len, max_len):
    return [word for word in wordlist if min_len <= len(word) <= max_len]


def generate_wordlist(args):
    base_words = []
    if args.name:
        base_words.append(args.name)
    if args.dob:
        base_words.append(args.dob)
    if args.city:
        base_words.append(args.city)

    symbols = args.symbols if args.symbols else ["@", "#", "_"]
    years = args.years if args.years else ["2020", "2021", "2022", "2023", "2024", "2025"]
    custom_words = args.custom if args.custom else []

    raw_words = combine_elements(base_words, symbols, years, custom_words)
    raw_words.update(base_words)
    raw_words.update(custom_words)

    final_words = filter_by_length(raw_words, args.min_length, args.max_length)

    if args.verbose:
        for word in final_words:
            print(word)

    with open(args.output, "w") as f:
        for word in final_words:
            f.write(word + "\n")

    print(f"\n[+] Wordlist saved to: {args.output} ({len(final_words)} entries)")


def main():
    parser = argparse.ArgumentParser(description="Astra - Smart Wordlist Generator for Ethical Hacking")
    parser.add_argument("--name", type=str, help="Target's name")
    parser.add_argument("--dob", type=str, help="Date of birth or year")
    parser.add_argument("--city", type=str, help="City or hometown")
    parser.add_argument("--symbols", nargs="*", help="Symbols to include (e.g. @ # _)")
    parser.add_argument("--years", nargs="*", help="Years to include (e.g. 2024 2025)")
    parser.add_argument("--custom", nargs="*", help="Custom keywords to use")
    parser.add_argument("--min-length", type=int, default=6, help="Minimum password length")
    parser.add_argument("--max-length", type=int, default=16, help="Maximum password length")
    parser.add_argument("--output", type=str, default="astra_wordlist.txt", help="Output filename")
    parser.add_argument("--verbose", action="store_true", help="Print passwords while generating")

    args = parser.parse_args()
    generate_wordlist(args)


if __name__ == "__main__":
    main()
