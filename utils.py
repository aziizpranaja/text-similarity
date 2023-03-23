def check_score(probability: float):
    return_value = {
        "probability": probability,
        "score": 0,
    }
    if 0.99 <= probability <= 1:
        return_value["score"] = 4
        return return_value
    elif 0.98 <= probability <= 0.99:
        return_value["score"] = 3
        return return_value
    elif 0.97 <= probability <= 0.98:
        return_value["score"] = 2
        return return_value
    elif 0.96 <= probability <= 0.97:
        return_value["score"] = 1
        return return_value
    elif probability <= 0.96:
        return return_value