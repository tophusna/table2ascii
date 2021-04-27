from table2ascii import table2ascii as t2a


def test_normal():
    text = t2a(
        header_row=["#", "G", "H", "R", "S"],
        body=[["1", "30", "40", "35", "30"], ["2", "30", "40", "35", "30"]],
        footer_row=["SUM", "130", "140", "135", "130"],
    )
    expected = (
        "╔═════╦═══════════════════════╗\n"
        "║  #  ║  G     H     R     S  ║\n"
        "╟─────╫───────────────────────╢\n"
        "║  1  ║  30    40    35    30 ║\n"
        "║  2  ║  30    40    35    30 ║\n"
        "╟─────╫───────────────────────╢\n"
        "║ SUM ║ 130   140   135   130 ║\n"
        "╚═════╩═══════════════════════╝\n"
    )
    assert text == expected
