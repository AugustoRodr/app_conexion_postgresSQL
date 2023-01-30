# Responsabilidades
# contiene el menu con las 5 opciones

from usuario_dao import UsuarioDao
from usuario import Usuario
from logger_base import logger

validacion=True
while validacion:
    print('MENU')
    print('1) Listar usuarios\n2) Agregar usuario\n3) Actualizar usuario\n4) Eliminar usuario\n5) Salir')
    opcion=input('Ingrese una de las opciones (1-5): ')
    if opcion=='1':
        usuarios= UsuarioDao.seleccionar()
        for usuario in usuarios:
            logger.debug(usuario)
        
    elif opcion=='2':
        u_name=input('Ingrese el Username: ')
        p_word=input('Ingrese el password: ')
        usuario= Usuario(username=u_name, password=p_word)
        registro_insertado= UsuarioDao.agregar(usuario)
        logger.debug(f'Registros insertados: {registro_insertado}')

    elif opcion=='3':
        u_name=input('Ingrese el Username: ')
        p_word=input('Ingrese el password: ')
        id_user=int(input('Ingrese el id del registro a actualizar: '))
        usuario= Usuario(id_usuario=id_user, username=u_name, password= p_word)
        registro_actualizado= UsuarioDao.actualizar(usuario)
        logger.debug(f'Registros actualizados: {registro_actualizado}')

    elif opcion=='4':
        id_user=int(input('Ingrese el id del registro a eliminar: '))
        usuario= Usuario(id_usuario=id_user)
        registro_eliminado= UsuarioDao.eliminar(usuario)
        logger.debug(f'Registros eliminados: {registro_eliminado}')

    elif opcion=='5':
        validacion=False

print('\nGracias por usar esta app.')