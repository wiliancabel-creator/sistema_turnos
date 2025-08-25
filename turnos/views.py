from django.shortcuts import render, redirect
from .models import Turno
from django.db.models import Case, When

def generar_turno(request):
    if request.method == 'POST':
        tipo = request.POST['tipo']
        ultimo = Turno.objects.filter(tipo=tipo).count()
        turno = Turno.objects.create(numero=ultimo + 1, tipo=tipo)
        # Guardamos el ID del turno en la sesión para mostrarlo después
        request.session['turno_id'] = turno.id
        return redirect('registro')  # Redirige a GET

    turno = None
    turno_id = request.session.pop('turno_id', None)
    if turno_id:
        turno = Turno.objects.get(id=turno_id)

    return render(request, 'turnos/registro.html', {'turno': turno})
def pantalla_espera(request):
    turnos = Turno.objects.filter(atendido=False).order_by('hora_creacion')
    return render(request, 'turnos/espera.html', {'turnos': turnos})

def panel_atencion(request):
    turno = Turno.objects.filter(atendido=False).order_by(
        Case(
            When(tipo='E', then=0),
            When(tipo='T', then=1),
            When(tipo='N', then=2),
        ),
        'hora_creacion'
    ).first()
    if turno:
        turno.atendido = True
        turno.save()
    return render(request, 'turnos/panel.html', {'turno': turno})
