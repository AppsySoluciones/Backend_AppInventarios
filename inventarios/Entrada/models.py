from django.db import models
from Fincas.models import Bodegas
from Insumo.models import Insumo
from Proveedor.models import Proveedor
from simple_history.models import HistoricalRecords
from datetime import datetime
import uuid

class Entrada(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateTimeField(default=datetime.now())
    bodega = models.ForeignKey(Bodegas,related_name='entradas_de_finca', on_delete=models.CASCADE, null=True)
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE, null=True)
    cantidad = models.FloatField()
    valor_unitario_entrada_a = models.FloatField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True)
    numero_factura = models.CharField(max_length=150, null=True)
    factura = models.FileField(upload_to='comprobantes/',null=True,blank=True)

    history = HistoricalRecords()

    def __str__(self):
        return f"{self.fecha_ingreso} - {self.insumo}"