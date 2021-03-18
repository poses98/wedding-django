from django.db import models
from django.urls import reverse
import uuid


class WebPassword(models.Model):
    password = models.CharField(
        max_length=50, help_text='Introduce la contraseña para el sitio web', verbose_name='Contraseña')
    is_required = models.BooleanField(
        default=False, help_text='¿Quieres que la web tenga contraseña?', verbose_name='Activada')

    class Meta:
        verbose_name = ("Contraseña")
        verbose_name_plural = ("Contraseña Global")

    def __str__(self):
        return "Contraseña"


class Confirmacion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                            help_text="ID única asociada a la confirmación")
    name = models.CharField(
        max_length=50, help_text='Introduce tu nombre', verbose_name='Nombre')
    surname = models.CharField(
        max_length=50, help_text='Introduce tu apellido', verbose_name='Apellido')

    bus_service = models.BooleanField(
        default=False, help_text='¿Necesitas autobús?', verbose_name='Autobús')
    bus = models.ForeignKey('Autobus', verbose_name="Lugar de autobús",
                            help_text="Responder sólo si se necesita autobús", blank=True, null=True, on_delete=models.RESTRICT)
    bus_place = models.CharField(max_length=50, help_text='Responder sólo si se necesita autobús y estás en el Valle del Baztan',
                                 verbose_name='¿En qué hotel te hospedarás?', blank=True, default="")

    song_name = models.CharField(max_length=50, help_text='¡Introduce una canción que quieres que suene durante la fiesta!',
                                 verbose_name='Canción y grupo', blank=True, null=True)
    food_restrictions = models.TextField(max_length=500, help_text='Especifica, en caso de tener acompañante, quién tiene la alergia/otro',
                                         verbose_name='Alergias alimenticias / Otros', blank=True, default='')

    class Meta:
        verbose_name = ("confirmación")
        verbose_name_plural = ("Confirmaciones")

    def __str__(self):
        return self.name


class Autobus(models.Model):
    name = models.CharField(
        max_length=50, help_text='Introduce nombre de sitio de partida', verbose_name='Lugar de partida')

    class Meta:
        verbose_name = "autobús"
        verbose_name_plural = "Autobuses"

    def __str__(self):
        return self.name


class SitiosInteres(models.Model):
    TIPO_SITIO = (
        ('h', 'Hotel'),
        ('r', 'Restaurante'),
        ('p', 'Peluqueria'),
        ('s', 'Lugar de interes')
    )
    site_type = models.CharField(
        max_length=1,
        choices=TIPO_SITIO,
        blank=False,
        default='',
        help_text='Escoge el tipo de sitio',
    )
    name = models.CharField(
        max_length=50, help_text='Introduce el nombre del sitio', verbose_name='Nombre', primary_key=True)
    phone = models.CharField(max_length=12, help_text='Introduce el número del sitio de interés (si tiene)',
                             verbose_name='Teléfono', blank=True, default='')
    web = models.URLField(help_text='Introduce el enlace a google maps',
                          verbose_name="Enlace a Google Maps", max_length=2000)
    picture = models.URLField(verbose_name='Foto del sitio', blank=True,
                              help_text="URL de la foto del sitio de interés", max_length=2000)

    class Meta:
        verbose_name = ("sitio de interés")
        verbose_name_plural = ("Sitios de interés")

    def __str__(self):
        return self.name


class Itinerario(models.Model):
    name = models.CharField(
        max_length=200, help_text="Introduce el nombre del evento (p.e Salida autobus Pamplona)", verbose_name="Nombre")
    description = models.TextField(
        max_length=1000, help_text="Introduce una descripción para el evento", verbose_name="Descripción del evento", blank=True)
    start_time = models.TimeField(
        verbose_name="Hora inicio", help_text="Introduce la hora de inicio")
    end_time = models.TimeField(
        verbose_name="Hora fin", help_text="Introduce la hora de finalización", blank=True, null=True)
    location_name = models.CharField(
        max_length=50, help_text='Introduce el nombre de la localización', verbose_name='Nombre localización', blank=True)
    location_url = models.URLField(help_text='Introduce el enlace a google maps',
                                   verbose_name="Enlace a Google Maps", max_length=2000, default="", blank=True)
    image = models.URLField(help_text='Introduce el enlace de la fotografía',
                            verbose_name="Enlace a la imagen", max_length=2000, default="")

    class Meta:
        verbose_name = ("evento")
        verbose_name_plural = ("Itinerario")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Itinerario_detail", kwargs={"pk": self.pk})


class InscripcionCampeonato(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                            help_text="ID única asociada al participante")
    name = models.CharField(
        max_length=20, verbose_name="Nombre", help_text="Introduce tu nombre")
    surname = models.CharField(
        max_length=50, verbose_name="Apellidos", help_text="Introduce tus apellidos")
    handicap = models.DecimalField(
        verbose_name="Handicap", help_text="Introduce tu handicap", decimal_places=2, max_digits=4)
    licencia = models.CharField(max_length=12, help_text='Introduce tu número de licencia',
                                verbose_name='Número de licencia', default='', null=True)
    wantToRent = models.BooleanField(default=False, help_text='¿Alquilarías palos?', verbose_name='Palos', blank=True)

    DIA = (
        ('m', 'Viernes por la mañana'),
        ('t', 'Viernes por la tarde'),
        ('i', 'Me da igual'),
    )

    day_pref = models.CharField(
        max_length=1,
        choices=DIA,
        blank=False,
        default='',
        help_text='¿Cuándo te viene mejor?',
        verbose_name='Hora'
    )

    class Meta:
        verbose_name = ('inscripción campeonato')
        verbose_name_plural = ('Inscripciones campeonato')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("InscripcionCampeonato_detail", kwargs={"pk": self.pk})


class CampeonatoGolf(models.Model):
    name = models.CharField(
        max_length=50, verbose_name="Nombre campeonato", help_text="p.e Campeonato de Golf")
    description = models.TextField(max_length=150, verbose_name="Descripcion",
                                   help_text="Esta es la descripcion que aparecerá debajo del título")
    lugar = models.CharField(
        max_length=50, verbose_name="Lugar", help_text="Lugar donde se celebrará")
    location_url = models.URLField(help_text='Introduce el enlace a google maps',
                                   verbose_name="Enlace a Google Maps", max_length=2000, default="", blank=True)
    fecha = models.DateTimeField(
        verbose_name="Fecha del campeonato", help_text="Introduce la fecha y hora del campeonato")

    class Meta:
        verbose_name = ("Info Campeonato")
        verbose_name_plural = ("Campeonato de Golf")

    def __str__(self):
        return self.name


class BestWishes(models.Model):
    name = models.CharField(
        max_length=50, help_text='Introduce tu nombre', verbose_name='Nombre')
    surname = models.CharField(
        max_length=50, help_text='Introduce tu apellido', verbose_name='Apellido')
    message = models.TextField(max_length=500, help_text='¡Introduce un mensaje para los novios!',
                               verbose_name='Mensaje', blank=True, default='')
    accepted = models.BooleanField(
        default=False, help_text='Si es seleccionado el mensaje se mostrara en el apartado de la web.', verbose_name='Visible', blank=True)

    class Meta:
        verbose_name = ('Mensaje para los novios')
        verbose_name_plural = ('Mensajes para los novios')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("BestWishes_detail", kwargs={"pk": self.pk})
# MODIFICABLES DE WEB


class LugarDeLaBoda(models.Model):
    name = models.CharField(max_length=20, verbose_name="Lugar de la boda",
                            help_text="Este es el texto que aparecerá en la página principal")
    mensaje = models.CharField(max_length=100, verbose_name="Mensaje",
                               help_text="Este es el texto que aparecerá en la página principal p.e.\"¡Estás invitado a la boda!\" ")

    class Meta:
        verbose_name = ("Lugar de la boda")
        verbose_name_plural = ("_Lugar de la boda")

    def __str__(self):
        return self.name


class ItinerarioHeader(models.Model):
    name = models.CharField(max_length=20, verbose_name="Nombre header",
                            help_text="Este es el texto que aparecerá en la página principal")
    description = models.CharField(max_length=150, verbose_name="Descripcion header",
                                   help_text="Esta es la descripcion que aparecerá debajo del título en la página principal")

    class Meta:
        verbose_name = ("Titulo Itinerario")
        verbose_name_plural = ("_Titulo Itinerario")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ItinerarioHeader_detail", kwargs={"pk": self.pk})


class NombresPareja(models.Model):
    novio = models.CharField(
        max_length=50, verbose_name="Nombre novio", help_text="Introduce el nombre del novio")
    novia = models.CharField(max_length=50, verbose_name="Nombre novia",
                             help_text="Introduce el nombre de la novia")
    descripcion_novio = models.TextField(max_length=400, verbose_name="Descripción novio",
                                         help_text="Introduce descripción del novio (déjalo en blanco si no quieres que aparezca nada)", blank=True, default="")
    descripcion_novia = models.TextField(max_length=400, verbose_name="Descripción novia",
                                         help_text="Introduce descripción de la novia (déjalo en blanco si no quieres que aparezca nada)", blank=True, default="")

    class Meta:
        verbose_name = ("Nombre")
        verbose_name_plural = ("_Nombres pareja")

    def __str__(self):
        return self.novio

    def get_absolute_url(self):
        return reverse("NombresPareja_detail", kwargs={"pk": self.pk})


class FechaDeBoda(models.Model):
    fecha = models.DateTimeField(
        verbose_name="Fecha de la boda", help_text="Introduce la fecha y hora de la boda")

    class Meta:
        verbose_name = ("Fecha de la boda")
        verbose_name_plural = ("_Fecha de la boda")

    def get_year(self):
        return self.fecha.year

    def get_month(self):
        return self.fecha.month

    def get_day(self):
        return self.fecha.day
