from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

from karyawan.models import Karyawan
from .models import Kehadiran,Izin
from .forms import IzinForm
import json
# Create your views here.

@login_required(login_url=settings.LOGIN_URL)
def kehadiran_view(request):
	daftar_hadir = Kehadiran.objects.filter(karyawan__id=request.session['karyawan_id']).order_by('waktu')

	if request.POST:
		bulan = request.POST['bulan']
		tahun = request.POST['tahun']

		daftar_hadir = Kehadiran.objects.filter(waktu__year=tahun,waktu__month=bulan,karyawan__id=request.session['karyawan_id']).order_by('waktu')

	context = {
		'daftar_hadir':daftar_hadir
	}

	return render(request,'kehadiran.html',context)

@login_required(login_url=settings.LOGIN_URL)
def izin_view(request):
	izin = Izin.objects.filter(karyawan__id=request.session['karyawan_id'])
	print(izin)
	context = {
		'daftar_izin':izin
	}
	return render(request,'list_izin.html',context)


@login_required(login_url=settings.LOGIN_URL)
def pengajuan_izin(request):
	if request.method == 'POST':
		form_data = request.POST
		form = IzinForm(form_data)
		if form.is_valid():
			izin = Izin(
					karyawan= Karyawan.objects.get(id=request.session['karyawan_id']),
					jenis_kehadiran= request.POST['jenis_kehadiran'],
					waktu_mulai=request.POST['waktu_mulai'],
					waktu_berhenti=request.POST['waktu_berhenti'],
					alasan=request.POST['alasan'],
					disetujui=False
				)
			izin.save()
			return redirect('/')
	else:
		form = IzinForm()

	return render(request,'tambah_izin.html',{'form':form})		

@login_required(login_url=settings.LOGIN_URL)
def report(request, bulan, tahun):
	temp_chart_data = []
	daftar_hadir = Kehadiran.objects.filter(waktu__year=tahun,waktu__month=bulan,karyawan__id=request.session['karyawan_id'])

	temp_chart_data.append({"x":"hadir","a":daftar_hadir.filter(jenis_kehadiran='hadir').count()})
	temp_chart_data.append({"x":"izin","a":daftar_hadir.filter(jenis_kehadiran='izin').count()})
	temp_chart_data.append({"x":"cuti","a":daftar_hadir.filter(jenis_kehadiran='cuti').count()})

	chart_data = json.dumps({"data":temp_chart_data})
	print(chart_data)
	context = {
		'chart_data':chart_data,
		'bulan':bulan,
		'tahun':tahun
	}

	return render(request,'grafik.html',context)







