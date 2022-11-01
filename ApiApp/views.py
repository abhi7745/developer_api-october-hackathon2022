from django.http import Http404, JsonResponse
from django.shortcuts import redirect, render

# django restframework
from rest_framework.decorators import api_view
from rest_framework.response import Response

# pagination - using function-based views
from rest_framework.pagination import PageNumberPagination

from ApiApp.models import Advocates
from .serializers import AdvocateSerializer

from django.db.models import Q
# Create your views here.

@api_view(['GET'])
def api(request):
    print(request.get_full_path())
    data = ['Welcome To October Hackathon 2022 - ⚙️ Challenge 1 - 🎃 APIs Edition', 'https://hackathon22.up.railway.app/advocates/', 'https://hackathon22.up.railway.app/advocates/francescociull4/']
    return Response(data)

# @api_view(['GET', 'POST'])
@api_view(['GET'])
def advocate_list(request):

    if request.method == 'GET':

        paginator = PageNumberPagination()
        paginator.page_size = 10
        person_objects = Advocates.objects.all()
        result_page = paginator.paginate_queryset(person_objects, request)
        # serializer = AdvocateSerializer(result_page, many=True)

        if not request.GET.get('query') == None:
            # query = ''
            query = request.GET.get('query')
            
            print('Query', query)

            if Advocates.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query)).exists():
                advocates = Advocates.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query))
                paginator = PageNumberPagination()
                paginator.page_size = 1
                person_objects = advocates
                result_page = paginator.paginate_queryset(person_objects, request)
                serializer = AdvocateSerializer(result_page, many=True)
                return paginator.get_paginated_response(serializer.data)
            
            else:
                print(query+' not exist')
                return Response(str(query)+' not exist')
        
        # serializer = AdvocateSerializer(advocates, many=True)
        # return Response(serializer.data)
        serializer = AdvocateSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    else:
        if request.method == 'POST':
            advocate = Advocates.objects.create(
                username=request.data['username'],
                name=request.data['name']
            )

            serializer = AdvocateSerializer(advocate, many=False)

            print(request.data)
            print('data saved to database')
            # return Response('Post request')
            return Response(serializer.data)
        
# @api_view(['GET', 'PUT', 'DELETE'])
@api_view(['GET'])
def advocate_detail(request, username):
    advocate = Advocates.objects.get(username=username)

    if request.method == 'GET':
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        advocate.username = request.data['username']
        advocate.name = request.data['name']
        advocate.save()
        print('data updated')

        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)

    if request.method == 'DELETE':
        advocate.delete()
        print('data deleted')
        return Response('User '+ str(advocate.username) +' was deleted')






# from rest_framework.views import APIView

# class AdvocatesDetail(APIView):
    
#     def get_object(self, username):
#         try:
#             return Advocates.objects.get(username=username)

#         except Advocates.DoesNotExist:
#             # raise Advocates
#             raise Http404

#     def get(self, request, username):
#         # advocate = Advocates.objects.get(username=username)
#         advocate = self.get_object(username)
#         serializer = AdvocateSerializer(advocate, many=False)
#         return Response(serializer.data)
#         # return Response('username')

#     def put(self, request, username):
#         # advocate = Advocates.objects.get(username=username)
#         advocate = self.get_object(username)
#         advocate.username = request.data['username']
#         advocate.name = request.data['name']
#         advocate.save()
#         print('data updated')

#         serializer = AdvocateSerializer(advocate, many=False)
#         return Response(serializer.data)

#     def delete(self, request, username):
#         # advocate = Advocates.objects.get(username=username)
#         advocate = self.get_object(username)
#         advocate.delete()
#         print('data deleted')
#         return Response('User '+ str(advocate.username) +' was deleted')


# {
#     "username":"abhi",
#     "name":"Abhijith KR"
# }


# pagination - using class-based views
# from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView

class set_Pagination(PageNumberPagination):
    page_size=10

class AdvocatesDetail(ListAPIView):

    queryset = Advocates.objects.all()
    serializer_class = AdvocateSerializer
    pagination_class= set_Pagination




# pagination - using function-based views
# from rest_framework.pagination import PageNumberPagination
@api_view(['GET'])
def checker(request):
    paginator = PageNumberPagination()
    paginator.page_size = 2
    person_objects = Advocates.objects.all()
    result_page = paginator.paginate_queryset(person_objects, request)
    serializer = AdvocateSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

