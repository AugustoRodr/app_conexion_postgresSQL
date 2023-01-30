from psycopg2 import pool
from logger_base import logger
import sys

class Conexion:
    __USER='postgres'
    __PASSWORD='admin'
    __HOST='localhost'
    __DATABASE='test_db'
    __PORT='5432'
    __MIN=1
    __MAX=5
    __POOL=None

    @classmethod
    def obtenerPool(cls):
        if cls.__POOL==None:
            try:
                cls.__POOL= pool.SimpleConnectionPool(cls.__MIN,cls.__MAX,
                                                    user=cls.__USER,
                                                    password=cls.__PASSWORD,
                                                    host=cls.__HOST,
                                                    database=cls.__DATABASE,
                                                    port=cls.__PORT)
                logger.debug(f'Creacion de pool exitosa: {cls.__POOL}')
                return cls.__POOL
            except Exception as e:
                logger.error(f'Error al crear el pool de conexion: {e}')
                sys.exit()
        else:
            return cls.__POOL
    
    @classmethod
    def obtenerConexion(cls):
        conexion= cls.obtenerPool().getconn()
        logger.debug(f'Conexion obtenida del pool: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls,conexion):
        cls.obtenerPool().putconn(conexion)
        logger.debug(f'Conexion regresada al pool: {conexion}')
        logger.debug(f'Estado del pool: {cls.__POOL}')
    
    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()
        logger.debug(f'Conexiones al pool cerradas: {cls.__POOL}')






if __name__=='__main__':
    conexion1=Conexion.obtenerConexion()

    Conexion.liberarConexion(conexion1)

    Conexion.cerrarConexiones()