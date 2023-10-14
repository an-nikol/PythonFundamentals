number_of_electrons = int(input())

shells = []

for shell in range(1, number_of_electrons + 1):
    max_electrons_per_shell = 2 * shell ** 2
    # when current electrons are enough to fill a shell
    if number_of_electrons >= max_electrons_per_shell:
        shells.append(max_electrons_per_shell)
        number_of_electrons -= max_electrons_per_shell
        if number_of_electrons == 0:
            break
    # when current electrons are not enough
    else:
        shells.append(number_of_electrons)
        break

print(shells)