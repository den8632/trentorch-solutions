def first_and_last(s: str) -> str:
    """
    Return a new string made of the first character of `s`
    followed by the last character of `s`.
    """
    if not s:
        return ""

    return s[0] + s[-1]


def reverse_string(s: str) -> str:
    """
    Return a new string containing the characters of `s` in
    reverse order. Use a slice with a negative step.
    """
    return s[::-1]


def every_kth_from(s: str, start: int, k: int) -> str:
    """
    Return the characters of `s` at positions start, start + k,
    start + 2k, ... continuing to the end of the string.
    `start` may be negative (counted from the end). `k` is
    always >= 1. If `start` is out of range, return "".

    Example: every_kth_from("abcdefgh", 1, 3) -> "beh"
    """
    if not (-len(s) <= start < len(s)):
        return ""

    return s[start::k]
