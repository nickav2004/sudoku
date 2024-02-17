import puzzle_numbers as pn

with open("smt-lib_code.smt2", "w") as file:

    for i in range(1, 10):
        for j in range(1, 10):
            for n in range(1, 10):
                file.write(
                    "(declare-const P_"
                    + str(i)
                    + "_"
                    + str(j)
                    + "_"
                    + str(n)
                    + " Bool)\n"
                )

    # Assert the given numbers
    for row, col, val in pn.p1_given_numbers:
        file.write(f"(assert P_{row}_{col}_{val})\n")

    for i in range(1, 10):
        for n in range(1, 10):
            row = "(assert (or"
            for j in range(1, 10):
                row += " " + "P_" + str(i) + "_" + str(j) + "_" + str(n)

            row += "))\n"
            file.write(row)

    for j in range(1, 10):
        for n in range(1, 10):
            column = "(assert (or"
            for i in range(1, 10):
                column += " " + "P_" + str(i) + "_" + str(j) + "_" + str(n)

            column += "))\n"
            file.write(column)

    for r in range(3):
        for c in range(3):
            for n in range(1, 10):
                block = "(assert (or"
                for i in range(1, 4):
                    for j in range(1, 4):
                        block += (
                            " "
                            + "P_"
                            + str(3 * r + i)
                            + "_"
                            + str(3 * c + j)
                            + "_"
                            + str(n)
                        )
                block += "))\n"
                file.write(block)

    for i in range(1, 10):
        for j in range(1, 10):
            for n in range(1, 10):
                cell = (
                    "(assert (or (not "
                    + "P_"
                    + str(i)
                    + "_"
                    + str(j)
                    + "_"
                    + str(n)
                    + ") (not (or"
                )
                for n1 in range(1, 10):
                    if n == n1:
                        continue
                    cell += " " + "P_" + str(i) + "_" + str(j) + "_" + str(n1)
                cell += "))))\n"
                file.write(cell)

    file.write("(check-sat)\n")
    file.write("(get-model)\n")
