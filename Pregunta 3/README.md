# EXAMEN 1 - CI3641 - PREGUNTA 3
# Jennifer Gámez 16-10396

## Instrucciones de Ejecucion. Buddy System

    - buddy_system.py: Contiene la clase BuddySystem.
    - main.py: Contiene el main() o la lógica principal de la aplicación.
    - test_buddy_system.py: Contiene las pruebas unitarias para la clase BuddySystem.

    Puede probar la clase de buddy system, ejecutando la terminal

    ``` python3 main.py ```

    Las instrucciones permitidas son: RESERVAR, LIBERAR, MOSTRAR, AYUDA y SALIR.
    
    Instrucciones del programa:
    1. Para reservar un bloque de memoria, escriba: RESERVAR tamaño_del_bloque nombre_del_proceso
       Ejemplo: RESERVAR Proceso1 32
    2. Para liberar un bloque de memoria asociado a un proceso, escriba: LIBERAR nombre_del_proceso
       Ejemplo: LIBERAR Proceso1
    3. Para mostrar el estado actual de la memoria y la lista de procesos, escriba: MOSTRAR
    4. Para ver estas instrucciones nuevamente, escriba: AYUDA
    5. Para salir del programa, escriba: SALIR.

## Requisitos del Sistema

Para realizar las pruebas de cobertura, asegúrate de cumplir con los siguientes requisitos:

1. Tener instalado pytest. Si no lo tienes instalado, puedes hacerlo con el siguiente comando:

    ``` pip install pytest```

2. Tener instalado coverage. Si no lo tienes instalado, puedes hacerlo con el siguiente comando:

    ``` pip install coverage```

Asegúrate de que ambas dependencias estén instaladas y configuradas en tu entorno antes de ejecutar las pruebas de cobertura.