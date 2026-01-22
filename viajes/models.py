from django.db import models
from django.core.validators import MinValueValidator


class Vehiculo(models.Model):
    TIPO_CHOICES = [
        ('Turbo', 'Turbo'),
        ('Sencillo', 'Sencillo'),
        ('Eléctrico', 'Eléctrico'),
    ]

    codigo = models.CharField(max_length=50, unique=True, verbose_name='Código')
    placa = models.CharField(max_length=10, verbose_name='Placa', help_text='Formato: ABC-123')
    tipo_vehiculo = models.CharField(
        max_length=20,
        choices=TIPO_CHOICES,
        verbose_name='Tipo de Vehículo'
    )
    fecha_inicio = models.DateTimeField(verbose_name='Fecha de Inicio')
    fecha_fin = models.DateTimeField(verbose_name='Fecha de Fin')
    numero_entregas = models.IntegerField(
        verbose_name='Número de Entregas',
        validators=[MinValueValidator(0)]
    )
    facturacion = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name='Facturación',
        validators=[MinValueValidator(0)]
    )
    observacion = models.TextField(
        blank=True,
        null=True,
        verbose_name='Observación'
    )
    cliente = models.CharField(max_length=100, verbose_name='Cliente')
    validado = models.BooleanField(default=False, verbose_name='Validado')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Vehículo'
        verbose_name_plural = 'Vehículos'
        ordering = ['-fecha_inicio']  # Ordenamiento descendente por fecha_inicio

    def __str__(self):
        return f"{self.placa} - {self.cliente}"
