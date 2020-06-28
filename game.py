import json
def set_charact(name):
    character = {
        "name": name,
        "level": 1,
        "hp": 100,
        "items":["가방","교과서"],
        "skill":["각성모드","전력질주"]
    }
    with open("save.txt", "w", encoding='utf-8') as f:
        json.dump(character, f, ensure_ascii = False, indent=4)
    # print("{0}님 반갑습니다. (HP {1})으로 게임을 시작합니다.".format(character["name"], character["hp"]))
    return character

def save_game(filename, charact):
    f = open(filename, "w", encoding="utf-8")
    for key in charact:
        print("%s,%s" % (key, charact[key]))
        f.write("%s:%s|n" % (key, charact[key]))
    f.close