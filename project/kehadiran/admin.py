from django.contrib import admin

# Register your models here.
from .models import *
from kehadiran.models import Kehadiran
import datetime

class KehadiranAdmin(admin.ModelAdmin):
	list_display = ['karyawan','jenis_kehadiran','waktu']
	list_filter = ('jenis_kehadiran',)
	search_fields = []
	list_per_page = 25

admin.site.register(Kehadiran,KehadiranAdmin)


class IzinAdmin(admin.ModelAdmin):
    list_display = ['karyawan', 'jenis_kehadiran', 'waktu_mulai', 'waktu_berhenti', 'disetujui']
    list_filter = ('jenis_kehadiran', 'disetujui')
    search_fields = ['alasan']
    list_per_page = 25
    actions = ['setujui','batalkan']

    def setujui(self,request,queryset):
    	for izin in queryset:
    		diff = izin.waktu_berhenti - izin.waktu_mulai
    		base = izin.waktu_berhenti
    		numdays = diff.days + 1
    		date_list = [base-datetime.timedelta(days=x) for x in range(0,numdays-1)]

    		for date in date_list:
    			print(date)
    			kehadiran = Kehadiran(karyawan=izin.karyawan,jenis_kehadiran=izin.jenis_kehadiran,waktu=date)
    			kehadiran.save()

    		izin.disetujui = True
    		izin.save()

    setujui.short_description = "Terima pengajuan izin yang dipilih"
    
    def batalkan(self,request,queryset):
    	queryset.update(disetujui=False)

    batalkan.short_description = "Tolak pengajuan izin yang dipilih"				


admin.site.register(Izin, IzinAdmin)