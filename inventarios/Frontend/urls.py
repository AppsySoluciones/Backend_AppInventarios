
from django.urls import path
from .views import *

urlpatterns = [
    path('', test_view, name='home'),
    path('login/',login_view, name='login'),
    path('logout/', logout_view, name='logout'),


    path('add-user/', add_user, name='add_user'),
    path('list-users/', list_users, name='list_users'),
    path('user/edit/<int:user_id>/', add_user, name='edit_user'),

    path('add-proveedor/', add_proveedor, name='add_proveedor'),
    path('list-proveedor/', list_proveedor, name='list_proveedor'),
    path('proveedor/edit/<int:prov_id>/', add_proveedor, name='edit_proveedor'),

    path('add-insumo/', add_insumo, name='add_insumo'),
    path('list-insumo/', list_insumo, name='list_insumo'),
    path('insumo/edit/<int:insumo_id>/', add_insumo, name='edit_insumo'),

    path('add-certificacion/', add_certificacion, name='add_certificacion'),
    path('list-certificacion/', list_certificacion, name='list_certificacion'),
    path('certificacion/edit/<int:cert_id>/', add_certificacion, name='edit_certificacion'),
    path('add-certificacion-insumo/', add_certificacion_insumo, name='add_certificacion_insumo'),
    

    path('add-ingrediente/', add_ingrediente, name='add_ingrediente'),
    path('list-ingrediente/', list_ingrediente, name='list_ingrediente'),
    path('ingrediente/edit/<int:ingrediente_id>/', add_ingrediente, name='edit_ingrediente'),
    path('add-ingrediente-insumo/', add_ingrediente_insumo, name='add_ingrediente_insumo'),

    path('add-unidad/', add_unidad, name='add_unidad'),
    path('list-unidad/', list_unidad, name='list_unidad'),
    path('unidad/edit/<int:unidad_id>/', add_unidad, name='edit_unidad'),
    path('add-unidad-insumo/', add_unidad_insumo, name='add_unidad_insumo'),

    

    path('add-grupo/', add_grupo, name='add_grupo'),
    path('list-grupo/', list_grupo, name='list_grupo'),
    path('add-grupo/edit/<str:grupo_id>/', add_grupo, name='edit_grupo'),
    path('add-grupo-insumo/', add_grupo_insumo, name='add_grupo_insumo'),
   

    path('list-entradas/', list_entradas, name='list_entradas'),
    path('inicialentrada/',list_entradas_primer_status,name='inicialentrada'),
    path('add-entradas/', add_entradas, name='add_entradas'),
    path('add-entradas/edit/<str:entradas_id>/', add_entradas, name='edit_entradas'),

    path('list-fincas/', list_fincas, name='list_fincas'),
    path('add-fincas/', add_fincas, name='add_fincas'),
    path('add-fincas/edit/<str:fincas_id>/', add_fincas, name='edit_fincas'),

    path('list-bodegas/', list_lotes, name='list_bodegas'),
    path('add-bodegas/', add_lotes, name='add_bodegas'),
    path('add-bodegas/edit/<int:lotes_id>/', add_lotes, name='edit_bodegas'),

    path('list-lotes/', list_bodegas, name='list_lotes'),
    path('add-lotes/', add_bodegas, name='add_lotes'),
    path('add-lotes/edit/<int:bodegas_id>/', add_bodegas, name='edit_lotes'),

    path('list-salidas/', list_salidas, name='list_salidas'),
    path('add-salidas/', add_salidas, name='add_salidas'),
    path('add-salidas/edit/<int:salidas_id>/', add_salidas, name='edit_salidas'),


    
]