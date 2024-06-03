SHOW_LIST = 3
SHOW_IPHONE = 5
SHOW_SAMSUNG = 7

event_mapping = {
    SHOW_LIST: ("plp", -1),
    SHOW_SAMSUNG: ("pdp", 1),
    SHOW_IPHONE: ("pdp", 2),
}


conversation = [
    "Hola",
    "Hola, soy el chatbot, en que te puedo ayudar?",
    "Quiero ver celulares de gama alta",
    "A la izquierda podes ver un listado de los mejores celulares",
    "Quiero ver un samsung ahora",
    "Hola! Estas hablando con el Samsung s24+"
    "Mostrame el iphone mejor",
    "Hola! Soy el nuevo Iphone 15, podes preguntarme lo que quieras saber sobre mí",
]