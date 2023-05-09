# project_template
Template basico de proyectos web

Este template está diseñado para tener estructuras básicas de herramientas básicas para un proyecto de desarrollo web:
1.- Airflow: como orquestador para procesos, pipelines de ingeniería de datos (ETL)
2.- API: un api rest para comunicación entre base de datos, kedro, streamlit, front y otros clientes.
3.- DB: un motor de base de datos. Por ahora se opta por PostgreSQL
4.- Front: no definido, pero podría ser un proyecto con react js
5.- Kedro: como orquestador de pipelines de Ciencia de Datos (DS)
6.- Streamlit: interfaz simple y de rápido desarrollo para resultados y visualización de tareas de Ciencia de Datos.

Dentro de cada carpeta se incluirán estructuras de carpetas básicas, más los Dockerfile con los contenedores de cada uno.
Un archivo Docker compose y Makefile nos ayudarán a hacer pruebas unitarias y despliegues locales.

Se debe evaluar esto para implementación en la nube.