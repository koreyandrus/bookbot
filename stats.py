def get_word_count(contents):
    word_list = contents.split()
    print(f"Found {len(word_list)} total words")

def get_char_count(contents):
    count_dict = {}
    count_list = []
    for char in contents:
        if char != " ":
            lower = char.lower()
            if lower in count_dict:
                count_dict[lower] += 1
            else:
                count_dict[lower] = 1
    for char, count in count_dict.items():
        if char.isalpha():
            count_list.append({"char": char, "num": count})
    count_list.sort(reverse=True, key=sort_on)
    for char in count_list:
        print(f"{char["char"]}: {char["num"]}")
    
def sort_on(items):
    return items["num"]