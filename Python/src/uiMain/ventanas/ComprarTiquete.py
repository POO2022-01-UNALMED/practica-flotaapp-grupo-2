from calendar import calendar, month
import imp
import tkinter as tk
from tkinter.tix import INTEGER

from setuptools import Command
from gestorAplicacion.viajes.Ciudad import Ciudad
from gestorAplicacion.viajes.Viaje import Viaje
from uiMain.Funcionalidades.Asignar import Asignar
from uiMain.Funcionalidades.Gestionar import Gestionar
from gestorAplicacion.personas.Comprador import Comprador
from gestorAplicacion.viajes.Tiquete import Tiquete
import os
import pathlib
from unittest import TestCase
from tkcalendar import Calendar, DateEntry

from datetime import datetime
from datetime import timedelta


class ComprarTiquete(tk.Frame):
    def __init__(self, window):
        super().__init__(window)
        self._window = window
        self._vTop = tk.Frame(self._window)
        self._vTop1 = tk.Frame(self._window)
        self._vTop2 = tk.Frame(self._window)
        self._vTop3 = tk.Frame(self._window)
        self._vTop4 = tk.Frame(self._window)
        self._vTop5 = tk.Frame(self._window)
        self.entrada_ = tk.StringVar()
        self.entrada_1 = tk.StringVar()
        self.entrada_2 = tk.StringVar()
        self.entrada_3 = tk.StringVar()
        self.entrada_4 = tk.StringVar()
        self.entrada_5 = tk.StringVar()
        self.entrada1 = tk.IntVar()
        self.entrada2 = tk.IntVar()
        self.entrada3 = tk.IntVar()
        self.entrada4 = tk.IntVar()
        self.entrada5 = tk.IntVar()
        self.entrada6 = tk.IntVar()

        def viaje():
            entrada2 = self.entrada_.get().upper()
            fechaTo = datetime.strptime(self.entrada_2.get(),"%Y-%m-%d")
            if entrada2 in listaInfo and fechaTo > datetime.now():
                ventana()
                obtenerFecha()
            else:
                ventana1()

        def obtenerFecha():
            self.entrada_2.get()
            
        title = tk.Label(self._vTop, text="C O M P R A R   T I Q U E T E").grid(row=0, column=3,padx=1, pady=10)
        origen = tk.Label(self._vTop, text=" Origen: ").grid(row=1,column=0, pady=10)
        origenMed = tk.Label(self._vTop, text=" MEDELLÍN ").grid(row=1,column=1, pady=10)
        destino = tk.Label(self._vTop, text=" Destino ").grid(row=1, column=2, padx=10, pady=10)
        entrada1 = tk.Entry(self._vTop,borderwidth=2, textvariable =self.entrada_).grid(row=1, column=3, padx=10, pady=10)
        cal = DateEntry(self._vTop,selectmode="day",date_pattern="yyyy-MM-dd",textvariable=self.entrada_2).grid(row=1, column=4, padx=10, pady=10)
        fecha1= tk.Button(self._vTop, text="Establecer Fecha", command=lambda:obtenerFecha).grid(row=2, column=4, padx=10, pady=10)
        boton = tk.Button(self._vTop, text="Buscar", command=viaje).grid(row=1, column=5, padx=10, pady=10)
        listaTotal = []
        listaInfo = [viaje.getDestino().getNombre() for viaje in Viaje.getViajes()]

        def funcionCiudad():
            ventana2()

        def funcionTiquete():
            ventana3()
            
        
        def enviarInfo():
            ventana5()
            
        
        def ventana():
            self._window.geometry("640x420")
            self._vTop.destroy()
            title1 = tk.Label(self._vTop1, text="C O M P R A R   T I Q U E T E").grid(row=0, column=1,pady=10)
            mensaje = tk.Label(self._vTop1, text="Seleccione un el tiquete que desea comprar").grid(row=1,column=1,padx=1,pady=10)
            lista = [viaje.getDestino().getNombre() for viaje in Viaje.getViajes()]
            for viaje in Viaje.getViajes():
                entrada2 = self.entrada_.get().upper()
                fechaTo = datetime.strptime(self.entrada_2.get(),"%Y-%m-%d")
                variable = listaInfo.index(entrada2)
                if entrada2 == listaInfo[variable] and entrada2 == viaje.getDestino().__str__() and fechaTo > datetime.now():
                    #print(viaje.getDestino())
                    contadorRow= 4
                    contador2 = 1
                    #print(len(viaje.tiquetesDisponibles()))
                    for x in range(len(viaje.tiquetesDisponibles())):
                        mostar = tk.Radiobutton(self._vTop1, text=viaje.tiquetesDisponibles()[x], variable=self.entrada3, value=contador2, command=funcionTiquete).grid(row=contadorRow, column=1)
                        listaTotal.append(viaje.tiquetesDisponibles()[x])
                        contador2 +=1 
                        contadorRow +=1
                    

        def ventana1():
            self._window.geometry("640x420")
            self._vTop.destroy()
            self._vTop1.destroy()
            title2 = tk.Label(self._vTop2, text="C O M P R A R   T I Q U E T E").grid(row=0, column=0,pady=10)
            mensaje = tk.Label(self._vTop2, text="En este momento no hay viajes disponibles para esta ciudad o la fecha no esta disponible \n puede elegir entre las siguientes ciudades:").grid(row=1, column=0, padx=10, pady=10)
            contador = 2
            otroContador = 1
            for viaje in Viaje.getViajes():
                opcion = tk.Radiobutton(self._vTop2, text=viaje.getDestino(),variable=self.entrada1, value=otroContador, command=funcionCiudad).grid(row=contador, column=0, padx=10, pady=10)
                contador += 1
                otroContador += 1

        def ventana2():
            self._window.geometry("640x420")
            self._vTop.destroy()
            self._vTop1.destroy()
            self._vTop2.destroy()
            title3 = tk.Label(self._vTop3, text="C O M P R A R   T I Q U E T E").grid(row=0, column=1,pady=10)
            listica = [viaje for viaje in Viaje.getViajes()]
            tiquetesUsar = listica[self.entrada1.get()-1].tiquetesDisponibles()
            aux = 1
            for newTiquete in tiquetesUsar:
                algo = tk.Radiobutton(self._vTop3, text=newTiquete, variable= self.entrada6, value=aux, command=funcionTiquete).grid(row=aux, column=1,pady=10)
                aux += 1 
                listaTotal.append(newTiquete)
                

        def ventana3():
            self._window.geometry("640x420")
            self._vTop.destroy()
            self._vTop1.destroy()
            self._vTop2.destroy()
            self._vTop3.destroy()
            title4 = tk.Label(self._vTop4, text="C O M P R A R   T I Q U E T E").grid(row=0, column=1,pady=10)
            tiqueteFinal = listaTotal[self.entrada3.get()-1]
            id = tk.Label(self._vTop4, text="Ingrese su CC:").grid(row=1, column=1, padx=10, pady=10)
            idEntry = tk.Entry(self._vTop4,borderwidth=2, textvariable =lambda:self.entrada4).grid(row=1, column=2, padx=10, pady=10)
            nombre = tk.Label(self._vTop4, text="Ingrese su nombre:").grid(row=2, column=1, padx=10, pady=10)
            nombreEntry = tk.Entry(self._vTop4,borderwidth=2, textvariable =self.entrada_4).grid(row=2, column=2, padx=10, pady=10)
            correo = tk.Label(self._vTop4, text="Ingrese su correo:").grid(row=3, column=1, padx=10, pady=10)
            correoEntry = tk.Entry(self._vTop4,borderwidth=2, textvariable =lambda:self.entrada5).grid(row=3, column=2, padx=10, pady=10)
            celular = tk.Label(self._vTop4, text="Ingrese su numero de celular:").grid(row=4, column=1, padx=10, pady=10)
            celularEntry = tk.Entry(self._vTop4,borderwidth=2, textvariable =self.entrada_5).grid(row=4, column=2, padx=10, pady=10)
            enviar = tk.Button(self._vTop4, text="Enviar", command=enviarInfo).grid(row=5, column=2, padx=10, pady=10)

        def ventana5():
            self._window.geometry("640x420")
            self._vTop.destroy()
            self._vTop1.destroy()
            self._vTop2.destroy()
            self._vTop3.destroy()
            self._vTop4.destroy()
            comprador = Comprador(self.entrada4.get(), self.entrada_4.get(),self.entrada5.get(),self.entrada_5.get())
            Asignar.asignarTiquete(comprador, listaTotal[self.entrada3.get()-1])
            title5 = tk.Label(self._vTop5, text="I N F O R M A C I O N   T I Q U E T E").grid(row=0, column=1,pady=10)
            mas = tk.Label(self._vTop5, text=comprador.__str__()).grid(row=1, column=1, padx=10, pady=10)
            mas1 = tk.Label(self._vTop5, text=listaTotal[self.entrada3.get()-1].__str__()).grid(row=2, column=1, padx=10, pady=10)
            

        self._vTop.pack()
        self._vTop1.pack()
        self._vTop2.pack()
        self._vTop3.pack()
        self._vTop4.pack()
        self._vTop5.pack()
        
        
    