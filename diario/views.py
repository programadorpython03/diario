from itertools import count
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pessoa, Diario
from datetime import datetime, timedelta
from django.db.models import Count
from django.db.models.functions import TruncMonth

# Create your views here.
'''
def home(request):
    textos = Diario.objects.all().order_by('create_at')[:3]

    #pessoas = Pessoa.objects.all()
    #nomes = [pessoa.nome for pessoa in pessoas]
    #qtds = []
    #for pessoa in pessoas:
    #    qtd = Diario.objects.filter(pessoas=pessoa).count()
    #    qtds.append(qtd)

    # GRAFICO 1
    pessoas_com_contagem = Pessoa.objects.annotate(qtd_diarios=Count('diario'))
    nomes = [ pessoa.nome for pessoa in pessoas_com_contagem ]
    qtds = [ pessoa.qtd_diarios for pessoa in pessoas_com_contagem ]

    # GRAFICO 2


    return render(request, 'home.html', {'textos': textos, 'nomes': nomes, 'qtds': qtds })

'''

def home(request):
    textos = Diario.objects.all().order_by('create_at')[:3]

    # GRAFICO 1 - Quantidade de diários por pessoa
    pessoas_com_contagem = Pessoa.objects.annotate(qtd_diarios=Count('diario'))
    nomes = [pessoa.nome for pessoa in pessoas_com_contagem]
    qtds = [pessoa.qtd_diarios for pessoa in pessoas_com_contagem]

    # GRAFICO 2 - Quantidade de diários por mês
    diarios_por_mes = Diario.objects.annotate(month=TruncMonth('create_at')) \
                                   .values('month') \
                                   .annotate(qtd_diarios=Count('id')) \
                                   .order_by('month')

    meses = [diario['month'].strftime('%B %Y') for diario in diarios_por_mes]  # Nome do mês e ano
    qtd_diarios_por_mes = [diario['qtd_diarios'] for diario in diarios_por_mes]

    return render(request, 'home.html', {
        'textos': textos,
        'nomes': nomes,
        'qtds': qtds,
        'meses': meses,
        'qtd_diarios_por_mes': qtd_diarios_por_mes
    })


def escrever(request):
    if request.method == 'GET':
    
        pessoas = Pessoa.objects.all()
        return render(request, 'escrever.html', {'pessoas': pessoas})
    
    elif request.method == 'POST':
    
        titulo = request.POST.get('titulo')
        tags = request.POST.getlist('tags')
        pessoas = request.POST.getlist('pessoas')
        texto = request.POST.get('texto')
        
        if len(titulo.strip()) == 0 or len(texto.strip()) == 0:
            # TODO: Adicionar mensagens de erro

            return redirect('escrever')

        diario = Diario(
            titulo = titulo,
            texto = texto
        )

        diario.set_tags(tags)

        diario.save()

        # for i in pessoas:
        #     pessoa = Pessoa.objects.get(id=1)
        #     diario.pessoas.add(pessoa)

        pessoa_obj = Pessoa.objects.filter(id__in=pessoas)
        diario.pessoas.add(*pessoa_obj)
        diario.save()

        # TODO: adicionar mensagens de sucesso

        return redirect('escrever')
    

def cadastrar_pessoa(request):
    if request.method == 'GET':
        return render(request, 'pessoa.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        foto = request.FILES.get('foto')
        
        pessoa = Pessoa(
            nome = nome,
            foto = foto
        )
        
        pessoa.save()
        return redirect('escrever')
    

def dia(request):
    data = request.GET.get('data')
    data_formatada = datetime.strptime(data, "%Y-%m-%d")
    diarios = Diario.objects.filter(create_at__gte=data_formatada).filter(create_at__lte=data_formatada+timedelta(days=1))
    return render(request, 'dia.html', {'diarios': diarios, 'total': diarios.count(), 'data': data} )



def excluir_dia(request):
    dia = datetime.strftime(request.GET.get('data'), '%Y-%m-%d')
    diarios = Diario.objects.filter(create_at__gte=dia).filter(create_at__lte=dia+timedelta(days=1))
    diarios.delete()
    return HttpResponse('teste')