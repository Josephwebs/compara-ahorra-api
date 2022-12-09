from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse
import json, traceback
from core.persistencia.models import Producto
from rest_framework.response import Response

TEXT_PLAIN = "text/plain"
NOT_FOUND = 'Registro no encontrado en el sistema.'
APPLICATION_JSON = 'application/json'

@api_view(['GET', 'POST', 'PUT'])
def load(request):
    if request.method == 'GET':  
        return find_all()
    elif request.method == 'POST':
        return create(request)
    elif request.method == 'PUT':
        return update(request)
    
@api_view(['GET', 'DELETE'])    
def load_id(request, id):
    if request.method == 'GET':
        return find_by_id(id)    
    if request.method == 'DELETE':
        return delete_by_id(id)    
    
def find_all():      
    productos = []
    try: 
        resultado = Producto.objects.all()
        for p in resultado:
            productos.append(p.to_json())
        return create_response(productos, status.HTTP_200_OK, APPLICATION_JSON)
    except Exception:
        traceback.print_exc()
        return productos    
   
def create(request):
    try: 
        print('create')
        payload = json.loads(request.body)
        print(payload)
        name = payload['name']
        price = payload['price'] 
        compare_at_price = payload['compare_at_price'] 
        image = payload['image'] 
        producto = Producto()
        producto.name = name
        producto.price = price
        producto.compare_at_price = compare_at_price
        producto.image = image
        producto.save()
        return create_response(producto.to_json(), status.HTTP_201_CREATED, APPLICATION_JSON)   
    except Exception:
        traceback.print_exc()
        return create_response(None, status.HTTP_500_INTERNAL_SERVER_ERROR, TEXT_PLAIN)        

def update(request):
    try: 
        print('create')
        payload = json.loads(request.body)
        print(payload)
        code = payload['id']
        name = payload['name']
        price = payload['price'] 
        compare_at_price = payload['compare_at_price'] 
        image = payload['image'] 
        producto = Producto.objects.get(pk=code)
        producto.name = name
        producto.price = price
        producto.compare_at_price = compare_at_price
        producto.image = image
        producto.save(force_update=True)
        return create_response(producto.to_json(), status.HTTP_200_OK, APPLICATION_JSON)  
    except Producto.DoesNotExist:
        return create_response('No se encontro el ID', status.HTTP_404_NOT_FOUND, TEXT_PLAIN)                        
    except Exception:
        traceback.print_exc()
        return create_response('No se encontro un ID valido para actualizar', status.HTTP_500_INTERNAL_SERVER_ERROR, TEXT_PLAIN)               

def find_by_id(id):
    print('find_by_id: ', id)          
    try:
        p = Producto.objects.get(pk=id)
        print('producto: ', p)
        return create_response(p.to_json(), status.HTTP_200_OK, APPLICATION_JSON)
    except Producto.DoesNotExist:
        return create_response(NOT_FOUND, status.HTTP_404_NOT_FOUND, TEXT_PLAIN)
    except Exception:
        traceback.print_exc()
        return create_response(None, status.HTTP_500_INTERNAL_SERVER_ERROR, TEXT_PLAIN)                                                  
                            
def delete_by_id(id):
    print('delete_by_id: ', id)          
    try:        
        p = Producto.objects.get(pk=id)
        p.delete()
        return create_response('producto {0} eliminado '.format(id), status.HTTP_200_OK, TEXT_PLAIN)
    except Producto.DoesNotExist:
        return create_response(NOT_FOUND, status.HTTP_404_NOT_FOUND, TEXT_PLAIN)        
    except Exception:
        traceback.print_exc()
        return create_response(None, status.HTTP_500_INTERNAL_SERVER_ERROR, TEXT_PLAIN)        

def create_response(payload, status_code, content_type):
    if payload is None:
        return Response(status=status_code)
    elif content_type is not None:
        return Response(payload, status=status_code, content_type=content_type)
    else:
        return Response(payload, status=status_code)