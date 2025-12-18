# Saludar
salutació = "Holaaa"
print(salutació)
print("Soy DRS, tu chatbot especializado en Fórmula 1 y MotoGP:)")
# Preguntar el Nombre
# Escribe la pregunta
nom = input("¿¿¿Cómo te llamas amante del motor???")
# Decirle que seleccione la última palabra, no la última letra
nom = nom.split(" ")
nom = nom[-1]
# Escribir la respuesta (con el nombre incluido)
print("Perfecto" + " " + nom + " " + "encantado de conocerte" + 3*"!")
print("Estoy aquí para llevarte directo a la pista con toda la información que necesitas: desde noticias, resultados y horarios, hasta análisis, curiosidades y estadísticas de tus pilotos y equipos favoritos. ¿Quieres saber quién hizo la pole, qué estrategia usaron en boxes o cómo va el campeonato? Yo te lo cuento al instante. Ya sea que sigas cada vuelta o estés empezando en el mundo del motor, ¡estás en el lugar correcto! ¿Listo para activar el DRS?")
# Preguntes
p_principal = (nom + "," + " " + 3*"¿" + "Que te gusta más F1 o MotoGP" + 3*"?")
p1_F1 = ("¿De que piloto de F1 actual te gustaría hablar" + " " + nom + "?")
p2_F1 = ("Ahora, de que equipo de F1 quieres que hablemos" + " " + nom + "?")
p3_F1 = ("¿Por último, de que leyenda de F1 te gustaría saber más" + " " + nom + "?")
p1_MGP = ("¿De que piloto de MotoGP actual te gustaría hablar" + " " + nom + "?")
p2_MGP = ("Ahora, de que equipo de MotoGP quieres que hablemos" + " " + nom + "?")
p3_MGP = ("¿Por último, de que leyenda de MotoGP te gustaría saber más" + " " + nom + "?")
preguntafinal = ("¿¿¿Quieres parar de hablar" + " " + nom + " " + "o hablar de otro tema" +3*"?")
preguntasF1 = [p1_F1,p2_F1,p3_F1]
preguntasMGP = [p1_MGP,p2_MGP,p3_MGP]
# Preguntarle la pregunta principal que deriva al resto
#import numpy
p_principal_respuesta = input(p_principal).lower()
#Si dice que prefiere F1
if "F1" in p_principal_respuesta or "Formula 1" in p_principal_respuesta or "formula" in p_principal_respuesta or "f1" in p_principal_respuesta:
    p1_F1_respuesta = input (p1_F1).lower()
#Primera pregunta de F1 con todas sus opciones
    if "alonso" in p1_F1_respuesta or "fernando" in p1_F1_respuesta or "nano" in p1_F1_respuesta or "don fernando alonso" in p1_F1_respuesta:
        print ("¡¡¡Fernando Alonso me encanta!!! El Nano es un piloto español de Fórmula 1, nacido en Oviedo en 1981. Es considerado uno de los mejores conductores de su generación por su talento, inteligencia en carrera y determinación. Debutó en la F1 en 2001 y se convirtió en campeón del mundo con Renault en 2005 y 2006, siendo el piloto más joven en lograrlo en ese momento. A lo largo de su carrera ha competido con equipos como McLaren, Ferrari y Aston Martin, destacándose por su capacidad para exprimir al máximo cualquier coche. Su pasión, constancia y carisma lo han convertido en una leyenda del automovilismo.")

    elif "sainz" in p1_F1_respuesta or "carlos" in p1_F1_respuesta or "smooth operator" in p1_F1_respuesta:
        print ("¡¡¡Que buen piloto!!! Carlos Sainz me gusta mucho, nacido en Madrid en 1994, es un piloto español de Fórmula 1 e hijo del campeón de rally Carlos Sainz. Debutó en 2015 con Toro Rosso (hoy Racing Bulls) y ha pasado por equipos como Renault, McLaren y Ferrari. Desde 2025 compite con Williams Racing, donde busca liderar el regreso del equipo británico a los primeros puestos de la parrilla.")

    elif "verstappen" in p1_F1_respuesta or "max" in p1_F1_respuesta or "super max" in p1_F1_respuesta:
        print ("¡¡¡Me encanta tu elección!!! Actualmente opino que Max és el mejor piloto de la parrilla, nacido en Bélgica en 1997 y criado en los Países Bajos. Debutó en 2015 con Toro Rosso y rápidamente ascendió a Red Bull Racing, con quienes ha ganado múltiples campeonatos mundiales. Conocido por su agresividad, velocidad y consistencia, Verstappen ha marcado una nueva era en la F1 dominando gran parte de las últimas temporadas.")

    elif "antonelli" in p1_F1_respuesta or "kimi" in p1_F1_respuesta:
        print ("¡¡¡El Lamine Yamal de la F1 jaja!!! Kimi Antonelli es un joven piloto italiano considerado una de las mayores promesas del automovilismo actual. Nacido el 25 de agosto de 2006, ha sido parte del programa de desarrollo de Mercedes desde muy temprana edad. Con un impresionante palmarés en karting y campeonatos como la Fórmula 4 Italiana y ADAC F4, ha demostrado un talento excepcional y madurez en pista. En 2024 dio el salto a la Fórmula 2 con el equipo Prema, y muchos lo ven como un futuro piloto de Fórmula 1, posiblemente con Mercedes. Su estilo de conducción preciso y su enfoque profesional lo destacan como un nombre a seguir en los próximos años.")

    elif "piastri" in p1_F1_respuesta or "oscar" in p1_F1_respuesta:
        print ("¡¡¡Gran piloto!!! Nacido en Melbourne en 2001, es un piloto australiano de Fórmula 1. Tras destacar en Fórmula Renault, F3 y F2, debutó en 2023 con McLaren y rápidamente se consolidó como uno de los jóvenes más prometedores de la parrilla, logrando victorias y podios, incluso és capaz de pelear por algún mundial")

    elif "hülkenberg" in p1_F1_respuesta or "nico" in p1_F1_respuesta:
        print ("¡¡¡Buen piloto veterano!!! Nico Hülkenberg, nacido en 1987 en Alemania, es un piloto de Fórmula 1 que debutó en 2010 con Williams. Ha competido para varios equipos y ganó las 24 Horas de Le Mans en 2015. Conocido por su constancia, logró su primer podio en F1 en 2025 y actualmente corre con Sauber.")

    elif "bortoleto" in p1_F1_respuesta or "gabriel" in p1_F1_respuesta:
        print ("¡¡¡Que joven promesa!!! Gabriel Bortoleto, nacido en 2004 en Brasil, es un joven piloto de Fórmula 1 que debutó en 2025 con Sauber. Campeón de Fórmula 2 en 2024, se ha destacado por su rápida adaptación y se perfila como una de las grandes promesas del automovilismo brasileño.")
    
    elif "colapinto" in p1_F1_respuesta or "franco" in p1_F1_respuesta:
        print ("¡¡¡Vaya piloto boludo!!! Franco Colapinto, nacido en 2003 en Argentina, es un piloto de Fórmula 1 que debutó en 2024 con Williams. En 2025 se unió a Alpine como titular tras la salida de Jack Doohan, destacando por su rapidez y talento, y representando el regreso del automovilismo argentino a la F1.")

    elif "leclerc" in p1_F1_respuesta or "charles" in p1_F1_respuesta or "il predestinato" in p1_F1_respuesta:
        print ("¡¡¡Il predestinato de Ferrari!!! Charles Leclerc es un piloto monegasco de Fórmula 1 nacido en 1997. Debutó en 2018 y desde 2019 corre para Ferrari. Destaca por su velocidad, talento y determinación, siendo una de las grandes promesas del automovilismo.")

    elif "russell" in p1_F1_respuesta or "george" in p1_F1_respuesta:
        print ("El hombre invisible jaja, ¡¡¡que gran piloto!!! George Russell es un piloto británico de Fórmula 1 nacido en 1998. Debutó en 2019 con Williams y desde 2022 corre para Mercedes. Es reconocido por su consistencia, talento y gran potencial en la parrilla.")

    elif "perez" in p1_F1_respuesta or "checo" in p1_F1_respuesta or "sergio" in p1_F1_respuesta or "bottas" in p1_F1_respuesta or "valtteri" in p1_F1_respuesta:
        print ("¡¡¡El veterano de Callidac!!! Vaya piloto, su nombre ya forma parte de la F1 siendo de los más veteranos en este siglo XXI. Deseando volverlo a ver el año que viene en las pistas, ¡¡¡estoy seguro que lo hará genial!!!")

    elif "norris" in p1_F1_respuesta or "lando" in p1_F1_respuesta:
        print ("¡¡¡Buen piloto la verdad!!! Lando Norris es un piloto británico de Fórmula 1 nacido en 1999. Debutó en 2019 con McLaren y se ha destacado por su velocidad y carisma dentro y fuera de las pistas aunque creo que no es muy regular, el talento lo tiene.")
    
    elif "bearman" in p1_F1_respuesta or "oliver" in p1_F1_respuesta or "oso" in p1_F1_respuesta or "hadjar" in p1_F1_respuesta or "isack" in p1_F1_respuesta:
        print ("¡¡¡Vaya Rookie has escogido!!! Le veo un futuro prometedor a este piloto. Las pocas carreras que ha disputado en la categoria reina ya ha demostrado su gran talento, ¡¡¡Dale unos años y un buen coche y verás!!!")

    elif "gasly" in p1_F1_respuesta or "pierre" in p1_F1_respuesta or "lawson" in p1_F1_respuesta or "liam" in p1_F1_respuesta or "albon" in p1_F1_respuesta or "alex" in p1_F1_respuesta or "tsunoda" in p1_F1_respuesta or "yuki" in p1_F1_respuesta or "stroll" in p1_F1_respuesta or "lance" in p1_F1_respuesta:
        print ("Bueno... No es mal piloto la verdad, no me gusta especialmente pero he de decir que más de una vez me ha callado la boca haciendo alguna carrera expectacular... Pero poco más jaja")

#Estos no me caen tan bien, entonces al decir mi opinión le pregunto si quiere seguir hablando, ya que no estoy de acuerdo:
    elif "hamilton" in p1_F1_respuesta or "lewis" in p1_F1_respuesta:
        pregunta_hamilton = input ("¿De verdad quieres saber más de él" + " " + nom + 3*"?").lower()
        if "si" in pregunta_hamilton or "por" in pregunta_hamilton or "supuesto" in pregunta_hamilton or "claro que si" in pregunta_hamilton:
            print ("Madre mía... No es por nada pero Hamilton no es buen piloto, vale que tiene muchos titulos pero si no le dan un coche 5 segundos más rapido que los otros, se te pone a llorar como un bebe. Espero que te haga reflexionar mi opinión.")
            print ("Igualmente... Toma lo que buscas: Lewis Hamilton es un piloto británico de Fórmula 1 y siete veces campeón del mundo. Debutó en 2007 con McLaren y se consolidó con Mercedes como uno de los más grandes de la historia. Además de su éxito en pista, es reconocido por su activismo y compromiso social.")
            pregunta_hamiltocon = input ("Viendo que piloto me has dicho y que a mí no me gusta... ¿¿Quieres seguir hablando??").lower()
            if "si" in pregunta_hamiltocon or "vale" in pregunta_hamiltocon:
                print ("Vale, pero que sepas que no estoy de acuerdo con que te guste este piloto ehh")
            elif "no" in pregunta_hamiltocon:
                print ("¿¿¿No??? Pues ahora te aguantas jaja")


    elif "ocon" in p1_F1_respuesta or "esteban" in p1_F1_respuesta:
        pregunta_ocon = input ("Jajajaja," + " " + nom + " " + 3*"¿" + "enserio quieres saber más sobre ese personaje" + 3*"?").lower()
        if "si" in pregunta_ocon or "por" in pregunta_ocon or "supuesto" in pregunta_ocon or "claro que si" in pregunta_ocon:
            print ("Yo lo siento pero por ahí no paso... Ocon no sirve para nada... Es inútil jaja, y encima francés.")
            pregunta_hamiltocon = input ("Viendo que piloto te gusta y que no estamos de acuerdo... ¿¿Quieres seguir hablando??").lower()
            if "si" in pregunta_hamiltocon or "vale" in pregunta_hamiltocon:
                print ("Vale, pero que sepas que no estoy de acuerdo con que te guste este piloto ehh")
            elif "no" in pregunta_hamiltocon:
                print ("¿¿¿No??? Pues ahora te aguantas jaja")
#Aquí la segunda respuesta de F1 con todas sus opciones:                  
    p2_F1_respuesta = input(p2_F1).lower()
    if "ferrari" in p2_F1_respuesta:
        print ("¡¡¡Fuaaa, mi equipo favorito jaja!!! La Scuderia Ferrari es el equipo más legendario de la Fórmula 1. Fundado en 1929 por Enzo Ferrari, ha estado presente desde la primera temporada del campeonato en 1950. Con su icónico color rojo y el famoso 'Cavallino Rampante' (caballo rampante), Ferrari representa pasión, tradición y excelencia automovilística. Es el equipo con más títulos en la historia de la F1, incluyendo campeonatos de pilotos y constructores. Pilotos históricos como Fernando Alonso, Michael Schumacher, Niki Lauda y Gilles Villeneuve han dejado su huella en Maranello. Soñar con pilotar para Ferrari es soñar con formar parte de la historia misma del automovilismo.")
    elif "mclaren" in p2_F1_respuesta:
        print ("¡¡¡Buena elección!!! McLaren es uno de los equipos más históricos y prestigiosos de la Fórmula 1. Fundado en 1963 por Bruce McLaren, el equipo británico ha ganado múltiples campeonatos del mundo y ha sido la cuna de leyendas como Fernando Alonso, Ayrton Senna, Alain Prost, Niki Lauda y Lewis Hamilton. Conocido por su innovación tecnológica y su espíritu competitivo, McLaren siempre ha sido un símbolo de velocidad, elegancia y evolución. Pilotar para McLaren es formar parte de una historia llena de gloria y también de futuro prometedor.")
    elif "aston" in p2_F1_respuesta or "martin" in p2_F1_respuesta:
        print ("¡Buena elección! Aston Martin, antes conocido como Racing Point y Force India, es un equipo con una historia reciente pero llena de evolución y lucha. Han contado con pilotos destacados como Sebastian Vettel y, por supuesto, Fernando Alonso, uno de los mejores de todos los tiempos. Con la llegada de Aston Martin en 2021, el equipo combina la tradición británica con ambición y tecnología avanzada. Pilotar aquí significa formar parte de un proyecto joven pero con grandes aspiraciones en la Fórmula 1.")
    elif "amg" in p2_F1_respuesta or "silver" in p2_F1_respuesta or "mercedes" in p2_F1_respuesta or "plateadas" in p2_F1_respuesta:
        print ("¡¡¡Una elección top!!! Mercedes es uno de los equipos más exitosos de la era moderna en Fórmula 1, con múltiples campeonatos de constructores y pilotos, especialmente durante su dominio con Lewis Hamilton. Es sinónimo de innovación, potencia y precisión alemana. Además, el joven talento Kimi Antonelli está fuertemente vinculado al futuro del equipo, siendo considerado uno de los pilotos más prometedores de su generación. Pilotar para Mercedes es estar en el corazón de la élite del automovilismo.")
    elif "red" in p2_F1_respuesta or "bull" in p2_F1_respuesta:
        print ("¡¡¡Una elección llena de adrenalina!!! Red Bull Racing es uno de los equipos más exitosos de las últimas décadas en Fórmula 1. Conocidos por su enfoque innovador y agresivo, dominaron una era con Sebastian Vettel y están volviendo a hacerlo con Max Verstappen. Su filosofía joven, audaz y orientada al rendimiento ha revolucionado el deporte. Pilotar para Red Bull significa estar en un equipo que no solo busca ganar, sino hacerlo con estilo y velocidad pura.")
    elif "williams" in p2_F1_respuesta:
        print ("¡¡¡Una elección con mucha historia!!! Williams es uno de los equipos más legendarios de la Fórmula 1, con múltiples campeonatos en su palmarés y una rica trayectoria que comenzó en 1977. Fue cuna de campeones como Nigel Mansell, Alain Prost y Ayrton Senna. Aunque en los últimos años ha enfrentado desafíos, ahora vuelven poco a poco a la cima. Por ello, sigue siendo un equipo con gran tradición y pasión por las carreras. Pilotar para Williams es ser parte de un legado histórico, con la misión de devolverlo a lo más alto.")
    elif "alpine" in p2_F1_respuesta or "renault" in p2_F1_respuesta or "bwt" in p2_F1_respuesta:
        print ("¡¡¡Muy buena elección!!! Alpine es la actual identidad del equipo Renault en la Fórmula 1, una escudería con una larga historia en el deporte. Bajo el nombre de Renault, fue donde Fernando Alonso logró sus dos campeonatos del mundo en 2005 y 2006, y volvió a correr tanto en 2008-2009 como en su etapa más reciente con Alpine entre 2021 y 2022. El equipo combina la experiencia de años en la F1 con el respaldo tecnológico del Grupo Renault y una visión ambiciosa hacia el futuro. Pilotar para Alpine es formar parte de un legado donde ya brillaron campeones, y donde aún se busca volver a lo más alto.")
    elif "sauber" in p2_F1_respuesta or "kick" in p2_F1_respuesta or "stake" in p2_F1_respuesta or "audi" in p2_F1_respuesta:
        print ("¡¡¡Una elección estratégica e interesante!!! El equipo Sauber, actualmente conocido como Kick Sauber, tiene una larga trayectoria en la Fórmula 1 desde los años 90, siendo una escudería reconocida por su capacidad para desarrollar talento y mantenerse competitiva con recursos limitados. En el pasado, compitió bajo el nombre de Alfa Romeo, y ahora se prepara para un futuro muy prometedor: en 2026 se convertirá oficialmente en el equipo oficial de Audi. Pilotar para Sauber hoy es estar en la antesala de uno de los proyectos más ambiciosos que veremos en la nueva era de la F1.")
    elif "haas" in p2_F1_respuesta or "money" in p2_F1_respuesta or "gram" in p2_F1_respuesta:
        print ("¡¡¡Una elección con carácter propio!!! Haas es el primer equipo estadounidense en la Fórmula 1 en varias décadas, debutando en 2016. Aunque es uno de los equipos más jóvenes del paddock, ha logrado hacerse un lugar gracias a su enfoque práctico y su asociación técnica con Ferrari. A lo largo de los años ha contado con pilotos experimentados y jóvenes promesas, siendo un equipo que sigue construyendo su camino en el deporte. Pilotar para Haas es aceptar el desafío de crecer junto a una escudería con mucho potencial.")
    elif "rb" in p2_F1_respuesta or "racing" in p2_F1_respuesta or "bulls" in p2_F1_respuesta or "visa" in p2_F1_respuesta or "cash" in p2_F1_respuesta:
        print ("¡Una elección con mucho futuro! Racing Bulls, anteriormente conocida como AlphaTauri y Toro Rosso, es el equipo filial de Red Bull Racing. A lo largo de los años ha sido una plataforma clave para desarrollar jóvenes talentos, como Sebastian Vettel —quien logró aquí su primera victoria— y más recientemente pilotos como Pierre Gasly o Yuki Tsunoda. Con una imagen renovada y mayor integración técnica con Red Bull, RB está creciendo como un equipo competitivo por derecho propio. Pilotar para Racing Bulls es estar en el radar directo de los campeones, con la oportunidad de brillar y dar el salto a lo más alto.")
#Ahora la última pregunta de F1, con sus diferentes opciones de respuestas
    p3_F1_respuesta = input(p3_F1).lower()
    if "schumacher" in p3_F1_respuesta or "michael" in p3_F1_respuesta or "kaiser" in p3_F1_respuesta:
        print ("Michael Schumacher es uno de los nombres más grandes en la historia de la Fórmula 1. Con 7 campeonatos del mundo y 91 victorias, dominó la era moderna con Ferrari y estableció estándares de excelencia y trabajo en equipo que aún inspiran, me gusta tu elección jaja.")
        
    elif "hamilton" in p3_F1_respuesta or "lewis" in p3_F1_respuesta:
        print ("Aunque no me guste mucho, he de decir que Lewis Hamilton es una superestrella del automovilismo, con 7 títulos mundiales y récords en victorias y poles. Más allá de su talento, es un referente en la lucha por la diversidad y la igualdad dentro y fuera de la pista.")
        
    elif "verstappen" in p3_F1_respuesta or "max" in p3_F1_respuesta:
        print ("Max Verstappen es la joven estrella que ha revolucionado la F1 en los últimos años. Con ya 4 campeonatos, es conocido por su agresividad y consistencia, y se perfila como una leyenda en activo del deporte, increible tu elección, buen gusto jaja.")
            
    elif "senna" in p3_F1_respuesta or "ayrton" in p3_F1_respuesta:
        print ("Ayrton Senna es una leyenda eterna de la F1, recordado por su increíble velocidad, carisma y espíritu competitivo. Sus 3 campeonatos y su trágica partida dejaron una huella imborrable en el deporte, increible tu elección, buen gusto jaja.")
            
    elif "prost" in p3_F1_respuesta or "alain" in p3_F1_respuesta:
        print ("Conocido como 'El Profesor', Alain Prost fue un piloto cerebral y estratégico, con 4 títulos mundiales. Su enfoque metódico y calma en pista le valieron un lugar especial en la historia de la F1, me gusta tu elección jaja.")
            
    elif "fangio" in p3_F1_respuesta or "juan" in p3_F1_respuesta or "manuel" in p3_F1_respuesta:
        print ("El argentino Juan Manuel Fangio dominó la Fórmula 1 en los años 50 con 5 campeonatos. Su elegancia y habilidad técnica marcaron el inicio de la era de las leyendas en el deporte, me gusta tu elección jaja.")
            
    elif "lauda" in p3_F1_respuesta or "niki" in p3_F1_respuesta:
        print ("Niki Lauda es símbolo de coraje y resiliencia. Tras un grave accidente en 1976, volvió a competir y ganó 3 títulos mundiales, dejando un legado imborrable de fortaleza y profesionalismo, increible tu elección, buen gusto jaja.")
            
    elif "alonso" in p3_F1_respuesta or "fernando" in p3_F1_respuesta or "Nano" in p3_F1_respuesta:
        print ("Fernando Alonso es uno de los pilotos más completos y longevos de la F1, con 2 campeonatos y una carrera que abarca más de dos décadas. Su talento y determinación lo mantienen en la élite, increible tu elección, buen gusto jaja.")
            
    elif "vettel" in p3_F1_respuesta or "sebastian" in p3_F1_respuesta:
        print ("Sebastian Vettel brilló con 4 títulos consecutivos en Red Bull, demostrando velocidad, inteligencia y carácter. Además, es un referente por su compromiso fuera de las pistas, me gusta tu elección jaja.")
            
    elif "surtees" in p3_F1_respuesta or "john" in p3_F1_respuesta:
        print ("John Surtees es único en la historia: campeón mundial tanto en motociclismo como en Fórmula 1. Su versatilidad y talento le dieron un lugar destacado en el automovilismo, no me esperaba esa respuesta pero veo que tienes sabios gustos jaja.")
    
    elif "pedro" in p3_F1_respuesta or "rosa" in p3_F1_respuesta or "de" in p3_F1_respuesta or "la" in p3_F1_respuesta:
        print ("Pedro de la Rosa es un piloto español de Fórmula 1 conocido por su talento y experiencia. Compitió en varias temporadas principalmente como piloto de pruebas y titular para equipos como Arrows, Jaguar y McLaren. Destacado por su habilidad técnica, también ha trabajado como comentarista y embajador del automovilismo en España.")
    
    elif "mazepin" in p3_F1_respuesta or "nikita" in p3_F1_respuesta:
        print ("Nikita Mazepin es un piloto ruso de Fórmula 1 que compitió en la temporada 2021 con el equipo Haas. Proveniente de una familia con fuerte apoyo financiero, su paso por la F1 fue controvertido y recibió críticas por su desempeño y comportamiento fuera de pista. Tras una única temporada, perdió su asiento y actualmente no participa en la Fórmula 1.")

    elif "latifi" in p3_F1_respuesta or "nicholas" in p3_F1_respuesta:
        print ("Nicholas Latifi es un piloto canadiense de Fórmula 1 que compitió principalmente con el equipo Williams entre 2020 y 2022. Reconocido por su perseverancia y esfuerzo, aunque sin grandes resultados destacados, se destacó por su profesionalismo y dedicación en el deporte. También tiene experiencia en categorías inferiores como la Fórmula 2.")


#Usuario le gusta F1
usuario_prefiere_F1 = "F1"
#Si en la pregunta principal se dice MotoGP    
if "motoGP" in p_principal_respuesta or "gp" in p_principal_respuesta or "moto" in p_principal_respuesta:
    p1_MGP_respuesta = input (p1_MGP).lower()
    if "marc" in p1_MGP_respuesta or "hormiga" in p1_MGP_respuesta or "trueno" in p1_MGP_respuesta:
        print ("¡¡¡Mi piloto favorito!!! Nacido en Cervera, España, Marc Márquez es una leyenda viva del motociclismo. Desde su debut en MotoGP en 2013, se hizo famoso por su estilo agresivo, adelantamientos imposibles y una ambición sin frenos. Conquistó 8 títulos mundiales (6 en la categoría reina) y dominó junto a Honda durante años, hasta que las lesiones complicaron su camino a partir de 2020. En 2023 y 2024 sorprendió al pasar al equipo Gresini Ducati, donde volvió a mostrar destellos de su mejor versión. Ahora, en 2025, Marc se une al equipo oficial Ducati, montando la mejor moto de la parrilla. Superando con mucha ventaja al resto de pilotos ha logrado su objetivo: volver a lo más alto y sumar su noveno título mundial. Marc no solo corre al límite: vive allí. Y esa es justamente la esencia que lo convierte en uno de los grandes de todos los tiempos.")
    
    elif "alex" in p1_MGP_respuesta:
        print ("¡¡¡Mi otro piloto favorito!!! Nacido en Cervera, como su hermano Marc, Álex Márquez ha forjado su propio camino en el motociclismo con constancia y determinación. Campeón del mundo en Moto3 (2014) y Moto2 (2019), llegó a MotoGP en 2020 con el equipo oficial Honda, logrando dos podios en su temporada de debut. Tras un paso por LCR Honda, en 2023 dio un nuevo aire a su carrera al fichar por Gresini Ducati, donde rápidamente se adaptó a la Desmosedici y volvió a luchar en posiciones de cabeza. Su estilo técnico y limpio, combinado con mayor confianza, le han permitido crecer como piloto dentro de una categoría cada vez más competitiva. En 2025, Álex sigue consolidado como una pieza clave del proyecto Gresini, demostrando que no vive a la sombra de nadie: su talento y trabajo hablan por sí solos. Con experiencia, velocidad y mentalidad fuerte, Álex Márquez sigue buscando su lugar en la historia de MotoGP... y cada año está más cerca.")
    
    elif "márquez" in p1_MGP_respuesta or "marquez" in p1_MGP_respuesta:
        pregunta_marquez_respuesta = input ("¿¿¿Pero a que Márquez te refieres jaja???").lower()
        if "Marc" in pregunta_marquez_respuesta or "marc" in pregunta_marquez_respuesta:
            print ("Vale vale, ahora me aclaro jaja ¡¡¡Adoro al mayor de los Márquez!!! Nacido en Cervera, España, Marc Márquez es una leyenda viva del motociclismo. Desde su debut en MotoGP en 2013, se hizo famoso por su estilo agresivo, adelantamientos imposibles y una ambición sin frenos. Conquistó 8 títulos mundiales (6 en la categoría reina) y dominó junto a Honda durante años, hasta que las lesiones complicaron su camino a partir de 2020. En 2023 y 2024 sorprendió al pasar al equipo Gresini Ducati, donde volvió a mostrar destellos de su mejor versión. Ahora, en 2025, Marc se une al equipo oficial Ducati, montando la mejor moto de la parrilla. Superando con mucha ventaja al resto de pilotos ha logrado su objetivo: volver a lo más alto y sumar su noveno título mundial. Marc no solo corre al límite: vive allí. Y esa es justamente la esencia que lo convierte en uno de los grandes de todos los tiempos.")
        elif "Alex" in pregunta_marquez_respuesta or "alex" in pregunta_marquez_respuesta:
            print ("Vale vale, ahora me aclaro jaja ¡¡¡Adoro al menor de los Márquez!!! Nacido en Cervera, como su hermano Marc, Álex Márquez ha forjado su propio camino en el motociclismo con constancia y determinación. Campeón del mundo en Moto3 (2014) y Moto2 (2019), llegó a MotoGP en 2020 con el equipo oficial Honda, logrando dos podios en su temporada de debut. Tras un paso por LCR Honda, en 2023 dio un nuevo aire a su carrera al fichar por Gresini Ducati, donde rápidamente se adaptó a la Desmosedici y volvió a luchar en posiciones de cabeza. Su estilo técnico y limpio, combinado con mayor confianza, le han permitido crecer como piloto dentro de una categoría cada vez más competitiva. En 2025, Álex sigue consolidado como una pieza clave del proyecto Gresini, demostrando que no vive a la sombra de nadie: su talento y trabajo hablan por sí solos. Con experiencia, velocidad y mentalidad fuerte, Álex Márquez sigue buscando su lugar en la historia de MotoGP... y cada año está más cerca.")

    elif "acosta" in p1_MGP_respuesta or "pedro" in p1_MGP_respuesta:
        print ("¡¡¡Me encanta tu elección!!! Con solo 21 años, Pedro Acosta ya es una de las mayores promesas de MotoGP. Campeón de Moto3 en 2021 en su temporada debut y de Moto2 en 2023, llegó a la categoría reina en 2024 con el equipo GasGas Tech3 KTM, demostrando madurez, velocidad y una confianza fuera de lo común. En 2025, Acosta sigue creciendo como piloto oficial KTM, mezclando agresividad e inteligencia en pista. Su estilo audaz y su capacidad para adaptarse rápidamente lo colocan como un firme candidato a ser campeón en muy poco tiempo. El futuro ya llegó, y se llama Pedro Acosta.")

    elif "martin" in p1_MGP_respuesta or "jorge" in p1_MGP_respuesta:
        print ("¡¡¡Vaya pilotazo!!! Jorge Martín, campeón del mundo de Moto3 en 2018, se ha consolidado como uno de los pilotos más rápidos y consistentes de MotoGP, y en 2025, tras años de lucha con Ducati Pramac, finalmente corre para el equipo oficial Aprilia, decidido a conquistar el título que ha rozado en temporadas anteriores.")

    elif "mir" in p1_MGP_respuesta or "joan" in p1_MGP_respuesta:
        print ("¡¡¡Que piloto!!! Joan Mir, campeón del mundo de MotoGP en 2020 con Suzuki, es un piloto de talento sólido y mentalidad fuerte que en 2025 sigue luchando por volver a lo más alto, ahora intentando recuperar sensaciones tras años difíciles en Honda.")

    elif "fernandez" in p1_MGP_respuesta or "raul" in p1_MGP_respuesta:
        print ("¡¡¡Que joven piloto!!! Raúl Fernández, subcampeón de Moto2 en 2021 tras una temporada espectacular, sigue buscando su lugar en MotoGP y en 2025 compite con Trackhouse Aprilia, decidido a demostrar todo su potencial en la categoría reina.")
    
    elif "aldeguer" in p1_MGP_respuesta or "fermin" in p1_MGP_respuesta:
        print ("¡¡¡Vaya Rookie!!! Fermín Aldeguer, una de las jóvenes promesas más destacadas del motociclismo español, llega a MotoGP en 2025 con el equipo Pramac Ducati tras un cierre de temporada dominante en Moto2, listo para dejar huella desde su debut en la categoría reina.")

    elif "bagnaia" in p1_MGP_respuesta or "pecco" in p1_MGP_respuesta or "francesco" in p1_MGP_respuesta:
        print ("¡¡¡!Buen piloto!! Pecco Bagnaia, campeón de MotoGP en 2022 con Ducati, es uno de los pilotos más completos y competitivos de la parrilla, y en 2025 continúa en el equipo oficial Ducati.")

    elif "bezzecchi" in p1_MGP_respuesta or "marco" in p1_MGP_respuesta:
        print ("¡¡¡Que gran elección!!! Marco Bezzecchi, piloto italiano talentoso y constante, compite en 2025 con la Aprilia, consolidándose como uno de los jóvenes talentos en alza dentro de MotoGP, con grandes expectativas para las próximas temporadas.")

    elif "quartararo" in p1_MGP_respuesta or "fabio" in p1_MGP_respuesta or "diablo" in p1_MGP_respuesta:
        print ("¡¡¡El diablo!!! Fabio Quartararo, campeón de MotoGP en 2021 con Yamaha, es un piloto rápido y agresivo que en 2025 sigue luchando por el título, enfrentando una temporada desafiante con un equipo Yamaha en plena evolución.")

    elif "ogura" in p1_MGP_respuesta or "ai" in p1_MGP_respuesta:
        print ("¡¡¡Buen Rookie la verdad!!! Ai Ogura, joven talento japonés de Moto2, destaca por su constancia y velocidad, y en 2025 busca seguir creciendo y dar el salto definitivo hacia MotoGP en un futuro cercano.")
    
    elif "binder" in p1_MGP_respuesta or "brad" in p1_MGP_respuesta or "maverick" in p1_MGP_respuesta or "viñales" in p1_MGP_respuesta or "zarco" in p1_MGP_respuesta or "johann" in p1_MGP_respuesta or "rins" in p1_MGP_respuesta or "oliveira" in p1_MGP_respuesta or "miguel" in p1_MGP_respuesta or "miller" in p1_MGP_respuesta or "jack" in p1_MGP_respuesta:
        print ("¡¡¡Buena elección!!! “La verdad es que es un piloto constante y competente, que aporta buen nivel aunque no suele destacar mucho, pero siempre está listo para aprovechar su oportunidad.”")

    elif "bastianini" in p1_MGP_respuesta or "enea" in p1_MGP_respuesta or "di" in p1_MGP_respuesta or "giannantonio" in p1_MGP_respuesta or "morbidelli" in p1_MGP_respuesta or "franco" in p1_MGP_respuesta or "marini" in p1_MGP_respuesta or "luca" in p1_MGP_respuesta:
        print ("¡¡¡Que piloto!!! La verdad es que es un piloto muy competitivo y constante, que suele estar cerca de los líderes y puede pelear por podios, aunque todavía le falta dar ese salto para ser de los mejores.")

    elif "chantra" in p1_MGP_respuesta or "somkiat" in p1_MGP_respuesta:
        print ("Que gracioso eres jaja")
    
                  
    p2_MGP_respuesta = input(p2_MGP).lower()
    if "ducati" in p2_MGP_respuesta or "corse" in p2_MGP_respuesta or "lenovo" in p2_MGP_respuesta:
        print ("¡¡¡Fuaaa, es de mis equipos favoritos jaja!!! Ducati Lenovo es uno de los equipos más fuertes y consistentes de MotoGP. Con una moto potente y tecnología de punta, siempre están en la pelea por victorias y campeonatos. Su combinación de pilotos talentosos y un gran trabajo en el desarrollo los convierte en un rival difícil de superar en cualquier circuito.")
    elif "aprilia" in p2_MGP_respuesta:
        print ("¡¡¡Buena elección!!! Aprilia Racing es un equipo en plena evolución, cada año mostrando mejoras significativas en MotoGP. Con pilotos jóvenes y talentosos, y una moto cada vez más competitiva, están creciendo como un serio rival para los equipos punteros y buscando consolidarse en la lucha por podios y victorias.")
    elif "gresini" in p2_MGP_respuesta or "bk8" in p2_MGP_respuesta:
        print ("¡¡¡Fuaaa, es de mis equipos favoritos jaja!!! BK8 Gresini Racing es un equipo con gran tradición y pasión en MotoGP, que ha sabido combinar experiencia y juventud para mantenerse competitivo. Con pilotos que aportan talento y ganas de crecer, y una alianza sólida con Ducati, siguen luchando para subir al podio y consolidarse entre los mejores.")
    elif "honda" in p2_MGP_respuesta or "hrc" in p2_MGP_respuesta:
        print ("¡¡¡Una elección top!!! Honda HRC Castrol es uno de los equipos históricos y más icónicos de MotoGP, con una larga tradición de campeonatos y pilotos legendarios. Aunque en los últimos años han enfrentado desafíos técnicos y de rendimiento, siguen trabajando duro para recuperar su lugar en la cima, apoyados en la experiencia de sus pilotos y la innovación constante.")
    elif "lcr" in p2_MGP_respuesta:
        print ("¡¡¡Wow!!! LCR Honda es un equipo independiente con mucha historia en MotoGP, conocido por su profesionalismo y constancia. Aunque no siempre cuenta con las motos más punteras, ha logrado resultados destacados gracias al talento y esfuerzo de sus pilotos, manteniéndose competitivo y luchando en cada carrera.")
    elif "monster" in p2_MGP_respuesta or "energy" in p2_MGP_respuesta or "yamaha" in p2_MGP_respuesta:
        print ("¡¡¡Una elección llena de adrenalina!!! Monster Energy Yamaha es uno de los equipos más emblemáticos de MotoGP, con una gran historia de éxitos y campeones. Aunque en los últimos años ha enfrentado altibajos y retos técnicos, sigue siendo un equipo competitivo con pilotos talentosos que luchan por volver a dominar la categoría.")
    elif "vr46" in p2_MGP_respuesta or "vr" in p2_MGP_respuesta:
        print ("¡¡¡Muy buena elección!!! VR46 Racing Team es el equipo fundado por Valentino Rossi que ha crecido rápidamente en MotoGP. Con un enfoque joven y ambicioso, apoyado en talento emergente y la colaboración con Ducati, busca consolidarse como una referencia en la categoría y luchar por podios y victorias.")
    elif "prima" in p2_MGP_respuesta or "pramac" in p2_MGP_respuesta:
        print ("¡¡¡Una elección estratégica e interesante!!! Prima Pramac Racing es un equipo sólido y con mucha experiencia en MotoGP, que combina pilotos veteranos y con talento con una estrecha colaboración con Yamaha. Siempre están en la pelea por buenos resultados y buscan crecer temporada tras temporada para acercarse a los equipos punteros.")
    elif "ktm" in p2_MGP_respuesta:
        print ("¡¡¡Una elección con carácter propio!!! KTM Factory Racing Team es un equipo joven pero ambicioso en MotoGP, conocido por su innovación y progreso constante. Con pilotos veloces y una moto en evolución, trabajan duro para consolidarse como candidatos a podios y victorias en una categoría cada vez más competitiva.")
    elif "3" in p2_MGP_respuesta or "tech" in p2_MGP_respuesta:
        print ("¡Una elección con mucho futuro! Tech3 KTM Factory Racing es un equipo satélite con gran experiencia en MotoGP, dedicado a desarrollar talento joven y ayudar en la evolución técnica de KTM. Aunque no siempre está en el podio, cumple un papel clave formando pilotos y aportando datos valiosos para el equipo oficial.")
    elif "trackhouse" in p2_MGP_respuesta:
        print ("¡Una elección con mucho futuro! Trackhouse Racing es el nuevo equipo estadounidense en MotoGP que llegó en 2024 con una propuesta fresca, moderna y ambiciosa. Con estructura sólida y el respaldo de Aprilia, buscan crecer rápidamente en la categoría, apostando por pilotos jóvenes y una identidad muy marcada dentro y fuera de la pista.")
        
    p3_MGP_respuesta = input(p3_MGP).lower()
    if "agostini" in p3_MGP_respuesta or "giacomo" in p3_MGP_respuesta:
        print ("Giacomo Agostini ostenta un récord histórico con 15 títulos mundiales, logrados principalmente en las categorías de 350cc y 500cc. Fue el dominador absoluto de los años 60 y 70, corriendo para marcas míticas como MV Agusta. Su legado permanece intacto como uno de los más grandes campeones que ha dado el motociclismo.")
        
    elif "nieto" in p3_MGP_respuesta or "angel" in p3_MGP_respuesta:
        print ("Ángel Nieto es una auténtica leyenda del motociclismo español, con 13 títulos mundiales (12+1, como él decía por superstición). Dominó las categorías de 50cc y 125cc, y fue pionero en abrir el camino para que España se convirtiera en una potencia del motociclismo mundial. Su figura es irreemplazable en la historia del deporte.")
        
    elif "marquez" in p3_MGP_respuesta or "marc" in p3_MGP_respuesta or "Marc" in p3_MGP_respuesta:
        print ("Marc Márquez cambió las reglas del juego en MotoGP desde su llegada en 2013. Con 8 títulos mundiales y un estilo espectacular basado en salvadas imposibles y agresividad total, marcó una era con Honda. A pesar de las lesiones, su espíritu de lucha y talento siguen haciendo historia.")
            
    elif "doohan" in p3_MGP_respuesta or "mick" in p3_MGP_respuesta:
        print ("Mick Doohan fue el piloto más dominante de la década de los 90, con cinco títulos consecutivos en 500cc entre 1994 y 1998. Su control absoluto sobre la moto y su fortaleza mental lo convirtieron en una leyenda con Honda. Su rivalidad con Crivillé y sus remontadas épicas lo hacen inolvidable.")
            
    elif "stoner" in p3_MGP_respuesta or "casey" in p3_MGP_respuesta:
        print ("Casey Stoner fue campeón del mundo en 2007 con Ducati y en 2011 con Honda, destacándose por su talento natural y velocidad en cualquier condición. Aunque su carrera fue corta, dejó una huella profunda por su pilotaje agresivo, directo y sin concesiones. Uno de los grandes talentos puros de MotoGP.")
            
    elif "lorenzo" in p3_MGP_respuesta or "jorge" in p3_MGP_respuesta:
        print ("Jorge Lorenzo fue campeón del mundo en cinco ocasiones, tres de ellas en MotoGP. Su estilo de pilotaje limpio, rápido y constante lo convirtió en uno de los grandes rivales de Valentino Rossi y Marc Márquez. Fue un perfeccionista dentro y fuera de la pista, con una enorme capacidad para mantener el ritmo de carrera.")
            
    elif "rainey" in p3_MGP_respuesta or "wayne" in p3_MGP_respuesta:
        print ("Wayne Rainey fue uno de los grandes nombres de los 90, con tres títulos en 500cc. Su pilotaje técnico y fino, junto con una mentalidad fuerte, lo llevaron a dominar una era muy competitiva. Su carrera se vio truncada por una lesión, pero su legado como luchador sigue presente.")
            
    elif "schwantz" in p3_MGP_respuesta or "kevin" in p3_MGP_respuesta:
        print ("Kevin Schwantz fue campeón del mundo en 1993 y se convirtió en uno de los pilotos más queridos por su estilo agresivo, corazón y entrega total en pista. Rival directo de Wayne Rainey, su número 34 fue retirado como homenaje a su enorme legado.")
            
    elif "roberts" in p3_MGP_respuesta or "kenny" in p3_MGP_respuesta:
        print ("Kenny Roberts Sr. fue el primer estadounidense en ganar el Mundial de 500cc, con tres títulos consecutivos. Introdujo un nuevo estilo de pilotaje, influenciado por el dirt-track, que revolucionó la categoría. Fue también un pionero fuera de la pista, cambiando el rol del piloto profesional.")
            
    elif "spencer" in p3_MGP_respuesta or "freddie" in p3_MGP_respuesta:
        print ("Freddie Spencer fue un talento precoz y brillante que hizo historia en 1985 al ganar los campeonatos de 250cc y 500cc en el mismo año. Su carrera fue breve debido a las lesiones, pero su habilidad y velocidad lo convirtieron en una leyenda recordada por su enorme calidad.")

    elif "pedrosa" in p3_MGP_respuesta or "dani" in p3_MGP_respuesta:
        print ("Dani Pedrosa ganó títulos en 125cc y 250cc y fue uno de los grandes nombres de MotoGP, aunque nunca logró el campeonato en la categoría reina. Su pilotaje suave y técnico, combinado con su capacidad de desarrollo, lo hicieron clave para Honda y más tarde para KTM, donde sigue influyendo como probador.")

    elif "criville" in p3_MGP_respuesta or "alex" in p3_MGP_respuesta:
        print ("Álex Crivillé hizo historia al convertirse en el primer español campeón del mundo en 500cc, en 1999. También fue campeón de 125cc en 1989. Fue un referente en los 90 y pieza clave para que el motociclismo español se abriera paso entre los grandes.")

    elif "biaggi" in p3_MGP_respuesta or "max" in p3_MGP_respuesta:
        print ("Max Biaggi fue campeón del mundo cuatro veces en 250cc y uno de los principales rivales de Valentino Rossi en los 2000. Su estilo elegante y competitivo lo llevó a pelear en MotoGP y luego a brillar en Superbikes, donde también fue campeón.")

    elif "capirossi" in p3_MGP_respuesta or "loris" in p3_MGP_respuesta:
        print ("Loris Capirossi fue campeón del mundo en 125cc y 250cc, y protagonizó una de las carreras más largas del motociclismo, con más de 300 Grandes Premios disputados. Fue un piloto aguerrido y constante, respetado por su compromiso y experiencia.")

    elif "surtees" in p3_MGP_respuesta or "michael" in p3_MGP_respuesta:
        print ("John Surtees es único en la historia: campeón mundial tanto en motociclismo como en Fórmula 1. Su versatilidad y talento le dieron un lugar destacado en el automovilismo, no me esperaba esa respuesta pero veo que tienes sabios gustos jaja.")

    elif "rossi" in p3_MGP_respuesta or "valentino" in p3_MGP_respuesta:
        print ("Mira, que te quede claro que Rossi es un guarro, un pegapatadas y un malisimo perdedor. Pero también ha ganado lo suyo... Así que voy a tener un minimo de respeto hacia él (lo que el no tiene hacia el resto) y voy a dejar aquí su información: Valentino Rossi, 9 veces campeón del mundo, es una de las mayores leyendas del motociclismo, ícono global y figura clave en la popularización de MotoGP.")

    usuario_prefiere_MotoGP = "MotoGP"

preguntafinal_respuesta = input (preguntafinal).lower()
if "bueno" in preguntafinal_respuesta or "tema" in preguntafinal_respuesta or "otro" in preguntafinal_respuesta or "hablando" in preguntafinal_respuesta or "seguir" in preguntafinal_respuesta:
    print ("Vale, pues te vuelvo a preguntar jaja")
    p_principal_respuesta = input(p_principal).lower()
    if "F1" in p_principal_respuesta or "Formula 1" in p_principal_respuesta or "formula" in p_principal_respuesta or "f1" in p_principal_respuesta:
        p1_F1_respuesta = input (p1_F1).lower()
#Primera pregunta de F1 con todas sus opciones
        if "alonso" in p1_F1_respuesta or "fernando" in p1_F1_respuesta or "nano" in p1_F1_respuesta or "don fernando alonso" in p1_F1_respuesta:
            print ("¡¡¡Fernando Alonso me encanta!!! El Nano es un piloto español de Fórmula 1, nacido en Oviedo en 1981. Es considerado uno de los mejores conductores de su generación por su talento, inteligencia en carrera y determinación. Debutó en la F1 en 2001 y se convirtió en campeón del mundo con Renault en 2005 y 2006, siendo el piloto más joven en lograrlo en ese momento. A lo largo de su carrera ha competido con equipos como McLaren, Ferrari y Aston Martin, destacándose por su capacidad para exprimir al máximo cualquier coche. Su pasión, constancia y carisma lo han convertido en una leyenda del automovilismo.")

        elif "sainz" in p1_F1_respuesta or "carlos" in p1_F1_respuesta or "smooth operator" in p1_F1_respuesta:
            print ("¡¡¡Que buen piloto!!! Carlos Sainz me gusta mucho, nacido en Madrid en 1994, es un piloto español de Fórmula 1 e hijo del campeón de rally Carlos Sainz. Debutó en 2015 con Toro Rosso (hoy Racing Bulls) y ha pasado por equipos como Renault, McLaren y Ferrari. Desde 2025 compite con Williams Racing, donde busca liderar el regreso del equipo británico a los primeros puestos de la parrilla.")

        elif "verstappen" in p1_F1_respuesta or "max" in p1_F1_respuesta or "super max" in p1_F1_respuesta:
            print ("¡¡¡Me encanta tu elección!!! Actualmente opino que Max és el mejor piloto de la parrilla, nacido en Bélgica en 1997 y criado en los Países Bajos. Debutó en 2015 con Toro Rosso y rápidamente ascendió a Red Bull Racing, con quienes ha ganado múltiples campeonatos mundiales. Conocido por su agresividad, velocidad y consistencia, Verstappen ha marcado una nueva era en la F1 dominando gran parte de las últimas temporadas.")

        elif "antonelli" in p1_F1_respuesta or "kimi" in p1_F1_respuesta:
            print ("¡¡¡El Lamine Yamal de la F1 jaja!!! Kimi Antonelli es un joven piloto italiano considerado una de las mayores promesas del automovilismo actual. Nacido el 25 de agosto de 2006, ha sido parte del programa de desarrollo de Mercedes desde muy temprana edad. Con un impresionante palmarés en karting y campeonatos como la Fórmula 4 Italiana y ADAC F4, ha demostrado un talento excepcional y madurez en pista. En 2024 dio el salto a la Fórmula 2 con el equipo Prema, y muchos lo ven como un futuro piloto de Fórmula 1, posiblemente con Mercedes. Su estilo de conducción preciso y su enfoque profesional lo destacan como un nombre a seguir en los próximos años.")

        elif "piastri" in p1_F1_respuesta or "oscar" in p1_F1_respuesta:
            print ("¡¡¡Gran piloto!!! Nacido en Melbourne en 2001, es un piloto australiano de Fórmula 1. Tras destacar en Fórmula Renault, F3 y F2, debutó en 2023 con McLaren y rápidamente se consolidó como uno de los jóvenes más prometedores de la parrilla, logrando victorias y podios, incluso és capaz de pelear por algún mundial")

        elif "hülkenberg" in p1_F1_respuesta or "nico" in p1_F1_respuesta:
            print ("¡¡¡Buen piloto veterano!!! Nico Hülkenberg, nacido en 1987 en Alemania, es un piloto de Fórmula 1 que debutó en 2010 con Williams. Ha competido para varios equipos y ganó las 24 Horas de Le Mans en 2015. Conocido por su constancia, logró su primer podio en F1 en 2025 y actualmente corre con Sauber.")

        elif "bortoleto" in p1_F1_respuesta or "gabriel" in p1_F1_respuesta:
            print ("¡¡¡Que joven promesa!!! Gabriel Bortoleto, nacido en 2004 en Brasil, es un joven piloto de Fórmula 1 que debutó en 2025 con Sauber. Campeón de Fórmula 2 en 2024, se ha destacado por su rápida adaptación y se perfila como una de las grandes promesas del automovilismo brasileño.")
    
        elif "colapinto" in p1_F1_respuesta or "franco" in p1_F1_respuesta:
            print ("¡¡¡Vaya piloto boludo!!! Franco Colapinto, nacido en 2003 en Argentina, es un piloto de Fórmula 1 que debutó en 2024 con Williams. En 2025 se unió a Alpine como titular tras la salida de Jack Doohan, destacando por su rapidez y talento, y representando el regreso del automovilismo argentino a la F1.")

        elif "leclerc" in p1_F1_respuesta or "charles" in p1_F1_respuesta or "il predestinato" in p1_F1_respuesta:
            print ("¡¡¡Il predestinato de Ferrari!!! Charles Leclerc es un piloto monegasco de Fórmula 1 nacido en 1997. Debutó en 2018 y desde 2019 corre para Ferrari. Destaca por su velocidad, talento y determinación, siendo una de las grandes promesas del automovilismo.")

        elif "russell" in p1_F1_respuesta or "george" in p1_F1_respuesta:
            print ("El hombre invisible jaja, ¡¡¡que gran piloto!!! George Russell es un piloto británico de Fórmula 1 nacido en 1998. Debutó en 2019 con Williams y desde 2022 corre para Mercedes. Es reconocido por su consistencia, talento y gran potencial en la parrilla.")

        elif "perez" in p1_F1_respuesta or "checo" in p1_F1_respuesta or "sergio" in p1_F1_respuesta or "bottas" in p1_F1_respuesta or "valtteri" in p1_F1_respuesta:
            print ("¡¡¡El veterano de Callidac!!! Vaya piloto, su nombre ya forma parte de la F1 siendo de los más veteranos en este siglo XXI. Deseando volverlo a ver el año que viene en las pistas, ¡¡¡estoy seguro que lo hará genial!!!")

        elif "norris" in p1_F1_respuesta or "lando" in p1_F1_respuesta:
            print ("¡¡¡Buen piloto la verdad!!! Lando Norris es un piloto británico de Fórmula 1 nacido en 1999. Debutó en 2019 con McLaren y se ha destacado por su velocidad y carisma dentro y fuera de las pistas aunque creo que no es muy regular, el talento lo tiene.")
    
        elif "bearman" in p1_F1_respuesta or "oliver" in p1_F1_respuesta or "oso" in p1_F1_respuesta or "hadjar" in p1_F1_respuesta or "isack" in p1_F1_respuesta:
            print ("¡¡¡Vaya Rookie has escogido!!! Le veo un futuro prometedor a este piloto. Las pocas carreras que ha disputado en la categoria reina ya ha demostrado su gran talento, ¡¡¡Dale unos años y un buen coche y verás!!!")

        elif "gasly" in p1_F1_respuesta or "pierre" in p1_F1_respuesta or "lawson" in p1_F1_respuesta or "liam" in p1_F1_respuesta or "albon" in p1_F1_respuesta or "alex" in p1_F1_respuesta or "tsunoda" in p1_F1_respuesta or "yuki" in p1_F1_respuesta or "stroll" in p1_F1_respuesta or "lance" in p1_F1_respuesta:
            print ("Bueno... No es mal piloto la verdad, no me gusta especialmente pero he de decir que más de una vez me ha callado la boca haciendo alguna carrera expectacular... Pero poco más jaja")

#Estos no me caen tan bien, entonces al decir mi opinión le pregunto si quiere seguir hablando, ya que no estoy de acuerdo:
        elif "hamilton" in p1_F1_respuesta or "lewis" in p1_F1_respuesta:
            pregunta_hamilton = input ("¿De verdad quieres saber más de él" + " " + nom + 3*"?").lower()
            if "si" in pregunta_hamilton or "por" in pregunta_hamilton or "supuesto" in pregunta_hamilton or "claro que si" in pregunta_hamilton:
                print ("Madre mía... No es por nada pero Hamilton no es buen piloto, vale que tiene muchos titulos pero si no le dan un coche 5 segundos más rapido que los otros, se te pone a llorar como un bebe. Espero que te haga reflexionar mi opinión.")
                print ("Igualmente... Toma lo que buscas: Lewis Hamilton es un piloto británico de Fórmula 1 y siete veces campeón del mundo. Debutó en 2007 con McLaren y se consolidó con Mercedes como uno de los más grandes de la historia. Además de su éxito en pista, es reconocido por su activismo y compromiso social.")
                pregunta_hamiltocon = input ("Viendo que piloto me has dicho y que a mí no me gusta... ¿¿Quieres seguir hablando??").lower()
                if "si" in pregunta_hamiltocon or "vale" in pregunta_hamiltocon:
                    print ("Vale, pero que sepas que no estoy de acuerdo con que te guste este piloto ehh")
                elif "no" in pregunta_hamiltocon:
                    print ("¿¿¿No??? Pues ahora te aguantas jaja")


        elif "ocon" in p1_F1_respuesta or "esteban" in p1_F1_respuesta:
            pregunta_ocon = input ("Jajajaja," + " " + nom + " " + 3*"¿" + "enserio ese personaje es tu piloto favorito" + 3*"?").lower()
            if "si" in pregunta_ocon or "por" in pregunta_ocon or "supuesto" in pregunta_ocon or "claro que si" in pregunta_ocon:
                print ("Yo lo siento pero por ahí no paso... Ocon no sirve para nada... Es inútil jaja, y encima francés.")
                pregunta_hamiltocon = input ("Viendo que piloto te gusta y que no estamos de acuerdo... ¿¿Quieres seguir hablando??").lower()
                if "si" in pregunta_hamiltocon or "vale" in pregunta_hamiltocon:
                    print ("Vale, pero que sepas que no estoy de acuerdo con que te guste este piloto ehh")
                elif "no" in pregunta_hamiltocon:
                    print ("¿¿¿No??? Pues ahora te aguantas jaja")
#Aquí la segunda respuesta de F1 con todas sus opciones:                  
        p2_F1_respuesta = input(p2_F1).lower()
        if "ferrari" in p2_F1_respuesta:
            print ("¡¡¡Fuaaa, mi equipo favorito jaja!!! La Scuderia Ferrari es el equipo más legendario de la Fórmula 1. Fundado en 1929 por Enzo Ferrari, ha estado presente desde la primera temporada del campeonato en 1950. Con su icónico color rojo y el famoso 'Cavallino Rampante' (caballo rampante), Ferrari representa pasión, tradición y excelencia automovilística. Es el equipo con más títulos en la historia de la F1, incluyendo campeonatos de pilotos y constructores. Pilotos históricos como Fernando Alonso, Michael Schumacher, Niki Lauda y Gilles Villeneuve han dejado su huella en Maranello. Soñar con pilotar para Ferrari es soñar con formar parte de la historia misma del automovilismo.")
        elif "mclaren" in p2_F1_respuesta:
            print ("¡¡¡Buena elección!!! McLaren es uno de los equipos más históricos y prestigiosos de la Fórmula 1. Fundado en 1963 por Bruce McLaren, el equipo británico ha ganado múltiples campeonatos del mundo y ha sido la cuna de leyendas como Fernando Alonso, Ayrton Senna, Alain Prost, Niki Lauda y Lewis Hamilton. Conocido por su innovación tecnológica y su espíritu competitivo, McLaren siempre ha sido un símbolo de velocidad, elegancia y evolución. Pilotar para McLaren es formar parte de una historia llena de gloria y también de futuro prometedor.")
        elif "aston" in p2_F1_respuesta or "martin" in p2_F1_respuesta:
            print ("¡Buena elección! Aston Martin, antes conocido como Racing Point y Force India, es un equipo con una historia reciente pero llena de evolución y lucha. Han contado con pilotos destacados como Sebastian Vettel y, por supuesto, Fernando Alonso, uno de los mejores de todos los tiempos. Con la llegada de Aston Martin en 2021, el equipo combina la tradición británica con ambición y tecnología avanzada. Pilotar aquí significa formar parte de un proyecto joven pero con grandes aspiraciones en la Fórmula 1.")
        elif "amg" in p2_F1_respuesta or "silver" in p2_F1_respuesta or "mercedes" in p2_F1_respuesta or "plateadas" in p2_F1_respuesta:
            print ("¡¡¡Una elección top!!! Mercedes es uno de los equipos más exitosos de la era moderna en Fórmula 1, con múltiples campeonatos de constructores y pilotos, especialmente durante su dominio con Lewis Hamilton. Es sinónimo de innovación, potencia y precisión alemana. Además, el joven talento Kimi Antonelli está fuertemente vinculado al futuro del equipo, siendo considerado uno de los pilotos más prometedores de su generación. Pilotar para Mercedes es estar en el corazón de la élite del automovilismo.")
        elif "red" in p2_F1_respuesta or "bull" in p2_F1_respuesta:
            print ("¡¡¡Una elección llena de adrenalina!!! Red Bull Racing es uno de los equipos más exitosos de las últimas décadas en Fórmula 1. Conocidos por su enfoque innovador y agresivo, dominaron una era con Sebastian Vettel y están volviendo a hacerlo con Max Verstappen. Su filosofía joven, audaz y orientada al rendimiento ha revolucionado el deporte. Pilotar para Red Bull significa estar en un equipo que no solo busca ganar, sino hacerlo con estilo y velocidad pura.")
        elif "williams" in p2_F1_respuesta:
            print ("¡¡¡Una elección con mucha historia!!! Williams es uno de los equipos más legendarios de la Fórmula 1, con múltiples campeonatos en su palmarés y una rica trayectoria que comenzó en 1977. Fue cuna de campeones como Nigel Mansell, Alain Prost y Ayrton Senna. Aunque en los últimos años ha enfrentado desafíos, ahora vuelven poco a poco a la cima. Por ello, sigue siendo un equipo con gran tradición y pasión por las carreras. Pilotar para Williams es ser parte de un legado histórico, con la misión de devolverlo a lo más alto.")
        elif "alpine" in p2_F1_respuesta or "renault" in p2_F1_respuesta or "bwt" in p2_F1_respuesta:
            print ("¡¡¡Muy buena elección!!! Alpine es la actual identidad del equipo Renault en la Fórmula 1, una escudería con una larga historia en el deporte. Bajo el nombre de Renault, fue donde Fernando Alonso logró sus dos campeonatos del mundo en 2005 y 2006, y volvió a correr tanto en 2008-2009 como en su etapa más reciente con Alpine entre 2021 y 2022. El equipo combina la experiencia de años en la F1 con el respaldo tecnológico del Grupo Renault y una visión ambiciosa hacia el futuro. Pilotar para Alpine es formar parte de un legado donde ya brillaron campeones, y donde aún se busca volver a lo más alto.")
        elif "sauber" in p2_F1_respuesta or "kick" in p2_F1_respuesta or "stake" in p2_F1_respuesta or "audi" in p2_F1_respuesta:
            print ("¡¡¡Una elección estratégica e interesante!!! El equipo Sauber, actualmente conocido como Kick Sauber, tiene una larga trayectoria en la Fórmula 1 desde los años 90, siendo una escudería reconocida por su capacidad para desarrollar talento y mantenerse competitiva con recursos limitados. En el pasado, compitió bajo el nombre de Alfa Romeo, y ahora se prepara para un futuro muy prometedor: en 2026 se convertirá oficialmente en el equipo oficial de Audi. Pilotar para Sauber hoy es estar en la antesala de uno de los proyectos más ambiciosos que veremos en la nueva era de la F1.")
        elif "haas" in p2_F1_respuesta or "money" in p2_F1_respuesta or "gram" in p2_F1_respuesta:
            print ("¡¡¡Una elección con carácter propio!!! Haas es el primer equipo estadounidense en la Fórmula 1 en varias décadas, debutando en 2016. Aunque es uno de los equipos más jóvenes del paddock, ha logrado hacerse un lugar gracias a su enfoque práctico y su asociación técnica con Ferrari. A lo largo de los años ha contado con pilotos experimentados y jóvenes promesas, siendo un equipo que sigue construyendo su camino en el deporte. Pilotar para Haas es aceptar el desafío de crecer junto a una escudería con mucho potencial.")
        elif "rb" in p2_F1_respuesta or "racing" in p2_F1_respuesta or "bulls" in p2_F1_respuesta or "visa" in p2_F1_respuesta or "cash" in p2_F1_respuesta:
            print ("¡Una elección con mucho futuro! Racing Bulls, anteriormente conocida como AlphaTauri y Toro Rosso, es el equipo filial de Red Bull Racing. A lo largo de los años ha sido una plataforma clave para desarrollar jóvenes talentos, como Sebastian Vettel —quien logró aquí su primera victoria— y más recientemente pilotos como Pierre Gasly o Yuki Tsunoda. Con una imagen renovada y mayor integración técnica con Red Bull, RB está creciendo como un equipo competitivo por derecho propio. Pilotar para Racing Bulls es estar en el radar directo de los campeones, con la oportunidad de brillar y dar el salto a lo más alto.")
#Ahora la última pregunta de F1, con sus diferentes opciones de respuestas
        p3_F1_respuesta = input(p3_F1).lower()
        if "schumacher" in p3_F1_respuesta or "michael" in p3_F1_respuesta or "kaiser" in p3_F1_respuesta:
            print ("Michael Schumacher es uno de los nombres más grandes en la historia de la Fórmula 1. Con 7 campeonatos del mundo y 91 victorias, dominó la era moderna con Ferrari y estableció estándares de excelencia y trabajo en equipo que aún inspiran, me gusta tu elección jaja.")
        
        elif "hamilton" in p3_F1_respuesta or "lewis" in p3_F1_respuesta:
            print ("Aunque no me guste mucho, he de decir que Lewis Hamilton es una superestrella del automovilismo, con 7 títulos mundiales y récords en victorias y poles. Más allá de su talento, es un referente en la lucha por la diversidad y la igualdad dentro y fuera de la pista.")
        
        elif "verstappen" in p3_F1_respuesta or "max" in p3_F1_respuesta:
            print ("Max Verstappen es la joven estrella que ha revolucionado la F1 en los últimos años. Con ya 4 campeonatos, es conocido por su agresividad y consistencia, y se perfila como una leyenda en activo del deporte, increible tu elección, buen gusto jaja.")
            
        elif "senna" in p3_F1_respuesta or "ayrton" in p3_F1_respuesta:
            print ("Ayrton Senna es una leyenda eterna de la F1, recordado por su increíble velocidad, carisma y espíritu competitivo. Sus 3 campeonatos y su trágica partida dejaron una huella imborrable en el deporte, increible tu elección, buen gusto jaja.")
            
        elif "prost" in p3_F1_respuesta or "alain" in p3_F1_respuesta:
            print ("Conocido como 'El Profesor', Alain Prost fue un piloto cerebral y estratégico, con 4 títulos mundiales. Su enfoque metódico y calma en pista le valieron un lugar especial en la historia de la F1, me gusta tu elección jaja.")
            
        elif "fangio" in p3_F1_respuesta or "juan" in p3_F1_respuesta or "manuel" in p3_F1_respuesta:
            print ("El argentino Juan Manuel Fangio dominó la Fórmula 1 en los años 50 con 5 campeonatos. Su elegancia y habilidad técnica marcaron el inicio de la era de las leyendas en el deporte, me gusta tu elección jaja.")
            
        elif "lauda" in p3_F1_respuesta or "niki" in p3_F1_respuesta:
            print ("Niki Lauda es símbolo de coraje y resiliencia. Tras un grave accidente en 1976, volvió a competir y ganó 3 títulos mundiales, dejando un legado imborrable de fortaleza y profesionalismo, increible tu elección, buen gusto jaja.")
            
        elif "alonso" in p3_F1_respuesta or "fernando" in p3_F1_respuesta or "Nano" in p3_F1_respuesta:
            print ("Fernando Alonso es uno de los pilotos más completos y longevos de la F1, con 2 campeonatos y una carrera que abarca más de dos décadas. Su talento y determinación lo mantienen en la élite, increible tu elección, buen gusto jaja.")
            
        elif "vettel" in p3_F1_respuesta or "sebastian" in p3_F1_respuesta:
            print ("Sebastian Vettel brilló con 4 títulos consecutivos en Red Bull, demostrando velocidad, inteligencia y carácter. Además, es un referente por su compromiso fuera de las pistas, me gusta tu elección jaja.")
            
        elif "surtees" in p3_F1_respuesta or "john" in p3_F1_respuesta:
            print ("John Surtees es único en la historia: campeón mundial tanto en motociclismo como en Fórmula 1. Su versatilidad y talento le dieron un lugar destacado en el automovilismo, no me esperaba esa respuesta pero veo que tienes sabios gustos jaja.")
    
        elif "pedro" in p3_F1_respuesta or "rosa" in p3_F1_respuesta or "de" in p3_F1_respuesta or "la" in p3_F1_respuesta:
            print ("Pedro de la Rosa es un piloto español de Fórmula 1 conocido por su talento y experiencia. Compitió en varias temporadas principalmente como piloto de pruebas y titular para equipos como Arrows, Jaguar y McLaren. Destacado por su habilidad técnica, también ha trabajado como comentarista y embajador del automovilismo en España.")
    
        elif "mazepin" in p3_F1_respuesta or "nikita" in p3_F1_respuesta:
            print ("Nikita Mazepin es un piloto ruso de Fórmula 1 que compitió en la temporada 2021 con el equipo Haas. Proveniente de una familia con fuerte apoyo financiero, su paso por la F1 fue controvertido y recibió críticas por su desempeño y comportamiento fuera de pista. Tras una única temporada, perdió su asiento y actualmente no participa en la Fórmula 1.")

        elif "latifi" in p3_F1_respuesta or "nicholas" in p3_F1_respuesta:
            print ("Nicholas Latifi es un piloto canadiense de Fórmula 1 que compitió principalmente con el equipo Williams entre 2020 y 2022. Reconocido por su perseverancia y esfuerzo, aunque sin grandes resultados destacados, se destacó por su profesionalismo y dedicación en el deporte. También tiene experiencia en categorías inferiores como la Fórmula 2.")
        
        print("Bueno... Hoy ya hemos hablado mucho, mejor seguimos hablando otro dia, paramos ahora para tener más conversaciones después jaja. Me alegro de conocerte, ¡¡¡Veo que compartimos una pasión muy bonita por el motor!!!")
        
#Usuario le gusta F1
usuario_prefiere_F1 = "F1"
#Si en la pregunta principal se dice MotoGP    
if "motoGP" in p_principal_respuesta or "gp" in p_principal_respuesta or "moto" in p_principal_respuesta:
        p1_MGP_respuesta = input (p1_MGP).lower()
        if "marc" in p1_MGP_respuesta or "hormiga" in p1_MGP_respuesta or "trueno" in p1_MGP_respuesta:
            print ("¡¡¡Mi piloto favorito!!! Nacido en Cervera, España, Marc Márquez es una leyenda viva del motociclismo. Desde su debut en MotoGP en 2013, se hizo famoso por su estilo agresivo, adelantamientos imposibles y una ambición sin frenos. Conquistó 8 títulos mundiales (6 en la categoría reina) y dominó junto a Honda durante años, hasta que las lesiones complicaron su camino a partir de 2020. En 2023 y 2024 sorprendió al pasar al equipo Gresini Ducati, donde volvió a mostrar destellos de su mejor versión. Ahora, en 2025, Marc se une al equipo oficial Ducati, montando la mejor moto de la parrilla. Superando con mucha ventaja al resto de pilotos ha logrado su objetivo: volver a lo más alto y sumar su noveno título mundial. Marc no solo corre al límite: vive allí. Y esa es justamente la esencia que lo convierte en uno de los grandes de todos los tiempos.")
    
        elif "alex" in p1_MGP_respuesta:
            print ("¡¡¡Mi otro piloto favorito!!! Nacido en Cervera, como su hermano Marc, Álex Márquez ha forjado su propio camino en el motociclismo con constancia y determinación. Campeón del mundo en Moto3 (2014) y Moto2 (2019), llegó a MotoGP en 2020 con el equipo oficial Honda, logrando dos podios en su temporada de debut. Tras un paso por LCR Honda, en 2023 dio un nuevo aire a su carrera al fichar por Gresini Ducati, donde rápidamente se adaptó a la Desmosedici y volvió a luchar en posiciones de cabeza. Su estilo técnico y limpio, combinado con mayor confianza, le han permitido crecer como piloto dentro de una categoría cada vez más competitiva. En 2025, Álex sigue consolidado como una pieza clave del proyecto Gresini, demostrando que no vive a la sombra de nadie: su talento y trabajo hablan por sí solos. Con experiencia, velocidad y mentalidad fuerte, Álex Márquez sigue buscando su lugar en la historia de MotoGP... y cada año está más cerca.")
    
        elif "márquez" in p1_MGP_respuesta or "marquez" in p1_MGP_respuesta:
            pregunta_marquez_respuesta = input ("¿¿¿Pero a que Márquez te refieres jaja???").lower()
            if "Marc" in pregunta_marquez_respuesta or "marc" in pregunta_marquez_respuesta:
                print ("Vale vale, ahora me aclaro jaja ¡¡¡Adoro al mayor de los Márquez!!! Nacido en Cervera, España, Marc Márquez es una leyenda viva del motociclismo. Desde su debut en MotoGP en 2013, se hizo famoso por su estilo agresivo, adelantamientos imposibles y una ambición sin frenos. Conquistó 8 títulos mundiales (6 en la categoría reina) y dominó junto a Honda durante años, hasta que las lesiones complicaron su camino a partir de 2020. En 2023 y 2024 sorprendió al pasar al equipo Gresini Ducati, donde volvió a mostrar destellos de su mejor versión. Ahora, en 2025, Marc se une al equipo oficial Ducati, montando la mejor moto de la parrilla. Superando con mucha ventaja al resto de pilotos ha logrado su objetivo: volver a lo más alto y sumar su noveno título mundial. Marc no solo corre al límite: vive allí. Y esa es justamente la esencia que lo convierte en uno de los grandes de todos los tiempos.")
            elif "Alex" in pregunta_marquez_respuesta or "alex" in pregunta_marquez_respuesta:
                print ("Vale vale, ahora me aclaro jaja ¡¡¡Adoro al menor de los Márquez!!! Nacido en Cervera, como su hermano Marc, Álex Márquez ha forjado su propio camino en el motociclismo con constancia y determinación. Campeón del mundo en Moto3 (2014) y Moto2 (2019), llegó a MotoGP en 2020 con el equipo oficial Honda, logrando dos podios en su temporada de debut. Tras un paso por LCR Honda, en 2023 dio un nuevo aire a su carrera al fichar por Gresini Ducati, donde rápidamente se adaptó a la Desmosedici y volvió a luchar en posiciones de cabeza. Su estilo técnico y limpio, combinado con mayor confianza, le han permitido crecer como piloto dentro de una categoría cada vez más competitiva. En 2025, Álex sigue consolidado como una pieza clave del proyecto Gresini, demostrando que no vive a la sombra de nadie: su talento y trabajo hablan por sí solos. Con experiencia, velocidad y mentalidad fuerte, Álex Márquez sigue buscando su lugar en la historia de MotoGP... y cada año está más cerca.")

        elif "acosta" in p1_MGP_respuesta or "pedro" in p1_MGP_respuesta:
            print ("¡¡¡Me encanta tu elección!!! Con solo 21 años, Pedro Acosta ya es una de las mayores promesas de MotoGP. Campeón de Moto3 en 2021 en su temporada debut y de Moto2 en 2023, llegó a la categoría reina en 2024 con el equipo GasGas Tech3 KTM, demostrando madurez, velocidad y una confianza fuera de lo común. En 2025, Acosta sigue creciendo como piloto oficial KTM, mezclando agresividad e inteligencia en pista. Su estilo audaz y su capacidad para adaptarse rápidamente lo colocan como un firme candidato a ser campeón en muy poco tiempo. El futuro ya llegó, y se llama Pedro Acosta.")

        elif "martin" in p1_MGP_respuesta or "jorge" in p1_MGP_respuesta:
            print ("¡¡¡Vaya pilotazo!!! Jorge Martín, campeón del mundo de Moto3 en 2018, se ha consolidado como uno de los pilotos más rápidos y consistentes de MotoGP, y en 2025, tras años de lucha con Ducati Pramac, finalmente corre para el equipo oficial Aprilia, decidido a conquistar el título que ha rozado en temporadas anteriores.")

        elif "mir" in p1_MGP_respuesta or "joan" in p1_MGP_respuesta:
            print ("¡¡¡Que piloto!!! Joan Mir, campeón del mundo de MotoGP en 2020 con Suzuki, es un piloto de talento sólido y mentalidad fuerte que en 2025 sigue luchando por volver a lo más alto, ahora intentando recuperar sensaciones tras años difíciles en Honda.")

        elif "fernandez" in p1_MGP_respuesta or "raul" in p1_MGP_respuesta:
            print ("¡¡¡Que joven piloto!!! Raúl Fernández, subcampeón de Moto2 en 2021 tras una temporada espectacular, sigue buscando su lugar en MotoGP y en 2025 compite con Trackhouse Aprilia, decidido a demostrar todo su potencial en la categoría reina.")
    
        elif "aldeguer" in p1_MGP_respuesta or "fermin" in p1_MGP_respuesta:
            print ("¡¡¡Vaya Rookie!!! Fermín Aldeguer, una de las jóvenes promesas más destacadas del motociclismo español, llega a MotoGP en 2025 con el equipo Pramac Ducati tras un cierre de temporada dominante en Moto2, listo para dejar huella desde su debut en la categoría reina.")

        elif "bagnaia" in p1_MGP_respuesta or "pecco" in p1_MGP_respuesta or "francesco" in p1_MGP_respuesta:
            print ("¡¡¡!Buen piloto!! Pecco Bagnaia, campeón de MotoGP en 2022 con Ducati, es uno de los pilotos más completos y competitivos de la parrilla, y en 2025 continúa en el equipo oficial Ducati.")

        elif "bezzecchi" in p1_MGP_respuesta or "marco" in p1_MGP_respuesta:
            print ("¡¡¡Que gran elección!!! Marco Bezzecchi, piloto italiano talentoso y constante, compite en 2025 con la Aprilia, consolidándose como uno de los jóvenes talentos en alza dentro de MotoGP, con grandes expectativas para las próximas temporadas.")

        elif "quartararo" in p1_MGP_respuesta or "fabio" in p1_MGP_respuesta or "diablo" in p1_MGP_respuesta:
            print ("¡¡¡El diablo!!! Fabio Quartararo, campeón de MotoGP en 2021 con Yamaha, es un piloto rápido y agresivo que en 2025 sigue luchando por el título, enfrentando una temporada desafiante con un equipo Yamaha en plena evolución.")

        elif "ogura" in p1_MGP_respuesta or "ai" in p1_MGP_respuesta:
            print ("¡¡¡Buen Rookie la verdad!!! Ai Ogura, joven talento japonés de Moto2, destaca por su constancia y velocidad, y en 2025 busca seguir creciendo y dar el salto definitivo hacia MotoGP en un futuro cercano.")
    
        elif "binder" in p1_MGP_respuesta or "brad" in p1_MGP_respuesta or "maverick" in p1_MGP_respuesta or "viñales" in p1_MGP_respuesta or "zarco" in p1_MGP_respuesta or "johann" in p1_MGP_respuesta or "rins" in p1_MGP_respuesta or "oliveira" in p1_MGP_respuesta or "miguel" in p1_MGP_respuesta or "miller" in p1_MGP_respuesta or "jack" in p1_MGP_respuesta:
            print ("¡¡¡Buena elección!!! “La verdad es que es un piloto constante y competente, que aporta buen nivel aunque no suele destacar mucho, pero siempre está listo para aprovechar su oportunidad.”")

        elif "bastianini" in p1_MGP_respuesta or "enea" in p1_MGP_respuesta or "di" in p1_MGP_respuesta or "giannantonio" in p1_MGP_respuesta or "morbidelli" in p1_MGP_respuesta or "franco" in p1_MGP_respuesta or "marini" in p1_MGP_respuesta or "luca" in p1_MGP_respuesta:
            print ("¡¡¡Que piloto!!! La verdad es que es un piloto muy competitivo y constante, que suele estar cerca de los líderes y puede pelear por podios, aunque todavía le falta dar ese salto para ser de los mejores.")

        elif "chantra" in p1_MGP_respuesta or "somkiat" in p1_MGP_respuesta:
            print ("Que gracioso eres jaja")
    
                  
        p2_MGP_respuesta = input(p2_MGP).lower()
        if "ducati" in p2_MGP_respuesta or "corse" in p2_MGP_respuesta or "lenovo" in p2_MGP_respuesta:
            print ("¡¡¡Fuaaa, es de mis equipos favoritos jaja!!! Ducati Lenovo es uno de los equipos más fuertes y consistentes de MotoGP. Con una moto potente y tecnología de punta, siempre están en la pelea por victorias y campeonatos. Su combinación de pilotos talentosos y un gran trabajo en el desarrollo los convierte en un rival difícil de superar en cualquier circuito.")
        elif "aprilia" in p2_MGP_respuesta:
            print ("¡¡¡Buena elección!!! Aprilia Racing es un equipo en plena evolución, cada año mostrando mejoras significativas en MotoGP. Con pilotos jóvenes y talentosos, y una moto cada vez más competitiva, están creciendo como un serio rival para los equipos punteros y buscando consolidarse en la lucha por podios y victorias.")
        elif "gresini" in p2_MGP_respuesta or "bk8" in p2_MGP_respuesta:
            print ("¡¡¡Fuaaa, es de mis equipos favoritos jaja!!! BK8 Gresini Racing es un equipo con gran tradición y pasión en MotoGP, que ha sabido combinar experiencia y juventud para mantenerse competitivo. Con pilotos que aportan talento y ganas de crecer, y una alianza sólida con Ducati, siguen luchando para subir al podio y consolidarse entre los mejores.")
        elif "honda" in p2_MGP_respuesta or "hrc" in p2_MGP_respuesta:
            print ("¡¡¡Una elección top!!! Honda HRC Castrol es uno de los equipos históricos y más icónicos de MotoGP, con una larga tradición de campeonatos y pilotos legendarios. Aunque en los últimos años han enfrentado desafíos técnicos y de rendimiento, siguen trabajando duro para recuperar su lugar en la cima, apoyados en la experiencia de sus pilotos y la innovación constante.")
        elif "lcr" in p2_MGP_respuesta:
            print ("¡¡¡Wow!!! LCR Honda es un equipo independiente con mucha historia en MotoGP, conocido por su profesionalismo y constancia. Aunque no siempre cuenta con las motos más punteras, ha logrado resultados destacados gracias al talento y esfuerzo de sus pilotos, manteniéndose competitivo y luchando en cada carrera.")
        elif "monster" in p2_MGP_respuesta or "energy" in p2_MGP_respuesta or "yamaha" in p2_MGP_respuesta:
            print ("¡¡¡Una elección llena de adrenalina!!! Monster Energy Yamaha es uno de los equipos más emblemáticos de MotoGP, con una gran historia de éxitos y campeones. Aunque en los últimos años ha enfrentado altibajos y retos técnicos, sigue siendo un equipo competitivo con pilotos talentosos que luchan por volver a dominar la categoría.")
        elif "vr46" in p2_MGP_respuesta or "vr" in p2_MGP_respuesta:
            print ("¡¡¡Muy buena elección!!! VR46 Racing Team es el equipo fundado por Valentino Rossi que ha crecido rápidamente en MotoGP. Con un enfoque joven y ambicioso, apoyado en talento emergente y la colaboración con Ducati, busca consolidarse como una referencia en la categoría y luchar por podios y victorias.")
        elif "prima" in p2_MGP_respuesta or "pramac" in p2_MGP_respuesta:
            print ("¡¡¡Una elección estratégica e interesante!!! Prima Pramac Racing es un equipo sólido y con mucha experiencia en MotoGP, que combina pilotos veteranos y con talento con una estrecha colaboración con Yamaha. Siempre están en la pelea por buenos resultados y buscan crecer temporada tras temporada para acercarse a los equipos punteros.")
        elif "ktm" in p2_MGP_respuesta:
            print ("¡¡¡Una elección con carácter propio!!! KTM Factory Racing Team es un equipo joven pero ambicioso en MotoGP, conocido por su innovación y progreso constante. Con pilotos veloces y una moto en evolución, trabajan duro para consolidarse como candidatos a podios y victorias en una categoría cada vez más competitiva.")
        elif "3" in p2_MGP_respuesta or "tech" in p2_MGP_respuesta:
            print ("¡Una elección con mucho futuro! Tech3 KTM Factory Racing es un equipo satélite con gran experiencia en MotoGP, dedicado a desarrollar talento joven y ayudar en la evolución técnica de KTM. Aunque no siempre está en el podio, cumple un papel clave formando pilotos y aportando datos valiosos para el equipo oficial.")
        elif "trackhouse" in p2_MGP_respuesta:
            print ("¡Una elección con mucho futuro! Trackhouse Racing es el nuevo equipo estadounidense en MotoGP que llegó en 2024 con una propuesta fresca, moderna y ambiciosa. Con estructura sólida y el respaldo de Aprilia, buscan crecer rápidamente en la categoría, apostando por pilotos jóvenes y una identidad muy marcada dentro y fuera de la pista.")
        
        p3_MGP_respuesta = input(p3_MGP).lower()
        if "agostini" in p3_MGP_respuesta or "giacomo" in p3_MGP_respuesta:
            print ("Giacomo Agostini ostenta un récord histórico con 15 títulos mundiales, logrados principalmente en las categorías de 350cc y 500cc. Fue el dominador absoluto de los años 60 y 70, corriendo para marcas míticas como MV Agusta. Su legado permanece intacto como uno de los más grandes campeones que ha dado el motociclismo.")
            
        elif "nieto" in p3_MGP_respuesta or "angel" in p3_MGP_respuesta:
            print ("Ángel Nieto es una auténtica leyenda del motociclismo español, con 13 títulos mundiales (12+1, como él decía por superstición). Dominó las categorías de 50cc y 125cc, y fue pionero en abrir el camino para que España se convirtiera en una potencia del motociclismo mundial. Su figura es irreemplazable en la historia del deporte.")
            
        elif "marquez" in p3_MGP_respuesta or "marc" in p3_MGP_respuesta or "Marc" in p3_MGP_respuesta:
            print ("Marc Márquez cambió las reglas del juego en MotoGP desde su llegada en 2013. Con 8 títulos mundiales y un estilo espectacular basado en salvadas imposibles y agresividad total, marcó una era con Honda. A pesar de las lesiones, su espíritu de lucha y talento siguen haciendo historia.")
            
        elif "doohan" in p3_MGP_respuesta or "mick" in p3_MGP_respuesta:
            print ("Mick Doohan fue el piloto más dominante de la década de los 90, con cinco títulos consecutivos en 500cc entre 1994 y 1998. Su control absoluto sobre la moto y su fortaleza mental lo convirtieron en una leyenda con Honda. Su rivalidad con Crivillé y sus remontadas épicas lo hacen inolvidable.")
            
        elif "stoner" in p3_MGP_respuesta or "casey" in p3_MGP_respuesta:
            print ("Casey Stoner fue campeón del mundo en 2007 con Ducati y en 2011 con Honda, destacándose por su talento natural y velocidad en cualquier condición. Aunque su carrera fue corta, dejó una huella profunda por su pilotaje agresivo, directo y sin concesiones. Uno de los grandes talentos puros de MotoGP.")
            
        elif "lorenzo" in p3_MGP_respuesta or "jorge" in p3_MGP_respuesta:
            print ("Jorge Lorenzo fue campeón del mundo en cinco ocasiones, tres de ellas en MotoGP. Su estilo de pilotaje limpio, rápido y constante lo convirtió en uno de los grandes rivales de Valentino Rossi y Marc Márquez. Fue un perfeccionista dentro y fuera de la pista, con una enorme capacidad para mantener el ritmo de carrera.")
            
        elif "rainey" in p3_MGP_respuesta or "wayne" in p3_MGP_respuesta:
            print ("Wayne Rainey fue uno de los grandes nombres de los 90, con tres títulos en 500cc. Su pilotaje técnico y fino, junto con una mentalidad fuerte, lo llevaron a dominar una era muy competitiva. Su carrera se vio truncada por una lesión, pero su legado como luchador sigue presente.")
            
        elif "schwantz" in p3_MGP_respuesta or "kevin" in p3_MGP_respuesta:
            print ("Kevin Schwantz fue campeón del mundo en 1993 y se convirtió en uno de los pilotos más queridos por su estilo agresivo, corazón y entrega total en pista. Rival directo de Wayne Rainey, su número 34 fue retirado como homenaje a su enorme legado.")
            
        elif "roberts" in p3_MGP_respuesta or "kenny" in p3_MGP_respuesta:
            print ("Kenny Roberts Sr. fue el primer estadounidense en ganar el Mundial de 500cc, con tres títulos consecutivos. Introdujo un nuevo estilo de pilotaje, influenciado por el dirt-track, que revolucionó la categoría. Fue también un pionero fuera de la pista, cambiando el rol del piloto profesional.")
            
        elif "spencer" in p3_MGP_respuesta or "freddie" in p3_MGP_respuesta:
            print ("Freddie Spencer fue un talento precoz y brillante que hizo historia en 1985 al ganar los campeonatos de 250cc y 500cc en el mismo año. Su carrera fue breve debido a las lesiones, pero su habilidad y velocidad lo convirtieron en una leyenda recordada por su enorme calidad.")

        elif "pedrosa" in p3_MGP_respuesta or "dani" in p3_MGP_respuesta:
            print ("Dani Pedrosa ganó títulos en 125cc y 250cc y fue uno de los grandes nombres de MotoGP, aunque nunca logró el campeonato en la categoría reina. Su pilotaje suave y técnico, combinado con su capacidad de desarrollo, lo hicieron clave para Honda y más tarde para KTM, donde sigue influyendo como probador.")

        elif "criville" in p3_MGP_respuesta or "alex" in p3_MGP_respuesta:
            print ("Álex Crivillé hizo historia al convertirse en el primer español campeón del mundo en 500cc, en 1999. También fue campeón de 125cc en 1989. Fue un referente en los 90 y pieza clave para que el motociclismo español se abriera paso entre los grandes.")

        elif "biaggi" in p3_MGP_respuesta or "max" in p3_MGP_respuesta:
            print ("Max Biaggi fue campeón del mundo cuatro veces en 250cc y uno de los principales rivales de Valentino Rossi en los 2000. Su estilo elegante y competitivo lo llevó a pelear en MotoGP y luego a brillar en Superbikes, donde también fue campeón.")

        elif "capirossi" in p3_MGP_respuesta or "loris" in p3_MGP_respuesta:
            print ("Loris Capirossi fue campeón del mundo en 125cc y 250cc, y protagonizó una de las carreras más largas del motociclismo, con más de 300 Grandes Premios disputados. Fue un piloto aguerrido y constante, respetado por su compromiso y experiencia.")

        elif "surtees" in p3_MGP_respuesta or "michael" in p3_MGP_respuesta:
            print ("John Surtees es único en la historia: campeón mundial tanto en motociclismo como en Fórmula 1. Su versatilidad y talento le dieron un lugar destacado en el automovilismo, no me esperaba esa respuesta pero veo que tienes sabios gustos jaja.")

        elif "rossi" in p3_MGP_respuesta or "valentino" in p3_MGP_respuesta:
            print ("Mira, que te quede claro que Rossi es un guarro, un pegapatadas y un malisimo perdedor. Pero también ha ganado lo suyo... Así que voy a tener un minimo de respeto hacia él (lo que el no tiene hacia el resto) y voy a dejar aquí su información: Valentino Rossi, 9 veces campeón del mundo, es una de las mayores leyendas del motociclismo, ícono global y figura clave en la popularización de MotoGP.")

        usuario_prefiere_MotoGP = "MotoGP"
        print("Bueno... Hoy ya hemos hablado mucho, mejor seguimos hablando otro dia, paramos ahora para tener más conversaciones después jaja. Me alegro de conocerte, ¡¡¡Veo que compartimos una pasión muy bonita por el motor!!!")

elif "paramos" in preguntafinal_respuesta or "parar" in preguntafinal_respuesta or "Adios" in preguntafinal_respuesta or "ya" in preguntafinal_respuesta:
        print ("Vale... Si cambias de opinion estoy aquí :(")
