# Escrevendo o arquivo de teste para a fase RED, função não encontrada
%%writefile test_outliers_red.py
def test_detect_outliers_iqr_basic():
    data = [10, 12, 11, 15, 11, 14, 100]  # 100 é um outlier evidente
    expected = [False, False, False, False, False, False, True]
    assert detect_outliers_iqr(data) == expected

# comando !pytest test_outliers_red.py