''' ~~~~~~~~~~~~~~~~ Creade/Read/Update/Delete ~~~~~~~~~~~~~~~~~~~ '''

# class CreateMixin:
#     def create(self, todo, key):
#         if key in self.todo:
#             return 'Задача под этим ключом уже существует'
#         else:
#             self.todo[key] = todo
#             return self.todo

# class DeleteMixin:
#     def delete(self,key):
#         self.todo.pop(key)
#         # print(self.todo)

# class UpdateMixin:
#     def update(self,key, new_value):
#         self.todo[key] = new_value

# class ReadMixin:
#     def read(self):
#         print(self.todo.items())

# class Notes(CreateMixin, DeleteMixin,ReadMixin, UpdateMixin):
#     todo = {}

# task = Notes()
# print(task.create('HomeWork', 1))
# print(task.create('Bu', 2))
# task.delete(2)
# task.update(3, 'Дааа')
# task.read()


from vuews import CreateMixin, ListingMixin, RetrieveMixin, UpdateMixin,DeleteMixin
class Products(CreateMixin, ListingMixin, RetrieveMixin, UpdateMixin, DeleteMixin):
    pass
product = Products()
# product.create()
# product.listing()
# product.retrieve()
# product.update()
product.delete()
