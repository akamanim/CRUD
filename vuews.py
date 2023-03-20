import json
file_path = 'data.json'
class GetMixin:
    def get_data(self):
        with open(file_path) as file:
            return json.load(file)
        
    def get_id(self):
        with open('id.txt', 'r') as file:
            id = int(file.read())
            id += 1
        with open('id.txt', 'w') as file:
            file.write(str(id))
        return id
    
class CreateMixin(GetMixin):
    def create(self):
        data = super().get_data()
        try:
            new_product = {
                'id': super().get_id(),
                'model' : input('Введите модель телефона: '),
                'price' : int(input('Введите стоимость телефона: ')),
                'color' : input('Введите цвет телефона: '),
                'storage': int(input('Введите память телефона: '))
            }
        except ValueError:
            print('Введите число!Пока орать не начал!!!')
            self.create()
        else:
            data.append(new_product)
            # print(data)

            with open(file_path, 'w') as file:
                json.dump(data, file)
                print('Successfully created')

class ListingMixin(GetMixin):
    def listing(self):
        print('Список телефонов')
        data = super().get_data()
        print(data)

class RetrieveMixin(GetMixin):
    def retrieve(self):
        data = super().get_data()

        try:
            id = int(input('Введите номер продукта: '))
        except ValueError:
            print('Введите в числовом формате! Пока орать не начал!!!')
            self.retrieve()
        else:
            one_product = list(filter(lambda x: x['id'] == id, data))
            # print(one_product)
            if not one_product:
                print('Такого продукта не существует')
            else:
                print(one_product[0])

class UpdateMixin(GetMixin):
    def update(self):
        data = super().get_data()
        try:
            id = int(input('Введите номер продукта: '))
        except ValueError:
            print('Введите в числовом формате! Пока орать не начал!!!')
            self.update()
        else:
            one_product = list(filter(lambda x: x['id'] == id, data))
            try:
                product = data.index(one_product[0])
            except:
                print('Такого продукта нет')
            else:    
                choice = int(input('Что вы хотите изменить? 1 - model, 2 - price, 3 - color, 4 - storage:  '))
                try:    
                    if choice == 1:
                        data[product]['model'] = input('Введите новую модель: ')
                        print(data[product])
                    elif choice == 2:
                        data[product]['price'] = int(input('Введите новую цену: '))
                        print(data[product])
                    elif choice == 3:
                        data[product]['color'] = input('Введите новый цвет: ')
                        print(data[product])
                    elif choice == 4:
                        data[product]['storage'] = int(input('Введите новую память: '))
                        print(data[product])
                    else:
                        print('Вы ввели не существующий номер')
                        self.update()
                except ValueError:
                    print('Вы ввели не верный формат')
                    self.update()
                with open(file_path, 'w') as file:
                    json.dump(data, file)

class DeleteMixin(GetMixin):
    def delete(self):
        data = super().get_data()
        try:
            id = int(input('Введите номер продукта: '))
        except ValueError:
            print('Введите в числовом формате! Пока орать не начал!!!')
            self.delete()
        else:
            one_product = list(filter(lambda x: x['id'] == id, data))
        if not one_product:
            print('Такого товара нет')
        product = data.index(one_product[0])
        data.pop(product)
        print(data)