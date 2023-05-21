print("20202727_김상현")
animal = {"닭" : "병아리",
          "개" : "강아지",
          "곰" : "능소니",
          "고등어" : "고도리",
          "명태" : "노가리",
          "말" : "망아지",
          "호랑이" : "개호주"};

while(True):
    my_animal = input(str(list(animal.keys())) + "중 새끼 이름을 알고 싶은 동물은?")
    if my_animal in animal:
        print("<%s>의 새끼는 <%s>입니다." %(my_animal, animal.get(my_animal)))
    elif my_animal == "끝" :
        break
    else :
        print("그런 동물은 없습니다. 확인해 보세요")