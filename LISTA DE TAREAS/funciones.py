from tkinter import *
from tkinter.messagebox import *
import orm
from Tablas.Lista_tareas import Lista_tareas
#creamos nuestra base de datos
db = orm.SQLiteORM("Lista_tareas")
db.crear_tabla(Lista_tareas)
#funcion limpiar

def limpiar(ventana):
    ventana.tarea_texto.delete(0,END)
    ventana.fecha.delete(0,END)
    ventana.descripcion.delete(0,END)
    ventana.tarea_texto.focus()

def nuevo(ventana):
    tarea = ventana.tarea_texto.get()
    fecha = ventana.fecha.get()
    descripcion = ventana.descripcion.get()
    date = {
        "Tarea":tarea,
        "Fecha":fecha,
        "Descripcion":descripcion
    }
    db.insertarUno('Tareas',date)
    showinfo(title='save', message='nuevo registro agregado')
    #nuevo
    id = db.mostrar('Tareas', where=f'Tarea="{tarea}"')[0][0]
    print(id)
    ventana.tabla_datos.insert('',END, text=id, values=(tarea,fecha,descripcion))
    limpiar(ventana)
#eliminar 
def eliminar(ventana):
    elemento_eliminar = ventana.tabla_datos.selection()
    dato = ventana.tabla_datos.item(elemento_eliminar)['text'] #sirve para mostrar el registro seleccionado
    ventana.tabla_datos.delete(elemento_eliminar)
    db.eliminar('Tareas',where=f'id= "{dato}"')
    #db.eliminar('Usuarios',where='Nombre="ggh"')
    showwarning(title='Delete', message='registro eliminado')

def actualizar(ventana):
    if ventana.nombre_texto.get()=='':
        showerror(title='error', message='que va actualizar si noy nada')
    else:
        nombre = ventana.nombre_texto.get()
        apellidos = ventana.apellido_texto.get()
        celular = ventana.celular_texto.get()
        elemento_actualizar = ventana.tabla_datos.selection()
        date = ventana.tabla_datos.item(elemento_actualizar)['text']
        mensaje = askyesno(title='actualizar', message='estas seguro que deseas actulizar esta hvda')
        if mensaje == True:
            limpiar(ventana)
            update = {
                'Nombre':nombre,
                'Apellido':apellidos,
                'Celular':celular
                }
            ventana.tabla_datos.selection_remove(elemento_actualizar)
            db.actualizar('Usuarios',update,where=f'id={date}')
            return ventana.tabla_datos.item(elemento_actualizar,text=date, values=(nombre,apellidos,celular))
        else:
            showinfo(title='no actualizo', message='no esta seleccionado')
            ventana.tabla_datos.selection_remove(elemento_actualizar)

        
def doble_clic(ventana,event):
    elemento_actualizar=ventana.tabla_datos.selection()
    captura_datos = ventana.tabla_datos.item(elemento_actualizar)
    mensaje = askyesno(title='actualizar', message='desde el registro')
    if mensaje == True:
        nombre = captura_datos['values'][0]
        apellidos = captura_datos['values'][1]
        celulular = captura_datos['values'][2]
        ventana.nombre_texto.insert(0,nombre)
        ventana.apellido_texto.insert(0,apellidos)
        ventana.celular_texto.insert(0,celulular)
    else:
        showinfo(title='actualizar',message='ningún registro seleccionado para actualizar')
        ventana.tabla_datos.selection_remove(elemento_actualizar)