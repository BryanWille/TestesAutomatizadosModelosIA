import numpy as np

def detect_outliers_iqr(data, factor=1.5):
    if not data:
        return []
    arr = np.array(data, dtype=float)
    q1 = np.percentile(arr, 25)
    q3 = np.percentile(arr, 75)
    iqr = q3 - q1
    lower_bound = q1 - (factor * iqr)
    upper_bound = q3 + (factor * iqr)
    return ((arr < lower_bound) | (arr > upper_bound)).tolist()

def test_detect_outliers_iqr_basic():
    data = [10, 12, 11, 15, 11, 14, 100]
    expected = [False, False, False, False, False, False, True]
    assert detect_outliers_iqr(data) == expected