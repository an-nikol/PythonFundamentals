command = input()

dwarf_info = {}
result_list = []
name_d = "name"
hat_d = "hat"
physic_d = "physic"
hat_len = "hat len"

while command != "Once upon a time":
    command = command.split(" <:> ")
    dwarf_name = command[0]
    dwarf_hat_color = command[1]
    dwarf_physics = int(command[2])
    if dwarf_hat_color not in dwarf_info:
        dwarf_info[dwarf_hat_color] = {}
    if dwarf_name not in dwarf_info[dwarf_hat_color]:
        dwarf_info[dwarf_hat_color][dwarf_name] = 0
    if dwarf_info[dwarf_hat_color][dwarf_name] < dwarf_physics:
        dwarf_info[dwarf_hat_color][dwarf_name] = dwarf_physics
    command = input()


def show_result():
    for hat in dwarf_info:
        for name, physic in dwarf_info[hat].items():
            result_list.append({hat_len: len(dwarf_info[hat]), name_d: name, physic_d: physic, hat_d: hat})
            # key creates a custom sorting method
    for show in sorted(result_list, key=lambda item: (-item[physic_d], -item[hat_len])):
        print(f"({show[hat_d]}) {show[name_d]} <-> {show[physic_d]}")


show_result()