# Una extensión de Tensela

[In English](README.md)

Un punto de partida para una extensión de [Tensela](https://tensela.com): un nodo, una acción, una entrada del clic
derecho, un panel y un icono, con sus pruebas y lo que la publica. El manual lo cuenta paso a paso:
**Extensiones → Escribir una extensión** (tensela.com/es/manual/extensions/write/).

## 1. Hazla tuya

1. Copia este repositorio (en GitHub, **Use this template**) con el nombre de tu extensión, por ejemplo
   `facade-tools`.
2. En `extension.toml`: `id = "facade-tools"`, su nombre, tu nombre, qué hace, su licencia y sus enlaces.
3. Renombra la carpeta `my_extension` como el id con `_` en vez de `-`: `facade_tools`.
4. En `my_extension/__init__.py` (ahora `facade_tools/__init__.py`), deja lo que te sirva y borra el resto.

## 2. Pruébala mientras la escribes

1. En Tensela: **Extensiones → Gestionar extensiones… → Cargar una carpeta…** y elige esta carpeta. Queda encendida
   en el acto, sin instalarla.
2. Cambia el código, guarda y aprieta **Recargar** (la flecha circular de su tarjeta). Tensela la vuelve a leer: no
   hace falta cerrarla.
3. Sus pruebas: `python -m pytest tests` (con Tensela importable: `pip install -e ruta/a/tensela`).

## 3. Empaquétala

```bash
tensela-app --pack-extension .
```

Con la AppImage: `Tensela.AppImage --pack-extension .`. Revisa su ficha, deja `<id>-<versión>.zip` al lado de la
carpeta y dice su SHA-256 (su huella). El `.zip` es lo que la gente instala (**Instalar desde un archivo…**).

## 4. Publícala

1. Pon su código en un repositorio público (el catálogo lo pide: cualquiera puede leer qué hace).
2. Marca una versión: `git tag v0.1.0 && git push --tags`. El flujo de `.github/workflows/release.yml` corre las
   pruebas, la empaqueta y adjunta el `.zip` y `SHA256SUMS` a una publicación (release).
3. Pide que entre al catálogo de tensela.com: un pull request al repositorio **tensela/tensela-extensions** con un
   archivo `extensions/<id>.json` (su README dice cómo). Se revisa: código público, permisos con sentido, nada
   escondido.

## 5. Actualízala

Cambia `version` en `extension.toml`, marca la versión nueva, y un pull request que cambie la versión, el enlace y la
huella en su archivo del catálogo. Quien instale el `.zip` nuevo ve «Actualiza la instalada».

## Licencia

Esta plantilla es tuya para usarla como quieras (CC0: sin condiciones). Tu extensión lleva la licencia que elijas en
`extension.toml`.
