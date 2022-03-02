def input_dictionary() -> dict:
    words = {}
    n = int(input())
    if 1 <= n <= 10 ** 5:
        for i in range(n):
            try:
                a, b = map(str, input().split())
                if len(a) < 16 and int(b) <= 10 ** 6:
                    words[a] = int(b)
            except ValueError as e:
                print(f"Exception {e}")
            i += 1
        return words


def append_elements(sorted_tuples: list) -> list:
    list_choice = []
    my_list = []
    for k, v in sorted_tuples:
        list_choice.append(k)
    if len(list_choice) > 0:
        my_list.append(list_choice)
        my_list.append([])
    else:
        my_list.append(list_choice)
    return my_list


def choice_words(my_word: str, words: dict) -> list:
    dict2 = {}
    for k, v in words.items():
        if v == 0:
            continue
        if my_word in k[:len(my_word)]:
            dict2[k] = v
    sorted_tuples = sorted(dict2.items(), key=lambda item: item[1], reverse=True)
    my_list = append_elements(sorted_tuples)
    return my_list


def word_input(words: dict) -> list:
    my_word = input()
    my_bool = True
    if len(my_word) < 16:
        for i in range(len(my_word) - 1):
            if 96 < ord(my_word[i]) < 123:
                continue
            else:
                my_bool = False
                break
        if my_bool is True:
            my_list = choice_words(my_word, words)
            return my_list


def print_word(main_list: list):
    if len(main_list[0]) < 11:
        for j in range(len(main_list)):
            print(*main_list[j], sep="\n")
    else:
        main_list[0] = main_list[0][:10]
        for j in range(len(main_list)):
            print(*main_list[j], sep="\n")


def word_output(main_list: list):
    for i in range(len(main_list)):
        if [] in main_list[i] and i == len(main_list) - 1 and len(main_list[i]) > 1:
            main_list[i].pop()
            print_word(main_list[i])
        if len(main_list[i]) == 1 and i == len(main_list) - 1:
            continue
        else:
            print_word(main_list[i])


def main():
    main_list = []
    words = input_dictionary()
    m = int(input())
    if 1 <= m <= 15000:
        for i in range(m):
            my_list = word_input(words)
            main_list.append(my_list)
        word_output(main_list)
    else:
        while m < 1 or m > 1500:
            m = int(input())
            if 1 <= m <= 15000:
                for i in range(m):
                    my_list = word_input(words)
                    main_list.append(my_list)
                word_output(main_list)


if __name__ == "__main__":
    main()
