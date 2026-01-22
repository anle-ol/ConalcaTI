from django.core.management.base import BaseCommand
from django.utils import timezone
from viajes.models import Vehiculo
from datetime import timedelta
import random
import string


class Command(BaseCommand):
    help = 'Genera 50 registros aleatorios de vehículos para pruebas'

    def handle(self, *args, **options):
        # Datos realistas para el sector logístico colombiano
        clientes_colombianos = [
            'Almacenes Éxito', 'Carulla', 'Olimpica', 'Falabella', 'Homecenter',
            'Almacenes La 14', 'Makro', 'Cencosud', 'Grupo Éxito', 'Almacenes Vivero',
            'Distribuidora Andina', 'Logística Nacional', 'Transportes del Valle',
            'Cargo Express', 'Mensajería Rápida', 'Distribuidora Central',
            'Logística Integral', 'Transportes Bogotá', 'Carga Segura',
            'Distribuidora del Norte', 'Logística del Sur', 'Transportes Antioquia',
            'Carga Nacional', 'Distribuidora Occidente', 'Logística Caribe'
        ]

        tipos_vehiculo = ['Turbo', 'Sencillo', 'Eléctrico']
        
        observaciones = [
            'Entrega exitosa sin novedades',
            'Retraso por tráfico en hora pico',
            'Cliente no disponible, reagendar entrega',
            'Mercancía en perfecto estado',
            'Requiere firma del destinatario',
            'Entrega urgente completada',
            'Revisión de inventario pendiente',
            'Entrega parcial completada',
            'Sin observaciones',
            'Cliente satisfecho con el servicio',
            'Requiere seguimiento especial',
            'Entrega programada para mañana',
            'Documentación completa',
            'Mercancía frágil manejada con cuidado',
            'Entrega nocturna completada'
        ]

        # Generar códigos únicos
        codigos_usados = set()
        
        # Limpiar datos existentes si se desea (opcional, comentado por seguridad)
        # Vehiculo.objects.all().delete()
        
        vehiculos_creados = 0
        
        for i in range(50):
            # Generar código único
            while True:
                codigo = f"VH-{random.randint(1000, 9999)}"
                if codigo not in codigos_usados:
                    codigos_usados.add(codigo)
                    break
            
            # Generar placa colombiana (formato: ABC-123)
            letras = ''.join(random.choices(string.ascii_uppercase, k=3))
            numeros = random.randint(100, 999)
            placa = f"{letras}-{numeros}"
            
            # Tipo de vehículo aleatorio
            tipo = random.choice(tipos_vehiculo)
            
            # Fechas aleatorias en los últimos 90 días
            dias_atras = random.randint(0, 90)
            fecha_inicio = timezone.now() - timedelta(days=dias_atras, hours=random.randint(0, 23), minutes=random.randint(0, 59))
            
            # Fecha fin entre 2 y 8 horas después de la fecha inicio
            horas_duracion = random.randint(2, 8)
            fecha_fin = fecha_inicio + timedelta(hours=horas_duracion, minutes=random.randint(0, 59))
            
            # Número de entregas realista (entre 5 y 50)
            numero_entregas = random.randint(5, 50)
            
            # Facturación realista (entre $500,000 y $5,000,000 COP)
            facturacion = random.uniform(500000, 5000000)
            
            # Cliente aleatorio
            cliente = random.choice(clientes_colombianos)
            
            # Observación aleatoria (70% de probabilidad de tener observación)
            observacion = random.choice(observaciones) if random.random() < 0.7 else ''
            
            # Estado de validación aleatorio (30% validados)
            validado = random.random() < 0.3
            
            # Crear el vehículo
            vehiculo = Vehiculo.objects.create(
                codigo=codigo,
                placa=placa,
                tipo_vehiculo=tipo,
                fecha_inicio=fecha_inicio,
                fecha_fin=fecha_fin,
                numero_entregas=numero_entregas,
                facturacion=round(facturacion, 2),
                observacion=observacion,
                cliente=cliente,
                validado=validado
            )
            
            vehiculos_creados += 1
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Se generaron exitosamente {vehiculos_creados} registros de vehiculos'
            )
        )
