# Informes de proyectos · [NOMBRE DEL LABORATORIO]

Archivo de informes finales y tesinas de los proyectos desarrollados en el laboratorio [NOMBRE DEL LABORATORIO] de la [Facultad de Ciencias Exactas, Físicas y Naturales](https://fcefyn.unc.edu.ar/) de la [Universidad Nacional de Córdoba](https://www.unc.edu.ar/).

Cada grupo que termina su proyecto deja acá su informe, con la información necesaria para que el siguiente grupo sepa **qué se hizo, qué quedó pendiente y dónde está el código**.

## Si sos un grupo nuevo

1. **Mirá el [índice](#índice-de-informes)** y buscá los proyectos relacionados con tu tema.
2. **Leé primero el `metadata.yml`** de cada uno, en particular `resumen` y `trabajo_futuro`. Es más rápido que abrir el PDF completo.
3. **Revisá los repositorios de código** enlazados en `repos` antes de empezar algo desde cero.
4. **Consultá el informe completo** de los proyectos que te sirvan de base.
5. Si vas a continuar una línea abierta, hablalo con [DIRECTOR/A O REFERENTE DEL LAB] antes de arrancar.

## Índice de informes

<!-- INDEX:START -->
<!-- Esta tabla se genera automáticamente a partir de los metadata.yml. No editar a mano. -->

| Año | Proyecto | Integrantes | Estado | Trabajo futuro |
|-----|----------|-------------|--------|----------------|
| 2026 | [Modelado y extensión de un planificador del sistema operativo mediante redes de Petri: integración de funcionalidades de monopolización de núcleos e inhibición de asignación de trabajo a procesadores](2026/modelado-extension-planificador-redes-petri/) | Leandro Agustín Drudi, Nicolás Goldman | Línea abierta | 6 tareas |
| 2024 | [Scheduling guiado por tipo de proceso para FreeBSD](2024/scheduling-guiado-por-tipo-de-proceso/) | Francisco Ignacio Bonino, Francisco Daniele | Línea abierta | 5 tareas |
| 2022 | [Comunicación desde espacio de usuario a espacio de kernel mediante metadatos en archivos ELF](2022/metadatos-elf-espacio-kernel/) | José María Cancinos, Julián González | Línea abierta | 3 tareas |
| 2021 | [Compiladores y ejecutables](2021/compiladores-y-ejecutables-pps/) | José Cancinos, Julián González | Terminado | 0 tareas |
| 2017 | [Modelado del planificador a corto plazo con redes de Petri](2017/modelado-planificador-redes-petri/) | Tomás Turina, Nicolás Papp | Línea abierta | 6 tareas |

<!-- INDEX:END -->

La tabla se actualiza sola: un workflow la regenera en cada Pull Request que toca un `metadata.yml`, así que no hace falta editarla a mano.

## Estructura del repositorio

```
.
├── README.md
├── CONTRIBUTING.md          # cómo agregar tu informe
├── MANTENIMIENTO.md         # configuración del repo, para quienes lo administran
├── template/                # copiá esta carpeta para tu informe
│   ├── metadata.yml
│   └── README.md
├── scripts/
│   └── generate_index.py    # genera la tabla de informes del README
├── .github/workflows/
│   └── update-index.yml     # corre el script en cada Pull Request
└── AAAA/                    # año de entrega
    └── nombre-corto/
        ├── informe.pdf
        ├── metadata.yml
        └── fuentes/         # LaTeX, docx u otros archivos fuente
```

## Cómo agregar tu informe

Las instrucciones paso a paso están en [CONTRIBUTING.md](CONTRIBUTING.md).

## Licencia

Salvo que se indique otra cosa en el `metadata.yml` de cada informe, el contenido de este repositorio se publica bajo [LICENCIA, por ejemplo CC BY 4.0](LICENSE). El código de los proyectos vive en sus propios repositorios, con su propia licencia.

## Contacto

Consultas sobre el repositorio o el laboratorio: [NOMBRE / MAIL / SITIO WEB DEL LAB].
