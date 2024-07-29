# Using pylint

'''
This is  a module that executes something
'''

number1 = 500
print(Number1)

#use in terminal in the path of this document: pylint document1.py -r y


#************* Module document1.py
#document1.py:1:0: F0001: No module named document1.py (fatal)
#PS C:\Users\danin\Desktop\Python Repositories\Python Proyects\My-Python-Repository> cd .\Practices\         
#PS C:\Users\danin\Desktop\Python Repositories\Python Proyects\My-Python-Repository\Practices> cd '.\Practice 8\'
#PS C:\Users\danin\Desktop\Python Repositories\Python Proyects\My-Python-Repository\Practices\Practice 8> pylint document1.py -r y
#************* Module document1
#document1.py:2:0: C0304: Final newline missing (missing-final-newline)
#document1.py:1:0: C0114: Missing module docstring (missing-module-docstring)
#document1.py:1:0: C0103: Constant name "number1" doesn't conform to UPPER_CASE naming style (invalid-name)
#document1.py:2:6: E0602: Undefined variable 'Number1' (undefined-variable)
#
#
#Report
#======
#2 statements analysed.
#
#Statistics by type
#------------------
#
#+---------+-------+-----------+-----------+------------+---------+
#|type     |number |old number |difference |%documented |%badname |
#+=========+=======+===========+===========+============+=========+
#|module   |1      |NC         |NC         |0.00        |0.00     |
#+---------+-------+-----------+-----------+------------+---------+
#|class    |0      |NC         |NC         |0           |0        |
#+---------+-------+-----------+-----------+------------+---------+
#|method   |0      |NC         |NC         |0           |0        |
#+---------+-------+-----------+-----------+------------+---------+
#|function |0      |NC         |NC         |0           |0        |
#+---------+-------+-----------+-----------+------------+---------+
#
#
#
#4 lines have been analyzed
#
#Raw metrics
#-----------
#
#+----------+-------+------+---------+-----------+
#|type      |number |%     |previous |difference |
#+==========+=======+======+=========+===========+
#|code      |3      |75.00 |NC       |NC         |
#+----------+-------+------+---------+-----------+
#|docstring |0      |0.00  |NC       |NC         |
#+----------+-------+------+---------+-----------+
#|comment   |0      |0.00  |NC       |NC         |
#+----------+-------+------+---------+-----------+
#|empty     |1      |25.00 |NC       |NC         |
#+----------+-------+------+---------+-----------+
#
#
#
#Duplication
#-----------
#
#+-------------------------+------+---------+-----------+
#|                         |now   |previous |difference |
#+=========================+======+=========+===========+
#|nb duplicated lines      |0     |NC       |NC         |
#+-------------------------+------+---------+-----------+
#|percent duplicated lines |0.000 |NC       |NC         |
#+-------------------------+------+---------+-----------+
#
#
#
#Messages by category
#--------------------
#
#+-----------+-------+---------+-----------+
#|type       |number |previous |difference |
#+===========+=======+=========+===========+
#|convention |3      |NC       |NC         |
#+-----------+-------+---------+-----------+
#|refactor   |0      |NC       |NC         |
#+-----------+-------+---------+-----------+
#|warning    |0      |NC       |NC         |
#+-----------+-------+---------+-----------+
#|error      |1      |NC       |NC         |
#+-----------+-------+---------+-----------+
#
#
#
#% errors / warnings by module
#-----------------------------
#
#+----------+-------+--------+---------+-----------+
#|module    |error  |warning |refactor |convention |
#+==========+=======+========+=========+===========+
#|document1 |100.00 |0.00    |0.00     |100.00     |
#+----------+-------+--------+---------+-----------+
#
#
#
#Messages
#--------
#
#+-------------------------+------------+
#|message id               |occurrences |
#+=========================+============+
#|undefined-variable       |1           |
#+-------------------------+------------+
#|missing-module-docstring |1           |
#+-------------------------+------------+
#|missing-final-newline    |1           |
#+-------------------------+------------+
#|invalid-name             |1           |
#+-------------------------+------------+
#
#
#
#
#-----------------------------------
#Your code has been rated at 0.00/10