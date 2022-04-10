import random


def combining(participants_list):
    pairs = dict()
    random.shuffle(participants_list)
    for current_giver in participants_list:
        receivers_list = list(participants_list)
        receivers_list.remove(current_giver)
        if len(pairs) > 0:
            for key, value in pairs.items():
                if value in receivers_list:
                    receivers_list.remove(value)

        if len(receivers_list) == 0:
            rand_giver = random.choice(list(pairs.keys()))
            pairs[current_giver] = pairs.get(rand_giver)
            pairs[rand_giver] = current_giver
        else:
            rand_num = random.randint(0, abs(len(receivers_list)-1))
            current_receiver = receivers_list[rand_num]
            pairs[current_giver] = current_receiver
    return pairs


def simple_combining(participants_list):
    pairs = dict()
    random.shuffle(participants_list)
    for current_giver in participants_list:
        if participants_list.index(current_giver) == len(participants_list) - 1:
            pairs[current_giver] = participants_list[0]
        else:
            pairs[current_giver] = participants_list[participants_list.index(current_giver)+1]
    return pairs


def creating_files(pairs_dict):
    for key, value in pairs_dict.items():
        with open("With love for {}.txt".format(key), "w") as file_handler:
            file_handler.write("Hello, dear mrs/mr {}. This year you will make happy {}. Ho-ho-ho".format(key, value))

    print("Можете смотреть с заботой приготовленные .txt файлы. Дарите чудеса!")


if __name__ == "__main__":
    print(
        "Добро пожаловать в распределитель для Тайного Санты.\nВведите, пожалуйста, количество человек, которые будут "
        "участвовать.")
    people_amount = input()
    participants = []
    print("Вам предстоит ввести имена участников. Только помните: имена не должны повторяться")
    for each in range(int(people_amount)):
        print(f"Введите имя {each + 1} участника")
        current_person = input()
        participants.append(current_person)
    print("Ну и наконец, обговорим правила: допустимо ли обменивание подарками между двумя участниками?")
    answer = input()
    if answer == "да" or answer == "yes":
        pairs = combining(participants)
    else:
        pairs = simple_combining(participants)
    # print(pairs)
    creating_files(pairs)
