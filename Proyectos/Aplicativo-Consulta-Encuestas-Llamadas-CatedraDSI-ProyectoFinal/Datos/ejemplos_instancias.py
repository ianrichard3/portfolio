encuestas = [

    #Encuesta 0 

    {"descripcion": "Atencion al Cliente",
        "fechafinvigencia": "25/09/2023",
        "preguntas":[
            {
                "pregunta": "¿Se soluciono su problema?",
                "respuestas posibles": [{
                    "descripcion": "Si se soluciono",
                    "valor":1 
                        },
                    {
                        "descripcion": "No se soluciono",
                        "valor": 2
                            }]
            },
            {
                "pregunta": "¿Como califica al representante que atendio su consulta?",
                "respuestas posibles": [{
                    "descripcion": "Mal",
                    "valor": 1
                        },
                    {
                        "descripcion": "Bien",
                        "valor": 2
                            },
                    {
                        "descripcion": "Muy Bien",
                        "valor": 3
                            }]
            },
            {
                "pregunta": "¿Recomendaria nuestro servicio a otras personas?",
                "respuestas posibles": [{
                    "descripcion": "Si",
                    "valor":1 
                        },
                    {
                        "descripcion": "No",
                        "valor": 2
                    },
                    {
                        "descripcion": "Tal vez",
                        "valor": 3
                    }
                    ]
            },
        ]
    },











    # ENCUESTA 1
    {
        "descripcion": "Atención al Cliente",
        "fechaFinVigencia": "08/12/2025",
        "preguntas":[
            {
                "pregunta":"¿Que tal ha sido la atencion proporcionada?",
                "respuestas posibles":[{
                    "descripcion": "Muy mala",
                    "valor":1
                },
                {
                    "descripcion":"Mala",
                    "valor":2
                },
                {
                    "descripcion":"Regular",
                    "valor":3
                },
                {
                    "descripcion":"Buena",
                    "valor":4
                },
                {
                    "descripcion":"Muy Buena",
                    "valor":5
                }
                ]
            },
            {
                "pregunta":"¿Recomendaría nuestro servicio a otras personas?",
                "respuestas posibles":[
                    {
                        "descripcion":"Si, lo recomendaría.",
                        "valor":1
                    },
                    {
                        "descripcion":"No, no lo recomendaría.",
                        "valor":2
                    }
                ]
            },
            {
                "pregunta":"¿Que tan satisfecho quedó después de la llamada?",
                "respuestas posibles":[
                    {
                        "descripcion":"Muy insatisfecho",
                        "valor":1
                    },
                    {
                        "descripcion":"Insatisfecho",
                        "valor":2
                    },
                    {
                        "descripcion":"Regular",
                        "valor":3
                    },
                    {
                        "descripcion":"Satisfecho",
                        "valor":4
                    },
                    {
                        "descripcion":"Muy Satisfecho",
                        "valor":5
                    }
                ]

            }
        ]
    },



    # ENCUESTA 2

    {
        "descripcion": "Atención al Cliente",
        "fechaFinVigencia": "28/02/2023",
        "preguntas":[
            {
                "pregunta":"¿Como calificaría la calidad de nuestro servicio?",
                "respuestas posibles":[{
                    "descripcion": "Muy mala",
                    "valor":1
                },
                {
                    "descripcion":"Mala",
                    "valor":2
                },
                {
                    "descripcion":"Regular",
                    "valor":3
                },
                {
                    "descripcion":"Buena",
                    "valor":4
                },
                {
                    "descripcion":"Muy Buena",
                    "valor":5
                }
                ]
            },
            {
                "pregunta":"¿Que tan satisfecho quedó después de la llamada?",
                "respuestas posibles":[
                    {
                        "descripcion":"Muy insatisfecho",
                        "valor":1
                    },
                    {
                        "descripcion":"Insatisfecho",
                        "valor":2
                    },
                    {
                        "descripcion":"Regular",
                        "valor":3
                    },
                    {
                        "descripcion":"Satisfecho",
                        "valor":4
                    },
                    {
                        "descripcion":"Muy Satisfecho",
                        "valor":5
                    }
                ]

            },
            {
                "pregunta":"¿Se logró solucionar su problema?",
                "respuestas posibles":[
                    {
                        "descripcion":"Si, se solucionó.",
                        "valor":1
                    },
                    {
                        "descripcion":"No, no se solucionó.",
                        "valor":2
                    }
                ]
            }
        ]
    },

    # ENCUESTA 3

    {
        "descripcion":"Atención al cliente",
        "fechaFinVigencia":"15/04/2026",
        "preguntas":[
            {
                "pregunta":"¿Que tal ha sido la atencion proporcionada?",
                "respuestas posibles":[{
                    "descripcion": "Muy mala",
                    "valor":1
                },
                {
                    "descripcion":"Mala",
                    "valor":2
                },
                {
                    "descripcion":"Regular",
                    "valor":3
                },
                {
                    "descripcion":"Buena",
                    "valor":4
                },
                {
                    "descripcion":"Muy Buena",
                    "valor":5
                }
                ]
            },
            {
                "pregunta":"¿Recomendaría nuestro servicio a otras personas?",
                "respuestas posibles":[
                    {
                        "descripcion":"Si, lo recomendaría.",
                        "valor":1
                    },
                    {
                        "descripcion":"No, no lo recomendaría.",
                        "valor":2
                    }
                ]
            },
            {
                "pregunta":"¿Se logró solucionar su problema?",
                "respuestas posibles":[
                    {
                        "descripcion":"Si, se solucionó.",
                        "valor":1
                    },
                    {
                        "descripcion":"No, no se solucionó.",
                        "valor":2
                    }
                ]
            }
        ]
    }
    
]




llamadas = [
    # LLAMADA 1
    {
        "descripcionOperador": "Operador1",
        "detalleAccionRequerida": "Comunicar Saldo",
        "duracion" : 2.5,
        "encuestaEnviada": True,
        "observacionAuditor": "SinObservacion",
        "cambios de estado": [
            {
                "Cambio Estado1": "PrimerEstado",
                "estado": "Inicializado"
            },
            {
                "Cambio Estado2": "SegundoEstado",
                "Estado": "Inicializado"

            }
        ],
        "cliente": {
            "dni": 12345678,
            "nombreCompleto": "Juan Pérez",
            "nroCelular": 555-123-4567
        },
        "respuestas de Clientes":[
            {
                "fechaEncuesta": "12/08/2022",
                "respuestaSeleccionada": "Si, se soluciono."
            },
            {
                "fechaEncuesta": "15/09/2022",
                "respuestaSeleccionada": "No, no se soluciono."
            }
        ]
    },

    # LLAMADA 2
    {
        "descripcionOperador": "Operador2",
        "detalleAccionRequerida": "Denunciar robo",
        "duracion" : 3.5,
        "encuestaEnviada": False,
        "observacionAuditor": "ConObservacion",
        "cambios de estado": [
            {
                "Cambio Estado1": "PrimerEstado",
                "Estado": "Inicializado"
            },
            {
                "Cambio Estado2": "SegundoEstado",
                "Estado": "Finalizado"
            }
        ],
        "cliente": {
            "dni": 23456789,
            "nombreCompleto": "María Rodríguez",
            "nroCelular": 367-234-5678

        },
        "respuestas de Clientes":[
            {
                "fechaEncuesta": "10/02/2022",
                "respuestaSeleccionada": "Si, se soluciono.",
                
            },
            {
                "fechaEncuesta": "09/05/2022",
                "respuestaSeleccionada": "No, no se soluciono.",
            }
        ]
    },
        
    # LLAMADA 3
    {
        "descripcionOperador": "Operador3",
        "detalleAccionRequerida": "Dar baja tarjeta",
        "duracion" : 1.5,
        "encuestaEnviada": True,
        "observacionAuditor": "SinObservacion",
        "cambios de estado": [
            {
                "Cambio Estado1": "PrimerEstado",
                "Estado": "Inicializado"
            },
            {
                "Cambio Estado2": "SegundoEstado",
                "Estado": "Finalizado"

            }
        ],
        "cliente": {
            "dni": 34567890,
            "nombreCompleto": "Carlos González",
            "nroCelular": 576-345-6789
        },
        "respuestas de Clientes":[
            {
                "fechaEncuesta": "19/07/2023",
                "respuestaSeleccionada": "Si, se soluciono."
                
            },
            {
                "fechaEncuesta": "29/08/2023",
                "respuestaSeleccionada": "No, no se soluciono."
            }   
                
        ]       
    }
]