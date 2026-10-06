def append_all(lst: list, items: list) -> None:
    """
    Add every element of `items` to the end of `lst`, in place,
    so that each element becomes its own new element of `lst`.
    Use extend(). Return nothing.
    """
    lst.extend(items)


def insert_sorted(lst: list, value) -> None:
    """
    `lst` is sorted in ascending order. Insert `value` in place
    so that the list stays sorted, placing it AFTER any existing
    elements equal to `value`. Use a loop to find the position
    and insert() to add it. Return nothing.
    """
    pos = 0

    while pos < len(lst) and lst[pos] <= value:
        pos += 1

    lst.insert(pos, value)


def flatten_one_level(list_of_lists: list) -> list:
    """
    Return a NEW list made of the elements of each inner list,
    in order. Do not change `list_of_lists` or its inner lists.
    Use extend() on a fresh list.
    """
    result = []

    for inner_list in list_of_lists:
        result.extend(inner_list)

    return result


def concat_identity_report(lst: list, extra: list) -> list:
    """
    Using the list `lst` given by the caller:
      1. Record id(lst). Perform `lst += extra`. Record whether
         id(lst) is unchanged (call this same_after_iadd).
      2. Record id(lst) again. Perform `lst = lst + extra`.
         Record whether id(lst) is unchanged (same_after_plus).
    Return a list [same_after_iadd, same_after_plus].
    (The caller's original list is changed by step 1 only.)
    """
    original_id = id(lst)

    lst += extra
    same_after_iadd = id(lst) == original_id

    before_plus_id = id(lst)

    lst = lst + extra
    same_after_plus = id(lst) == before_plus_id

    return [same_after_iadd, same_after_plus]


def remove_all(lst: list, value) -> None:
    """
    Remove EVERY element equal to `value` from `lst`, in place
    (the caller's list object must keep its id()). Consecutive
    duplicates must all be removed. Return nothing.
    """
    lst[:] = [item for item in lst if item != value]
         


def pop_last_n(lst: list, n: int) -> list:
    """
    Remove the last `n` elements of `lst` in place and return
    them in their ORIGINAL order as a new list. If n <= 0,
    remove nothing and return []. If n >= len(lst), remove
    everything.

    Example: lst = [1, 2, 3, 4]; pop_last_n(lst, 2) -> [3, 4]
             and lst is now [1, 2]
    """

    if n <= 0:
        return []

    removed = lst[-n:]
    del lst[-n:]
    return removed


def delete_every_other(lst: list) -> None:
    """
    Remove the elements at positions 0, 2, 4, ... from `lst`,
    in place, using del with an extended slice. Return nothing.
    """
    del lst[::2]


def remove_first_or_report(lst: list, value) -> bool:
    """
    If `value` is in `lst`, remove its first occurrence in place
    and return True. If it is not present, leave `lst` unchanged
    and return False. Check with `in` before removing; do not
    let remove() fail.
    """

    if value in lst:
        lst.remove(value)
        return True

    return False
