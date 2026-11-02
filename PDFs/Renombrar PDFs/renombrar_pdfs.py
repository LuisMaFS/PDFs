import os

def renombrar_archivos_escaneo(ruta_carpeta):
    print(f'Leyendo archivos en: "{ruta_carpeta}"...\n')
    
    archivos = os.listdir(ruta_carpeta)
    renombrados_exitosos = 0
    consecutivos_procesados = []
    
    for archivo in archivos:
        if archivo.lower().endswith('.pdf'):
            # Verificamos si el archivo tiene el guion bajo del escáner
            if "_" in archivo:
                partes = archivo.rsplit("_", 1)
                base_original = partes[0]
                sufijo_con_ext = partes[1] # Ej: "001.pdf"
                
                # Separamos el contador del escáner de su extensión
                if "." in sufijo_con_ext:
                    contador_scanner_str, ext = sufijo_con_ext.rsplit(".", 1)
                    
                    # VALIDACION ESTRICTA:
                    # 1. La base debe tener exactamente 24 caracteres numéricos.
                    # 2. El contador del escáner debe ser puramente numérico.
                    # 3. El contador debe tener como MÁXIMO 6 dígitos (longitud entre 1 y 6).
                    if (len(base_original) == 24 and base_original.isdigit() and 
                        contador_scanner_str.isdigit() and 1 <= len(contador_scanner_str) <= 6):
                        
                        # Convertimos el contador del escáner a entero
                        contador_num = int(contador_scanner_str)
                        consecutivos_procesados.append(contador_num)
                        
                        contador_6d = f"{contador_num:06d}"
                        
                        # Reemplazamos los 6 dígitos del consecutivo (posiciones 14 a 20) en la base original
                        nuevo_nombre_base = base_original[:14] + contador_6d + base_original[20:]
                        nuevo_nombre_archivo = nuevo_nombre_base + "." + ext
                        
                        # Rutas completas para el renombrado
                        ruta_antigua = os.path.join(ruta_carpeta, archivo)
                        ruta_nueva = os.path.join(ruta_carpeta, nuevo_nombre_archivo)
                        
                        # Ejecutamos el cambio de nombre
                        os.rename(ruta_antigua, ruta_nueva)
                        print(f"Renombrado: {archivo} -> {nuevo_nombre_archivo}")
                        renombrados_exitosos += 1
                    else:
                        print(f"AVISO: El archivo '{archivo}' fue omitido (el sufijo excede los 6 digitos o la base no es valida).")
            else:
                # Los archivos sin guion bajo se ignoran y no se tocan
                print(f"AVISO: El archivo '{archivo}' no tiene guion bajo, fue omitido.")

    # Imprimimos el reporte final con el rango de consecutivos
    print("=" * 45)
    print("           REPORTE DE RENOMBRADO           ")
    print("=" * 45)
    print(f"Total de archivos renombrados: {renombrados_exitosos}")
    
    if consecutivos_procesados:
        min_val = min(consecutivos_procesados)
        max_val = max(consecutivos_procesados)
        print(f"Consecutivo menor procesado  : {min_val:06d}")
        print(f"Consecutivo mayor procesado  : {max_val:06d}")
    else:
        print("No se procesaron consecutivos validos.")

if __name__ == "__main__":
    # Busca y procesa los archivos en la misma carpeta donde se ejecute el script o el .exe
    renombrar_archivos_escaneo(".")
    input("\nPresiona Enter para salir...")