import tkinter as tk
from tkinter import ttk
from Evento import Evento;
from datetime import date
from tkcalendar import DateEntry
from AdministradorDeFechas import AdministradorDeFechas
from tkinter import messagebox
import locale
class ComponenteEvento(tk.Frame):
    colorDeFondo = "#BFDFB2"
    fuenteDelComponente = "consolas 14 bold"
    colorBotones = "#62CFA4";
    def __init__(self, padre,tabla,manejadorDeLaListaEventos):
        super().__init__(padre)
        self.tablaEventos=tabla;
        fechaActual=date.today();
        self.manejadorDeLaListaEventos = manejadorDeLaListaEventos
        locale.setlocale(locale.LC_ALL, "es_ES");
        self.titulo=tk.StringVar();
        #self.fecha=tk.StringVar();
        self.hora=tk.StringVar();
        self.duracion=tk.IntVar(value=1);
        #self.descipcion=tk.StringVar();
        self.importancia=tk.BooleanVar();
        #self.fechaRecordatorio=tk.StringVar();
        self.horaRecordatorio=tk.StringVar();
        self.identificadorEvento=tk.StringVar();
        self.contenedorForm=tk.LabelFrame(self,text="Agregar nuevo Evento",font=self.fuenteDelComponente,padx=30,pady=30);
        self.contenedorForm.grid(row=0, column=0,padx=10,pady=10);
        tk.Label(self.contenedorForm, text="Titulo", font=self.fuenteDelComponente,bg=self.colorDeFondo).grid(row=0, column=0)
        self.tituloInput=tk.Entry(self.contenedorForm, textvariable=self.titulo, font=self.fuenteDelComponente)
        self.tituloInput.grid(row=0, column=1, columnspan=3, sticky="we")
        tk.Label(self.contenedorForm, text="Fecha",
                 font=self.fuenteDelComponente).grid(row=1, column=0)
        self.fechaInput = DateEntry(self.contenedorForm, locale="es_ES", font=self.fuenteDelComponente, mindate=fechaActual)
        self.fechaInput.grid(row=1, column=1,sticky="we");
        tk.Label(self.contenedorForm, text="Hora", font=self.fuenteDelComponente).grid(
            row=1, column=2, ipadx=5, ipady=5)
        self.horaInput=tk.Entry(self.contenedorForm, textvariable=self.hora, font=self.fuenteDelComponente, justify="center")
        self.horaInput.grid(row=1, column=3, padx=5, pady=5, sticky="we")
        tk.Label(self.contenedorForm, text="Duracion", font=self.fuenteDelComponente).grid(
            row=2, column=0,padx=5,pady=5);
        self.duracionInput=tk.Entry(self.contenedorForm, textvariable=self.duracion, font=self.fuenteDelComponente, justify="center")
        self.duracionInput.grid(row=2, column=1);
        tk.Label(self.contenedorForm, text="Importante", font=self.fuenteDelComponente).grid(
            row=2, column=2, padx=10, pady=10)
        self.checkButtonInput=tk.Checkbutton(self.contenedorForm, variable=self.importancia, font=self.fuenteDelComponente, bg=self.colorDeFondo)
        self.checkButtonInput.grid(row=2, column=3)
        tk.Label(self.contenedorForm, text="Fecha de Recordatorio", font=self.fuenteDelComponente).grid(
            row=3, column=0,columnspan=2, ipadx=5);
        tk.Label(self.contenedorForm, text="Hora de Recordatorio", font=self.fuenteDelComponente).grid(
            row=3, column=2, columnspan=2,ipadx=5);
        self.fechaRecordatorioInput = DateEntry(
            self.contenedorForm, locale="es_ES", font=self.fuenteDelComponente, mindate=fechaActual)
        self.fechaRecordatorioInput.grid(row=4, column=0, columnspan=2);
        self.horaRecordatorioInput=tk.Entry(self.contenedorForm, textvariable=self.horaRecordatorio,font=self.fuenteDelComponente, justify="center")
        self.horaRecordatorioInput.grid(row=4, column=2, columnspan=2);
        tk.Label(self.contenedorForm, text="Identificar Evento como", font=self.fuenteDelComponente).grid(
            row=5, column=0,columnspan=2,pady=10)
        self.identificadoInput=tk.Entry(self.contenedorForm, textvariable=self.identificadorEvento,font=self.fuenteDelComponente, justify="center")
        self.identificadoInput.grid( row=5, column=2, columnspan=2, sticky="we", pady=10)
        tk.Label(self.contenedorForm,text="Descripción",font=self.fuenteDelComponente).grid(row=6,column=0,columnspan=4,pady=5);
        self.descripcion = tk.Text(
            self.contenedorForm, font=self.fuenteDelComponente,height=5,width=60);
        self.descripcion.grid(row=7, column=0, columnspan=4,padx=5,pady=5);
        self.botonCrearEvento=tk.Button(self.contenedorForm, text="Agregar Evento", command=self.setEvento,
                  padx=5, pady=5,font=self.fuenteDelComponente,bg=self.colorBotones);
        self.botonCrearEvento.grid(
            row=8, column=0, columnspan=4, sticky="snew");
        self.botonEditarEvento = tk.Button(
        self.contenedorForm, text="Editar", font=self.fuenteDelComponente, bg=self.colorBotones,
        command=self.modificarEvento);
        self.botonCancelarEdicion = tk.Button(self.contenedorForm, text="Cancelar Edicion",
                                              command=self.reestabecerBotonOriginal, font=self.fuenteDelComponente, bg="#CF6562")
    def setEvento(self):
        if(not self.comprobarEntrysVacios()):
            self.cargarEvento();            
            self.tablaEventos.agregarEventoATabla(self.evento);
        else:
            messagebox.showwarning(
                "Advertencia", "Existen entradas sin completar");

    def getEvento(self):
        return self.evento;

    def colocarRegistrosCargadosEnCampos(self,evento):
        fechaFormateadaADate = AdministradorDeFechas.cadenaDeFechaADate(
            evento["fecha"])
        fechaRecordatorioFormateada = AdministradorDeFechas.cadenaDeFechaADate(
            evento["fechaRecordatorio"])

        self.tituloInput.delete(0, tk.END)
        self.tituloInput.insert(0, evento["titulo"])
        #self.fechaInput.delete(0, tk.END)
        self.fechaInput.set_date(fechaFormateadaADate)
        self.horaInput.delete(0, tk.END)
        self.horaInput.insert(0, evento["hora"])
        self.duracionInput.delete(0, tk.END)
        self.duracionInput.insert(0, evento["duracion"])

        if (evento["importancia"]):
            self.checkButtonInput.select()
        else:
            self.checkButtonInput.deselect()
        
        self.fechaRecordatorioInput.set_date(fechaRecordatorioFormateada)
        self.horaRecordatorioInput.delete(0, tk.END)
        self.horaRecordatorioInput.insert(0, evento["horaRecordatorio"])
        self.identificadoInput.delete(0, tk.END)
        self.identificadoInput.insert(0, evento["identificadorEvento"])
        self.descripcion.delete("1.0", 'end-1c')
        self.descripcion.insert(tk.INSERT, evento["descripcion"])

    def editarRegistro(self,evento,indice,indiceFilaTabla):
        print(evento);
        #Declaro los botones
        self.contenedorForm.configure(text="Modificar Evento")
        self.botonCrearEvento.grid_forget()
      
        #Para que los botones no se agregue el mismo componente en la misma posicion
        self.botonCancelarEdicion.grid_forget();
        self.botonEditarEvento.grid_forget();
        
        #Se guardan los indices para luego pasarlos a la clase de la tabla
        self.indiceElementoAEditar=indice;
        self.indiceFilaTabla=indiceFilaTabla;       

        self.colocarRegistrosCargadosEnCampos(evento);

        self.botonEditarEvento.grid(row=8, column=0, columnspan=2,sticky="we",padx=5);
        
        self.botonCancelarEdicion.grid(row=8, column=2, columnspan=2,sticky="we",padx=5);

    def reestabecerBotonOriginal(self):
        self.botonEditarEvento.grid_forget()
        self.botonCancelarEdicion.grid_forget()
        self.contenedorForm.configure(
            text="Agregar nuevo Evento")
        self.botonCrearEvento.grid(
            row=8, column=0, columnspan=4, sticky="snew")
    
    def comprobarEntrysVacios(self):
        lista=[self.tituloInput,self.horaInput,self.duracionInput,self.horaRecordatorio,self.identificadorEvento];
        for entry in lista:
            if(not entry.get()):
               return True; 
    def cargarEvento(self):
        self.evento = Evento(self.titulo.get(),
                             self.fechaInput.get_date(),
                             self.hora.get(),
                             self.duracion.get(),
                             self.fechaRecordatorioInput.get_date(),
                             self.horaRecordatorio.get(),
                             self.identificadorEvento.get(),
                             self.descripcion.get("1.0", 'end-1c'),
                             self.importancia.get())
    def modificarEvento(self):
        self.cargarEvento();
        print(self.evento);
        print(self.manejadorDeLaListaEventos.contenedorObjetos[self.indiceElementoAEditar]);
        self.manejadorDeLaListaEventos.contenedorObjetos[self.indiceElementoAEditar] = self.evento.getEventoComoDict();
        self.manejadorDeLaListaEventos.escribirEnFichero();
        self.tablaEventos.modificarFila(self.evento,self.indiceFilaTabla);
    
""" app = ComponenteEvento(tk.Tk())
app.grid();

app.mainloop();
 """