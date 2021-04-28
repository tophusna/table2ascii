from .table_style import TableStyle


a = TableStyle.from_string("┌─┬─┐││     ├─┼─┤└┴─┘")
b = TableStyle.from_string("┌─┬─┐││┝━┿━┥├─┼─┤└┴─┘")
c = TableStyle.from_string("┌─┬─┐││╞═╪═╡├─┼─┤└┴─┘")
d = TableStyle.from_string("╭─┬─╮││     ├─┼─┤╰┴─╯")
e = TableStyle.from_string("╭─┬─╮││┝━┿━┥├─┼─┤╰┴─╯")
f = TableStyle.from_string("╭─┬─╮││╞═╪═╡├─┼─┤╰┴─╯")
g = TableStyle.from_string("┏━┳━┓┃┃     ┣━╋━┫┗┻━┛")
h = TableStyle.from_string("┌─┬─┐││┠─╂─┨├─┼─┤└┴─┘")
i = TableStyle.from_string("╔═╦═╗║║     ╠═╬═╣╚╩═╝")
j = TableStyle.from_string("╔═╦═╗║║╟─╫─╢╠═╬═╣╚╩═╝")
k = TableStyle.from_string(" ───    ━━━  ───  ── ")
l = TableStyle.from_string("+-+-+||     +-+-+++-+")
m = TableStyle.from_string("+-+-+||+=+=++-+-+++-+")
n = TableStyle.from_string("+=+=+HH     +=+=+++=+")
o = TableStyle.from_string("+=+=+HH+-+-++=+=+++=+")
p = TableStyle.from_string(" ---    ===  ---  -- ")
q = TableStyle.from_string("     |||-|-|         ")
