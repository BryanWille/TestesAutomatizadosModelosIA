from hypothesis import given, strategies as st
import numpy as np

@given(
    data=st.lists(
        st.floats(allow_nan=False, allow_infinity=False, min_value=-1e5, max_value=1e5),
        min_size=5,
        max_size=100
    ),
    shift=st.floats(min_value=-1000, max_value=1000),
    scale=st.floats(min_value=0.1, max_value=100)
)
def test_outlier_translation_and_scale_invariance(data, shift, scale):
    arr = np.array(data)

    # Detecção na série original
    original_outliers = detect_outliers_iqr(arr)

    # Detecção na série transformada
    transformed_data = (arr * scale) + shift
    transformed_outliers = detect_outliers_iqr(transformed_data)

    assert original_outliers == transformed_outliers

# Executando o teste de propriedade diretamente
test_outlier_translation_and_scale_invariance()
print('Teste de propriedade passou com sucesso!')