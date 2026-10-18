# ia101-demo

Repositorio de práctica de la sesión 2 del curso IA 101 de Colombiana de Trasplantes. Todos los datos son inventados.

`consolidar.py` lee `datos/indicadores_ejemplo.csv` y escribe en `salida/` un resumen por servicio y mes.

```
python3 consolidar.py
```

Para practicar, haz un fork a tu cuenta de GitHub, ábrelo en la pestaña Code de la app de escritorio de Claude y pide un cambio en modo Plan. Revisa el diff, corre `/code-review` y abre el pull request en tu propio fork.

Hoy el script falla porque una fila de agosto trae vacía la oportunidad en días. Ese es el ejercicio: pedirle a Claude que lo detecte y avise, sin tocar los datos.

En este repositorio, y en cualquier otro, no entran datos de pacientes.
