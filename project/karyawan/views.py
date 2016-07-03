from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .models import Karyawan
# Create your views here.

@login_required(login_url=settings.LOGIN_URL)
def profil(request):
	karyawan = Karyawan.objects.get(id=request.session['karyawan_id'])
	context = {
		'karyawan':karyawan
	}
	return render(request,'profile.html',context)
