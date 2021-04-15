import yaml


class YamlOperation:
    def __init__(self,path='../../config/elocation.yaml'):
        with open(path, 'r+', encoding='utf8') as file:
            self.data = yaml.load(file, Loader=yaml.FullLoader)

    def get_locator(self,page,locator_name):
        return self.data[page][locator_name]

# ya_op = YamlOperation('../config/elocation.yaml')
# print(ya_op.get_locator('CustomerPage','newcustomerwindowtitle'))