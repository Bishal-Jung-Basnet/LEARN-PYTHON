def string_methods():
    s = "hello world"
    #capital
    capatilized = s.capitalize()
    print(f"capatilize(): {capatilized}")
    #title example
    tite_case = s.title()
    print(f"Title(): {tite_case}")
    #centered example
    centered = s.center(20)
    print(f"center(): '{centered}'")
    #count(sub) example
    count_occurrances = s.count('o')
    print(f"Count(o): {count_occurrances}")
    #find(sub) example
    find_position = s.find('o')
    print(f"find(o): {find_position}")
string_methods()