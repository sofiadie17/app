from app.wsgi import *
from blog.models import Categoria

# print('Hola!!')
# categorias = Categoria.objects.all()
# print(type(categorias))
# print(categorias)

'''
categoria = Categoria(nombre="python 3")
categoria.save()

categoriaPython = Categoria.objects.get(pk=1)
print(categoriaPython)


categoria2 = Categoria(nombre="Django")
categoria2.save()

categoria3 = Categoria(nombre="PHP")
categoria3.save()

categoria4 = Categoria(nombre="JavaScript")
categoria4.save()

categorias = Categoria.objects.filter(nombre__endswith=3)
print(categorias) '''