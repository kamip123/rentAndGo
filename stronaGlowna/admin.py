from django.contrib import admin
from .models import Komentarz, OfertyStronaGlownaOsobowe, OfertyStronaGlownaWieksze
# Register your models here.


admin.site.register(Komentarz)
admin.site.register(OfertyStronaGlownaOsobowe)
admin.site.register(OfertyStronaGlownaWieksze)
