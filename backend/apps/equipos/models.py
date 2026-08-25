from django.db import models


class Equipo(models.Model):
    id_equipo = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = "equipo"

    def __str__(self):
        return str(self.id_equipo)