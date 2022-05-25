from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# se crea un objetos de tipo Club 
club1 = Club(nombre="Barcelona", deporte="Fútbol", \
        fundacion=1920)

# Se crean objeto de tipo Jugador
jugador1 = Jugador(nombre ="Damian Diaz", dorsal=10, posicion="mediocampo", \
        club=club1)

archivo1 = open("data/datos_clubs.txt","r")
archivo2 = open("data/datos_jugadores.txt", "r")

registros = archivo1.readlines();
registros2 = archivo2.readlines();

for r in registros2:
        nombre = r.split(";")[3]
        dorsal = r.split(";")[2] 
        posicion = r.split(";")[1]
        cl = session.query(Club).filter_by(nombre = r.split(";")[0]).one()
        jugar = Jugador (nombre = nombre, dorsal = dorsal, posicion=posicion, club = cl)
        session.add(jugar)

session.commit()



