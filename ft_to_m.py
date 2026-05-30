#!/usr/bin/env python3

import argparse


def ft_to_m(feet: float) -> float:
    return feet * 0.3048


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert feet to meters.")
    parser.add_argument("feet", type=float, help="Value in feet")
    args = parser.parse_args()

    meters = ft_to_m(args.feet)
    print(f"{args.feet} ft = {meters:.4f} m")


if __name__ == "__main__":
    main()
