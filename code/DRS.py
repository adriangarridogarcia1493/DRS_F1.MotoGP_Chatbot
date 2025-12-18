# -*- coding: utf-8 -*-
"""
@data: Thu Oct 30 08:04:00 2025
@author: Adrián Garrido García
@descripcio: Chatbot DRS, especializado en Fórmula 1 y MotoGP.
"""

####### Variables, llistes, diccionaris #######################################
# variables
# definimos la salutacio
salutacio = "Holaaa"
# definimos el nom
nom = ""
#definimos la acción de seguir hablando, lo que sería el True, que nos sirve para poner parte del codigo en bucle
seguir_hablando = True

# llistes
#todas las respuestas de la pregunta principal hacia la F1
respuestas_f1 = ["f1", "formula 1", "formula", "fórmula"]
#todas las respuestas de la pregunta principal hacia la MotoGP
respuestas_mgp = ["motogp", "moto gp", "motos", "moto"]

# diccionaris
# las respuestas del chatbot hacia las anteriores opciones, F1 o MotoGP
resumen_temas = {
    "f1": "¡Perfecto! Pues hablemos de Fórmula 1",
    "motogp": "¡Perfecto! Vamos a hablar de MotoGP"
}

# Todas las bromas posibles, tanto de F1 como MotoGP
bromas = [
    "¿Por qué Verstappen nunca juega a las escondidas? Porque siempre lo encuentran en la pole jajaja",
    "Le preguntaron a un ingeniero de Ferrari si podían ir más rápido. Dijo: ‘Sí, pero solo cuando ya es demasiado tarde’ jajaja",
    "¿Qué hace un piloto de F1 cuando se aburre? Da una vuelta… y otra… y otra… Jajaja",
    "Dicen que en Ferrari son muy educados: siempre dejan pasar algunas oportunidades de ganar jajaja",
    "¿Por qué los mecánicos de Red Bull nunca pelean entre ellos? Porque todo lo resuelven en un pit stop jajaja",
    "Mi amigo dijo que su coche acelera como un F1: también desaparece cuando llueve jajaja",
    "¿Cómo sabes que un piloto novato está nervioso? Porque entra al box y se estaciona bien jajaja",
    "¿Por qué los pilotos nunca cuentan chismes? Porque todo lo que dicen corre demasiado jajaja",
    "En Ferrari implementaron un sistema anti-errores: consiste en no mirar la estrategia jajaja",
    "¿Por qué el Safety Car nunca se estresa? Porque sabe que siempre lo siguen jajaja",
    "Dicen que Alonso nunca llega tarde porque aunque este el último termina adelantando a todos jajaja",
    "Le pregunté a Alonso cuál es su superpoder y dijo: ‘Convertir cualquier tractor en un F1 jajaja",
    "¿Por qué Alonso nunca pierde en un laberinto? Porque encuentra el hueco por fuera jajaja",
    "Cuando Alonso dice ‘plan’, los demás equipos corren para averiguar cuál es jajaja",
    "Alonso sabe que empieza una nueva temporada cuando ya saca más rendimiento del coche del que debería jajaja",
    "¿Por qué los pilotos de MotoGP nunca tienen frío? Porque siempre van con el motor calentito jajaja",
    "Un piloto de MotoGP fue al psicólogo y le dijo: ‘Doctor, tengo demasiadas curvas en mi vida’ jajaja",
    "¿Qué hace un piloto cuando pierde el móvil? Toma la trazada ideal… hasta encontrarlo jajaja",
    "Dicen que en Cervera gastan poco en zapatillas: total, nunca caminan, siempre vuelan jajaja",
    "¿Por qué los pilotos de MotoGP no usan despertador? Porque siempre se despriertan para ver Moto3 jajaja",
    "¿Cuál es el peor enemigo de un piloto? Un mosquito… justo en la visera jajaja",
    "¿Por qué los mecánicos de MotoGP son tan optimistas? Porque siempre piensan que el próximo ajuste sí lo arregla todo jajaja",
    "Un fan dijo que quería sentir la velocidad de MotoGP… así que abrió la factura de la luz jajaja",
    "Dicen que Marc Márquez no necesita GPS porque siempre encuentra el límite jajaja",
    "¿Por qué Marc nunca siempre gana en los videojuegos? Porque hasta la consola sabe que nadie podría con él jajaja",
    "Le preguntaron a Marc su truco para adelantar y respondió: ‘Aparecer donde nadie lo espera’ jajaja",
    "¿Cómo sabes que Márquez está en forma? Porque hasta los pilotos se apartan por respeto jajaja",
    "Marc dijo que iba a tomarse el día con calma… y solo ganó la carrera, no hizo la vuelta rápida jajaja"
]

# Todas las predicciones posibles, tanto de F1 como MotoGP
predicciones = [
    "Carlos Sainz luchará por multiples podios este año",
    "Pedro Acosta ganará una carrera pronto",
    "Hamilton anunciará su retiro en 2026, Ferrari no le renovará jajaja",
    "Habrá lluvia en el próximo GP, se viene un carrerón"
    "Alonso vuelve al podio en una carrera en mojado",
    "Verstappen logra su 5º título en Abu Dabhi superando a los fracasados McLaren",
    "Un piloto de Mercedes chocará contra uno de los 5 primeros",
    "Ferrari fallará en la estrategia y cederá puntos a sus rivales",
    "Alex Márquez adelantará en la última curva a su hermano para ganar el gran premio",
    "Un rookie sorprende con victoria inesperada",
    "Ferrari vuelve a tener problemas en boxes",
    "Kimi Antonelli hace una remontada épica",
    "Norris se estrella contra el muro",
    "Newey hará que Alonso gane el 3r mundial",
    "Márquez salvará otra caída imposible",
    "Bezzequi pierde victoria por error",
    "Bagnaia vuelve a quejarse de la moto jajaja",
    "Martín logra el primer podio con la Aprilia",
    "Rossi sigue llorando en su casa",
    "La Aprilia y la KTM sorprende con ritmo constante",
    "Márquez vuelve a ser campeón el año que viene",
    "Una Honda o Yamaha logra podio inesperado",
    "Fernando Alonso al fin logra la ansiada 33"
]

####### Funcions ##############################################################
# Ahora definimos la función de saludar
def saludar():
    """Saluda al usuario y presenta el chatbot."""
    print(salutacio)
    print("Soy DRS, tu chatbot especializado en Fórmula 1 y MotoGP :)")
# Ahora definimos la función para obtener el nombre
def obtener_nombre():
    """Pide el nombre al usuario y devuelve la última palabra."""
    nom = input("¿¿¿Cómo te llamas amante del motor??? ")
# La siguiente linea de codigo nos ayuda a repartir la respuesta del usuario en palabras y escoge la ultima ya que suele ser el nombre
    nom = nom.split(" ")[-1]
    print("Perfecto" + " " + nom + " " + "encantado de conocerte!!!")
    print("Estoy aquí para llevarte directo a la pista con toda la información que necesitas: "
          "desde noticias, resultados y horarios, hasta análisis, curiosidades y estadísticas "
          "de tus pilotos y equipos favoritos.")
    print("¿Quieres saber quién hizo la pole, qué estrategia usaron en boxes o cómo va el campeonato?")
    print("Yo te lo cuento al instante. ¡Listo para activar el DRS!")
    return nom

# Aquí pregunta al usuario de que quiere hablar, después de escoger la opción "hablar"
def preguntar_tema(nom):
    """Pregunta al usuario de qué tema quiere hablar."""
    return input(nom + "," + " " + "¿De qué quieres hablar hoy, F1 o MotoGP? ").lower()

# ---- ACCIONES DE TEMA -------------------------------------------------------
#Ahora definimos la que anteriormente era acción principal del chatbot, ahora es una de muchas
# A continuación será la parte de F1
def hablar_f1(nom):
    """Todo tu bloque de respuestas de F1."""
    print(nom+ "," + " " + "¡Perfecto! Vamos a hablar de Fórmula 1")
# Eso sí, mantengo TODO el bloque de código actual de F1.
# Pimera pregunta, la del piloto:
    pilotof1 = input("¿De qué piloto de F1 te gustaría hablar" + " " + nom + "?").lower()
# Si el usuario quiere hablar de Alonso:
    if "alonso" in pilotof1 or "fernando" in pilotof1 or "nano" in pilotof1 or "don fernando alonso" in pilotof1:
        print ("¡¡¡Fernando Alonso me encanta!!! El Nano es un piloto español de Fórmula 1, nacido en Oviedo en 1981. Es considerado uno de los mejores conductores de su generación por su talento, inteligencia en carrera y determinación. Debutó en la F1 en 2001 y se convirtió en campeón del mundo con Renault en 2005 y 2006, siendo el piloto más joven en lograrlo en ese momento. A lo largo de su carrera ha competido con equipos como McLaren, Ferrari y Aston Martin, destacándose por su capacidad para exprimir al máximo cualquier coche. Su pasión, constancia y carisma lo han convertido en una leyenda del automovilismo.")
# Si el usuario quiere hablar de Sainz:
    elif "sainz" in pilotof1 or "carlos" in pilotof1 or "smooth operator" in pilotof1:
        print ("¡¡¡Que buen piloto!!! Carlos Sainz me gusta mucho, nacido en Madrid en 1994, es un piloto español de Fórmula 1 e hijo del campeón de rally Carlos Sainz. Debutó en 2015 con Toro Rosso (hoy Racing Bulls) y ha pasado por equipos como Renault, McLaren y Ferrari. Desde 2025 compite con Williams Racing, donde busca liderar el regreso del equipo británico a los primeros puestos de la parrilla.")
# Si el usuario quiere hablar de Verstappen:
    elif "verstappen" in pilotof1 or "max" in pilotof1 or "super max" in pilotof1:
        print ("¡¡¡Me encanta tu elección!!! Actualmente opino que Max és el mejor piloto de la parrilla, nacido en Bélgica en 1997 y criado en los Países Bajos. Debutó en 2015 con Toro Rosso y rápidamente ascendió a Red Bull Racing, con quienes ha ganado múltiples campeonatos mundiales. Conocido por su agresividad, velocidad y consistencia, Verstappen ha marcado una nueva era en la F1 dominando gran parte de las últimas temporadas.")
# Si el usuario quiere hablar de Antonelli:
    elif "antonelli" in pilotof1 or "kimi" in pilotof1:
        print ("¡¡¡Para mí el mejor rookie de este año jaja!!! Kimi Antonelli es un joven piloto italiano considerado una de las mayores promesas del automovilismo actual. Nacido el 25 de agosto de 2006, ha sido parte del programa de desarrollo y la academia de Mercedes desde muy temprana edad. Con un impresionante palmarés en karting y campeonatos como la Fórmula 4 Italiana y ADAC F4, ha demostrado un talento excepcional y madurez en pista. En 2024 dio el salto a la Fórmula 2 con el equipo Prema, y posteriormente se convirtió en piloto de Fórmula 1 gracias a Mercedes. Su estilo de conducción preciso y su enfoque profesional lo destacan como un nombre a seguir en los próximos años.")
# Si el usuario quiere hablar de Piastri:
    elif "piastri" in pilotof1 or "oscar" in pilotof1:
        print ("¡¡¡Gran piloto!!! Nacido en Melbourne en 2001, es un piloto australiano de Fórmula 1. Tras destacar en Fórmula Renault, F3 y F2, debutó en 2023 con McLaren y rápidamente se consolidó como uno de los jóvenes más prometedores de la parrilla, logrando victorias y podios, incluso és capaz de pelear por algún mundial")
# Si el usuario quiere hablar de Hülkenberg:
    elif "hülkenberg" in pilotof1 or "nico" in pilotof1:
        print ("¡¡¡Buen piloto veterano!!! Nico Hülkenberg, nacido en 1987 en Alemania, es un piloto de Fórmula 1 que debutó en 2010 con Williams. Ha competido para varios equipos y ganó las 24 Horas de Le Mans en 2015. Conocido por su constancia, logró su primer podio en F1 en 2025 y actualmente corre con Sauber.")
# Si el usuario quiere hablar de Bortoleto:
    elif "bortoleto" in pilotof1 or "gabriel" in pilotof1:
        print ("¡¡¡Que joven promesa!!! Gabriel Bortoleto, nacido en 2004 en Brasil, es un joven piloto de Fórmula 1 que debutó en 2025 con Sauber. Campeón de Fórmula 2 en 2024, se ha destacado por su rápida adaptación y se perfila como una de las grandes promesas del automovilismo brasileño.")
# Si el usuario quiere hablar de Colapinto:
    elif "colapinto" in pilotof1 or "franco" in pilotof1:
        print ("¡¡¡Vaya piloto boludo!!! Franco Colapinto, nacido en 2003 en Argentina, es un piloto de Fórmula 1 que debutó en 2024 con Williams. En 2025 se unió a Alpine como titular tras la salida de Jack Doohan, destacando por su rapidez y talento, y representando el regreso del automovilismo argentino a la F1.")
# Si el usuario quiere hablar de Leclerc:
    elif "leclerc" in pilotof1 or "charles" in pilotof1 or "il predestinato" in pilotof1:
        print ("¡¡¡Il predestinato de Ferrari!!! Charles Leclerc es un piloto monegasco de Fórmula 1 nacido en 1997. Debutó en 2018 y desde 2019 corre para Ferrari. Destaca por su velocidad, talento y determinación, siendo una de las grandes promesas del automovilismo.")
# Si el usuario quiere hablar de Russell:
    elif "russell" in pilotof1 or "george" in pilotof1:
        print ("El hombre invisible jaja, ¡¡¡que gran piloto!!! George Russell es un piloto británico de Fórmula 1 nacido en 1998. Debutó en 2019 con Williams y desde 2022 corre para Mercedes. Es reconocido por su consistencia, talento y gran potencial en la parrilla.")
# Si el usuario quiere hablar de Perez o Bottas:
    elif "perez" in pilotof1 or "checo" in pilotof1 or "sergio" in pilotof1 or "bottas" in pilotof1 or "valtteri" in pilotof1:
        print ("¡¡¡El veterano de Callidac!!! Vaya piloto, su nombre ya forma parte de la F1 siendo de los más veteranos en este siglo XXI. Deseando volverlo a ver el año que viene en las pistas, ¡¡¡estoy seguro que lo hará genial!!!")
# Si el usuario quiere hablar de Norris:
    elif "norris" in pilotof1 or "lando" in pilotof1:
        print ("¡¡¡Buen piloto la verdad!!! Lando Norris es un piloto británico de Fórmula 1 nacido en 1999. Debutó en 2019 con McLaren y se ha destacado por su velocidad y carisma dentro y fuera de las pistas aunque creo que no es muy regular, el talento lo tiene.")
# Si el usuario quiere hablar de Bearman:
    elif "bearman" in pilotof1 or "oliver" in pilotof1 or "oso" in pilotof1 or "hadjar" in pilotof1 or "isack" in pilotof1:
        print ("¡¡¡Vaya Rookie has escogido!!! Le veo un futuro prometedor a este piloto. Las pocas carreras que ha disputado en la categoria reina ya ha demostrado su gran talento, ¡¡¡Dale unos años y un buen coche y verás!!!")
# Si el usuario quiere hablar del resto de pilotos:
    elif "gasly" in pilotof1 or "pierre" in pilotof1 or "lawson" in pilotof1 or "liam" in pilotof1 or "albon" in pilotof1 or "alex" in pilotof1 or "tsunoda" in pilotof1 or "yuki" in pilotof1 or "stroll" in pilotof1 or "lance" in pilotof1:
        print ("Bueno... No es mal piloto la verdad, no me gusta especialmente pero he de decir que más de una vez me ha callado la boca haciendo alguna carrera expectacular... Pero poco más jaja")
# Si el usuario quiere hablar de Hamilton (Al chatbot no le cae muy bien... Así que no se corta y le dice lo que opina jaja):
    elif "hamilton" in pilotof1 or "lewis" in pilotof1:
        pregunta_hamilton = input ("¿De verdad quieres saber más de él" + " " + nom + 3*"?").lower()
        if "si" in pregunta_hamilton or "por" in pregunta_hamilton or "supuesto" in pregunta_hamilton or "claro que si" in pregunta_hamilton:
            print ("Madre mía... No es por nada pero Hamilton no es buen piloto, vale que tiene muchos titulos pero si no le dan un coche 5 segundos más rapido que los otros, se te pone a llorar como un bebe. Espero que te haga reflexionar mi opinión.")
            print ("Igualmente... Toma lo que buscas: Lewis Hamilton es un piloto británico de Fórmula 1 y siete veces campeón del mundo. Debutó en 2007 con McLaren y se consolidó con Mercedes como uno de los más grandes de la historia. Además de su éxito en pista, es reconocido por su activismo y compromiso social.")
            pregunta_hamiltocon = input ("Viendo que piloto me has dicho y que a mí no me gusta... ¿¿Quieres seguir hablando??").lower()
            if "si" in pregunta_hamiltocon or "vale" in pregunta_hamiltocon:
                print ("Vale, pero que sepas que no estoy de acuerdo con que te guste este piloto ehh")
            elif "no" in pregunta_hamiltocon:
                print ("¿¿¿No??? Pues ahora te aguantas jaja")
# Si el usuario quiere hablar de Ocon (Al chatbot no le cae muy bien... Así que no se corta y le dice lo que opina jaja):
    elif "ocon" in pilotof1 or "esteban" in pilotof1:
        pregunta_ocon = input ("Jajajaja," + " " + nom + " " + 3*"¿" + "enserio quieres saber más sobre ese personaje" + 3*"?").lower()
        if "si" in pregunta_ocon or "por" in pregunta_ocon or "supuesto" in pregunta_ocon or "claro que si" in pregunta_ocon:
            print ("Yo lo siento pero por ahí no paso... Ocon no sirve para nada... Es inútil jaja, y encima francés.")
            pregunta_hamiltocon = input ("Viendo que piloto te gusta y que no estamos de acuerdo... ¿¿Quieres seguir hablando??").lower()
            if "si" in pregunta_hamiltocon or "vale" in pregunta_hamiltocon:
                print ("Vale, pero que sepas que no estoy de acuerdo con que te guste este piloto ehh")
            elif "no" in pregunta_hamiltocon:
                print ("¿¿¿No??? Pues ahora te aguantas jaja")    
# Si el usuario quiere hablar de un piloto que no entiende el chatbot:
    else:
        print("Interesante elección, pero no tengo datos sobre ese piloto todavía.")

# Segunda pregunta, la de equipos:    
    equipof1 = input("Ahora, de que equipo de F1 quieres que hablemos" + " " + nom + "?").lower()
# Si el usuario quiere hablar de Ferrari:
    if "ferrari" in equipof1:
        print("¡¡¡Fuaaa, mi equipo favorito jaja!!! La Scuderia Ferrari es el equipo más legendario de la Fórmula 1. Fundado en 1929 por Enzo Ferrari, ha estado presente desde la primera temporada del campeonato en 1950. Con su icónico color rojo y el famoso 'Cavallino Rampante' (caballo rampante), Ferrari representa pasión, tradición y excelencia automovilística. Es el equipo con más títulos en la historia de la F1, incluyendo campeonatos de pilotos y constructores. Pilotos históricos como Fernando Alonso, Michael Schumacher, Niki Lauda y Gilles Villeneuve han dejado su huella en Maranello. Soñar con pilotar para Ferrari es soñar con formar parte de la historia misma del automovilismo.")
# Si el usuario quiere hablar de McLaren:
    elif "mclaren" in equipof1:
        print ("¡¡¡Buena elección!!! McLaren es uno de los equipos más históricos y prestigiosos de la Fórmula 1. Fundado en 1963 por Bruce McLaren, el equipo británico ha ganado múltiples campeonatos del mundo y ha sido la cuna de leyendas como Fernando Alonso, Ayrton Senna, Alain Prost, Niki Lauda y Lewis Hamilton. Conocido por su innovación tecnológica y su espíritu competitivo, McLaren siempre ha sido un símbolo de velocidad, elegancia y evolución. Pilotar para McLaren es formar parte de una historia llena de gloria y también de futuro prometedor.")
# Si el usuario quiere hablar de Aston Martin:
    elif "aston" in equipof1 or "martin" in equipof1:
        print ("¡Buena elección! Aston Martin, antes conocido como Racing Point y Force India, es un equipo con una historia reciente pero llena de evolución y lucha. Han contado con pilotos destacados como Sebastian Vettel y, por supuesto, Fernando Alonso, uno de los mejores de todos los tiempos. Con la llegada de Aston Martin en 2021, el equipo combina la tradición británica con ambición y tecnología avanzada. Pilotar aquí significa formar parte de un proyecto joven pero con grandes aspiraciones en la Fórmula 1.")
# Si el usuario quiere hablar de Mercedes:
    elif "amg" in equipof1 or "silver" in equipof1 or "mercedes" in equipof1 or "plateadas" in equipof1:
        print ("¡¡¡Una elección top!!! Mercedes es uno de los equipos más exitosos de la era moderna en Fórmula 1, con múltiples campeonatos de constructores y pilotos, especialmente durante su dominio con Lewis Hamilton. Es sinónimo de innovación, potencia y precisión alemana. Además, el joven talento Kimi Antonelli está fuertemente vinculado al futuro del equipo, siendo considerado uno de los pilotos más prometedores de su generación. Pilotar para Mercedes es estar en el corazón de la élite del automovilismo.")
# Si el usuario quiere hablar de Red Bull:
    elif "red" in equipof1 or "bull" in equipof1:
        print ("¡¡¡Una elección llena de adrenalina!!! Red Bull Racing es uno de los equipos más exitosos de las últimas décadas en Fórmula 1. Conocidos por su enfoque innovador y agresivo, dominaron una era con Sebastian Vettel y están volviendo a hacerlo con Max Verstappen. Su filosofía joven, audaz y orientada al rendimiento ha revolucionado el deporte. Pilotar para Red Bull significa estar en un equipo que no solo busca ganar, sino hacerlo con estilo y velocidad pura.")
# Si el usuario quiere hablar de Williams:
    elif "williams" in equipof1:
        print ("¡¡¡Una elección con mucha historia!!! Williams es uno de los equipos más legendarios de la Fórmula 1, con múltiples campeonatos en su palmarés y una rica trayectoria que comenzó en 1977. Fue cuna de campeones como Nigel Mansell, Alain Prost y Ayrton Senna. Aunque en los últimos años ha enfrentado desafíos, ahora vuelven poco a poco a la cima. Por ello, sigue siendo un equipo con gran tradición y pasión por las carreras. Pilotar para Williams es ser parte de un legado histórico, con la misión de devolverlo a lo más alto.")
# Si el usuario quiere hablar de Alpine:
    elif "alpine" in equipof1 or "renault" in equipof1 or "bwt" in equipof1:
        print ("¡¡¡Muy buena elección!!! Alpine es la actual identidad del equipo Renault en la Fórmula 1, una escudería con una larga historia en el deporte. Bajo el nombre de Renault, fue donde Fernando Alonso logró sus dos campeonatos del mundo en 2005 y 2006, y volvió a correr tanto en 2008-2009 como en su etapa más reciente con Alpine entre 2021 y 2022. El equipo combina la experiencia de años en la F1 con el respaldo tecnológico del Grupo Renault y una visión ambiciosa hacia el futuro. Pilotar para Alpine es formar parte de un legado donde ya brillaron campeones, y donde aún se busca volver a lo más alto.")
# Si el usuario quiere hablar de Sauber:
    elif "sauber" in equipof1 or "kick" in equipof1 or "stake" in equipof1 or "audi" in equipof1:
        print ("¡¡¡Una elección estratégica e interesante!!! El equipo Sauber, actualmente conocido como Kick Sauber, tiene una larga trayectoria en la Fórmula 1 desde los años 90, siendo una escudería reconocida por su capacidad para desarrollar talento y mantenerse competitiva con recursos limitados. En el pasado, compitió bajo el nombre de Alfa Romeo, y ahora se prepara para un futuro muy prometedor: en 2026 se convertirá oficialmente en el equipo oficial de Audi. Pilotar para Sauber hoy es estar en la antesala de uno de los proyectos más ambiciosos que veremos en la nueva era de la F1.")
# Si el usuario quiere hablar de Haas:
    elif "haas" in equipof1 or "money" in equipof1 or "gram" in equipof1:
        print ("¡¡¡Una elección con carácter propio!!! Haas es el primer equipo estadounidense en la Fórmula 1 en varias décadas, debutando en 2016. Aunque es uno de los equipos más jóvenes del paddock, ha logrado hacerse un lugar gracias a su enfoque práctico y su asociación técnica con Ferrari. A lo largo de los años ha contado con pilotos experimentados y jóvenes promesas, siendo un equipo que sigue construyendo su camino en el deporte. Pilotar para Haas es aceptar el desafío de crecer junto a una escudería con mucho potencial.")
# Si el usuario quiere hablar de RB:
    elif "rb" in equipof1 or "racing" in equipof1 or "bulls" in equipof1 or "visa" in equipof1 or "cash" in equipof1:
        print ("¡Una elección con mucho futuro! Racing Bulls, anteriormente conocida como AlphaTauri y Toro Rosso, es el equipo filial de Red Bull Racing. A lo largo de los años ha sido una plataforma clave para desarrollar jóvenes talentos, como Sebastian Vettel —quien logró aquí su primera victoria— y más recientemente pilotos como Pierre Gasly o Yuki Tsunoda. Con una imagen renovada y mayor integración técnica con Red Bull, RB está creciendo como un equipo competitivo por derecho propio. Pilotar para Racing Bulls es estar en el radar directo de los campeones, con la oportunidad de brillar y dar el salto a lo más alto.")
# Si el usuario quiere hablar de un equipo que no entiende el chatbot:
    else:
        print("Interesante elección, pero no tengo datos sobre ese piloto todavía.")

# Tercera pregunta, la de las leyendas:
    leyendaf1 = input("¿Por último, de que leyenda de F1 te gustaría saber más" + " " + nom + "?").lower()
# Si el usuario quiere hablar de Schumacher:
    if "schumacher" in leyendaf1 or "michael" in leyendaf1 or "kaiser" in leyendaf1:
        print ("Michael Schumacher es uno de los nombres más grandes en la historia de la Fórmula 1. Con 7 campeonatos del mundo y 91 victorias, dominó la era moderna con Ferrari y estableció estándares de excelencia y trabajo en equipo que aún inspiran, me gusta tu elección jaja.")
# Si el usuario quiere hablar de Hamilton:
    elif "hamilton" in leyendaf1 or "lewis" in leyendaf1:
        print ("Aunque no me guste mucho, he de decir que Lewis Hamilton es una superestrella del automovilismo, con 7 títulos mundiales y récords en victorias y poles. Más allá de su talento, es un referente en la lucha por la diversidad y la igualdad dentro y fuera de la pista.")
# Si el usuario quiere hablar de Verstappen:
    elif "verstappen" in leyendaf1 or "max" in leyendaf1:
        print ("Max Verstappen es la joven estrella que ha revolucionado la F1 en los últimos años. Con ya 4 campeonatos, es conocido por su agresividad y consistencia, y se perfila como una leyenda en activo del deporte, increible tu elección, buen gusto jaja.")
# Si el usuario quiere hablar de Senna:
    elif "senna" in leyendaf1 or "ayrton" in leyendaf1:
        print ("Ayrton Senna es una leyenda eterna de la F1, recordado por su increíble velocidad, carisma y espíritu competitivo. Sus 3 campeonatos y su trágica partida dejaron una huella imborrable en el deporte, increible tu elección, buen gusto jaja.")
# Si el usuario quiere hablar de Prost:
    elif "prost" in leyendaf1 or "alain" in leyendaf1:
        print ("Conocido como 'El Profesor', Alain Prost fue un piloto cerebral y estratégico, con 4 títulos mundiales. Su enfoque metódico y calma en pista le valieron un lugar especial en la historia de la F1, me gusta tu elección jaja.")
# Si el usuario quiere hablar de Fangio:
    elif "fangio" in leyendaf1 or "juan" in leyendaf1 or "manuel" in leyendaf1:
        print ("El argentino Juan Manuel Fangio dominó la Fórmula 1 en los años 50 con 5 campeonatos. Su elegancia y habilidad técnica marcaron el inicio de la era de las leyendas en el deporte, me gusta tu elección jaja.")
# Si el usuario quiere hablar de Lauda:
    elif "lauda" in leyendaf1 or "niki" in leyendaf1:
        print ("Niki Lauda es símbolo de coraje y resiliencia. Tras un grave accidente en 1976, volvió a competir y ganó 3 títulos mundiales, dejando un legado imborrable de fortaleza y profesionalismo, increible tu elección, buen gusto jaja.")
# Si el usuario quiere hablar de Alonso:
    elif "alonso" in leyendaf1 or "fernando" in leyendaf1 or "Nano" in leyendaf1:
        print ("Fernando Alonso es uno de los pilotos más completos y longevos de la F1, con 2 campeonatos y una carrera que abarca más de dos décadas. Su talento y determinación lo mantienen en la élite, increible tu elección, buen gusto jaja.")
# Si el usuario quiere hablar de Vettel:
    elif "vettel" in leyendaf1 or "sebastian" in leyendaf1:
        print ("Sebastian Vettel brilló con 4 títulos consecutivos en Red Bull, demostrando velocidad, inteligencia y carácter. Además, es un referente por su compromiso fuera de las pistas, me gusta tu elección jaja.")
# Si el usuario quiere hablar de Surtees:
    elif "surtees" in leyendaf1 or "john" in leyendaf1:
        print ("John Surtees es único en la historia: campeón mundial tanto en motociclismo como en Fórmula 1. Su versatilidad y talento le dieron un lugar destacado en el automovilismo, no me esperaba esa respuesta pero veo que tienes sabios gustos jaja.")
# Si el usuario quiere hablar de De La Rosa:
    elif "pedro" in leyendaf1 or "rosa" in leyendaf1 or "de" in leyendaf1 or "la" in leyendaf1:
        print ("Pedro de la Rosa es un piloto español de Fórmula 1 conocido por su talento y experiencia. Compitió en varias temporadas principalmente como piloto de pruebas y titular para equipos como Arrows, Jaguar y McLaren. Destacado por su habilidad técnica, también ha trabajado como comentarista y embajador del automovilismo en España.")
# Si el usuario quiere hablar de Mazepin:
    elif "mazepin" in leyendaf1 or "nikita" in leyendaf1:
        print ("Nikita Mazepin es un piloto ruso de Fórmula 1 que compitió en la temporada 2021 con el equipo Haas. Proveniente de una familia con fuerte apoyo financiero, su paso por la F1 fue controvertido y recibió críticas por su desempeño y comportamiento fuera de pista. Tras una única temporada, perdió su asiento y actualmente no participa en la Fórmula 1.")
# Si el usuario quiere hablar de Latifi:
    elif "latifi" in leyendaf1 or "nicholas" in leyendaf1:
        print ("Nicholas Latifi es un piloto canadiense de Fórmula 1 que compitió principalmente con el equipo Williams entre 2020 y 2022. Reconocido por su perseverancia y esfuerzo, aunque sin grandes resultados destacados, se destacó por su profesionalismo y dedicación en el deporte. También tiene experiencia en categorías inferiores como la Fórmula 2.")
# Si el usuario quiere hablar de una leyenda que no entiende el chatbot:
    else:
        print("Interesante elección, pero no tengo datos sobre ese piloto todavía.") 

# Ahora la parte de hablar de MotoGP
def hablar_motogp(nom):
    """Aquí va todo tu bloque de respuestas de MotoGP."""
    print(nom + "," + " " + " ¡Perfecto! Vamos a hablar de MotoGP")
    # Aquí puedes mantener TODO tu bloque de código actual de MotoGP.
#Primera pregunta, la de los pilotos
    pilotomgp = input("¿De qué piloto de MotoGP te gustaría hablar? ").lower()
# Si quiere hablar de Marc Márquez:
    if "marc" in pilotomgp or "hormiga" in pilotomgp or "trueno" in pilotomgp:
        print ("¡¡¡Mi piloto favorito!!! Nacido en Cervera, España, Marc Márquez es una leyenda viva del motociclismo. Desde su debut en MotoGP en 2013, se hizo famoso por su estilo agresivo, adelantamientos imposibles y una ambición sin frenos. Conquistó 8 títulos mundiales (6 en la categoría reina) y dominó junto a Honda durante años, hasta que las lesiones complicaron su camino a partir de 2020. En 2023 y 2024 sorprendió al pasar al equipo Gresini Ducati, donde volvió a mostrar destellos de su mejor versión. Ahora, en 2025, Marc se une al equipo oficial Ducati, montando la mejor moto de la parrilla. Superando con mucha ventaja al resto de pilotos ha logrado su objetivo: volver a lo más alto y sumar su noveno título mundial. Marc no solo corre al límite: vive allí. Y esa es justamente la esencia que lo convierte en uno de los grandes de todos los tiempos.")
# Si quiere hablar de Alex Márquez:
    elif "alex" in pilotomgp:
        print ("¡¡¡Mi otro piloto favorito!!! Nacido en Cervera, como su hermano Marc, Álex Márquez ha forjado su propio camino en el motociclismo con constancia y determinación. Campeón del mundo en Moto3 (2014) y Moto2 (2019), llegó a MotoGP en 2020 con el equipo oficial Honda, logrando dos podios en su temporada de debut. Tras un paso por LCR Honda, en 2023 dio un nuevo aire a su carrera al fichar por Gresini Ducati, donde rápidamente se adaptó a la Desmosedici y volvió a luchar en posiciones de cabeza. Su estilo técnico y limpio, combinado con mayor confianza, le han permitido crecer como piloto dentro de una categoría cada vez más competitiva. En 2025, Álex sigue consolidado como una pieza clave del proyecto Gresini, demostrando que no vive a la sombra de nadie: su talento y trabajo hablan por sí solos. Con experiencia, velocidad y mentalidad fuerte, Álex Márquez sigue buscando su lugar en la historia de MotoGP... y cada año está más cerca.")
# Si quiere hablar de algun Márquez, como són 2 le preguntamos cual:
    elif "márquez" in pilotomgp or "marquez" in pilotomgp:
        pregunta_marquez_respuesta = input ("¿¿¿Pero a que Márquez te refieres jaja???").lower()
        if "mayor" in pregunta_marquez_respuesta or "marc" in pregunta_marquez_respuesta:
            print ("Vale vale, ahora me aclaro jaja ¡¡¡Adoro al mayor de los Márquez!!! Nacido en Cervera, España, Marc Márquez es una leyenda viva del motociclismo. Desde su debut en MotoGP en 2013, se hizo famoso por su estilo agresivo, adelantamientos imposibles y una ambición sin frenos. Conquistó 8 títulos mundiales (6 en la categoría reina) y dominó junto a Honda durante años, hasta que las lesiones complicaron su camino a partir de 2020. En 2023 y 2024 sorprendió al pasar al equipo Gresini Ducati, donde volvió a mostrar destellos de su mejor versión. Ahora, en 2025, Marc se une al equipo oficial Ducati, montando la mejor moto de la parrilla. Superando con mucha ventaja al resto de pilotos ha logrado su objetivo: volver a lo más alto y sumar su noveno título mundial. Marc no solo corre al límite: vive allí. Y esa es justamente la esencia que lo convierte en uno de los grandes de todos los tiempos.")
        elif "menor" in pregunta_marquez_respuesta or "alex" in pregunta_marquez_respuesta:
            print ("Vale vale, ahora me aclaro jaja ¡¡¡Adoro al menor de los Márquez!!! Nacido en Cervera, como su hermano Marc, Álex Márquez ha forjado su propio camino en el motociclismo con constancia y determinación. Campeón del mundo en Moto3 (2014) y Moto2 (2019), llegó a MotoGP en 2020 con el equipo oficial Honda, logrando dos podios en su temporada de debut. Tras un paso por LCR Honda, en 2023 dio un nuevo aire a su carrera al fichar por Gresini Ducati, donde rápidamente se adaptó a la Desmosedici y volvió a luchar en posiciones de cabeza. Su estilo técnico y limpio, combinado con mayor confianza, le han permitido crecer como piloto dentro de una categoría cada vez más competitiva. En 2025, Álex sigue consolidado como una pieza clave del proyecto Gresini, demostrando que no vive a la sombra de nadie: su talento y trabajo hablan por sí solos. Con experiencia, velocidad y mentalidad fuerte, Álex Márquez sigue buscando su lugar en la historia de MotoGP... y cada año está más cerca.")
# Si quiere hablar de Acosta:
    elif "acosta" in pilotomgp or "pedro" in pilotomgp:
        print ("¡¡¡Me encanta tu elección!!! Con solo 21 años, Pedro Acosta ya es una de las mayores promesas de MotoGP. Campeón de Moto3 en 2021 en su temporada debut y de Moto2 en 2023, llegó a la categoría reina en 2024 con el equipo GasGas Tech3 KTM, demostrando madurez, velocidad y una confianza fuera de lo común. En 2025, Acosta sigue creciendo como piloto oficial KTM, mezclando agresividad e inteligencia en pista. Su estilo audaz y su capacidad para adaptarse rápidamente lo colocan como un firme candidato a ser campeón en muy poco tiempo. El futuro ya llegó, y se llama Pedro Acosta.")
# Si quiere hablar de Martín:
    elif "martin" in pilotomgp or "jorge" in pilotomgp:
        print ("¡¡¡Vaya pilotazo!!! Jorge Martín, campeón del mundo de Moto3 en 2018, se ha consolidado como uno de los pilotos más rápidos y consistentes de MotoGP, y en 2025, tras años de lucha con Ducati Pramac, finalmente corre para el equipo oficial Aprilia, decidido a conquistar el título que ha rozado en temporadas anteriores.")
# Si quiere hablar de Mir:
    elif "mir" in pilotomgp or "joan" in pilotomgp:
        print ("¡¡¡Que piloto!!! Joan Mir, campeón del mundo de MotoGP en 2020 con Suzuki, es un piloto de talento sólido y mentalidad fuerte que en 2025 sigue luchando por volver a lo más alto, ahora intentando recuperar sensaciones tras años difíciles en Honda.")
# Si quiere hablar de Fernandez:
    elif "fernandez" in pilotomgp or "raul" in pilotomgp:
        print ("¡¡¡Que joven piloto!!! Raúl Fernández, subcampeón de Moto2 en 2021 tras una temporada espectacular, sigue buscando su lugar en MotoGP y en 2025 compite con Trackhouse Aprilia, decidido a demostrar todo su potencial en la categoría reina.")
# Si quiere hablar de Aldeguer:
    elif "aldeguer" in pilotomgp or "fermin" in pilotomgp:
        print ("¡¡¡Vaya Rookie!!! Fermín Aldeguer, una de las jóvenes promesas más destacadas del motociclismo español, llega a MotoGP en 2025 con el equipo Pramac Ducati tras un cierre de temporada dominante en Moto2, listo para dejar huella desde su debut en la categoría reina.")
# Si quiere hablar de Bagnaia:
    elif "bagnaia" in pilotomgp or "pecco" in pilotomgp or "francesco" in pilotomgp:
        print ("¡¡¡!Buen piloto!! Pecco Bagnaia, campeón de MotoGP en 2022 con Ducati, es uno de los pilotos más completos y competitivos de la parrilla, y en 2025 continúa en el equipo oficial Ducati.")
# Si quiere hablar de Bezzecchi:
    elif "bezzecchi" in pilotomgp or "marco" in pilotomgp:
        print ("¡¡¡Que gran elección!!! Marco Bezzecchi, piloto italiano talentoso y constante, compite en 2025 con la Aprilia, consolidándose como uno de los jóvenes talentos en alza dentro de MotoGP, con grandes expectativas para las próximas temporadas.")
# Si quiere hablar de Quartararo:
    elif "quartararo" in pilotomgp or "fabio" in pilotomgp or "diablo" in pilotomgp:
        print ("¡¡¡El diablo!!! Fabio Quartararo, campeón de MotoGP en 2021 con Yamaha, es un piloto rápido y agresivo que en 2025 sigue luchando por el título, enfrentando una temporada desafiante con un equipo Yamaha en plena evolución.")
# Si quiere hablar de Ogura:
    elif "ogura" in pilotomgp or "ai" in pilotomgp:
        print ("¡¡¡Buen Rookie la verdad!!! Ai Ogura, joven talento japonés de Moto2, destaca por su constancia y velocidad, y en 2025 busca seguir creciendo y dar el salto definitivo hacia MotoGP en un futuro cercano.")
# Si quiere hablar de un piloto normal:
    elif "binder" in pilotomgp or "brad" in pilotomgp or "maverick" in pilotomgp or "viñales" in pilotomgp or "zarco" in pilotomgp or "johann" in pilotomgp or "rins" in pilotomgp or "oliveira" in pilotomgp or "miguel" in pilotomgp or "miller" in pilotomgp or "jack" in pilotomgp:
        print ("¡¡¡Buena elección!!! “La verdad es que es un piloto constante y competente, que aporta buen nivel aunque no suele destacar mucho, pero siempre está listo para aprovechar su oportunidad.”")
# Si quiere hablar de un piloto bastante bueno:
    elif "bastianini" in pilotomgp or "enea" in pilotomgp or "di" in pilotomgp or "giannantonio" in pilotomgp or "morbidelli" in pilotomgp or "franco" in pilotomgp or "marini" in pilotomgp or "luca" in pilotomgp:
        print ("¡¡¡Que piloto!!! La verdad es que es un piloto muy competitivo y constante, que suele estar cerca de los líderes y puede pelear por podios, aunque todavía le falta dar ese salto para ser de los mejores.")
# Si quiere hablar de Chantra:
    elif "chantra" in pilotomgp or "somkiat" in pilotomgp:
        print ("Que gracioso eres jaja")
# Si quiere hablar de Moreira:
    elif "moreira" in pilotomgp or "diogo" in pilotomgp:
        print ("¡¡¡Que piloto!!! El brasileño Diogo Moreira se ha proclamado campeón del mundo de Moto2 en 2025, haciendo historia para su país. Con solo 21 años, ha destacado por su rapidez y madurez en pista, dominando una temporada muy competitiva. Su gran rendimiento le ha valido un fichaje con el equipo LCR Honda para 2026, donde debutará en MotoGP con el objetivo de seguir creciendo y consolidarse entre la élite del motociclismo mundial.")    
# Si quiere hablar de Razgatlıoğlu:
    elif "razgatlıoğlu" in pilotomgp or "toprak" in pilotomgp or "razgatlioglu" in pilotomgp:
        print ("¡¡¡Que piloto!!! El piloto turco Toprak Razgatlıoğlu, estrella del WorldSBK, se prepara para dar el salto a MotoGP en 2026 con el equipo Prima Pramac. Reconocido por su agresividad, habilidad en las curvas y consistencia en las carreras, Toprak ha dejado su sello en el Mundial de Superbike con múltiples victorias y títulos que lo consolidan como uno de los mejores pilotos de su generación. Su llegada a la categoría reina promete emoción y talento sobre la pista, llevando su experiencia y competitividad al máximo nivel del motociclismo.")
# Si quiere hablar de algun piloto que el chatbot no reconoce:
    else:
        print("Interesante elección, pero no tengo datos sobre ese piloto todavía.")
    
# Seguna pregunta, la de los equipos:
    equipomgp = input("Ahora, de que equipo de MotoGP quieres que hablemos" + " " + nom + "?").lower()
# Si quiere hablar de Ducati Corse:
    if "ducati" in equipomgp or "corse" in equipomgp or "lenovo" in equipomgp:
        print ("¡¡¡Fuaaa, es de mis equipos favoritos jaja!!! Ducati Lenovo es uno de los equipos más fuertes y consistentes de MotoGP. Con una moto potente y tecnología de punta, siempre están en la pelea por victorias y campeonatos. Su combinación de pilotos talentosos y un gran trabajo en el desarrollo los convierte en un rival difícil de superar en cualquier circuito.")
# Si quiere hablar de Aprilia:
    elif "aprilia" in equipomgp:
        print ("¡¡¡Buena elección!!! Aprilia Racing es un equipo en plena evolución, cada año mostrando mejoras significativas en MotoGP. Con pilotos jóvenes y talentosos, y una moto cada vez más competitiva, están creciendo como un serio rival para los equipos punteros y buscando consolidarse en la lucha por podios y victorias.")
# Si quiere hablar de Gresini:
    elif "gresini" in equipomgp or "bk8" in equipomgp:
        print ("¡¡¡Fuaaa, es de mis equipos favoritos jaja!!! BK8 Gresini Racing es un equipo con gran tradición y pasión en MotoGP, que ha sabido combinar experiencia y juventud para mantenerse competitivo. Con pilotos que aportan talento y ganas de crecer, y una alianza sólida con Ducati, siguen luchando para subir al podio y consolidarse entre los mejores.")
# Si quiere hablar de Honda:
    elif "honda" in equipomgp or "hrc" in equipomgp:
        print ("¡¡¡Una elección top!!! Honda HRC Castrol es uno de los equipos históricos y más icónicos de MotoGP, con una larga tradición de campeonatos y pilotos legendarios. Aunque en los últimos años han enfrentado desafíos técnicos y de rendimiento, siguen trabajando duro para recuperar su lugar en la cima, apoyados en la experiencia de sus pilotos y la innovación constante.")
# Si quiere hablar de LCR Honda:
    elif "lcr" in equipomgp:
        print ("¡¡¡Wow!!! LCR Honda es un equipo independiente con mucha historia en MotoGP, conocido por su profesionalismo y constancia. Aunque no siempre cuenta con las motos más punteras, ha logrado resultados destacados gracias al talento y esfuerzo de sus pilotos, manteniéndose competitivo y luchando en cada carrera.")
# Si quiere hablar de Yamaha Oficial:
    elif "monster" in equipomgp or "energy" in equipomgp or "yamaha" in equipomgp:
        print ("¡¡¡Una elección llena de adrenalina!!! Monster Energy Yamaha es uno de los equipos más emblemáticos de MotoGP, con una gran historia de éxitos y campeones. Aunque en los últimos años ha enfrentado altibajos y retos técnicos, sigue siendo un equipo competitivo con pilotos talentosos que luchan por volver a dominar la categoría.")
# Si quiere hablar del VR46:
    elif "vr46" in equipomgp or "vr" in equipomgp:
        print ("¡¡¡Muy buena elección!!! VR46 Racing Team es el equipo fundado por Valentino Rossi que ha crecido rápidamente en MotoGP. Con un enfoque joven y ambicioso, apoyado en talento emergente y la colaboración con Ducati, busca consolidarse como una referencia en la categoría y luchar por podios y victorias.")
# Si quiere hablar de Prima Pramac:
    elif "prima" in equipomgp or "pramac" in equipomgp:
        print ("¡¡¡Una elección estratégica e interesante!!! Prima Pramac Racing es un equipo sólido y con mucha experiencia en MotoGP, que combina pilotos veteranos y con talento con una estrecha colaboración con Yamaha. Siempre están en la pelea por buenos resultados y buscan crecer temporada tras temporada para acercarse a los equipos punteros.")
# Si quiere hablar de KTM:
    elif "ktm" in equipomgp:
        print ("¡¡¡Una elección con carácter propio!!! KTM Factory Racing Team es un equipo joven pero ambicioso en MotoGP, conocido por su innovación y progreso constante. Con pilotos veloces y una moto en evolución, trabajan duro para consolidarse como candidatos a podios y victorias en una categoría cada vez más competitiva.")
# Si quiere hablar de KTM Tech 3:
    elif "3" in equipomgp or "tech" in equipomgp:
        print ("¡Una elección con mucho futuro! Tech3 KTM Factory Racing es un equipo satélite con gran experiencia en MotoGP, dedicado a desarrollar talento joven y ayudar en la evolución técnica de KTM. Aunque no siempre está en el podio, cumple un papel clave formando pilotos y aportando datos valiosos para el equipo oficial.")
# Si quiere hablar de Trackhouse:
    elif "trackhouse" in equipomgp:
        print ("¡Una elección con mucho futuro! Trackhouse Racing es el nuevo equipo estadounidense en MotoGP que llegó en 2024 con una propuesta fresca, moderna y ambiciosa. Con estructura sólida y el respaldo de Aprilia, buscan crecer rápidamente en la categoría, apostando por pilotos jóvenes y una identidad muy marcada dentro y fuera de la pista.")
# Si quiere hablar de un equipo que el chatbot no reconoce:
    else:
        print("Interesante elección, pero no tengo datos sobre ese equipo todavía.")
    
# Tercera pregunta, la de la leyenda
    leyendamgp = input("¿Por último, de que leyenda de MotoGP te gustaría saber más" + " " + nom + "?").lower()
# Si quiere hablar de Agostini:
    if "agostini" in leyendamgp or "giacomo" in leyendamgp:
        print ("Giacomo Agostini ostenta un récord histórico con 15 títulos mundiales, logrados principalmente en las categorías de 350cc y 500cc. Fue el dominador absoluto de los años 60 y 70, corriendo para marcas míticas como MV Agusta. Su legado permanece intacto como uno de los más grandes campeones que ha dado el motociclismo.")
# Si quiere hablar de Nieto:
    elif "nieto" in leyendamgp or "angel" in leyendamgp:
        print ("Ángel Nieto es una auténtica leyenda del motociclismo español, con 13 títulos mundiales (12+1, como él decía por superstición). Dominó las categorías de 50cc y 125cc, y fue pionero en abrir el camino para que España se convirtiera en una potencia del motociclismo mundial. Su figura es irreemplazable en la historia del deporte.")
# Si quiere hablar de Marc Márquez:
    elif "marquez" in leyendamgp or "marc" in leyendamgp or "Marc" in leyendamgp:
        print ("Marc Márquez cambió las reglas del juego en MotoGP desde su llegada en 2013. Con 8 títulos mundiales y un estilo espectacular basado en salvadas imposibles y agresividad total, marcó una era con Honda. A pesar de las lesiones, su espíritu de lucha y talento siguen haciendo historia.")
# Si quiere hablar de Doohan:
    elif "doohan" in leyendamgp or "mick" in leyendamgp:
        print ("Mick Doohan fue el piloto más dominante de la década de los 90, con cinco títulos consecutivos en 500cc entre 1994 y 1998. Su control absoluto sobre la moto y su fortaleza mental lo convirtieron en una leyenda con Honda. Su rivalidad con Crivillé y sus remontadas épicas lo hacen inolvidable.")
# Si quiere hablar de Stoner:
    elif "stoner" in leyendamgp or "casey" in leyendamgp:
        print ("Casey Stoner fue campeón del mundo en 2007 con Ducati y en 2011 con Honda, destacándose por su talento natural y velocidad en cualquier condición. Aunque su carrera fue corta, dejó una huella profunda por su pilotaje agresivo, directo y sin concesiones. Uno de los grandes talentos puros de MotoGP.")
# Si quiere hablar de Lorenzo:
    elif "lorenzo" in leyendamgp or "jorge" in leyendamgp:
        print ("Jorge Lorenzo fue campeón del mundo en cinco ocasiones, tres de ellas en MotoGP. Su estilo de pilotaje limpio, rápido y constante lo convirtió en uno de los grandes rivales de Valentino Rossi y Marc Márquez. Fue un perfeccionista dentro y fuera de la pista, con una enorme capacidad para mantener el ritmo de carrera.")
# Si quiere hablar de Rainey:
    elif "rainey" in leyendamgp or "wayne" in leyendamgp:
        print ("Wayne Rainey fue uno de los grandes nombres de los 90, con tres títulos en 500cc. Su pilotaje técnico y fino, junto con una mentalidad fuerte, lo llevaron a dominar una era muy competitiva. Su carrera se vio truncada por una lesión, pero su legado como luchador sigue presente.")
# Si quiere hablar de Schwantz:
    elif "schwantz" in leyendamgp or "kevin" in leyendamgp:
        print ("Kevin Schwantz fue campeón del mundo en 1993 y se convirtió en uno de los pilotos más queridos por su estilo agresivo, corazón y entrega total en pista. Rival directo de Wayne Rainey, su número 34 fue retirado como homenaje a su enorme legado.")
# Si quiere hablar de Roberts:
    elif "roberts" in leyendamgp or "kenny" in leyendamgp:
        print ("Kenny Roberts Sr. fue el primer estadounidense en ganar el Mundial de 500cc, con tres títulos consecutivos. Introdujo un nuevo estilo de pilotaje, influenciado por el dirt-track, que revolucionó la categoría. Fue también un pionero fuera de la pista, cambiando el rol del piloto profesional.")
# Si quiere hablar de Spencer:
    elif "spencer" in leyendamgp or "freddie" in leyendamgp:
        print ("Freddie Spencer fue un talento precoz y brillante que hizo historia en 1985 al ganar los campeonatos de 250cc y 500cc en el mismo año. Su carrera fue breve debido a las lesiones, pero su habilidad y velocidad lo convirtieron en una leyenda recordada por su enorme calidad.")
# Si quiere hablar de Pedrosa:
    elif "pedrosa" in leyendamgp or "dani" in leyendamgp:
        print ("Dani Pedrosa ganó títulos en 125cc y 250cc y fue uno de los grandes nombres de MotoGP, aunque nunca logró el campeonato en la categoría reina. Su pilotaje suave y técnico, combinado con su capacidad de desarrollo, lo hicieron clave para Honda y más tarde para KTM, donde sigue influyendo como probador.")
# Si quiere hablar de Criville:
    elif "criville" in leyendamgp or "alex" in leyendamgp:
        print ("Álex Crivillé hizo historia al convertirse en el primer español campeón del mundo en 500cc, en 1999. También fue campeón de 125cc en 1989. Fue un referente en los 90 y pieza clave para que el motociclismo español se abriera paso entre los grandes.")
# Si quiere hablar de Biaggi:
    elif "biaggi" in leyendamgp or "max" in leyendamgp:
        print ("Max Biaggi fue campeón del mundo cuatro veces en 250cc y uno de los principales rivales de Valentino Rossi en los 2000. Su estilo elegante y competitivo lo llevó a pelear en MotoGP y luego a brillar en Superbikes, donde también fue campeón.")
# Si quiere hablar de Capirossi:
    elif "capirossi" in leyendamgp or "loris" in leyendamgp:
        print ("Loris Capirossi fue campeón del mundo en 125cc y 250cc, y protagonizó una de las carreras más largas del motociclismo, con más de 300 Grandes Premios disputados. Fue un piloto aguerrido y constante, respetado por su compromiso y experiencia.")
# Si quiere hablar de Surtees:
    elif "surtees" in leyendamgp or "john" in leyendamgp:
        print ("John Surtees es único en la historia: campeón mundial tanto en motociclismo como en Fórmula 1. Su versatilidad y talento le dieron un lugar destacado en el automovilismo, no me esperaba esa respuesta pero veo que tienes sabios gustos jaja.")
# Si quiere hablar de Rossi:
    elif "rossi" in leyendamgp or "valentino" in leyendamgp:
        print ("Mira, que te quede claro que Rossi es un guarro, un pegapatadas y un malisimo perdedor. Pero también ha ganado lo suyo... Así que voy a tener un minimo de respeto hacia él (lo que el no tiene hacia el resto) y voy a dejar aquí su información: Valentino Rossi, 9 veces campeón del mundo, es una de las mayores leyendas del motociclismo, ícono global y figura clave en la popularización de MotoGP.")
# Si quiere hablar de leyenda que el chatbot no conoce:
    else:
        print("Interesante elección, pero no tengo datos sobre ese piloto todavía.")

# Nueva función, la de hacer una broma, solo importa "random" y, junto a la lista del principio, escribe una aleatoria:
def hacer_broma():
    """Cuenta una broma al azar."""
    import random
    print(nom + " " + " aquí va una broma jaja, espero que te haga gracia:")
    print(random.choice(bromas))

# Otra funcón nueva, la de comparar 2 pilotos, aquí hay trampa ya que solo hace escribir al usuario 2 pilotos y, posteriormente, pone sus respuestas en una frase predeterminada:
def comparar():
    """Compara dos pilotos."""
    p1 = input("Dime el primer piloto a comparar: ")
    p2 = input("Dime el segundo piloto: ")
    print("Comparando a" + " " + p1 + " " + "y" + " " + p2 + "...")
    print(p1 + " " + "es rápido, pero" + " " + p2 + " " + "tiene más experiencia. ¡Ambos son increíbles!")
# Otra función más nueva, la de calcular, en este caso, el tiempo que perderá el piloto más lento respecto al más rápido:
def calcular():
    """Calcula algo sencillo relacionado con el motor."""
# Se usa int para las vueltas, ya que se encarga de los numeros enteros:
    vueltas = int(input("¿Cuántas vueltas quedan en la carrera? "))
# Y se usa float para los segundos, ya que se encarga de los decimales:
    segundos = float(input("¿Cuántos segundos pierde por vuelta el coche más lento? "))
# Aquí multiplica esos 2 valores y, posteriormente, da el resultado:
    perdida = vueltas * segundos
    print(f"En total perderá unos {perdida:.2f} segundos respecto al líder")

# Otra función nueva más, la de predecir, aquí se hace lo mismo que en las bromas, se hace una lista, después se importa "random" y por último se escribe y ya:
def predecir():
    """Predice el futuro del motor."""
    import random
    print("Dejame predecir el futuro... Te aseguro que pasará esto:")
    print(random.choice(predicciones))

# Otra función nueva más, esta también tiene truco ya que no sirve para nada jaja, se deja que el usuario plantee una pregunta y el chatbot solo la copia y le dice que no tiene suficiente información para responderla:
def preguntar_libre():
    """Deja que el usuario haga una pregunta libre."""
    pregunta = input("Hazme una pregunta sobre F1 o MotoGP: ")
    print(f"Mmm... buena pregunta sobre '{pregunta}', pero necesito más datos, intentaré aprender más jaja")

# La última función nueva, donde solo el usuario elige que quiere dibujar, y el chatbot lo hace:
def dibujar():
    """Dibuja un coche o moto con texto."""
    print("Venga " + " " + nom + "," + " " + "Te dejo elegir entre dibujar un coche o una moto.")
    eleccion = input("(coche/moto): ").lower()
    if "coche" in eleccion:
        print("""
⠀⠀⢀⣀⣀⣠⣤⣤⣤⣶⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣼⡿⢿⣿⣿⣿⣿⣿⣿⣯⣿⣿⡏⣀⣤⣤⣶⣶⣶⣶⣾⣿⣿⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠙⣿⣷⣿⣄⢈⣀⣠⣼⣯⣹⣋⣹⣿⣿⣯⣥⣾⣟⣹⣿⣾⣿⣏⣀⣠⣤⣤⣤⣤⣤⡀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⣙⡟⠛⠿⠿⠿⠿⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣀⣠⣤⣶⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣧⡒⠶⠦⣤⣀⠀⠀⠀⣠⣾⣿⣯⣟⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢹⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠉⠻⢤⣀⠀⣶⣴⣦⣶⡶⡆⢠⠿⣿⢿⣿⣿⣿⣿⣷⣶⣬⣍⣛⣶⣾⣭⣻⢿⣿⠿⣿⣿⣿⣿⣿⣿⣆⡇⠀⣰⣶⡤⣤⣄⠀⠀⠀⠀
⠀⠛⣻⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣬⣿⣿⣷⣼⣬⣿⣿⣿⣿⣿⣤⣽⣿⣿⣿⣷⣾⣿⣯⣭⣷⣿⣿⣿⠿⣿⣶⣤⣘⡙⠛⠿⣿⣿⠇⠀⣿⣿⣗⣿⣿⣆⠀⠀⠀
⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠉⠛⠺⠿⢿⣿⣿⣿⣾⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣾⣿⣿⣶⣶⣽⡻⣧⠈⢻⣯⣽⣿⣷⣶⠾⣍⣦⠸⢿⣿⣿⣿⣿⣿⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠿⠿⢿⣿⣿⣿⣿⣟⣏⣛⣛⣷⣾⣿⣿⡿⣡⣶⣬⡹⣷⣽⣇⣠⣯⠉⠉⠙⠛⠷⣿⣽⣿⣦⣤⡙⠻⢿⣟⣧⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⢹⣿⣇⢿⣿⣿⡇⣿⣿⣿⣿⣿⠋⠛⢲⡶⢾⣿⣿⡿⣿⣿⣿⣷⣦⡘⣿⣷⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣷⣤⣭⣾⣿⣿⣿⠟⢹⣘⣾⣿⣆⣤⣿⣗⣿⣿⣿⣿⣿⣿⣿⡿⠟⠃
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⠾⣽⣿⡿⠟⠉⠀⠸⠿⢾⣭⣟⣻⠟⢹⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀      
        """)
    elif "moto" in eleccion:
        print("""
                     ⣀⣤⢤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣁⣈⣟⣀⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⢸⣁⡩⠟⠉⣠⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣍⣀⣠⠴⡾⠙⠺⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⡇⢹⡞⢁⡆⠈⠲⡱⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠁⠘⡌⠇⢸⠁⠀⠀⠁⠘⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠤⣀⣀⣠⠚⠁⢀⡔⠙⢆⢸⠀⢀⡇⠀⠀⠈⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡤⠞⠁⠀⠀⢀⣹⣀⡴⠋⠀⢀⡼⠋⠉⢸⠃⠀⠀⠀⠈⣧⠀⠀⠀⢀⣀⣀⣠⣤⡤⣤⣀⠀
⠀⠀⠀⠀⠀⣠⠖⠉⠀⠀⣠⣴⣞⣿⣿⣿⡞⣯⠟⠉⢀⡤⠖⠯⣤⣤⠤⠤⠀⠉⣷⡞⠉⠉⣁⣀⠀⠚⠁⣠⠼⠃
⠀⠀⠀⠀⢰⡇⣠⠔⠒⡆⠻⣿⣀⠽⣯⣀⣀⣈⣶⣾⣅⣒⣁⡴⠊⠁⠀⠀⠀⣠⠟⢉⣷⣿⣷⠌⣡⠴⢯⣥⡀⠀
⠀⠀⠀⠀⠘⢿⣥⣤⣶⣧⠤⠤⠽⠶⠉⠭⣿⣇⣀⠙⠢⣴⠉⠀⠠⣀⠤⣴⠾⠗⠒⢋⣿⣿⣿⣯⠅⠀⠀⠀⠉⠀
⠀⠀⠀⠀⢴⣖⣿⡛⢻⠿⣖⣦⣀⡀⢀⣠⠶⠿⢯⠉⠀⠘⢦⡀⠀⠘⢆⣸⣤⣴⣾⣿⣿⣿⣿⠙⢆⠀⠀⠀⠀⠀
⠀⠀⣠⠖⠀⣀⡈⡿⠈⢹⡿⢿⣌⠉⠁⠀⠳⡀⠈⣤⣴⠖⡾⠙⣦⣤⠜⠻⣿⣿⣍⣴⠋⣹⢧⣤⣀⠙⢦⡀⠀⠀
⠀⣰⠁⢠⣾⣿⠃⠇⢠⡿⠁⡈⢏⢳⡀⠀⠀⠹⡾⢋⡤⢴⣃⢤⡇⣙⣦⠀⠈⠹⣟⣿⣿⣦⣤⣬⣯⠱⡄⢳⠀⠀
⢠⠇⠀⡿⣹⠁⢠⣷⣿⠃⡄⢱⢸⠀⢇⠀⠀⠀⢀⣼⡀⣸⠃⠠⢡⣽⣿⡇⠀⣰⣛⡛⠦⠽⠿⠟⢻⡇⢸⠈⡆⠀
⢸⡄⠀⣧⢻⡀⠀⠉⠁⢠⠇⡜⣼⣠⠃⠀⣀⡴⠋⠀⠻⣄⠀⠒⣂⠀⠸⢀⠜⠛⢿⠯⣉⣳⡒⢒⣼⠇⢸⢀⠇⠀
⠀⢳⡀⠹⣟⠙⠢⠤⠒⣁⠜⣽⣹⢁⣤⣾⣛⣁⣀⣀⣀⣈⣛⣋⣁⣙⣦⡘⣆⠈⢣⡀⠈⣉⡿⠋⣠⢋⡜⠀⠀
⠀⠀⠑⢤⣀⠉⠑⢚⣉⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠈⠳⣄⠀⠉⠛⠓⠒⢉⣡⠞⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠈⠙⠒⠒⠒⠒⠉⠀
        """)
# Esto último es para cuando el usuario no elige entre todas las funciones que tiene el chatbot, diga que no lo entiende:
    else:
        print("No te he entendido, pero era un bonito intento de arte jaja")


# ---- MENÚ DE ACCIONES -------------------------------------------------------
# Esta parte sirve para dar las opciones que tiene el chatbot al usuario, definiendo la acción que introduce el resto de acciones:
def seleccionar_accion(nom):
    """Permite elegir qué quiere hacer el usuario."""
    print(nom + "," + " " +  "¿¿¿qué te apetece hacer???")
    eleccion = input("(hablar/broma/comparar/calcular/predecir/preguntar/dibujar/stop): ").lower()

# Y ahora, seria la parte de todas las acciones, pero resumido y corto gracias a las funciones antes definidas:
# Si el usuario decide parar, hace esto (después dire que es salir):
    if eleccion == "stop":
        print("Perfecto" + " " + nom + ", ¡ha sido un placer hablar contigo!")
        return "salir"
# Aquí si quiere hablar, pues se le "devuelve" hablar:
    elif eleccion == "hablar":
        return "hablar"
# Aquí si quiere broma, pues se le "devuelve" broma:    
    elif eleccion == "broma":
        hacer_broma()
# Aquí si quiere comparar, pues se le "devuelve" comparar:    
    elif eleccion == "comparar":
        comparar()
# Aquí si quiere calcular, pues se le "devuelve" calcular:    
    elif eleccion == "calcular":
        calcular()
# Aquí si quiere predecir, pues se le "devuelve" predecir:
    elif eleccion == "predecir":
        predecir()
# Aquí si quiere preguntar, pues se le "devuelve" preguntar:
    elif eleccion == "preguntar":
        preguntar_libre()
# Aquí si quiere dibujar, pues se le "devuelve" dibujar:
    elif eleccion == "dibujar":
        dibujar()
# Aquí si no entiende que quiere , pues se lo dice y le "devuelve" otra, que seria la acción de volver al menú general después de hacer algo:
    else:
        print("No te he entendido... ¿Podrias repetirlo" + " " + nom + "?")
    return "otra" 



##### Codi principal del xatbot ###############################################
#Este ya seria el codigo ENTERO RESUMIDO, que pasa, que esta parte es identica a la del programa, excepto por la linea de código de if __name__ == "__main__": que sirve para ejecutar un bloque de código únicamente cuando el archivo se ejecuta como script principal. Por tanto, pondré esta parte con asteriscos y la siguiente sin:
#Las primeras funciones que ha de hacer para presentarse
#saludar()
#nom = obtener_nombre()
    
#Aquí ya entra en el bucle para que cada vez que escoja una acción, pueda hacerla y, cuando acabe pueda escoger otra:
#while seguir_hablando:
    #accion = seleccionar_accion(nom)
# Si esa acción es salir, osea stop en el tablero, se dice que seguir_hablando es falso para romper el bucle:
    #if accion == "salir":
        #seguir_hablando = False
# Si la acción es hablar, se le plantean los 2 temas:
    #elif accion == "hablar":
        #tema = preguntar_tema(nom)
# Si quiere hablar de F1:
        #if any(p in tema for p in respuestas_f1):
            #hablar_f1(nom)
# Si quiere hablar de MotoGP
        #elif any(p in tema for p in respuestas_mgp):
            #hablar_motogp(nom)
# Si no reconoce de que hablar:
        #else:
            #print("No he entendido si hablas de F1 o MotoGP... ¿Podrias repetirlo" + " " + nom + "?")
# Si la acción fue otra, vuelve al menú general automáticamente


####### Programa ##############################################################
# Ahora sí, este sería el código ENTERO RESUMIDO junto a la línea de código que ya hemos mencionado antes:
if __name__ == "__main__":
#Las primeras funciones que ha de hacer para presentarse
    saludar()
    nom = obtener_nombre()
    
#Aquí ya entra en el bucle para que cada vez que escoja una acción, pueda hacerla y, cuando acabe pueda escoger otra:
    while seguir_hablando:
        accion = seleccionar_accion(nom)
# Si esa acción es salir, osea stop en el tablero, se dice que seguir_hablando es falso para romper el bucle:
        if accion == "salir":
            seguir_hablando = False
# Si la acción es hablar, se le plantean los 2 temas:
        elif accion == "hablar":
            tema = preguntar_tema(nom)
# Si quiere hablar de F1:
            if any(p in tema for p in respuestas_f1):
                hablar_f1(nom)
# Si quiere hablar de MotoGP
            elif any(p in tema for p in respuestas_mgp):
                hablar_motogp(nom)
# Si no reconoce de que hablar:
            else:
                print("No he entendido si hablas de F1 o MotoGP... ¿Podrias repetirlo" + " " + nom + "?")
# Si la acción fue otra, vuelve al menú general automáticamente
