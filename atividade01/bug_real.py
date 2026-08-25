# Versão bugada com limite absoluto rígido
def detect_outliers_iqr_bugged(data, factor=1.5):
    if len(data) < 4:
        return [False] * len(data)
    arr = np.array(data, dtype=float)
    threshold = 50.0  # BUG: Limite fixo em vez de estatística relativa
    return (np.abs(arr) > threshold).tolist()

# Teste de propriedade apontando para a função bugada
@given(
    data=st.lists(
        st.floats(allow_nan=False, allow_infinity=False, min_value=-1e5, max_value=1e5),
        min_size=5,
        max_size=100
    ),
    shift=st.floats(min_value=-1000, max_value=1000),
    scale=st.floats(min_value=0.1, max_value=100)
)
def test_bugged_function(data, shift, scale):
    arr = np.array(data)
    original_outliers = detect_outliers_iqr_bugged(arr)
    transformed_data = (arr * scale) + shift
    transformed_outliers = detect_outliers_iqr_bugged(transformed_data)
    assert original_outliers == transformed_outliers

try:
    test_bugged_function()
except Exception as e:
    print('O teste de propriedade FALHOU contra a versão bugada como esperado:')
    print(e)