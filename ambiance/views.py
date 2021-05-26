from django.http import HttpResponse
from django.template import Template, Context

def saludo(request): #firts view
        doc_externo=open("C:/Proyect/ambiance/ambiance/Plantillas/Platilla_1.html") 
        plt=Template(doc_externo.read())
        doc_externo.close()
        ctx=Context()
        documento=plt.render(ctx)
        return HttpResponse(documento) 
        