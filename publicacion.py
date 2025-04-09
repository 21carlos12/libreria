class Publicacion:
    def __init__(self, titulo, autor, anio_publicacion):
        self._titulo = titulo
        self._autor = autor
        self._anio_publicacion = anio_publicacion

    def __str__(self):
        return f"{self._titulo} por {self._autor}, publicado en {self._anio_publicacion}"

    @property
    def titulo(self):
        return self._titulo

    @property
    def autor(self):
        return self._autor

    @property
    def anio_publicacion(self):
        return self._anio_publicacion