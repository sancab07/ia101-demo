"""Consolida indicadores mensuales por servicio. Datos inventados, solo para práctica."""
import csv
from collections import defaultdict
from pathlib import Path

ENTRADA = Path(__file__).parent / "datos" / "indicadores_ejemplo.csv"
SALIDA = Path(__file__).parent / "salida" / "resumen.csv"


def leer(ruta):
    with open(ruta, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def validar(filas):
    """Devuelve una lista de avisos por cada celda vacía, con su número de fila en el CSV."""
    avisos = []
    for numero, fila in enumerate(filas, start=2):
        for columna, valor in fila.items():
            if valor is None or not valor.strip():
                avisos.append(f"Fila {numero}: '{columna}' está vacía ({fila['servicio']}, {fila['mes']}, {fila['sede']})")
    return avisos


def consolidar(filas):
    totales = defaultdict(lambda: {"atenciones": 0, "oportunidad_dias": []})
    for fila in filas:
        clave = (fila["servicio"], fila["mes"])
        totales[clave]["atenciones"] += int(fila["atenciones"])
        totales[clave]["oportunidad_dias"].append(float(fila["oportunidad_dias"]))
    resumen = []
    for (servicio, mes), v in sorted(totales.items()):
        promedio = sum(v["oportunidad_dias"]) / len(v["oportunidad_dias"])
        resumen.append({"servicio": servicio, "mes": mes,
                        "atenciones": v["atenciones"],
                        "oportunidad_promedio": round(promedio, 1)})
    return resumen


def escribir(resumen, ruta):
    ruta.parent.mkdir(exist_ok=True)
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["servicio", "mes", "atenciones", "oportunidad_promedio"])
        w.writeheader()
        w.writerows(resumen)


if __name__ == "__main__":
    filas = leer(ENTRADA)
    avisos = validar(filas)
    if avisos:
        print("El CSV trae celdas vacías; corrígelas en el origen y vuelve a correr:")
        for aviso in avisos:
            print(" -", aviso)
        raise SystemExit(1)
    resumen = consolidar(filas)
    escribir(resumen, SALIDA)
    print(f"{len(resumen)} filas en {SALIDA}")
