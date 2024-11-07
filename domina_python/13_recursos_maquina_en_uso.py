import psutil

def recursos_usados_cpu():
    nucleos = psutil.cpu_count(logical=False)
    print("Cantidad de nucleos: ", nucleos)

    carga = psutil.getloadavg()
    print("Carga promedio: ", carga)

    usa = psutil.cpu_percent(interval=5, percpu=True)
    print("El porcentaje de uso de la cpu:  ", usa)


recursos_usados_cpu()
