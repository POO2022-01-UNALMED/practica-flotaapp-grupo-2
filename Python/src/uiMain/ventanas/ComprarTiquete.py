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
from tkinter import messagebox

from datetime import datetime


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
        self.entrada7 = tk.IntVar()

        def viaje():
            #popUp()
            entrada2 = self.entrada_.get().upper()
            entrada = self.entrada_1.get().upper()
            fechaTo = datetime.strptime(self.entrada_2.get(),"%Y-%m-%d")
            
            #if fechaTo > datetime.now():
            con = 1
            conRow = 3
            for viajecito in Viaje.getViajes():
                selection = tk.Radiobutton(self._vTop, text=viajecito, variable= self.entrada7, value=con, command=ventana).grid(row=conRow, column=2, padx=10, pady=10)
                con += 1
                conRow += 1
                #ventana()
                obtenerFecha()
                
            #else:
                #ventana1()

        def obtenerFecha():
            mostrarFecha = tk.Label(self._vTop,text="La fecha seleccionada es: " + self.entrada_2.get()).grid(row=4, column=1, padx=10, pady=10)
            print(self.entrada_2.get())
            
            
        def popUp1():
            fechaTo = datetime.strptime(self.entrada_2.get(),"%Y-%m-%d")
            if fechaTo < datetime.now():
                error = messagebox.showerror("Error", "Seleccione una fecha mayor a la de hoy")
            else:
                obtenerFecha()
                boton = tk.Button(self._vTop, text="Buscar Viajes", command=viaje).grid(row=2, column=2, padx=10, pady=10)

            

        def popUp():
            comprador = Comprador(self.entrada4.get(), self.entrada_4.get(),self.entrada_5.get(),self.entrada5.get())
            v = messagebox.askquestion("Confirmar Información", str(comprador))
            print(v)
            if v == "yes":
                enviarInfo()
            else:
                ventana3()
            
        title = tk.Label(self._vTop, text="C O M P R A R   T I Q U E T E").grid(row=0, column=2,padx=1, pady=10)
        inst = tk.Label(self._vTop, text=" Señor usuario primero seleccione la fecha haciendo click en el boton 'Establecer Fecha'\n luego dar click al boton 'Buscar Viajes'").grid(row=1, column=2, padx=10, pady=10)
        fechita = tk.Label(self._vTop, text=" Fecha ").grid(row=2,column=0, pady=10)
        cal = DateEntry(self._vTop,selectmode="day",date_pattern="yyyy-MM-dd",textvariable=self.entrada_2).grid(row=2, column=1, padx=10, pady=10)
        fecha1= tk.Button(self._vTop, text="Establecer Fecha", command=popUp1).grid(row=3, column=1, padx=10, pady=10)
        #boton = tk.Button(self._vTop, text="Buscar Viajes", command=viaje).grid(row=2, column=2, padx=10, pady=10)
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
            mensaje = tk.Label(self._vTop1, text="Seleccion de tiquete a comprar").grid(row=1,column=1,padx=1,pady=10)
            contadorRow= 4
            contador2 = 1
            viajeVerdad = Viaje.getViajes()[int(self.entrada7.get()-1)]
            if len(viajeVerdad.tiquetesDisponibles()) == 0:
                disculpa = tk.Label(self._vTop1, text=" Señor usuario no hay tiquetes disponibles \n para este viaje").grid(row=2, column=1, padx=10,pady=10)
            else:
                #print(viajeVerdad.tiquetesDisponibles())
                for x in range(len(viajeVerdad.tiquetesDisponibles())):
                    mostar = tk.Radiobutton(self._vTop1, text=viajeVerdad.tiquetesDisponibles()[x], variable=self.entrada3, value=contador2, command=funcionTiquete).grid(row=contadorRow, column=1)
                    listaTotal.append(viajeVerdad.tiquetesDisponibles()[x])
                    #print(viajeVerdad.tiquetesDisponibles()[x])
                    contadorRow +=1
                    contador2 += 1

        """def ventana1():
            self._window.geometry("640x420")
            self._vTop.destroy()
            self._vTop1.destroy()
            title2 = tk.Label(self._vTop2, text="C O M P R A R   T I Q U E T E").grid(row=0, column=0,pady=10)
            mensaje = tk.Label(self._vTop2, text="En este momento no hay viajes disponibles para esta ciudad o la fecha no esta disponible \n puede elegir entre las siguientes ciudades:").grid(row=1, column=0, padx=10, pady=10)
            contador = 2
            otroContador = 1
            #otralista = [viaje.tiquetesDisponibles() for viaje in Viaje.getViajes()]
            for viaje in  Viaje.getViajes(): 
                opcion = tk.Radiobutton(self._vTop2, text=viaje.getDestino(),variable=self.entrada1, value=otroContador, command=funcionCiudad).grid(row=contador, column=0, padx=10, pady=10)
                contador += 1
                otroContador += 1
                print(self.entrada_2.get())"""
  
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
            idEntry = tk.Entry(self._vTop4,borderwidth=2, textvariable =self.entrada4).grid(row=1, column=2, padx=10, pady=10)
            nombre = tk.Label(self._vTop4, text="Ingrese su nombre:").grid(row=2, column=1, padx=10, pady=10)
            nombreEntry = tk.Entry(self._vTop4,borderwidth=2, textvariable =self.entrada_4).grid(row=2, column=2, padx=10, pady=10)
            correo = tk.Label(self._vTop4, text="Ingrese su correo:").grid(row=3, column=1, padx=10, pady=10)
            correoEntry = tk.Entry(self._vTop4,borderwidth=2, textvariable =self.entrada_5).grid(row=3, column=2, padx=10, pady=10)
            celular = tk.Label(self._vTop4, text="Ingrese su numero de celular:").grid(row=4, column=1, padx=10, pady=10)
            celularEntry = tk.Entry(self._vTop4,borderwidth=2, textvariable =self.entrada5).grid(row=4, column=2, padx=10, pady=10)
            enviar = tk.Button(self._vTop4, text="Enviar", command=popUp).grid(row=5, column=2, padx=10, pady=10)    

        def ventana5():
            self._window.geometry("640x420")
            self._vTop.destroy()
            self._vTop1.destroy()
            self._vTop2.destroy()
            self._vTop3.destroy()
            self._vTop4.destroy()
            title5 = tk.Label(self._vTop5, text="I N F O R M A C I O N   T I Q U E T E").grid(row=0, column=1,pady=10)
            comprador = Comprador(self.entrada4.get(), self.entrada_4.get(),self.entrada_5.get(),self.entrada5.get())
            Asignar.asignarTiquete(comprador, listaTotal[self.entrada3.get()-1])
            mas = tk.Label(self._vTop5, text=comprador.__str__()).grid(row=1, column=1, padx=10, pady=10)
            mas1 = tk.Label(self._vTop5, text=listaTotal[self.entrada3.get()-1].__str__()).grid(row=2, column=1, padx=10, pady=10)
            mas2 = tk.Label(self._vTop5, text="Gracias por viajar con nosotros \n FLOTA-APP").grid(row=3, column=1, padx=10, pady=10)

        self._vTop.pack()
        self._vTop1.pack()
        self._vTop2.pack()
        self._vTop3.pack()
        self._vTop4.pack()
        self._vTop5.pack()

        ComprarTiquete.mainloop()
