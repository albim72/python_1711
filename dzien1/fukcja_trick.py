def counter(step=[0]):
    step[0] += 1
    return step[0]

    #step_list = [0]  -> tworzone jeden raz!

print(counter())
print(counter.__defaults__)
print(counter())
print(counter.__defaults__)
print(counter())
print(counter.__defaults__)
print(counter())
print(counter.__defaults__)
print(counter())
print(counter.__defaults__)

