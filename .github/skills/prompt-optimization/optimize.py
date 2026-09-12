#!/usr/bin/env python3

import math
import re
import sys


FILLER_PATTERNS = [
    r"\bplease\b",
    r"\bkindly\b",
    r"\bi would like you to\b",
    r"\bcould you\b",
    r"\bcan you please\b",
    r"\bif possible\b",
    r"\bmake sure that\b",
    r"\bI want you to\b",
    r"\bI need you to\b",
]


def estimate_tokens(text: str) -> int:
    """
    Rough token estimate.

    This is NOT the exact tokenizer used by GitHub Copilot.
    Approximation: ~4 characters per token.
    """
    return math.ceil(len(text) / 4)


def normalize_whitespace(text: str) -> str:
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def remove_filler(text: str) -> str:
    result = text

    for pattern in FILLER_PATTERNS:
        result = re.sub(
            pattern,
            "",
            result,
            flags=re.IGNORECASE,
        )

    return result


def optimize(text: str) -> str:
    result = normalize_whitespace(text)

    result = remove_filler(result)

    result = normalize_whitespace(result)

    return result


def calculate(original: str, optimized: str):
    original_tokens = estimate_tokens(original)
    optimized_tokens = estimate_tokens(optimized)

    saved = max(0, original_tokens - optimized_tokens)

    if original_tokens:
        reduction = (saved / original_tokens) * 100
    else:
        reduction = 0

    return {
        "original_chars": len(original),
        "optimized_chars": len(optimized),
        "original_tokens": original_tokens,
        "optimized_tokens": optimized_tokens,
        "tokens_saved": saved,
        "reduction": reduction,
    }


def main():
    if len(sys.argv) > 1:
        original = " ".join(sys.argv[1:])
    else:
        original = sys.stdin.read()

    optimized = optimize(original)

    stats = calculate(original, optimized)

    print("\nOriginal:")
    print(original)

    print("\nOptimized:")
    print(optimized)

    print("\nToken Estimate:")
    print(f"Original characters : {stats['original_chars']}")
    print(f"Optimized characters: {stats['optimized_chars']}")
    print(f"Original tokens     : {stats['original_tokens']}")
    print(f"Optimized tokens    : {stats['optimized_tokens']}")
    print(f"Tokens saved        : {stats['tokens_saved']}")
    print(f"Reduction           : {stats['reduction']:.2f}%")

    print("\nNOTE:")
    print("Token counts are estimates, not actual GitHub Copilot usage.")


if __name__ == "__main__":
    main()