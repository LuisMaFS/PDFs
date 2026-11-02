import os

def analizar_consecutivos_carpeta(ruta_carpeta):
    consecutivos_encontrados = set()
    total_archivos = 0
    
    print(f'Leyendo archivos en: "{ruta_carpeta}"...\n')
    
    # Recorremos todos los elementos dentro de la carpeta especificada
    for archivo in os.listdir(ruta_carpeta):
        # Filtramos únicamente los archivos que terminen en .pdf (sin importar mayúsculas/minúsculas)
        if archivo.lower().endswith('.pdf'):
            total_archivos += 1  # Contamos TODOS los PDFs que hay en la carpeta
            
            # Quitamos la extensión .pdf para quedarnos solo con el nombre
            nombre_sin_ext = archivo[:-4]
            
            # REGLA ESTRICTA: Debe medir exactamente 24 caracteres Y ser puramente numérico
            if len(nombre_sin_ext) == 24 and nombre_sin_ext.isdigit():
                # Cortamos por posiciones exactas para el consecutivo (del 14 al 20)
                consecutivo_str = nombre_sin_ext[14:20]
                consecutivo_num = int(consecutivo_str)
                consecutivos_encontrados.add(consecutivo_num)
            else:
                # Si tiene letras, otros caracteres, o más/menos de 24 dígitos, se avisa para revisión
                print(f"AVISO: El archivo '{archivo}' no cumple con el formato numérico estricto de 24 dígitos -> ¡REVÍSALO!python")

    # Validamos si encontramos al menos un consecutivo válido
    if not consecutivos_encontrados:
        print("\nNo se encontraron consecutivos válidos de 24 dígitos puros en los PDFs.")
        return

    # Determinamos el número menor y mayor de la lista válida encontrada
    min_val = min(consecutivos_encontrados)
    max_val = max(consecutivos_encontrados)
    
    # Creamos un conjunto con el rango completo desde el menor hasta el mayor
    rango_completo = set(range(min_val, max_val + 1))
    
    # Restamos el rango completo menos los que sí tenemos para hallar los huecos (faltantes)
    faltantes = sorted(list(rango_completo - consecutivos_encontrados))
    
    # Imprimimos el reporte final con los resultados
    print("=" * 45)
    print("           REPORTE DE AUDITORIA PDFS           ")
    print("=" * 45)
    print(f"Total de PDFs en la carpeta       : {total_archivos}")
    print(f"Consecutivo menor valido          : {min_val:06d}")
    print(f"Consecutivo mayor valido          : {max_val:06d}")
    
    # Si hay números faltantes, los listamos formateados a 6 dígitos
    if faltantes:
        print(f"\nFALTAN {len(faltantes)} ARCHIVOS EN EL CONSECUTIVO:")
        for f in faltantes:
            print(f"   - Falta el consecutivo: {f:06d}")
    else:
        print("\nExcelente! La secuencia de numeros validos esta completa, no falta ningun numero en el rango.")

# Punto de entrada principal del script
if __name__ == "__main__":
    # El punto "." indica que buscará en la misma carpeta donde ejecutes este script o el .exe
    analizar_consecutivos_carpeta(".")
    
    # Evita que la ventana del .exe se cierre automáticamente al terminar
    input("\nPresiona Enter para salir...")