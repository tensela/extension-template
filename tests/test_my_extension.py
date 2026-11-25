"""The tests of the extension: its card reads well, its node computes, and it packs. Run them with
`python -m pytest tests` from this folder, with Tensela importable (pip install -e path/to/tensela)."""
from pathlib import Path

import pytest

from tensela import extensions as E
from tensela.graph import Graph

HERE = Path(__file__).resolve().parent.parent


@pytest.fixture
def loaded(tmp_path, monkeypatch):
    monkeypatch.setenv("XDG_CONFIG_HOME", str(tmp_path / "config"))
    monkeypatch.setenv("XDG_DATA_HOME", str(tmp_path / "share"))
    ext = E.read(HERE)
    assert not ext.problem, ext.problem
    E.load(ext)
    yield ext
    E.unload(ext.id)


def test_its_card_is_right(loaded):
    assert loaded.version and loaded.description and loaded.author


def test_the_fold_node_computes(loaded):
    g = Graph()
    g.node("Fold", "roof", length=10, folds=5, rise=1.5)
    curve = g.value("roof")
    assert curve.kind is not None and curve.kind.name.startswith("curve")


def test_it_packs(loaded, tmp_path):
    target, fingerprint = E.pack(HERE, tmp_path)
    assert target.name == f"{loaded.id}-{loaded.version}.zip" and len(fingerprint) == 64
    assert E.look_inside(target)[0].id == loaded.id
