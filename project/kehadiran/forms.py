from django.forms import ModelForm
from django import forms
from .models import Izin

class IzinForm(ModelForm):
	class Meta:
		model = Izin
		fields = ['jenis_kehadiran', 'waktu_mulai', 'waktu_berhenti', 'alasan']
		labels = {
			'jenis_kehadiran':'Jenis Izin',
			'waktu_mulai': 'Waktu mulai Izin',
			'waktu_berhenti': 'Waktu Berhenti Izin',
			'alasan': 'Alasan Izin'
		}
		error_messages = {
			'jenis_kehadiran':{'required':'anda haru pilih salah satu jenis'},
			'waktu_mulai':{'required':'anda harus masukan waktu mulai izin'},
			'waktu_berhenti':{'required':'anda harus masukan waktu berhenti izin'},
			'alasan':{'required':'anda harus masukan alasan izin'},
		}
		widgets = {
			'alasan':forms.Textarea(attrs={'cols':50,'rows':10})
		}