# Cómo agregar tu informe

Esta guía es para los grupos que terminan su proyecto y quieren dejar el informe en el repositorio.

## Antes de empezar

- Tu informe tiene que estar **aprobado**, o tener el visto bueno de tu director/a para publicarse.
- **Todos los integrantes** del grupo tienen que estar de acuerdo con la publicación.
- Pedile a [NOMBRE / MAIL DEL REFERENTE DEL LAB] que te agregue al team [Alumnos](https://github.com/orgs/Proyecto-Scheduler/teams/alumnos) del repositorio. Con ese acceso trabajás en una rama del propio repositorio.

## Paso a paso

1. **Clonás el repositorio** y creás una rama: `git switch -c informe/nombre-corto`, donde `nombre-corto` es un nombre descriptivo, pero corto del proyecto.
2. **Copiá la carpeta `plantilla/`** a `AAAA/nombre-corto/`, donde `AAAA` es el año de entrega.
3. **Agregá el PDF** como `informe.pdf`.
4. **Agregá las fuentes (opcional)** (LaTeX, docx, figuras originales) en la carpeta `fuentes/`.
5. **Completá el `metadata.yml`** (ver abajo).
6. **Probalo en tu máquina** (opcional): instalá PyYAML con `pip install pyyaml` y ejecutá `python scripts/generate_index.py --check`. Si algo está mal, te dice qué.
7. **Subí la rama y abrí un Pull Request** hacia `main`, con el título `Informe AAAA: Título del proyecto`.
8. **Esperá al workflow.** Valida tu `metadata.yml` y, si hace falta, agrega a tu rama un commit con la tabla del README actualizada. Si falla, el PR muestra el error: corregilo y volvé a subir.
9. **Si vas a subir más cambios, hacé antes `git pull --rebase`** para traer el commit del workflow. Si no, el push te va a ser rechazado.
10. Alguien del lab revisa el PR, te pide cambios si hacen falta y lo incorpora.

¿No tenés acceso al repositorio? Podés hacer un fork y abrir el PR desde ahí. En ese caso el workflow no puede commitear por vos: ejecutá `python scripts/generate_index.py` en tu máquina y subí también el README resultante.

## Convención de nombres

- Carpeta: `AAAA/nombre-corto`, donde `AAAA` es el año de entrega y tiene que coincidir con `anio` en el `metadata.yml`.
- El nombre corto va en minúsculas, **sin espacios, tildes ni caracteres especiales**, con guiones para separar palabras.
- Ejemplo: `2024/shceduler-con-redes-de-petri`
- El PDF siempre se llama `informe.pdf`.

## Campos del `metadata.yml`

```yaml
titulo: Título completo del proyecto
titulo_corto: Título corto para el índice # opcional, útil si el título es muy largo
anio: 2025
integrantes:
  - Nombre Apellido
  - Nombre Apellido
director: Nombre Apellido
codirector: Nombre Apellido # opcional
resumen: >
  Tres o cuatro líneas: qué problema se atacó, qué se hizo
  y cuál fue el resultado.
estado: terminado # terminado | linea-abierta
repos:
  - https://github.com/org/repo
trabajo_futuro:
  - Tarea concreta que quedó pendiente
  - Otra tarea concreta
palabras_clave: [palabra1, palabra2, palabra3]
relacionados: # opcional: informes previos o vinculados
  - 2022/nombre-corto
```

**Obligatorios:** `titulo`, `anio`, `integrantes`, `director`, `resumen` y `estado`.

- **`estado`:** `terminado` si no queda trabajo relevante para continuar, o `linea-abierta` si otro grupo puede retomarlo.
- **`trabajo_futuro`:** una lista de tareas. Es lo que más le sirve al grupo siguiente, así que sé concreto: intentá evitar frases como "se podría mejorar el rendimiento" sin decir dónde ni cómo.
- **`relacionados`:** cada ítem tiene el formato `AAAA/nombre-corto` y tiene que apuntar a un informe que exista en el repositorio.

## Checklist del Pull Request

- [ ] El informe está aprobado y todos los integrantes aceptan publicarlo
- [ ] La carpeta es `AAAA/nombre-corto` y el año coincide con `anio`
- [ ] Incluye `informe.pdf` y un `metadata.yml` completo
- [ ] Incluí las fuentes en `fuentes/` (o aclaré por qué no)
- [ ] Los enlaces a repositorios funcionan y son accesibles
- [ ] No edité a mano la tabla del README (se genera sola)

## Archivos pesados

Si tu informe o sus anexos superan los **50 MB**, no los subas directamente al repositorio. Consultá con el laboratorio para usar Git LFS o un release.

## Correcciones y actualizaciones

Si encontrás un error en un informe existente, o querés actualizar el estado de una línea de trabajo (por ejemplo, "esto ya lo retomó el grupo de 2026"), abrí un Pull Request o un Issue con el cambio propuesto.

## Dudas

Escribile a [NOMBRE / MAIL DEL REFERENTE DEL LAB] o abrí un Issue con la etiqueta `consulta`.
