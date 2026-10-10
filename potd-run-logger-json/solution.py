def build_run_record(
    run_id: str, hyperparameters: list[tuple[str, str]], metrics: list[tuple[str, str]]
) -> dict:
    """
    Build a canonical training-run record.

    run_id: the run's id.
    hyperparameters: (key, value) pairs, in input order, keys may repeat.
    metrics: (key, value) pairs, same shape.

    Return {"run_id": run_id, "hyperparameters": {...}, "metrics": {...}}.
    Within each inner dict, keys are sorted alphabetically. A repeated key
    keeps its LAST value (later pairs overwrite earlier ones). An empty
    list of pairs gives an empty {} for that field, not an omitted key.
    """
    hyperparameter_dict = {}
    for key, value in hyperparameters:
        hyperparameter_dict[key] = value

    metric_dict = {}
    for key, value in metrics:
        metric_dict[key] = value

    return {
        "run_id": run_id,
        "hyperparameters": dict(sorted(hyperparameter_dict.items())),
        "metrics": dict(sorted(metric_dict.items())),
    }
