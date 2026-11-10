"""Executa cada notebook do curso e confere que todas as verificações passaram.

Cada notebook termina imprimindo "Módulo N concluído: K verificações aprovadas."; qualquer
verificação que falhe interrompe a execução com AssertionError.

Uso: pytest -q                       (todos; leva cerca de 15 minutos)
     pytest -q -k "05_bsm or 06_crr"  (só alguns)
"""
import re
from pathlib import Path

import nbformat
import pytest
from nbclient import NotebookClient

RAIZ = Path(__file__).resolve().parents[1]
NOTEBOOKS = sorted(RAIZ.glob("[0-9][0-9]_*.ipynb"))


def test_ha_16_modulos():
    assert len(NOTEBOOKS) == 16


@pytest.mark.parametrize("caminho", NOTEBOOKS, ids=[p.stem for p in NOTEBOOKS])
def test_notebook_executa(caminho):
    nb = nbformat.read(caminho, as_version=4)
    NotebookClient(nb, timeout=900, kernel_name="python3", resources={"metadata": {"path": str(RAIZ)}}).execute()
    saidas = "".join(
        o.get("text", "") for c in nb.cells if c.cell_type == "code" for o in c.get("outputs", []) if o.get("output_type") == "stream"
    )
    modulo = int(caminho.name[:2])
    m = re.search(rf"Módulo {modulo} concluído: (\d+) verificações aprovadas", saidas)
    assert m, "o notebook não chegou à célula final"
    assert int(m.group(1)) > 0
    assert "FALHOU" not in saidas
