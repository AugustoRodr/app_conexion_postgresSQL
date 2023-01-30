from conexion import Conexion
from logger_base import logger

class Cursor:
    def __init__(self):
        self.__cursor=None
        self.__conn=None

    def __enter__(self):
        logger.debug('Inicio de with __enter__()')
        self.__conn=Conexion.obtenerConexion()
        self.__cursor=self.__conn.cursor()
        return self.__cursor
    
    def __exit__(self,exception_type, exception_value, exception_traceback):
        logger.debug('Se ejecuta metodo __exit__()')
        if exception_value:
            self.__conn.rollback()
            logger.debug(f'Ocurrio una excepcion: {exception_value}')
        else:
            self.__conn.commit()
            logger.debug('Commit de la transaccion')
        self.__cursor.close()
        # REGRESO la conexion, NO la cierro
        Conexion.liberarConexion(self.__conn)