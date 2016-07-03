from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from karyawan.models import Karyawan, Akun
# Create your views here.


def login_view(request):
	if request.POST:
		#cek data post
		user = authenticate(username=request.POST['username'],password=request.POST['password'])
		#cek jika user ada
		if user is not None:
			#cek jika user aktif
			if user.is_active:
				try:
					#get object from akun model 
					akun = Akun.objects.get(akun=user.id)
					#do login
					login(request,user)
					#set session
					request.session['karyawan_id'] = akun.karyawan.id
					request.session['jenis_akun'] = akun.jenis_akun
					request.session['username'] = request.POST['username']
				except:
					#set flash message
					messages.add_message(request,messages.INFO,'akun ini belum terhubung dengan data karyawan. hubungi administrator')

				return redirect('/')

			else:
				messages.add_message(request,messages.INFO,'user belum terferifikasi')
		else:
			messages.add_message(request,messages.INFO,'username dan password salah')
	return render(request,'login.html')


def logout_view(request):
	logout(request)
	return redirect('/')						
