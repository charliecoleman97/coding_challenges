"""
Script to test the count_three() function
"""

from count_freq_substring import count_three

def test_full_substring() -> dict:
    """Test a full substring """
    freq_string = 'ACATCACA'
    test_output_dict = {
            'ACA': 2,
            'CAT': 1,
            'ATC': 1,
            'CAC': 1
            }
    assert count_three(freq_string) == test_output_dict


def test_string_under_3() -> dict:
    """Should return an empty dict"""
    freq_string = 'AC'
    test_output_dict = {}
    assert count_three(freq_string) == test_output_dict

