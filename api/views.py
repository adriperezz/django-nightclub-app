from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from realEstate.models import *
from .serializers import *
from rest_framework.parsers import FileUploadParser
from rest_framework import status


#################  RESUMEN GENERAL  #################
### api/
@api_view(['GET'])
def apiResumen(request):
    api_urls = {
        'Office Addresses': '/office-address/',
        'House Addresses': '/house-address/',
        'Offices': '/offices/',
        'Image Offices': '/image-offices/', 
        'Houses': '/houses/',
        'Image Houses': '/image-houses/',
        'Agents': '/agents/',
        'Users': '/users/'
    }
    return Response(api_urls)

#################  DIRECCIONES OFICINAS  #################
### api/office-address/
@api_view(['GET'])
def apiOfficeAddresses(request):
    office_addresses_url = {
        'List': '/list/',
        'Detail View': '/detail/<str:id>/',
        'Create': '/create/',
        'Update': '/update/<str:id>/', 
        'Delete': '/delete/<str:id>/'
    }
    return Response(office_addresses_url)

### api/office-address/list
@api_view(['GET'])
def officeAddressesList(request):
    officeAddresses = OfficeAddress.objects.all()
    serializers = OfficeAddressSerializer(officeAddresses, many=True)
    return Response(serializers.data)

### api/office-address/detail/<str:id>/
@api_view(['GET'])
def officeAddressesDetail(request, id):
    officeAddress = OfficeAddress.objects.get(id=id)
    serializers = OfficeAddressSerializer(officeAddress, many=False)
    return Response(serializers.data)

### api/office-address/create
@api_view(["POST"])
def officeAddressCreate(request):
    serializer = OfficeAddressSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

### api/office-address/update/<str:id>/
@api_view(["PUT"])
def officeAddressUpdate(request, id):
    officeAddress = OfficeAddress.objects.get(id=id)
    serializer = OfficeAddressSerializer(officeAddress, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

### api/office-address/delete/<str:id>/
@api_view(["DELETE"])
def officeAddressDelete(request, id):
    officeAddress = OfficeAddress.objects.get(id=id)
    officeAddress.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

#################  DIRECCIONES CASAS  #################
### api/house-address/
@api_view(['GET'])
def apiHouseAddresses(request):
    house_addresses_url = {
        'List': '/list/',
        'Detail View': '/detail/<str:id>/',
        'Create': '/create/',
        'Update': '/update/<str:id>/', 
        'Delete': '/delete/<str:id>/'
    }
    return Response(house_addresses_url)

### api/house-address/list
@api_view(['GET'])
def houseAddressesList(request):
    houseAddresses = HouseAddress.objects.all()
    serializers = HouseAddressSerializer(houseAddresses, many=True)
    return Response(serializers.data)

### api/house-address/detail/<str:id>/
@api_view(['GET'])
def houseAddressesDetail(request, id):
    houseAddress = HouseAddress.objects.get(id=id)
    serializers = HouseAddressSerializer(houseAddress, many=False)
    return Response(serializers.data)

### api/house-address/create
@api_view(["POST"])
def houseAddressCreate(request):
    serializer = HouseAddressSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

### api/house-address/update/<str:id>/
@api_view(["PUT"])
def houseAddressUpdate(request, id):
    houseAddress = HouseAddress.objects.get(id=id)
    serializer = HouseAddressSerializer(houseAddress, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

### api/house-address/delete/<str:id>/
@api_view(["DELETE"])
def houseAddressDelete(request, id):
    houseAddress = HouseAddress.objects.get(id=id)
    houseAddress.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

#################  OFICINAS  #################
### api/offices/
@api_view(['GET'])
def apiOffices(request):
    offices_url = {
        'List': '/list/',
        'Detail View': '/detail/<str:id>/',
        'Create': '/create/',
        'Update': '/update/<str:id>/', 
        'Delete': '/delete/<str:id>/'
    }
    return Response(offices_url)

### api/offices/list
@api_view(['GET'])
def officesList(request):
    offices = Office.objects.all()
    serializers = OfficeSerializer(offices, many=True)
    return Response(serializers.data)

### api/offices/detail/<str:id>/
@api_view(['GET'])
def officeDetail(request, id):
    office = Office.objects.get(id=id)
    serializers = OfficeSerializer(office, many=False)
    return Response(serializers.data)

### api/offices/create
@api_view(["POST"])
def officeCreate(request):
    serializer = OfficeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

### api/offices/update/<str:id>/
@api_view(["PUT"])
def officeUpdate(request, id):
    office = Office.objects.get(id=id)
    serializer = OfficeSerializer(office, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

### api/offices/delete/<str:id>/
@api_view(["DELETE"])
def officeDelete(request, id):
    office = Office.objects.get(id=id)
    office.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

#################  FOTOS OFICINAS  #################
### api/image-offices/
@api_view(['GET'])
def apiImageOffices(request):
    image_offices_url = {
        'List': '/list/',
        'Detail View': '/detail/<str:id>/',
        'Create': '/create/',
        'Delete': '/delete/<str:id>/'
    }
    return Response(image_offices_url)

### api/image-offices/list
@api_view(['GET'])
def imageOfficesList(request):
    imageOffices = ImageOffice.objects.all()
    serializers = ImageOfficeSerializer(imageOffices, many=True)
    return Response(serializers.data)

### api/image-offices/detail/<str:id>/
@api_view(['GET'])
def imageOfficeDetail(request, id):
    imageOffice = ImageOffice.objects.get(id=id)
    serializers = ImageOfficeSerializer(imageOffice, many=False)
    return Response(serializers.data)

### api/image-office/create
@api_view(["POST"])
def imageOfficeCreate(request):
    serializer = ImageOfficeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

### api/image-office/delete/<str:id>/
@api_view(["DELETE"])
def imageOfficeDelete(request, id):
    imageOffice = ImageOffice.objects.get(id=id)
    imageOffice.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

#################  CASAS  #################
### api/houses/
@api_view(['GET'])
def apiHouses(request):
    houses_url = {
        'List': '/list/',
        'Detail View': '/detail/<str:id>/',
        'Create': '/create/',
        'Update': '/update/<str:id>/', 
        'Delete': '/delete/<str:id>/'
    }
    return Response(houses_url)

### api/houses/list
@api_view(['GET'])
def housesList(request):
    houses = House.objects.all()
    serializers = HouseSerializer(houses, many=True)
    return Response(serializers.data)

### api/houses/detail/<str:ref>/
@api_view(['GET'])
def houseDetail(request, ref):
    house = House.objects.get(reference=ref)
    serializers = HouseSerializer(house, many=False)
    return Response(serializers.data)

### api/houses/create
@api_view(["POST"])
def houseCreate(request):
    serializer = HouseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

### api/houses/update/<str:id>/
@api_view(["PUT"])
def houseUpdate(request, id):
    house = House.objects.get(id=id)
    serializer = HouseSerializer(house, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

### api/houses/delete/<str:id>/
@api_view(["DELETE"])
def houseDelete(request, id):
    house = House.objects.get(id=id)
    house.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

#################  FOTOS CASAS  #################
### api/image-houses/
@api_view(['GET'])
def apiImageHouses(request):
    image_houses_url = {
        'List': '/list/',
        'All Images From House': '/house/<str:id>/',
        'Detail View': '/detail/<str:id>/',
        'Create': '/create/',
        'Delete': '/delete/<str:id>/'
    }
    return Response(image_houses_url)

### api/image-houses/list
@api_view(['GET'])
def imageHousesList(request):
    imageHouses = ImageHouse.objects.all()
    serializers = ImageHouseSerializer(imageHouses, many=True)
    return Response(serializers.data)

### api/image-houses/house/str:id>/
@api_view(['GET'])
def imageHouseSpecificHouse(request, id):
    imageHouseSpecificHouse = ImageHouse.objects.filter(relatedHouse = id)
    serializers = ImageHouseSerializer(imageHouseSpecificHouse, many=True)
    return Response(serializers.data)

### api/image-houses/detail/<str:id>/
@api_view(['GET'])
def imageHouseDetail(request, id):
    imageHouse = ImageHouse.objects.get(id=id)
    serializers = ImageHouseSerializer(imageHouse, many=False)
    return Response(serializers.data)

### api/image-house/create
@api_view(["POST"])
def imageHouseCreate(request):
    serializer = ImageHouseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

### api/image-house/delete/<str:id>/
@api_view(["DELETE"])
def imageHouseDelete(request, id):
    imageHouse = ImageHouse.objects.get(id=id)
    imageHouse.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

#################  AGENTES  #################
### api/agents/
@api_view(['GET'])
def apiAgents(request):
    agents_url = {
        'List': '/list/',
        'Detail View': '/detail/<str:id>/',
        'Create': '/create/',
        'Update': '/update/<str:id>/', 
        'Delete': '/delete/<str:id>/'
    }
    return Response(agents_url)

### api/agents/list
@api_view(['GET'])
def agentsList(request):
    agents = Agent.objects.all()
    serializers = AgentSerializer(agents, many=True)
    return Response(serializers.data)

### api/agents/detail/<str:id>/
@api_view(['GET'])
def agentDetail(request, id):
    agent = Agent.objects.get(id=id)
    serializers = AgentSerializer(agent, many=False)
    return Response(serializers.data)

### api/agents/create
@api_view(["POST"])
def agentCreate(request):
    serializer = AgentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

### api/agents/update/<str:id>/
@api_view(["PUT"])
def agentUpdate(request, id):
    agent = Agent.objects.get(id=id)
    serializer = UserSerializer(agent, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

### api/agents/delete/<str:id>/
@api_view(["DELETE"])
def agentDelete(request, id):
    agent = Agent.objects.get(id=id)
    agent.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

#################  USUARIOS  #################
### api/users/
@api_view(['GET'])
def apiUsers(request):
    users_url = {
        'List': '/list/',
        'List Photos Specific House': '/list/<str:id>/',
        'Detail View': '/detail/<str:id>/',
        'Create': '/create/',
        'Update': '/update/<str:id>/', 
        'Delete': '/delete/<str:id>/'
    }
    return Response(users_url)

### api/users/list
@api_view(['GET'])
def usersList(request):
    users = User.objects.all()
    serializers = UserSerializer(users, many=True)
    return Response(serializers.data)

### api/users/detail/<str:id>/
@api_view(['GET'])
def userDetail(request, id):
    user = User.objects.get(id=id)
    serializers = UserSerializer(user, many=False)
    return Response(serializers.data)

### api/users/create
@api_view(["POST"])
def userCreate(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

### api/users/update/<str:id>/
@api_view(["PUT"])
def userUpdate(request, id):
    user = User.objects.get(id=id)
    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

### api/users/delete/<str:id>/
@api_view(["DELETE"])
def userDelete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)