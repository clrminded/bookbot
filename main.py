def word_count_of_book(file_path_of_book):
    with open(file_path_of_book) as f:
        file_contents = f.read()
        words = file_contents.split()
    return len(words) # frankenstein = 77986



def character_count_of_book(file_path_to_book):
    count_array = []
    character_count = {}
    with open(file_path_to_book) as f:
        file_contents = f.read()
        lower_cased_file_contents = file_contents.lower()

    for c in lower_cased_file_contents:
        if not c.isalpha():
            continue
        if c not in character_count:
            character_count[c] = 1
        else:
            character_count[c] += 1

    
    for key in character_count:
        count_array.append({"letter": key, "count": character_count[key]})

    def sort_on(dict):
        return dict["count"]

    count_array.sort(reverse=True, key=sort_on)
    return count_array

def create_report(path_to_file):
    print(f"--- Begin report of {path_to_file} ---")
    total_count = word_count_of_book(path_to_file)
    print(f"{total_count} words found in the document")
    print()
    array = character_count_of_book(path_to_file)
    for dict in array:
        letter = dict["letter"]
        count = dict["count"]
        print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")





def main():
    create_report("books/frankenstein.txt")
  

main()