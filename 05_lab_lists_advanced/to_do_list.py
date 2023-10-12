to_do_list = [0] * 10
while True:
    note = input()

    if note == 'End':

        break

    # split into two elements
    importance, task = note.split('-')
    index_importance = int(importance) - 1
    to_do_list[index_importance] = task


print([task for task in to_do_list if not task == 0])