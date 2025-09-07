def get_num_words(file):
    words = file.split()
    return len(words)

def uniques(file):
    unique_counts = {}
    case = file.lower()
    for c in case:
        if c in unique_counts:
            unique_counts[c] += 1
        else:
            unique_counts[c] = 1
    return unique_counts

def report(file):
    new_list = uniques(file)
    sorted_list = []
    for letter, number in new_list.items():
        if not letter.isalpha():
            continue
        sorted_list.append({"char": letter, "num": number})
    sorted_list.sort(key=lambda x: x["num"], reverse=True)

    return sorted_list
    
