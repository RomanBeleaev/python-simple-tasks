people = ""
count = 0
while True:
    count += 1
    name = input(f"{count}) enter someone's name >> ")
    if name == "":
        if count % 3 == 0:
            break
        else:
            while count % 3 == 0:
                count += 1
                people += f"{'|':12}"
    people += f'|{name:12}'

    if count % 3 == 0:
        people += "|\n"

print(people)





# Dane Tom Levy Holly Kane Verter Sol