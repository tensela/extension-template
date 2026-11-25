# A Tensela extension

A starting point for an extension of [Tensela](https://tensela.com): a node, an action, a right-click entry, a panel
and an icon, with its tests and what publishes it. The manual tells everything step by step:
**Extensions → Write an extension** (tensela.com/manual/extensions/write/). [En español](README.es.md).

## 1. Make it yours

1. Copy this repository (on GitHub, **Use this template**) with the name of your extension, for example
   `facade-tools`.
2. In `extension.toml`: `id = "facade-tools"`, its name, your name, what it does, its licence and its links.
3. Rename the folder `my_extension` as the id with `_` instead of `-`: `facade_tools`.
4. In `my_extension/__init__.py` (now `facade_tools/__init__.py`), keep what you need and delete the rest.

## 2. Try it while you write it

1. In Tensela: **Extensions → Manage extensions… → Load a folder…** and choose this folder. It is on at once, without
   installing it.
2. Change the code, save, and press **Reload** (the round arrow on its card). Tensela reads it again: you do not
   need to close it.
3. Its tests: `python -m pytest tests` (with Tensela importable: `pip install -e path/to/tensela`).

## 3. Pack it

```bash
tensela-app --pack-extension .
```

With the AppImage: `Tensela.AppImage --pack-extension .`. It checks its card, leaves `<id>-<version>.zip` beside the
folder and says its SHA-256 (its fingerprint). The `.zip` is what people install (**Install from a file…**).

## 4. Publish it

1. Put its code in a public repository (the catalogue asks for it: anyone can read what it does).
2. Tag a version: `git tag v0.1.0 && git push --tags`. The workflow of `.github/workflows/release.yml` runs the
   tests, packs it and attaches the `.zip` and `SHA256SUMS` to a release.
3. Ask for it to enter the catalogue of tensela.com: a pull request to the repository **tensela/tensela-extensions**
   with a file `extensions/<id>.json` (its README says how). It is reviewed: public code, permissions that make sense,
   nothing hidden.

## 5. Update it

Change `version` in `extension.toml`, tag the new version, and a pull request that changes the version, the link and
the fingerprint in its file of the catalogue. Whoever installs the new `.zip` sees «It updates the one installed».

## Licence

This template is yours to use as you like (CC0: no conditions). Your extension carries the licence you choose in
`extension.toml`.
