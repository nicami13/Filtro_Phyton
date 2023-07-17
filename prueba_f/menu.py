import os 
import json
import core
import os

diccCita={'data':[]}
def cargaCita():
    global diccCita
    if (core.checkFile('citas.json')):
        diccCita=core.LoadInfo('citas.json')
    else:
        core.crearInfo('citas.json',diccCita)

    print()
if __name__=='__main__':
    cargaCita()
    while True:
        
         
            f=True
            while f:
                    os.system('clear')
                    print("╔═══════════════════════════════════╗")
                    print("║        CLINICA BUENAMUERTE        ║")
                    print("╚═══════════════════════════════════╝")
                    print(' 1.Ingresar cita.\n','2.Buscar cita.\n','3.Edicion de cita\n','4.Cancelacion de cita\n','0.salir.')
                    try:
                        op=int(input('ingresar opcion de lo que desea realizar: '))
                        os.system('clear')
                        break

                    except:
                        os.system('clear')
                        print(' OPCION INVALIDA.\n','Talvez ingresaste una letra(a,b,c) o algun simbolo(%,",#)')
                        input('presione enter para continuar...')

                        os.system('clear')



            if int(op)==1:
                
                cita={
                'paciente':'',
                'fecha de la cita':'',
                'hora de la cita':'',
                'motivo de consulta':''
                }
                while True:
                    print("╔═══════════════════════════════════╗")
                    print("║         INGRESO DE CITAS          ║")
                    print("╚═══════════════════════════════════╝")
                    try:
                        cita['paciente']=input('ingresar el nombre del paciente: ')
                        os.system('clear')
                        break
                    except:
                        os.system('clear')
                        print(' DATO INVALIDA.\n','Talvez ingresaste algun simbolo(%,",#) o algun valor invalido')
                        input('presione enter para continuar...')
                        os.system('clear')
                while True:
                    try:
                        print('ingrear la fecha de la siguiente manera DD/MM/AAAA')
                        cita['fecha de la cita']=input(' fecha de la cita: ')
                        os.system('clear')
                        a=cita['fecha de la cita'].count('/')
                        if(a!=2):
                            print('Fecha ingresada de manera incorecta.')
                            os.system('clear')
                            input('presiona enter para ingresar fecha nuevamente...')
                            os.system('clear')
                            print('Recuerda que debe ser de la siguiente manera DD/MM/AAAA')
                            cita['fecha de la cita']=input(':')
                            os.system('clear')
                        break
                    except:
                        os.system('clear')
                        print(' DATO INVALIDA.\n','Talvez ingresaste algun simbolo(%,",#) o algun valor invalido')
                        input('presione enter para continuar...')
                        os.system('clear')
                while True:
                    try:
                        print('ingresar hora con sistema 24H de la siguiente manera HH(hora):mm(minutos).')
                        cita['hora de la cita']=input('hora de la cita: ')        
                        b=cita['hora de la cita'].count(':')
                        os.system('clea r')

                        if b!=1:
                            print('hora ingresada de manera incorrecta.')
                            print('recuerda que debe ser de la siguiente manera HH(horas):mm(minutos)')
                            cita['hora de la cita']=input(':')
                        break
                    except:
                        os.system('clear')
                        print(' DATO INVALIDA.\n','Talvez ingresaste algun simbolo(%,",#) o algun valor invalido')
                        input('presione enter para continuar...')
                        os.system('clear')
                


                print('por favor da una pequeña descripcion del motivo de su consulta.')
                cita['motivo de consulta']=input('  :')

                diccCita['data'].append(cita)
                core.crearInfo('citas.json',cita)
    # 1. El programa debe tener un menú que permita al usuario seleccionar diferentes opciones:
    # agregar cita, buscar cita, modificar cita, cancelar cita y salir del programa.
    # 2. Cada cita médica debe tener los siguientes datos: nombre del paciente, fecha de la cita,
    # hora de la cita y motivo de la consulta.
    # 3. Al agregar una cita, el programa debe solicitar al usuario que ingrese los datos
    # correspondientes y luego guardar la cita en un archivo JSON.
    # 4. Al buscar una cita, el programa debe solicitar al usuario un criterio de búsqueda (por
    # ejemplo, nombre del paciente o fecha de la cita) y mostrar todas las citas que coincidan
    # con ese criterio.
    # 5. Al modificar una cita, el programa debe permitir al usuario seleccionar una cita de la lista
    # de citas y solicitar los nuevos datos para actualizarla en el archivo JSON.
    # 6. Al cancelar una cita, el programa debe permitir al usuario seleccionar una cita de la lista
    # de citas y eliminarla del archivo JSON.
    # 7. Al salir del programa, se deben guardar todos los cambios realizados en el archivo JSON
    # y mostrar un mensaje de despedida.
            if (int(op)==   2):
             t=True
             while t:
                print("╔═══════════════════════════════════╗")
                print("║         MENU DE BUSQUEDA          ║")
                print("╚═══════════════════════════════════╝")
                paciente=input('ingresar nombre del paciente: ')
                fecha=input('ingresar fecha:')
                for i,item in enumerate(diccCita['data']):
                   if item['paciente']==paciente and item['fecha de la cita']==fecha:

                       print('PACIENTE:',item['paciente'])
                       print('FECHA:',item['fecha de la cita'])
                       print('HORA:',item['hora de la cita'])
                       print('MOTIVO:',item['motivo de consulta'])
                       input('presiona enter para continuar...')
                       t=False

                   
                else:
                      print('NO SEA ENCONTRADO UNA CITA CON ESTOS DATOS')
                      input('presione enter para continuar...') 
                      os.system('clear')
                      t=False
                 
                    
               
            if (int(op)==3):
                
            
             while  True:
                try:
                     print("╔═══════════════════════════════════╗")
                     print("║        EDICION DE CITAS           ║")
                     print("╚═══════════════════════════════════╝")

                     for i,item in enumerate(diccCita['data']):
                        print(i,'NOMBRE PACIENTE:',item['paciente'],'FECHA:',item['fecha de la cita'])
                     a=input('ingresa la numeracion de la cita que desea editar: ')
                     cita_seleccionada=diccCita['data'][int(a)]
                     noma=cita_seleccionada['paciente']
                     feca=cita_seleccionada['fecha de la cita']
                     hora=cita_seleccionada['hora de la cita']
                     mota=cita_seleccionada['motivo de consulta']
                     break
                except:
                    os.system('clear')
                    print('Numeracion digitada invalida.')
                    input('presione enter para continuar...')
                    os.system('clear')
             os.system('clear')
             cita_seleccionada['paciente']=input('ingresar el nuevo nombre del paciente o presiona enter para omitir:')
             if cita_seleccionada['paciente']=='':
                     cita_seleccionada['paciente']=noma
             os.system('clear')

             cita_seleccionada['fecha de la cita']=input('ingresar nueva fecha de la cita o presiona enter para omitir: ')
             os.system('clear')
             if cita_seleccionada['fecha de la cita']=='':
                     cita_seleccionada['fecha de la cita']=feca

             a=cita_seleccionada['fecha de la cita'].count('/')
             if cita_seleccionada['fecha de la cita']!='' and a!=2:                    
                print('Fecha ingresada de manera incorecta.')
                os.system('clear')
                input('presiona enter para ingresar fecha nuevamente...')
                os.system('clear')
                print('Recuerda que debe ser de la siguiente manera DD/MM/AAAA')
                cita_seleccionada['fecha de la cita']=input(':')
                os.system('clear')

             cita_seleccionada['hora de la cita']=input('ingresa la nueva hora de la cita o presiona enter para omitir: ')
             os.system('clear')
             if cita_seleccionada['hora de la cita']=='':
                cita_seleccionada['hora de la cita']=hora
             b=cita_seleccionada['hora de la cita'].count(':')
             os.system('clear')

             if b!=1:
                print('hora ingresada de manera incorrecta.')
                print('recuerda que debe ser de la siguiente manera HH(horas):mm(minutos)')
                cita_seleccionada['hora de la cita']=input(':')
             os.system('clear') 
             cita_seleccionada['motivo de consulta']=input('ingresar el nuevo motivo de la cita o presiona enter para omitir:')
             if cita_seleccionada['motivo de consulta']=='':
                cita_seleccionada['motivo de consulta']=mota  
                diccCita['data'].append(cita_seleccionada)
            
            
             core.EditarData('citas.json',diccCita)
            
            if (int(op)==4):
                while True:
                    try:
                        print("╔═══════════════════════════════════╗")
                        print("║        CANCELACION DE CITAS       ║")
                        print("╚═══════════════════════════════════╝")
                        for i,item in enumerate(diccCita['data']):
                            print(i,'NOMBRE PACIENTE:',item['paciente'],'FECHA:',item['fecha de la cita'])
                        a=input('ingresa la numeracion de la cita que desea editar: ')
                        diccCita['data'].pop(int(a))
                        core.EditarData("citas.json",diccCita)
                    except:
                        os.system('clear')
                        print('Numeracion digitada invalida.')
                        input('presione enter para continuar...')
                        os.system('clear')

            if (int(op)==0):
             print('HASTA PRONTO :)')
             break
            if int(op)>4 or int(op)<0:
                 print('opcion invalida.')
                 input('presione enter para continuar...')

            


                   


                
        


