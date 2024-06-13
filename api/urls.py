from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiResumen, name="Resumen API"),
    path('office-address/', views.apiOfficeAddresses, name="Direcciones Oficinas"),
    path('office-address/list/', views.officeAddressesList, name="Lista Direcciones Oficinas"),
    path('office-address/detail/<str:id>/', views.officeAddressesDetail, name="Detalles Direccion Oficina"),
    path('office-address/create/', views.officeAddressCreate, name="Crear Direccion Oficina"),
    path('office-address/update/<str:id>/', views.officeAddressUpdate, name="Actualizar Direccion Oficina"),
    path('office-address/delete/<str:id>/', views.officeAddressDelete, name="Borrar Direccion Oficina"),

    path('house-address/', views.apiHouseAddresses, name="Direcciones Casas"),
    path('house-address/list/', views.houseAddressesList, name="Lista Direcciones Casas"),
    path('house-address/detail/<str:id>/', views.houseAddressesDetail, name="Detalles Direccion Casa"),
    path('house_address/create/', views.houseAddressCreate, name="Crear Direccion Casa"),
    path('house_address/update/<str:id>/', views.houseAddressUpdate, name="Actualizar Direccion Casa"),
    path('house-address/delete/<str:id>/', views.houseAddressDelete, name="Borrar Direccion Casa"),

    path('offices/', views.apiOffices, name="Oficinas"),
    path('offices/list', views.officesList, name="Lista Oficinas"),
    path('offices/detail/<str:id>/', views.officeDetail, name="Detalles Oficina"),
    path('offices/create/', views.officeCreate, name="Crear Oficina"),
    path('offices/update/<str:id>/', views.officeUpdate, name="Actualizar Casa"),
    path('offices/delete/<str:id>/', views.officeDelete, name="Borrar Oficina"),

    path('image-offices/', views.apiImageOffices, name="Imagenes Oficinas"),
    path('image-offices/list/', views.imageOfficesList, name="Lista Imagenes Oficinas"),
    path('image-offices/detail/<str:id>/', views.imageOfficeDetail, name="Detalles Imagen Oficina"),
    path('image-offices/create/', views.imageOfficeCreate, name="Crear Imagen Oficina"),
    path('image-office/delete/<str:id>/', views.imageOfficeDelete, name="Borrar Imagen Oficina"),

    path('houses/', views.apiHouses, name="Casas"),
    path('houses/list/', views.housesList, name="Lista Casas"),
    path('houses/detail/<str:ref>/', views.houseDetail, name="Detalles Casa"),
    path('houses/create/', views.houseCreate, name="Crear Casa"),
    path('houses/update/<str:id>/', views.houseUpdate, name="Actualizar Casa"),
    path('houses/delete/<str:id>/', views.houseDelete, name="Borrar Casa"),

    path('image-houses/', views.apiImageHouses, name="Imagenes Casas"),
    path('image-houses/list/', views.imageHousesList, name="Lista Imagenes Casas"),
    path('image-houses/house/<str:id>/', views.imageHouseSpecificHouse, name="Lista Imagenes Casas"),
    path('image-houses/detail/<str:id>/', views.imageHouseDetail , name="Detalles Imagen Casa"),
    path('image-houses/create/', views.imageHouseCreate, name="Crear Imagen Casa"),
    path('image-houses/delete/<str:id>/', views.imageHouseDelete, name="Borrar Imagen Casa"),

    path('agents/', views.apiAgents, name="Agentes"),
    path('agents/list/', views.agentsList, name="Lista Agentes"),
    path('agents/detail/<str:id>/', views.agentDetail , name="Detalles Agente"),
    path('agents/create/', views.agentCreate, name="Crear Agente"),
    path('agents/update/<str:id>/', views.agentUpdate, name="Actualizar Agentes"),
    path('agents/delete/<str:id>/', views.agentDelete, name="Borrar Agente"),

]