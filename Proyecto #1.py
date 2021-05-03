#Sistema de reservación de boletos.

"""
Nombre del programa: Sistema de reservación de boletos.
Entradas: Este programa como base recibirá un menú de opciones(Opciones administrativas, Opciones de usuario normal y Salir).
              Menú de Opciones

              3 - Opciones administrativas

              4 - Opciones de usuario normal

              4.4 - Salir
              
            3 - Opciones administrativas: Para acceder a este apartado, recibirá una clave de acceso para habilitar la función(Menú administrativo) y este mismo
              mostrará un menú llamado "Menú Administrativo" (Gestión de empresas, Gestión de transporte por empresa, Gestión de viaje,
              Consultar historial de reservaciones, Estadísticas de viaje).

              Menú Administrativo

              3.1 - Gestión de empresas

              3.2 - Gestión de transporte por empresa

              3.3 - Gestión de viaje

              3.4 - Consultar el historial de reservaciones

              3.5 - Estadísticas de viajes

                  3.1 - Gestión de empresas: Recibirá una Cédula jurídica, Nombre y Ubicación(Dirección de la empresa)
                                             con el fin de dar un mantenimiento a las empresas.

                        Gestión de empresas

                        Cédula Jurídica:

                        Nombre:

                        Ubicación:

                  3.2 - Gestión de transporte por empresa: Recibirá una Placa, Marca, Modelo, Año, Empresa,
                                                           Cantidad de asientos clase VIP, clase normal y clase económica
                                                           con el fin de dar mantenimiento al transporte.
                                                           
                        Gestión de transporte por empresa

                        Placa:

                        Marca:

                        Modelo:

                        Año:

                        Empresa:

                        Cantidad de asientos clase VIP:

                        Cantidad de asientos clase normal:

                        Cantidad de asientos clase económica:

                  3.3 - Gestión de viaje: Recibirá un Número de viaje(Este es generado automáticamente), Ciudad de salida, Fecha y hora de salida,
                                          Ciudad de llegada, Fecha y hora de llegada, Empresa y transporte,
                                          Monto del asiento clase VIP, Monto del asiento clase normal, Monto del asiento clase económica, esto
                                          con el fin de registrar viajes.

                        Gestión de viaje

                        Número de viaje:

                        Ciudad de salida:

                        Fecha y hora de salida:

                        Ciudad de llegada:

                        Fecha y hora de llegada:

                        Empresa y transporte:

                        Monto del asiento clase VIP:

                        Monto del asiento clase normal:

                        Monto del asiento clase económica:

                  3.4 - Consultar el historial de reservaciones: Mostrar una lista de las reservaciones generadas por el sistema.

                        Historial

                        Identificador:

                        Nombre de la persona que reserva:

                        Número de viaje:

                        Fecha y hora de la reservación:

                        Empresa, transporte:

                        Lugar, fecha y hora de salida:

                        Lugar, fecha y hora de llegada:

                        Cantidad de asientos reservados en clase VIP, clase normal, clase económica:

                        Monto de reservación:

                  3.5 - Estadísticas de viajes: Seleccionar un viaje y mostrar los siguientes detalles:

                        Número de viaje:

                        Empresa transporte:

                        Lugar, fecha y hora de salida:

                        Lugar, fecha y hora de llegada:

                        Cantidad de asientos clase VIP reservados y asientos clase VIP disponibles:

                        Cantidad de asientos normal reservados y asientos normal disponibles:

                        Cantidad de asientos económico reservados y asientos económico disponibles:

                        Costo por boleto vip, normal y económico:
 
                        Monto recaudado por el viaje:

            4 - Opciones generales: Ingresar por medio del menú principal y por ende, habilitar demás funciones(Menú General) "Consulta de viajes,
                Reservación de viaje, Cancelación de reservación, Salir".

                        4.1 - Cancelación de viajes

                        4.2 - Reservación de viaje

                        4.3 - Cancelación de reservación

                        4.4 - Salir

                      4.1 - Consulta de viajes: Mostrar una lista de viajes de cada viaje.
                            Por cada viaje indicar lo solicitado(Número de viaje, Ciudad de salida, Fecha y hora de salida, Ciudad de llegada,
                            Fecha y hora de llegada, Empresa y transporte, Monto clase VIP, Monto clase normal, Monto clase económica).

                            Consulta de viajes

                            Número de viaje:

                            Ciudad de salida:

                            Fecha y hora de salida:

                            Ciudad de llegada:

                            Fecha y hora de llegada:

                            Empresa y transporte:

                            Monto clase VIP:

                            Monto clase normal

                            Monto clase económica:

                      4.2 - Reservación de viaje: Mostrar y escoger el diferente tipo de viaje(Son distintas opciones, por lo cual mostrará el Número de Viaje,
                            Empresa, Lugar de salida y llegada y las fechas). Luego indicar el nombre, La cantidad de espacios a reservar en clase vip, normal y
                            económica(Se deberá reservar al menos un asiento en total. Se le entregará un comprobante (Se mostrará en pantalla,
                            no debe exportarse ni imprimir) al cliente con la siguiente información: Identificador de la reserva(Generado automáticamente),
                            Nombre de la persona que reserva, Fecha y hora de de la reservación(capturado del sistema), Empresa, Transporte,
                            Lugar, fecha y hora salida, lugar, fecha y hora llegada, Cantidad de asientos reservados en clase vip, clase normal y clase económica y
                            Monto de reservación (calcular según cantidad, tipos y montos de asientos).

                      4.3 - Cancelación de reservación: Ingresar el identificador de la reserva.

                      4.4 - Salir: Salir del programa.
                                        
Salidas: Retornar un Menú Principal donde se encuentren las Opciones Administrativas, Opciones de usuario normal y Salir.

                3 - Opciones administrativas: Retornar un Menú Administrativo donde se encuentren todas las funcionalidades que tiene este apartado
                                              (Gestión de empresas, Gestión de transporte por empresa, Gestión de viaje, Consultar historial de reservaciones,
                                              Estadísticas de viaje).

                      3.1 - Gestión de empresas: Dar mantenimiento a las empresas (Cédula jurídica, Nombre, Ubicación(Dirección del negocio).

                      3.2 - Gestión de transporte por empresa: Dar mantenimiento a los transportes que poseen las empresas(Placa, Marca, Modelo, Año,
                                                               Empresa, Cantidad de asientos clase VIP, clase normal y clase económica).

                      3.3 - Gestión de viaje: Pemitir registrar viajes(Número de viaje(generado automáticamente), Ciudad de salida, Fecha y hora de salida,
                                              Ciudad de llegada, Fecha y hora de llegada, Empresa y transporte(Seleccionar de la lista existente pertenecientes
                                              a la empresa), Monto clase VIP, monto clase normal y monto clase económica).

                      3.4 - Consultar el historial de reservaciones: Mostrar una lista de reservaciones generadas en el sistema. Por cada reservación mostrar
                                                                     (Identificador, Nombre de la persona que reserva, Número de viaje, Fecha y hora de la reservación,
                                                                     Empresa, transporte, Lugar fecha y hora de salida, Lugar fecha y hora de llegada,
                                                                     Cantidad de asientos reservados VIP, clase normal, clase económica, Monto de reservación).

                      3.5 - Estadísticas de viaje: Seleccionar un viaje y mostrar el siguiente detalle(Número de viaje, Empresa, transporte,
                                                   Lugar fecha y hora de salida, Lugar, fecha y hora de llegada, Cantidad de asientos clase VIP reservados y asientos
                                                   clase VIP disponibles, Cantidad de asientos normal reservados y asientos normal disponibles,
                                                   Cantidad de asientos económico reservados y asientos económico disponibles,
                                                   Costo por boleto vip, normal y económico, Monto recaudado por el viaje).

                4. Opciones generales: Retornar el Menú General(Consulta de viajes, Reservación de viaje, Cancelación de reservación, Salir).

                      4.1 - Consulta de viajes: Mostrar una lista de los viajes. Por cada viaje retornar el Número de viaje, Ciudad de salida, Fecha y hora de salida,
                                                Ciudad de llegada, Fecha y hora de llegada, Empresa y transporte, Monto clase VIP, monto clase normal y
                                                monto clase económica.

                      4.2 - Reservación de viaje: Seleccionar el viaje que desea y luego indicar; El nombre, La cantidad espacios a reservar en clase VIP,
                                                  normal y económica, Identificador de la reserva(generado automáticamente), Nombre de la persona que reserva,
                                                  Fecha y hora de la reservación(capturadas del sistema), Empresa, Transporte,
                                                  Lugar, fecha y hora salida, lugar, fecha y hora llegada,
                                                  Cantidad de asientos reservados en clase vip, clase normal y clase económica y
                                                  Monto de reservación (calcular según cantidad, tipos y montos de asientos).

                                                  Nombre:

                                                  Cantidad de espacios a reservar en clase VIP, normal y económica:

                                                  Identificador de la reserva(Se genera automáticamente):

                                                     Nombre de la persona que reserva:

                                                     Fecha y hora de la reservación(Se captura del sistema):

                                                     Empresa:

                                                     Transporte:

                                                     Lugar, fecha y hora salida. Lugar, fecha y hora llegada:

                                                     Cantidad de asientos reservados en clase vip, clase normal y clase económica:

                                                     Monto de reservación:
                                                     
                      4.3 - Cancelación de reservación: Cancelar la reserva del viaje.

                      4.4 - Salir: Salir del programa.

Restricciones: 3 - Opciones generales: Ingresar al Menú Principal por medio de una clave de acceso que debe de estar generada y guardada en el disco.

                      3.1 - Gestión de empresas: Debe permitir incluir, eliminar, o modificar empresas, además de mostrarlas. La información que debe
                                                 almacenar por empresa debe ser; Cédula jurídica, Nombre y Ubicación(Dirección del negocio).
                                                 No pueden existir empresas con la misma cédula y no pueden eliminarse empresas que hayan sido asociadas
                                                 con algún transporte.

                      3.2 - Gestión de transporte por empresa: Debe permitir incluir, eliminar o modificar transporte, además de mostrarlos.
                                                               La información que se debe almacenar por transporte será: Placa, Marca, Modelo, Año,
                                                               Empresa(Esta seleccionarla de la lista existente del punto 3.1),
                                                               Cantidad asientos clase vip, clase normal y clase económica. 

                                                               No pueden existir dos transportes con la misma matrícula y no pueden eliminarse transportes
                                                               que estén registrados en un viaje.

                      3.3 - Gestión de viaje: Debe permitir registrar viajes, se debe permitir incluir, eliminar o modificar viajes, además de mostrarlos.
                                              La información que se debe almacenar por viaje será:
                                              Número de viaje(Generado automáticamente), Ciudad de salida,
                                              Fecha y hora de salida, Ciudad de llegada, Fecha y hora de llegada, Empresa y transporte(Seleccionar de la lista
                                              existente pertenecientes a la empresa seleccionada), Monto asiento clase VIP, monto clase normal y monto clase económica.

                      3.4 - Consultar historial de reservaciones: Mostrar una lista de las reservaciones generadas en el sistema. Por cada reservación debe mostrar
                                                                  lo siguiente:

                                                                  Identificador:

                                                                  Nombre de la persona que reserva:

                                                                  Número de viaje:

                                                                  Fecha y hora de la reservación:

                                                                  Empresa, transporte:

                                                                  Lugar, fecha y hora de salida:

                                                                  Lugar, fecha y hora de llegada:

                                                                  Cantidad de asientos reservados en clase VIP, clase normal y clase económica:

                                                                  Monto de reservación:

                                                                  Toda la información anterior se debe filtrar por:

                                                                  Rango de fecha de salida:

                                                                  Rango de fecha de llegada:

                                                                  Rango de fecha de la reservación:

                                                                  Lugar de salida y llegada:

                                                                  Para la filtración de la información, se debe implementar un menú para seleccionar el tipo de filtro.

                       3.5 - Estadísticas de viaje: Se debe selecionar un viaje(Mostrar al usuario los existentes).
                                                    Por ende, mostrar los siguientes detalles:

                                                    Número de viaje:

                                                    Empresa, transporte:

                                                    Lugar, fecha y hora de salida:

                                                    Lugar, fecha y hora de llegada:

                                                    Cantidad de asientos clase vip reservados y asientos clase vip disponibles:

                                                    Cantidad de asientos normal reservados y asientos normal disponibles:

                                                    Cantidad de asientos económico reservados y asientos económico disponibles:

                                                    Costo por boleto vip, normal y económico:

                                                    Monto recaudado por el viaje:

                4 - Opciones Generales: Ingresar únicamente por medio del Menú Principal y se deben habilitar las siguientes funcionalidades del Menú General:

                                        Consulta de viajes:

                                        Reservación de viaje:

                                        Cancelación de reservación:

                                        Salir:

                        4.1 - Consulta de viajes: Mostrar una lista de los viajes. Por cada viaje debe mostrar lo siguiente:

                                        Número de viaje:

                                        Ciudad de salida:

                                        Fecha y hora de salida:

                                        Ciudad de llegada:

                                        Fecha y hora de llegada:

                                        Empresa y transporte:

                                        Monto clase VIP, monto clase normal y monto clase económica:

                                        Se debe poder filtrar la información por:

                                        Empresa:

                                        Lugar de salida:

                                        Lugar de llegada:

                                        Rango de fecha de salida:

                                        Rango de fecha de llegada:

                                        Para la filtración de la información, se debe implementar un menú para seleccionar el tipo de filtro.


                         4.2 - Reservación de viaje: Se debe seleccionar el viaje una vez que se haya realizado la reservación(Mostrar al usuario información de número
                                                     de viaje, empresa, lugar de salida y llegada, y fechas). El usuario selecciona uno y luego indicar lo siguiente:

                                                     Nombre:

                                                     Cantidad de espacios a reservar en clase VIP, normal y económica:
                                                     En el caso de la cantidad de espacios a reservar en clase VIP, normal y económica; se debe reservar al menos un
                                                     asiento y se le entregará un comprobante en la pantalla al usuario con la siguiente información:

                                                     Identificador de la reserva(Se genera automáticamente):

                                                     Nombre de la persona que reserva:

                                                     Fecha y hora de la reservación(Se captura del sistema):

                                                     Empresa:

                                                     Transporte:

                                                     Lugar, fecha y hora salida. Lugar, fecha y hora llegada:

                                                     Cantidad de asientos reservados en clase vip, clase normal y clase económica:

                                                     Monto de reservación(Calcular el monto de la reservación):

                                                     Se debe validar que para la cantidad de asientos reservados en cada categoría existan espacios disponibles.
                                                     Esta funcionalidad alimenta el registro de reservaciones que se consulta en la parte administrativa.

                         4.3 - Cancelación de reservación: Se debe indicar el identificador de la reserva y se debe eliminar el sistema de la reservación con todos los
                                                           respectivos datos, también debe liberar los asientos reservados.

                         4.4 - Salir: Salir del programa, debe almacenar toda la información para que sean datos persistentes.
                                      Se debe mantener para los siguientes usos del programa.
"""

def menuPrincipal():
    print("3 - Opciones administrativas.")
    print("4 - Opciones de usuario normal.")
    print("4.4 - Salir.")
    opciones = input("")
    
    if (opciones == '3'):
        print("3.1 - Gestión de empresas.")
        print("3.2 - Gestión de transporte por empresa.")
        print("3.3 - Gestión de viaje.")
        print("3.4 - Consultar el historial de reservaciones.")
        print("3.5 - Estadísticas de viaje.")
        opciones == input('')

        if (opciones == '3.1'):
            print("Gestión de empresas.")
            cedulaJuridica = int(input("Cédula jurídica: "))
            nombre = str(input("Nombre: "))
            ubicacion = str(input("Ubicación del negocio: "))

        elif (opciones == '3.2'):
            print("Gestión de transporte por empresa.")
            placa = str(input("Placa: "))
            marca = str(input("Marca: "))
            modelo = str(input("Modelo: "))
            año = str(input("Año: "))
            empresa = str(input("Empresa: "))
            cantidadDeAsientosVIP = int(input("Cantidad de asientos clase VIP: "))
            cantidadDeAsientosNormal = int(input("Cantidad de asientos clase normal: "))
            cantidadeAsientosEconómica = int(input("Cantidad de clase económica: "))

        elif (opciones == '3.3'):
            print("Gestión de viaje.")
            numeroDeViaje = print("")
            ciudadDeSalida = str(input("Ciudad de salida: "))
            fechaYhoraDeSalida = str(input("Fecha y hora de salida: "))
            ciudadDellegada = str(input("Ciudad de llegada: "))
            fechaYhoraDellegada = str(input("Fecha y hora de llegada: "))
            empresaYtransporte = print("")
            precioDeAsientosVIP = str(input("Monto de asientos clase VIP: "))
            precioDeAsientosNormal = str(input("Monto de asientos clase normal: "))
            precioDeAsientosEconomica = str(input("Monto de asientos clase económica: "))

        elif (opciones == '3.4'):
            print("Consultar el historial de reservaciones.")
            identificador = print("Identificador: ")
            nombreReservador = print("Nombre de la persona que reserva: ")
            numeroDeViaje = print("Número de viaje: ")
            fechaYhoraDeLaReservacion = print("Fecha y hora de la reservación: ")
            empresa,transporte = print("Empresa, transporte: ")
            lugar,fechaYhorasalida = print("Lugar, fecha y hora de salida: ")
            lugar,fechaYhorallegada = print("Lugar, fecha y hora de llegada: ")
            cantidadDeAsientosReservadosVIP = print("Cantidad de asientos reservados en clase VIP: ")
            cantidadDeAsientosReservadosNormal = print("Cantidad de asientos reservados en clase normal: ")
            cantidadDeAsientosReservadosEconomica = print("Cantidad de asientos reservados en clase económica: ")
            montoDeReservación = print("Monto de resevación: ")

        elif (opciones == '3.5'):
            print("Estadísticas de viajes.")
            numeroDeViaje = print("Número de viaje: ")
            empresa,transporte = print("Empresa y transporte: ")
            lugar,fechaYhorasalida = print("Lugar, fecha y hora salida: ")
            lugar,fechaYhorallegada = print("Lugar, fecha y hora llegada: ")
            cantidadDeAsientosVIP = print("Cantidad de asientos clase VIP reservados y asientos clase VIP disponibles: \n")
            cantidadDeAsientosNormal = print("Cantidad de asientos clase normal reservados y asientos clase normal disponibles: \n")
            cantidadDeAsientosEconomico = print("Cantidad de asientos clase económico reservados y asientos clase económico disponibles: \n")
            costoBoletoVIP = print("Costo por boleto clase VIP: ")
            costoBoletoNormal = print("Costo por boleto clase normal: ")
            costoBoletoEconomico = print("Costo por boleto clase económico: ")
            recaudacion = print("Monto recaudado por el viaje: ")

        else:
            return print("Error: Este dígito no es reconocido por el sistema.")
    elif (opciones == '4'):
        print("4.1 - Consulta de viajes.")
        print("4.2 - Reservación de viaje.")
        print("4.3 - Cancelación de reservación.")
        print("4.4 - Salir")
        opciones = input("")

        if (opciones == '4.1'):
            print("Consulta de viajes")
            print("Número de viaje: ")
            print("Ciudad de salida: ")
            print("Fecha y hora de salida: ")
            print("Ciudad de llegada: ")
            print("Fecha y hora de llegada: ")
            print("Empresa y transporte: ")
            print("Monto clase VIP: ")
            print("Monto clase normal: ")
            print("Monto clase económica: ")

        if (opciones == '4.2'):
            print("Reservación de viaje.")
            nombre = str(input("Nombre: "))
            espaciosPorReservar = str(input("Cantidad de espacios a reservar: \nClase VIP: \nClase normal: \nClase económica: "))
            identificador = print("")
            nombreDeLaPersonaReservadora = str(input("Nombre de la persona que reserva: "))
            fechaYhoraDeLaReservación = print("")
            empresa = str(input("Empresa: "))
            transporte = str(input("Transporte: "))
            fechasYhoras = str(input("Lugar, fecha y hora de salida: \nLugar, fecha y hora de llegada"))
            asientosReservadosVIP = str(input("Cantidad de asientos reservados clase VIP: "))
            asientosReservadosNormal = str(input("Cantidad de asientos clase normal: "))
            asientosReservadosEconomica = str(input("Cantidad de asienstos clase económica: "))
            montoDeReservación = print("")

        if (opciones == '4.3'):
            print("Cancelación de reservación")
            identificador = str(input("Identificador: "))

        if (opciones == '4.4'):
            return print("Hasta pronto.")
