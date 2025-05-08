def merge_dicts(dict1, dict2):
    merged_dict = {}
    for key, value in dict1.items():
        merged_dict[key] = value
    for key, value in dict2.items():
        merged_dict[key] = value
    
    return merged_dict
