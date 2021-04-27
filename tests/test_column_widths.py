from table2ascii import table2ascii as t2a

import pytest


def test_column_widths():
    text = t2a(
        header=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer=["TOTL", "130", "140", "135", "130"],
        first_col_heading=True,
        last_col_heading=True,
        column_widths=[7, 5, 5, 5, 8],
    )
    expected = (
        "╔═══════╦═════════════════╦════════╗\n"
        "║   #   ║  G     H     R  ║   S    ║\n"
        "╟───────╫─────────────────╫────────╢\n"
        "║   1   ║ 30    40    35  ║   30   ║\n"
        "║   2   ║ 30    40    35  ║   30   ║\n"
        "╟───────╫─────────────────╫────────╢\n"
        "║ TOTL  ║ 130   140   135 ║  130   ║\n"
        "╚═══════╩═════════════════╩════════╝\n"
    )
    assert text == expected


def test_wrong_number_column_widths():
    with pytest.raises(ValueError):
        t2a(
            header=["#", "G", "H", "R", "S"],
            body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
            footer=["TOTL", "130", "140", "135", "130"],
            first_col_heading=True,
            last_col_heading=True,
            column_widths=[7, 5, 5, 5],
        )


def test_negative_column_widths():
    with pytest.raises(ValueError):
        t2a(
            header=["#", "G", "H", "R", "S"],
            body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
            footer=["TOTL", "130", "140", "135", "130"],
            first_col_heading=True,
            last_col_heading=True,
            column_widths=[7, 5, 5, 5, -1],
        )
