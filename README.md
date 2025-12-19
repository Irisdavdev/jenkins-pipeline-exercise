# 🚴‍♂️ Cicloturismo Pipeline: Automatización CI/CD para Bases de Datos

Este proyecto demuestra la implementación de un flujo de **Integración Continua (CI)** utilizando **Jenkins** y **Docker** para automatizar el despliegue de esquemas y datos en una base de datos **PostgreSQL**. La solución garantiza que cada cambio en el código o en la estructura SQL se valide y aplique de forma automática.

## 🎯 Objetivos del Proyecto

* **Automatización Total:** Ejecución de scripts Python y SQL mediante disparadores automáticos.
* **Entornos Aislados:** Uso de contenedores Docker y entornos virtuales de Python para garantizar la portabilidad.
* **Gestión de Datos:** Procesamiento dinámico de archivos de configuración de base de datos.

## 🛠️ Tecnologías Utilizadas

* **Orquestación:** Jenkins (Pipeline as Code).
* **Lenguajes:** Python 3.9 🐍 y SQL.
* **Infraestructura:** Docker 🐳 y PostgreSQL 🐘.
* **Control de Versiones:** Git y GitHub.

---

## 🏗️ Arquitectura del Pipeline

El `Jenkinsfile` define un ciclo de vida completo dividido en las siguientes etapas:

1. **Información de Inicio:** Validación de variables de entorno y metadatos de la ejecución.
2. **Preparación del Entorno:** Creación de un `virtualenv` para aislar dependencias.
3. **Gestión de Dependencias:** Instalación automatizada de librerías vía `pip`.
4. **Ejecución de Lógica:** Ejecución del script Python que interactúa con PostgreSQL.
5. **Post-Ejecución:** Limpieza automática y notificación de estados (Éxito/Fallo).

---

## 🚧 Desafíos Técnicos y Soluciones

Durante el desarrollo, abordé diversos problemas de infraestructura y código:

1. **Conectividad Red Docker:** El contenedor de Jenkins no alcanzaba al host local (Postgres).,Configuré postgresql.conf . para escuchar en todas las interfaces (*) y autoricé la subred de Docker en pg_hba.conf 🛡️.
2. **Persistencia de Datos:** El script fallaba al no encontrar la base de datos destino.,"Implementé la creación manual de la DB cicloturismo mediante terminal, asegurando la infraestructura antes de la ejecución 🐘."

## 🤖 Automatización (Triggers)

He configurado un **Poll SCM** (`H/2 * * * *`) que permite a Jenkins "vigilar" el repositorio de GitHub.

* **Resultado:** El pipeline se dispara automáticamente a los 2 minutos de detectar un `push` en la rama `main`.

## 📈 Resultado Final

El sistema es capaz de recibir un archivo `setup.sql` mediante parámetros, procesarlo y actualizar la tabla de `rutas` en tiempo real. Esto reduce el error humano y acelera el tiempo de despliegue de cambios en la base de datos. 🏁

---

*Proyecto desarrollado como parte de mi aprendizaje en DevOps e Integración Continua.*

---
