class BaseModel:
    PK = 1
    TYPE = 'Basic Model'

    def __init__(self, data_type, title, content, created_at, updated_at):
        self.PK = BaseModel.PK
        self.data_type = data_type
        self.title = title
        self.content = content
        self.created_at = created_at
        self.updated_at = updated_at
        BaseModel.PK += 1

    def save(self):
        print('데이터를 저장합니다.')


class Novel(BaseModel):
    def __init__(self, data_type, title, content, created_at, updated_at, author):
        super().__init__(data_type, title, content, created_at, updated_at)
        self.author = author


class Other(BaseModel):
    TYPE = 'Other Model'

    def save(self):
        print('데이터를 다른 장소에 저장합니다.')


class ExtendedModel(Novel, Other):
    def __init__(self):
        self.extended_type = 'Extended Type'

    def display_info(self):
        print(
            f'PK: {Novel.PK}, TYPE: {Other.TYPE}, EXtended Type: {self.extended_type}')

    def save(self):
        print('데이터를 확장해서 저장합니다.')


extened_instance = ExtendedModel()
print('ExtendedModel 인스턴스의 정보 출력 및 저장 메서드 호출')
extened_instance.display_info()
extened_instance.save()
