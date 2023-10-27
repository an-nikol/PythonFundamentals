class Party:
    def __init__(self):
        self.people = []


party_object = Party()
name = input()
while name != 'End':
    party_object.people.append(name)
    name = input()

print(f"Going: {', '.join(party_object.people)}")
print(f"Total: {len(party_object.people)}")