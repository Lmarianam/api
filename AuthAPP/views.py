from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Company
import json   

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class CompanyView(View):

    def get(self, request, id=0):

        if id > 0:
            companies = list(Company.objects.filter(id=id).values())
            if companies:
                company = companies[0]
                datos = {'message': "Success", 'company': company}
            else:
                datos = {'message': "Company not found"}
        else:
            companies = list(Company.objects.values())
            if len(companies) > 0:
                datos = {'message': "Success", 'companies': companies}
            else:
                datos = {'message': "Companies not found"}

        return JsonResponse(datos)

    def post(self, request):
        try:
            jd = json.loads(request.body.decode('utf-8'))
            Company.objects.create(
                name=jd['name'],
                website=jd['website'],
                foundation=jd['foundation']
            )
            return JsonResponse({'message': "Success"})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    def put(self, request, id=0):   # <<--- id=0 para evitar errores
        print("RAW BODY:", request.body)

        try:
            jd = json.loads(request.body.decode('utf-8'))
            companies = list(Company.objects.filter(id=id).values())

            if len(companies) > 0:
                company = Company.objects.get(id=id)
                company.name = jd['name']
                company.website = jd['website']
                company.foundation = jd['foundation']
                company.save()
                datos = {'message': "Success"}
            else:
                datos = {'message': "Company not found"}

            return JsonResponse(datos)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    def delete(self, request, id=0):
        companies = list(Company.objects.filter(id=id).values())
        if len(companies) > 0:
            Company.objects.get(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Company not found"}
        return JsonResponse(datos)
