from django.urls import path
from . import views
urlpatterns =[
    path('',views.index,name='index'),
    #anasayfaya  istek gelirse views'te ki index kısmını aç
    path('books',views.books,name='books'),
    path('authors',views.authors,name='authors'),
    path('authordetails/<int:authorId>',views.authorDetails,name='authordetails')
    

]