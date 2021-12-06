"""
Script to test the count_three() function
"""

from count_freq_substring import count_three


def test_full_substring() -> dict:
    """Test a full substring """
    long_string = 'ACATCACA'
    test_output_dict = {
            'ACA': 2,
            'CAT': 1,
            'ATC': 1,
            'TCA': 1,
            'CAC': 1
            }
    assert count_three(long_string) == test_output_dict


def test_string_under_3() -> dict:
    """Should return an empty dict"""
    short_string = 'AC'
    empty_dict = {}
    assert count_three(short_string) == empty_dict

