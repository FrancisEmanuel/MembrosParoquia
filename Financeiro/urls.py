from django.urls import path
from .views import EntradaCreate, EntradaList, EntradaDetail, EntradaUpdate, EntradaDelete
from .views import SaidaCreate, SaidaList, SaidaDetail, SaidaUpdate, SaidaDelete
from .views import CategoriaCreate, CategoriaList, CategoriaDetail, CategoriaUpdate, CategoriaDelete

urlpatterns = [
    path('entrada_list/', EntradaList.as_view(), name='entrada_list_cbv'),
    path('entrada_create/', EntradaCreate.as_view(), name='entrada_create_cbv'),
    path('entrada_detail/<int:pk>/', EntradaDetail.as_view(), name='entrada_detail_cbv'),
    path('entrada_update/<int:pk>/', EntradaUpdate.as_view(), name='entrada_update_cbv'),
    path('entrada_delete/<int:pk>/', EntradaDelete.as_view(), name='entrada_delete_cbv'),

    path('saida_list/', SaidaList.as_view(), name='saida_list_cbv'),
    path('saida_create/', SaidaCreate.as_view(), name='saida_create_cbv'),
    path('saida_detail/<int:pk>/', SaidaDetail.as_view(), name='saida_detail_cbv'),
    path('saida_update/<int:pk>/', SaidaUpdate.as_view(), name='saida_update_cbv'),
    path('saida_delete/<int:pk>/', SaidaDelete.as_view(), name='saida_delete_cbv'),

    path('Categoria_list/', CategoriaList.as_view(), name='Categoria_list_cbv'),
    path('Categoria_create/', CategoriaCreate.as_view(), name='Categoria_create_cbv'),
    path('Categoria_detail/<int:pk>/', CategoriaDetail.as_view(), name='Categoria_detail_cbv'),
    path('Categoria_update/<int:pk>/', CategoriaUpdate.as_view(), name='Categoria_update_cbv'),
    path('Categoria_delete/<int:pk>/', CategoriaDelete.as_view(), name='Categoria_delete_cbv'),
]
