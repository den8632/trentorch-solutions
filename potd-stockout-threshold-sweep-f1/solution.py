def best_f1_threshold(scores: list[float], y: list[int]) -> tuple[float, float]:
    """
    The score threshold that maximizes F1 (predict positive if score >= t).

    scores: n predicted scores. y: n true labels, each 0 or 1.

    For each distinct value in scores, using it as threshold t, compute
    F1(t) over the whole dataset. Return (best_threshold, best_f1).

    Ties for the best F1 are broken by the LARGER threshold. A threshold
    where precision or recall is undefined (a zero denominator) can never
    win. Sort once and sweep with running TP/FP counts, O(n log n), not
    a from-scratch recompute per threshold.
    """
    if len(scores) != len(y):
        raise ValueError("scores and y must have the same length")
    if not scores:
        raise ValueError("scores must not be empty")

    total_positives = sum(y)
    pairs = sorted(zip(scores, y), key=lambda pair: pair[0], reverse=True)

    tp = fp = 0
    best_threshold = None
    best_f1 = -1.0
    i = 0

    while i < len(pairs):
        threshold = pairs[i][0]
        while i < len(pairs) and pairs[i][0] == threshold:
            if pairs[i][1] == 1:
                tp += 1
            else:
                fp += 1
            i += 1

        fn = total_positives - tp
        if tp + fp > 0 and tp + fn > 0:
            f1 = 2 * tp / (2 * tp + fp + fn)
            
            if f1 > best_f1:
                best_threshold = threshold
                best_f1 = f1

    if best_threshold is None:
        raise ValueError("no threshold has defined precision and recall")

    return best_threshold, best_f1
