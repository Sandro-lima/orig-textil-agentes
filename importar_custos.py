import csv
import sys
import zipfile
from decimal import Decimal, ROUND_HALF_UP

from openpyxl import load_workbook

def costs(path):
    sheet = load_workbook(path, data_only=True, read_only=True)["Custos por modelo"]
    seen = set()
    for name, yield_kg, price_kg, consumption, sewing, cut, other, *_ in sheet.iter_rows(min_row=7, max_col=10, values_only=True):
        if not isinstance(name, str) or not name.strip() or name.casefold().startswith("exemplo"):
            continue
        name = name.strip()
        key = name.casefold()
        if key in seen:
            raise ValueError(f"Modelo duplicado: {name}")
        seen.add(key)
        required = [yield_kg, price_kg, consumption, sewing]
        optional = [0 if value is None else value for value in (cut, other)]
        inputs = required + optional
        if not all(type(value) in (float, int) and value >= 0 for value in inputs) or not all(value > 0 for value in required[:3]):
            yield (name, *inputs, "", "", "incompleto")
            continue
        y, p, c, s, t, o = map(lambda value: Decimal(str(value)), inputs)
        tissue = p / y * c
        total = (tissue + s + t + o).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        yield (name, *inputs, tissue.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP), total, "aguarda_validacao")

def export(source, output):
    writer = csv.writer(output, delimiter=";", lineterminator="\n")
    writer.writerow(["modelo", "rendimento_m_kg", "tecido_brl_kg", "consumo_m_peca", "costura_brl", "corte_brl", "outros_brl", "tecido_brl_peca", "custo_brl_peca", "status"])
    rows = list(costs(source))
    midi_name = "vestido midi"
    linked_name = "vestido com costas trançadas"
    midi = next((row for row in rows if row[0].casefold() == midi_name), None)
    for row in rows:
        if row[0].casefold() == linked_name:
            amount = midi[-2] if midi else ""
            status = "vinculado_ao_midi_aguarda_validacao" if amount != "" else "custo_do_midi_incompleto"
            row = (row[0], *[""] * 7, amount, status)
        writer.writerow([str(value).replace(".", ",") if isinstance(value, (float, Decimal)) else value for value in row])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Uso: python importar_custos.py caminho/planilha.xlsx")
    export(sys.argv[1], sys.stdout)
