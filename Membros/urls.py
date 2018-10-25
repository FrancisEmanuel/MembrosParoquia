from django.urls import path
from .views import MembroCreate, MembroList, MembroDetail, MembroUpdate, MembroDelete

urlpatterns = [
    path('membro_list/', MembroList.as_view(), name='membro_list_cbv'),
    path('membro_create/', MembroCreate.as_view(), name='membro_create_cbv'),
    path('membro_detail/<int:pk>/', MembroDetail.as_view(), name='membro_detail_cbv'),
    path('membro_update/<int:pk>/', MembroUpdate.as_view(), name='membro_update_cbv'),
    path('membro_delete/<int:pk>/', MembroDelete.as_view(), name='membro_delete_cbv'),
]
