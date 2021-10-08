from django.db import models

# Create your models here.

#Inicio Scrit.

class ClienteXxi(models.Model):
    id_cliente = models.BigIntegerField(primary_key=True)
    nombre_cli = models.CharField(max_length=30)
    correo_cli = models.CharField(max_length=30)
    telefono_cli = models.BigIntegerField()
    direccion_cli = models.CharField(max_length=50, blank=True, null=True)
    contrasena_cli = models.CharField(max_length=40)

    
    def __str__(self) :
        return self.nombre_cli



class EmpleadosXxi(models.Model):
    id_empleado = models.BigIntegerField(primary_key=True)
    nombre_emp = models.CharField(max_length=15)
    apellido_pat_emp = models.CharField(max_length=15)
    apellido_mat_emp = models.CharField(max_length=15)
    salario = models.BigIntegerField()
    fecha_nac = models.DateField()
    direccion_emp = models.CharField(max_length=30)
    telefono_emp = models.BigIntegerField()
    correo_emp = models.CharField(max_length=30)
    tipo_emplado_xxi_id_tipo_empleado = models.ForeignKey('TipoEmpladoXxi', models.DO_NOTHING, db_column='tipo_emplado_xxi_id_tipo_empleado')
    contrasena_emp = models.CharField(max_length=12)

    
    def __str__(self) :
        return self.nombre_emp

class FacturaXxi(models.Model):
    id_factura = models.BigIntegerField(primary_key=True)
    fecha = models.DateField()
    total = models.BigIntegerField()
    cliente_xxi_id_cliente = models.ForeignKey(ClienteXxi, models.DO_NOTHING, db_column='cliente_xxi_id_cliente')
    tipo_pago_xxi_id_tipo_pago = models.ForeignKey('TipoPagoXxi', models.DO_NOTHING, db_column='tipo_pago_xxi_id_tipo_pago')

    
    def __str__(self) :
        return self.fecha

class IngredientesXxi(models.Model):
    id_ingrediente = models.BigIntegerField(primary_key=True)
    ingrediente = models.CharField(max_length=15)
    marca = models.CharField(max_length=12)
    cantidad = models.BigIntegerField()

   
    def __str__(self) :
        return self.ingrediente

class MesaXxi(models.Model):
    id_mesa = models.BigIntegerField(primary_key=True)
    capacidad = models.BigIntegerField()

    
    def __str__(self) :
        return self.capacidad

class OrdenesXxi(models.Model):
    id_orden = models.BigIntegerField(primary_key=True)
    fecha = models.DateField()
    pagado = models.CharField(max_length=1)
    detalle = models.CharField(max_length=20)
    estado = models.CharField(max_length=12)
    cliente_xxi_id_cliente = models.ForeignKey(ClienteXxi, models.DO_NOTHING, db_column='cliente_xxi_id_cliente')
    mesa_xxi_id_mesa = models.ForeignKey(MesaXxi, models.DO_NOTHING, db_column='mesa_xxi_id_mesa')

    
    def __str__(self) :
        return self.estado

class ProductosXxi(models.Model):
    id_producto = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=15)
    precio = models.BigIntegerField()
    tipo_producto_xxi_id_tipo_producto = models.ForeignKey('TipoProductoXxi', models.DO_NOTHING, db_column='tipo_producto_xxi_id_tipo_producto')

    
    def __str__(self) :
        return self.nombre

class ProveedoresXxi(models.Model):
    id_proveedor = models.BigIntegerField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=15)
    telefono = models.BigIntegerField()
    correo = models.CharField(max_length=30)

    
    def __str__(self) :
        return self.nombre_proveedor

class Relation10(models.Model):
    ordenes_xxi_id_orden = models.OneToOneField(OrdenesXxi, models.DO_NOTHING, db_column='ordenes_xxi_id_orden', primary_key=True)
    factura_xxi_id_factura = models.ForeignKey(FacturaXxi, models.DO_NOTHING, db_column='factura_xxi_id_factura')

    


class Relation12(models.Model):
    mesa_xxi_id_mesa = models.OneToOneField(MesaXxi, models.DO_NOTHING, db_column='mesa_xxi_id_mesa', primary_key=True)
    cliente_xxi_id_cliente = models.ForeignKey(ClienteXxi, models.DO_NOTHING, db_column='cliente_xxi_id_cliente')

   


class Relation13(models.Model):
    cliente_xxi_id_cliente = models.OneToOneField(ClienteXxi, models.DO_NOTHING, db_column='cliente_xxi_id_cliente', primary_key=True)
    reservas_xxi_id_reserva = models.ForeignKey('ReservasXxi', models.DO_NOTHING, db_column='reservas_xxi_id_reserva')

    

class Relation3(models.Model):
    empleados_xxi_id_empleado = models.OneToOneField(EmpleadosXxi, models.DO_NOTHING, db_column='empleados_xxi_id_empleado', primary_key=True)
    ordenes_xxi_id_orden = models.ForeignKey(OrdenesXxi, models.DO_NOTHING, db_column='ordenes_xxi_id_orden')

    


class Relation31(models.Model):
    productos_xxi_id_producto = models.OneToOneField(ProductosXxi, models.DO_NOTHING, db_column='productos_xxi_id_producto', primary_key=True)
    ingredientes_xxi_id_ingrediente = models.ForeignKey(IngredientesXxi, models.DO_NOTHING, db_column='ingredientes_xxi_id_ingrediente')

  


class Relation32(models.Model):
    productos_xxi_id_producto = models.OneToOneField(ProductosXxi, models.DO_NOTHING, db_column='productos_xxi_id_producto', primary_key=True)
    ordenes_xxi_id_orden = models.ForeignKey(OrdenesXxi, models.DO_NOTHING, db_column='ordenes_xxi_id_orden')

    


class Relation33(models.Model):
    ingredientes_xxi_id_ingrediente = models.OneToOneField(IngredientesXxi, models.DO_NOTHING, db_column='ingredientes_xxi_id_ingrediente', primary_key=True)
    proveedores_xxi_id_proveedor = models.ForeignKey(ProveedoresXxi, models.DO_NOTHING, db_column='proveedores_xxi_id_proveedor')

    

class Relation8(models.Model):
    cliente_xxi_id_cliente = models.OneToOneField(ClienteXxi, models.DO_NOTHING, db_column='cliente_xxi_id_cliente', primary_key=True)
    ordenes_xxi_id_orden = models.ForeignKey(OrdenesXxi, models.DO_NOTHING, db_column='ordenes_xxi_id_orden')

    


class ReservasXxi(models.Model):
    id_reserva = models.BigIntegerField(primary_key=True)
    fecha_hora = models.DateField()
    cliente_xxi_id_cliente = models.ForeignKey(ClienteXxi, models.DO_NOTHING, db_column='cliente_xxi_id_cliente')

    
    def __str__(self) :
        return self.fecha_hora

class TipoEmpladoXxi(models.Model):
    id_tipo_empleado = models.BigIntegerField(primary_key=True)
    tipo_empleado = models.CharField(max_length=15)

    
    def __str__(self) :
        return self.tipo_empleado

class TipoPagoXxi(models.Model):
    id_tipo_pago = models.BigIntegerField(primary_key=True)
    tipo_pago = models.CharField(max_length=12)

    
    def __str__(self) :
        return self.tipo_pago

class TipoProductoXxi(models.Model):
    id_tipo_producto = models.BigIntegerField(primary_key=True)
    tipo_producto = models.CharField(max_length=15)

    
    def __str__(self) :
        return self.tipo_producto

#Fin Scrit.