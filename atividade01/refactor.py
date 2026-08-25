import numpy as np

def detect_outliers_iqr(data, factor=1.5):
    if len(data) == 0:
        return []

    arr = np.array(data, dtype=float)

    # Identifica valores não numéricos e infinitos
    invalid_mask = np.isnan(arr) | np.isinf(arr)
    valid_data = arr[~invalid_mask]

    # Valida tamanho mínimo para cálculo de quartis
    if len(valid_data) < 4:
        return invalid_mask.tolist()

    q1, q3 = np.percentile(valid_data, [25, 75])
    iqr = q3 - q1

    lower_bound = q1 - (factor * iqr)
    upper_bound = q3 + (factor * iqr)

    outliers = (arr < lower_bound) | (arr > upper_bound) | invalid_mask
    return outliers.tolist()