food_list = [
    {
        '종류': '한식',
        '이름': '잡채'
    },
    {
        '종류': '채소',
        '이름': '토마토'
    },
    {
        '종류': '중식',
        '이름': '자장면'
    },
]

# 아래에 코드를 작성하시오.
for i in range(len(food_list)) :
    if food_list[i]['이름'] == '토마토' :
        food_list[i]['종류'] = '과일'
    if food_list[i]['이름'] == '자장면' :
        print('자장면엔 고춧가루지')
    print(f'{food_list[i]["이름"]} 은/는 {food_list[i]["종류"]} (이)다.')
print(food_list)

cnt = 0
while cnt < len(food_list) :
    if food_list[cnt]['이름'] == '토마토' :
        food_list[cnt]['종류'] = '과일'
    if food_list[cnt]['이름'] == '자장면' :
        print('자장면엔 고춧가루지')
    print(f'{food_list[cnt]["이름"]} 은/는 {food_list[cnt]["종류"]} (이)다.')
    cnt += 1
print(food_list)
