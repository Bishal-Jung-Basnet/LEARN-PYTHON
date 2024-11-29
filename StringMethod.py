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
    #join(list) example
    words = ["apple", "banana", "mango"]
    joined_string=",".join(words)
    print(f"join(list): {joined_string}")
    #ljust(width) example
    left_justified = s.ljust(20)
    print(f"ljust(20): {left_justified}")
    #lower() example
    lower_case = s.lower()
    print(f"lower(): {lower_case}")
    #lstrip() example
    stripped_left = s.lstrip()
    print(f"lstrip(): {stripped_left}")
    #replace(oldsub, newsub)
    replaced = s.replace('hello', 'hi')
    print(f"replace('hello', 'hi'): {replaced}")
    #rfind(sub) example
    right_find_position = s.rfind('o')
    print(f"rfind('o): {right_find_position}")
string_methods()