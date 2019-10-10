from django.contrib import admin
from .models import Questionnaire, UserProfile, StockRecommendation, Sector, Industry, Stock

# Register your models here.

admin.site.register(Questionnaire)
admin.site.register(UserProfile)
admin.site.register(StockRecommendation)
admin.site.register(Sector)
admin.site.register(Industry)
admin.site.register(Stock)





