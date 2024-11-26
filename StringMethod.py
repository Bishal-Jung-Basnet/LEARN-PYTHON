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
string_methods()