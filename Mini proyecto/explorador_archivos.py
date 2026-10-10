class ExploradorRecursivo:

    def imprimir_arbol(self, sistema: dict, nivel: int = 0) -> None:
        """Muestra la indentacion del directorio y carpetas."""
        for nombre, contenido in sistema.items():
            print("    " * nivel + f"- {nombre}")

            if isinstance(contenido, dict):
                self.imprimir_arbol(contenido, nivel + 1)

    def buscar_archivo(
        self, sistema: dict, nombre_buscado: str, ruta_actual: str = ""
    ) -> str | None:
        """Busca a qué ruta pertenece un archivo específico de forma minuciosa."""
        for nombre, contenido in sistema.items():
            ruta = f"{ruta_actual}/{nombre}"

            if nombre == nombre_buscado and not isinstance(contenido, dict):
                return ruta

            if isinstance(contenido, dict):
                resultado = self.buscar_archivo(
                    contenido, nombre_buscado, ruta
                )
                if resultado:
                    return resultado

        return None

    def contar_archivos(self, sistema: dict) -> int:
        """Retorna la cantidad total de archivos (las carpetas no cuentan)."""
        total = 0
        for contenido in sistema.values():
            if isinstance(contenido, dict):
                total += self.contar_archivos(contenido)
            else:
                total += 1
        return total

"""Bloque de pruebas de impresión"""
sistema_archivos = {
    "Documentos": {
        "Clases de bases de datos.txt": "10kb",
        "fotos": {"MYGG.png": "2mb", "Cesar.jpg": "1mb"},
    },
    "favoritos.": "1gb",
}

explorador = ExploradorRecursivo()

print("---- Árbol de Directorios ----")
explorador.imprimir_arbol(sistema_archivos)

print("\n--- BÚSQUEDA DE ARCHIVO ---")
print("Ruta encontrada:", explorador.buscar_archivo(sistema_archivos, "perro.jpg"))

print("\n--- TOTAL DE ARCHIVOS ---")
print("Cantidad total:", explorador.contar_archivos(sistema_archivos))