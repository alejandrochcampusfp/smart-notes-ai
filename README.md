# Estructura del Proyecto

    ```text
    app-portfolio-ia/
    │
    ├── app/
    │   ├── static/
    │   │   └── index.html       # La interfaz visual bonita (HTML + Tailwind CSS + JavaScript)
    │   ├── database.py          # Conexión limpia y segura con SQLite
    │   ├── models.py            # Tabla de notas/tareas
    │   ├── schemas.py           # Validación estricta con Pydantic (seguridad anti-inyecciones)
    │   ├── crud.py              # Operaciones seguras en base de datos
    │   ├── ai_service.py        # Integración limpia con la IA de Groq (gratis)
    │   └── main.py              # FastAPI que une la API y sirve la web en la ruta raíz (/)
    │
    ├── .env                     # Tu clave de Groq
    ├── Dockerfile               # Para empaquetarlo y desplegarlo gratis
    └── requirements.txt         # Dependencias



SmartNotes AI - Gestor Inteligente de Notas 🧠✨
    Aplicación web desarrollada como parte de un portfolio técnico que combina un backend en FastAPI, un frontend limpio y funcional, y la potencia de la inteligencia artificial a través de la API de Groq para generar resúmenes automáticos de notas en tiempo real.



🚀 Características
    Creación de Notas Inteligentes: Escribe notas y obtén resúmenes automáticos generados por IA al instante.

    Integración con Groq (LLMs): Utiliza modelos de lenguaje avanzados para sintetizar textos largos de forma profesional.

    Arquitectura Contenedorizada: Preparado para ejecutarse de manera aislada y sencilla mediante Docker.



🛠️ Tecnologías Utilizadas
    Backend: Python, FastAPI, Uvicorn, Requests.

    Inteligencia Artificial: Groq API (openai/gpt-oss-20b).

    Despliegue: Docker.

    Entorno: Variables de entorno seguras con python-dotenv.




⚙️ Cómo poner en marcha el proyecto
    1. Requisitos previos
    Tener instalado Docker en tu equipo.

    Una clave de API de Groq (GROQ_API_KEY).

    2. Configurar las variables de entorno
    Crea un archivo .env en la raíz del proyecto y añade tu clave:
    GROQ_API_KEY=tu_clave_de_groq_aqui

    3. Ejecutar con Docker
    Abre tu terminal en la carpeta del proyecto y ejecuta los siguientes comandos:
    # Construir la imagen sin caché
    docker build --no-cache -t smart-notes-app .

    # Arrancar el contenedor
    docker run --rm --name smart-notes --env-file .env -p 8000:8000 smart-notes-app

    Una vez lanzado, abre tu navegador y entra en: http://localhost:8000




🧪 Texto de prueba recomendado
    Puedes copiar y pegar el siguiente texto en la aplicación para comprobar el funcionamiento del resumen automático por IA:

    Título: Proyecto de domótica para casa
    Contenido: Esta semana tengo que terminar la instalación de los sensores de temperatura y humedad en el salón. También hay que configurar la automatización de las persianas para que bajen automáticamente cuando se haga de noche y revisar por qué la conexión MQTT con el servidor de Home Assistant está dando pequeños cortes intermitentes por la tarde.
