from django.contrib import admin
from areaProductos.models import Estado_del_pedido, Producto, Cargo, Empleado, Turno, Paciente, Pedido, Armazon, Lado, Detalle_producto, Lente, Tipo_de_pedido, Forma_de_pago, Nombre_producto


# Register your models here.
class Estado_del_pedidoAdmin(admin.ModelAdmin):
    list_diplay = ("estado",)
    list_filter = ("estado",)

admin.site.register(Estado_del_pedido, Estado_del_pedidoAdmin)


class CargoAdmin(admin.ModelAdmin):
    list_display = ("tarea",)
    list_filter = ("tarea",)

admin.site.register(Cargo, CargoAdmin)


class ArmazonAdmin(admin.ModelAdmin):
    list_display = ("armazon","precio",)

admin.site.register(Armazon, ArmazonAdmin)


class LadoAdmin(admin.ModelAdmin):
    list_display = ("lado",)

admin.site.register(Lado, LadoAdmin)


class Detalle_productoAdmin(admin.ModelAdmin):
    list_display = ("detalle",)

admin.site.register(Detalle_producto, Detalle_productoAdmin)


class LenteAdmin(admin.ModelAdmin):
    list_display = ("lado", "detalle", "precio",)
    list_filter = ("lado", "detalle", "precio",)

admin.site.register(Lente, LenteAdmin)


class Tipo_de_pedidoAdmin(admin.ModelAdmin):
    list_display = ("tipo",)

admin.site.register(Tipo_de_pedido, Tipo_de_pedidoAdmin)

class Nombre_productoAdmin(admin.ModelAdmin):
    list_display = ("nombre", )
    list_filter = ("nombre", )

admin.site.register(Nombre_producto, Nombre_productoAdmin)



class Forma_de_pagoAdmin(admin.ModelAdmin):
    list_display = ("forma",)

admin.site.register(Forma_de_pago, Forma_de_pagoAdmin)



class ProductoAdmin(admin.ModelAdmin):
    list_display = ("precio", "producto",)
    list_filter = ("precio", "producto",)

admin.site.register(Producto, ProductoAdmin)



class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "email", "telefono", "cargo")
    list_filter = ("nombre", "apellido", "cargo")

admin.site.register(Empleado, EmpleadoAdmin)



class TurnoAdmin(admin.ModelAdmin):
    list_display = ("medico", "turno", "asistencia")
    list_filter = ("medico", "turno", "asistencia")

admin.site.register(Turno, TurnoAdmin)



class PacienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "email", "telefono",) # empleado es el médico
    list_filter = ("nombre", "apellido", )

admin.site.register(Paciente, PacienteAdmin)



class PedidoAdmin(admin.ModelAdmin):
    list_display = ("tipo_de_pedido", "forma_de_pago", "estado", "cliente", "producto", "vendedor", "lente", "armazon",)
    list_filter = ("tipo_de_pedido", "forma_de_pago", "estado", "cliente", "producto", "vendedor", "lente", "armazon",)

admin.site.register(Pedido, PedidoAdmin)