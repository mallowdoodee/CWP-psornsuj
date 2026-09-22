def array_of_names(person):
    arr_name = []
    for first_name, last_name in person.items():
        arr_name.append(first_name.capitalize() + " " + last_name.capitalize())
    return arr_name

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

print(array_of_names(persons))
