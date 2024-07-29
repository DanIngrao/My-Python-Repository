def Sumar(número1, número2):
    return número1+número2

suma = Sumar(5,7)
print(suma)

# ************* Module practica_pylint
# practica_pylint.py:5:0: C0304: Final newline missing (missing-final-newline)
# practica_pylint.py:1:0: C0114: Missing module docstring (missing-module-docstring)
# practica_pylint.py:1:0: C0116: Missing function or method docstring (missing-function-docstring)
# practica_pylint.py:1:0: C0103: Function name "Sumar" doesn't conform to snake_case naming style (invalid-name)
# practica_pylint.py:1:10: C2401: Argument name "número1" contains a non-ASCII character, consider renaming it. (non-ascii-name)
# practica_pylint.py:1:20: C2401: Argument name "número2" contains a non-ASCII character, consider renaming it. (non-ascii-name)
# practica_pylint.py:4:0: C0103: Constant name "suma" doesn't conform to UPPER_CASE naming style (invalid-name)
# 
# 
# Report
# ======
# 4 statements analysed.
# 
# Statistics by type
# ------------------
# 
# +---------+-------+-----------+-----------+------------+---------+
# |type     |number |old number |difference |%documented |%badname |
# +=========+=======+===========+===========+============+=========+
# |module   |1      |NC         |NC         |0.00        |0.00     |
# +---------+-------+-----------+-----------+------------+---------+
# |class    |0      |NC         |NC         |0           |0        |
# +---------+-------+-----------+-----------+------------+---------+
# |method   |0      |NC         |NC         |0           |0        |
# +---------+-------+-----------+-----------+------------+---------+
# |function |1      |NC         |NC         |0.00        |100.00   |
# +---------+-------+-----------+-----------+------------+---------+
# 
# 
# 
# 7 lines have been analyzed
# 
# Raw metrics
# -----------
# 
# +----------+-------+------+---------+-----------+
# |type      |number |%     |previous |difference |
# +==========+=======+======+=========+===========+
# |code      |5      |71.43 |NC       |NC         |
# +----------+-------+------+---------+-----------+
# |docstring |0      |0.00  |NC       |NC         |
# +----------+-------+------+---------+-----------+
# |comment   |0      |0.00  |NC       |NC         |
# +----------+-------+------+---------+-----------+
# |empty     |2      |28.57 |NC       |NC         |
# +----------+-------+------+---------+-----------+
# 
# 
# 
# Duplication
# -----------
# 
# +-------------------------+------+---------+-----------+
# |                         |now   |previous |difference |
# +=========================+======+=========+===========+
# |nb duplicated lines      |0     |NC       |NC         |
# +-------------------------+------+---------+-----------+
# |percent duplicated lines |0.000 |NC       |NC         |
# +-------------------------+------+---------+-----------+
# 
# 
# 
# Messages by category
# --------------------
# 
# +-----------+-------+---------+-----------+
# |type       |number |previous |difference |
# +===========+=======+=========+===========+
# |convention |7      |NC       |NC         |
# +-----------+-------+---------+-----------+
# |refactor   |0      |NC       |NC         |
# +-----------+-------+---------+-----------+
# |warning    |0      |NC       |NC         |
# +-----------+-------+---------+-----------+
# |error      |0      |NC       |NC         |
# +-----------+-------+---------+-----------+
# 
# 
# 
# % errors / warnings by module
# -----------------------------
# 
# +----------------+------+--------+---------+-----------+
# |module          |error |warning |refactor |convention |
# +================+======+========+=========+===========+
# |practica_pylint |0.00  |0.00    |0.00     |100.00     |
# +----------------+------+--------+---------+-----------+
# 
# 
# 
# Messages
# --------
# 
# +---------------------------+------------+
# |message id                 |occurrences |
# +===========================+============+
# |non-ascii-name             |2           |
# +---------------------------+------------+
# |invalid-name               |2           |
# +---------------------------+------------+
# |missing-module-docstring   |1           |
# +---------------------------+------------+
# |missing-function-docstring |1           |
# +---------------------------+------------+
# |missing-final-newline      |1           |
# +---------------------------+------------+
# 
# 
# 
# 
# -----------------------------------
# Your code has been rated at 0.00/10