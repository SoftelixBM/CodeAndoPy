from django.db import models
from django.contrib.auth.models import User

class Persona(models.Model):
    usuario = models.ForeignKey(User)
    cedula = models.CharField(max_length=8, unique=True)
    fecha_nacimiento = models.DateField()

    def __unicode__(self):
        return "%s"%(self.usuario.first_name)

    def __str__(self):
        return "%s"%(self.usuario.first_name)

    def get_nombre_completo(self):
        return "%s %s"%(self.usuario.first_name, self.usuario.last_name)

    #def get_edad(self):
    #    return "%d"

    class Meta():
        db_table = "personas"

#tabla Asignatura
class Asignatura(models.Model):
    nombre = models.CharField(max_length=15)
    profesor = models.ForeignKey()

#tabla Aulas
class Aula(models.Model):
    descripcion = models.CharField(max_length=50, unique=True, blank=False)
    limite = models.IntegerField()
    asignatura = models.ForeignKey(Asignatura)

    def get_limite(self):
        return "%s"%(self.limite)

class Clase(models.Model):
    clase = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=50)
    profesor = models.ForeignKey()

class Comentario(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    comentario = models.CharField(max_length=300)
    usuario = models.ManyToOneRel()

    def obtener_comentarios(self):
        return "%s %s %s"%(self.usuario, self.comentario, self.fecha)

class Permiso(models.Model, Usuario):
    descripcion = models.CharField(max_length=35)
    usuario = models.ForeignKey()

#tabla Profesor
class Profesor(models.Model):

    especialidad = models.CharField(max_length=30)
    asignatura = models.ForeignKey(Asignatura)
    usuario = models.OneToOneField(Usuario, Foreingkey=True)
    persona = models.OneToOneField(Persona, Fpreingkey=True)

    def obtener_nombre_completo(self):
        return "%s %s"%(self.nombre, self.apellido)