from django.urls import path
from .views import EntradaListCreateView, EntradaRetrieveUpdateDeleteView, InventarioHistoricoView, InventarioEstadoActualView, EntradaHistoricoView,EntradaPrimerHistoricoView,entradas_proximas_a_vencer
from .views import comprobante, EntradasListView, EntradasPorInsumoView
urlpatterns = [
    path('list-create/', EntradaListCreateView.as_view(), name='entrada-list-create'),
    path('retrieve/<str:pk>/', EntradaRetrieveUpdateDeleteView.as_view(), name='entrada-retrieve-update-delete'),
    path('retrieve/delete/<str:pk>/', EntradaRetrieveUpdateDeleteView.as_view(), name='entrada-retrieve-update-delete-ID'),
    path('inventario/historico/<int:insumo_id>/', InventarioHistoricoView.as_view(), name='inventario-historico'),
    path('inventario/estado-actual/', InventarioEstadoActualView.as_view(), name='inventario-estado-actual'),
    path('inventario/historico/', EntradaHistoricoView.as_view(), name='entrada-historico'),
    path('inventario/inicialentrada/', EntradaPrimerHistoricoView.as_view(), name='entrada-historico'),
    path('entradas-proximas-a-vencer/', entradas_proximas_a_vencer, name='entradas_proximas_a_vencer'),
    path('comprobante/<str:pk>/',comprobante),
    path('maestro-stock/',EntradasListView.as_view(),name='stock_master'),
    path('master-precio-insumo/<str:codigo_insumo>/',EntradasPorInsumoView.as_view(),name='master_precio_insumo'), 
    
    
]
