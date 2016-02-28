# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 14:17:13 2016

@author: Tecnicamente
"""
import sys, os, string, csv, numpy, scipy.stats
import matplotlib.pyplot as plt

def ControlloParametriPassati (parametri):
# quando la funzione viene chiamata le si deve passare il comando "sys.argv"
	if len(parametri)<3:
		print"Uso: ", parametri[0], "file-dati-da-leggere file-dati-da-produrre-in-uscita"
		sys.exit(2)
	else:
		return

def CreaFileOutput (file):
# quando la funzione viene chiamata si deve passare "sys.argv[2]"
	#print "sono in CreaFileOutput prima del try"
	try:
	#	print "sono in CreaFileOutput dentro try"
		OutputFile = open(file,"w")
		print "Creato il file: ",file
	except:
		print "sono in CreaFileOutput dentro except"
		print "Errore nella creazione del file: ", file
		sys.exit(2)
	return OutputFile

def FileDati(file):
	try:
		InputFile = open(file,"r")
		print "Letto il file: ",file
	except:
		print "Impossibile leggere il file: ",file
		sys.exit(2)
	return InputFile

def ConvertiInCSV(InputFile,OuputFile):
	PrimaRiga = True
	for Riga in InputFile:
		stringa = list(Riga)
		if PrimaRiga == True:
			#RigaElaborata = Riga.replace(",","\t")
			OutputFile.write(Riga)
			PrimaRiga = False
		else:
		# correggo le "," che indicano i decimali in "."
		# essendo il formato variabile posso solo imporre di sostituire
		# la5 e 7 occorrenza della "," con il "."
			ContatoreVirgole = 0
			for PosizioneCarattere in range(len(Riga)):
				if Riga[PosizioneCarattere] == ",":
					ContatoreVirgole += 1
					if (ContatoreVirgole == 5):
						stringa[PosizioneCarattere] = "."
					if (ContatoreVirgole == 7):
						stringa[PosizioneCarattere] = "."
			NuovaRiga = "".join(stringa)
			#print Riga
			#print NuovaRiga
		
			OutputFile.write(NuovaRiga)
	return

def GraficoDati(file):
	tempo		= []
	download	= []
	upload		= []
	
	reader = csv.reader(file,delimiter=',')

	i = 0
	for row in reader:
		if row[1] == "Wifi":
			#print row[0],"\t",row[4],"\t",row[5]
			tempo.append(row[0])
			download.append(row[4])
			upload.append(row[5])
			print tempo[i],"\t", download[i],"\t", upload[i]
			i = i+1
	
	print "-"*60
	#TendenzaDownload = scipy.stats.linregress(range(len(download)), download)
	#TendenzaUpload	 = scipy.stats.linregress(range(len(upload)), upload)

	# Inverto la lista per rispettare la cronologia
	download.reverse()
	upload.reverse()
	tempo.reverse()
	#TendenzaDownload.reverse()
	#TendenzaUpload.reverse()

	plt.plot(download,	label = "Download MB/s")
	plt.plot(upload,	label = "Upload MB/s")
	
	#plt.plot(TendenzaDownload,	label = "Tendenza Download")
	#plt.plot(TendenzaUpload,	label = "Tendenza Upload")
	
	plt.grid(); plt.legend(), plt.show()
	return
	
	
# MAIN
ControlloParametriPassati(sys.argv)

InputFile = FileDati(sys.argv[1])
OutputFile = CreaFileOutput(sys.argv[2])

ConvertiInCSV(InputFile,OutputFile)

InputFile.close()
OutputFile.close()

GraficoDati(FileDati(sys.argv[2]))



