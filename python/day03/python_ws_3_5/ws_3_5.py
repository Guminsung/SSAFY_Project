number_of_people = 0
number_of_book = 100
name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

def increase_user():
    global number_of_people
    number_of_people += 1

def create_user(name, age, address):
    increase_user()
    user_info = {'name' : name, 'age' : age, 'address' : address}
    print(f'{name}님 환영합니다!')
    return user_info

many_user = list(map(create_user, name, age, address))

def rental_book(info):
    decrease_book(info['age']//10)
    print(f'{info["name"]}님의 {info["age"]//10}권의 책을 대여하였습니다.')

def decrease_book(book):
    global number_of_book
    number_of_book -= book
    print(f'남은 책의 수 : {number_of_book}')

list(map(lambda x : rental_book(x), many_user))
