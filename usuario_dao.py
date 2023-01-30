from cursor_del_pool import Cursor
from usuario import Usuario
from logger_base import logger

class UsuarioDao:
    __SELECCIONAR='select * from usuarios order by id_usuario'
    __ACTUALIZAR='update usuarios set username=%s, password=%s where id_usuario=%s'
    __AGREGAR='insert into usuarios(username, password) values(%s,%s)'
    __ELIMINAR='delete from usuarios where id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with Cursor() as cursor:
            logger.debug(cursor.mogrify(cls.__SELECCIONAR))
            cursor.execute(cls.__SELECCIONAR)
            registros= cursor.fetchall()
            usuarios=[]
            for registro in registros:
                usuario=Usuario(registro[0],registro[1],registro[2])
                usuarios.append(usuario)
            #usuario es una lista de objetos.
            return usuarios
        

    @classmethod
    def actualizar(cls,usuario):#usuario: objeto de entidad Usuario
        with Cursor() as cursor:
            logger.debug(cursor.mogrify(cls.__ACTUALIZAR))
            valores=(usuario.get_username(),usuario.get_password(),usuario.get_id_usuario())
            cursor.execute(cls.__ACTUALIZAR,valores)
            return cursor.rowcount

    @classmethod
    def agregar(cls,usuario):#usuario: objeto de entidad Usuario
        with Cursor() as cursor:
            logger.debug(cursor.mogrify(cls.__AGREGAR))
            valores=(usuario.get_username(),usuario.get_password())
            cursor.execute(cls.__AGREGAR,valores)
            return cursor.rowcount

    @classmethod
    def eliminar(cls,usuario):#usuario: objeto de entidad Usuario
        with Cursor() as cursor:
            logger.debug(cursor.mogrify(cls.__ELIMINAR))
            valores=(usuario.get_id_usuario(),)
            cursor.execute(cls.__ELIMINAR,valores)
            return cursor.rowcount