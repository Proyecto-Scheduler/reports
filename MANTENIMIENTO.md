# Mantenimiento del repositorio

Notas para quienes administran el repositorio. Los grupos que suben informes no necesitan leerlas: para eso está [CONTRIBUTING.md](CONTRIBUTING.md).

## Accesos

- Los grupos trabajan en ramas del propio repositorio, no en forks. Para eso se los agrega al team [Alumnos](https://github.com/orgs/Proyecto-Scheduler/teams/alumnos) con rol **Write**.
- Al terminar cada cohorte conviene sacar a esos grupos del team o bajarlos a **Read**, así el acceso no se acumula.

## Protección de `main`

- Exigir Pull Request y al menos una aprobación antes de mergear.
- **No marcar el check `update-index` como obligatorio.** El workflow agrega un commit a la rama del PR con el token por defecto de GitHub, y esos commits no disparan checks. Si el check fuera obligatorio, el PR quedaría esperando un resultado que nunca llega.
- Igual se ve en el PR: si la metadata es inválida, el workflow falla y el PR muestra una cruz roja. Quien revisa debería mirarla antes de mergear.
- Si preferís que sea obligatorio, creá un secret `INDEX_BOT_TOKEN` con un token personal de acceso (fine-grained, limitado a este repositorio, con permiso de escritura en el contenido). El workflow lo usa automáticamente, el commit del bot vuelve a disparar los checks y el que corre después pasa sin cambios. Los commits quedan a nombre de la cuenta dueña del token.

## Cómo funciona el índice

- `scripts/generate_index.py` lee todos los `AAAA/nombre-corto/metadata.yml` y reemplaza la tabla del README entre `<!-- INDEX:START -->` y `<!-- INDEX:END -->`. Ignora `plantilla/`.
- El workflow `.github/workflows/update-index.yml` lo ejecuta en cada Pull Request hacia `main` que toque un `metadata.yml`, el README, el script o el propio workflow.
- Si el PR viene de una rama del repositorio, el workflow commitea el README actualizado en esa rama. Si viene de un fork, no tiene permiso de escritura y solo verifica; quien abre el PR tiene que correr el script a mano.
- Para verificar sin modificar nada: `python scripts/generate_index.py --check`.

## Problemas frecuentes

- **Conflicto en el README entre dos PRs:** cuando entra uno, el otro puede quedar con conflicto en la tabla. Se resuelve actualizando la rama, ejecutando `python scripts/generate_index.py` y commiteando el README.
- **El workflow falla con errores de metadata:** el mensaje indica el archivo y el campo. Los más comunes son un `anio` que no coincide con la carpeta, un `estado` fuera de `terminado` / `linea-abierta`, o una referencia en `relacionados` que no tiene el formato `AAAA/nombre-corto`.
- **El push de un grupo es rechazado:** el workflow agregó un commit a su rama. Tienen que ejecutar `git pull --rebase` y volver a subir.
