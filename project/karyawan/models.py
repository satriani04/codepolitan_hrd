from django.db import models

# Create your models here.
from django.contrib.auth.models import User


#model divisi
class Divisi(models.Model):
	nama = models.CharField(max_length=120)
	keterangan = models.TextField(blank=True)

	def __str__(self):
		return self.nama

class Jabatan(models.Model):
	nama = models.CharField(max_length=120)
	keterangan = models.TextField(blank=True)

	def __str__(self):
		return self.nama

class Karyawan(models.Model):
	JENIS_KELAMIN = (
			('pria','Pria'),
			('wanita','Wanita')
		)

	JENIS_KARYAWAN = (
			('magang','Magang'),
			('kontrak','Kontrak'),
			('tetap','Tetap'),
		)

	nama = models.CharField(max_length=100)
	alamat = models.TextField(blank=True)
	jenis_kelamin = models.CharField(max_length=20, choices=JENIS_KELAMIN)					
	jenis_karyawan = models.CharField(max_length=20, choices=JENIS_KARYAWAN)
	no_telepon = models.CharField(max_length=100, blank=True)					
	email = models.CharField(max_length=100, blank=True)					
	no_rekening = models.CharField(max_length=100)
	pemilik_rekening = models.CharField(max_length=100)
	divisi = models.ForeignKey(Divisi)
	jabatan = models.ForeignKey(Jabatan)

	def __str__(self):
		return self.nama

class Akun(models.Model):
	JENIS_AKUN = (
			('karyawan','Karyawan'),
			('admin','Administrator'),
		)

	akun = models.ForeignKey(User)
	karyawan = models.ForeignKey(Karyawan)
	jenis_akun = models.CharField(max_length=100, choices=JENIS_AKUN)

	def  __str__(self):
		return self.karyawan.nama									