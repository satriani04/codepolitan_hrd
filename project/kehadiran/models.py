from django.db import models

# Create your models here.
from karyawan.models import Karyawan

class Kehadiran(models.Model):
	JENIS_KEHADIRAN = (
			('izin','Izin'),
			('cuti','Cuti'),
			('alpa','Tanpa Alasan'),
			('hadir','Hadir'),
		)

	karyawan = models.ForeignKey(Karyawan)
	jenis_kehadiran = models.CharField(max_length=50, choices=JENIS_KEHADIRAN)
	waktu = models.DateField()

	def __str__(self):
		return self.karyawan.nama


class Izin(models.Model):
	JENIS_IZIN = (
			('izin','Izin'),
			('cuti','Cuti')
		)
	karyawan = models.ForeignKey(Karyawan)
	jenis_kehadiran = models.CharField(max_length=50,choices=JENIS_IZIN)
	waktu_mulai = models.DateField()
	waktu_berhenti = models.DateField()
	alasan = models.TextField()
	disetujui = models.BooleanField(default=False)

	def __str__(self):
		return self.karyawan.nama

