def create_an_empty_list():
    return []

def create_a_list():
    return [1,2,3,4]

def add_element_to_end_of_list(l, element):
    l.append(element)
    return l

def add_element_to_start_of_list(l, element):
    new_list = [element] + l
    return new_list

def remove_element_from_end_of_list(l):
    if len(l) > 0:
        return l[:-1]

def remove_element_from_start_of_list(l):
    if len(l) >  0:
        return l[1:]

def retrieve_first_element_from_list(l):
    if len(l) > 0:
        return l[0]

def retrieve_element_from_index(l, index):
    if 0 <= index < len(l):
        return l[index]

def retrieve_last_element_from_list(l):
    if len(l) > 0:
        return l[-1]
