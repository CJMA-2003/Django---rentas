from django.urls import path
from . import views

urlpatterns = [
    #path('', views.menu, name='menu'),
    path('', views.inicio, name='inicio'),
    #Modulo de casas
    path('casa/', views.Modulocasa, name='modulo_casa'),
    path('casa/crear/', views.crearCasas, name='crear_casa'),
    path('casa/editar/<int:id>/', views.editarCasa, name='editar_casa'),
    path('casa/eliminar/<int:id>/', views.eliminarCasa, name='eliminar_casa'),
    path('casa/formulario/', views.formularioCasa, name='formulario_casa'),
    path('casa/formulario/<int:id>', views.formularioCasa, name='formulario_casa'),
    #Modulo de inquilino
    path('inquilino/', views.moduloInquilino, name='modulo_inquilino'),
    path('inquilino/formulario/', views.formularioInquilino, name='formulario_inquilino'),
    path('inquilino/formulario/<int:id>', views.formularioInquilino, name='formulario_inquilino'),
    path('inquilino/crear/', views.crearInquilino, name='crear_inquilino'),
    path('inquilino/eliminar/<int:id>', views.eliminarInquilino, name='eliminar_inquilino'),
    path('inquilino/editar/<int:id>',views.editarInquilino,name='editar_inquilino'),
    #modulo de pagos
    path('pagos/', views.moduloPago, name='modulo_pago'),
    path('formulario-pagos/', views.formularioPago, name='formulario_pago'),
    path('formulario-pagos/<int:id>', views.formularioPago, name='formulario_pago'),
    path('pago/crear/', views.crearPago, name='crear_pago'),
    path('pago/editar/<int:id>', views.editarPago, name='editar_pago'),
    path('pago/eliminar/<int:id>', views.formularioPago, name='eliminar_pago'),
    
]
