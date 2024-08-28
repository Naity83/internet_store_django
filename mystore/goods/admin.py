from django.contrib import admin
from .models import Categories, Products

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = ["name"]

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    
    list_display = [
        "name",
        "category",
        "quantity",
        "price",
        "discount",
        "get_sell_price",  # Используем метод для отображения цены со скидкой
    ]
    
    list_editable = ["price", "discount", "quantity"]
    
    search_fields = [
        "name",
        "description",
        "rootstock",
        "ripening_period",
        "pollinators",
        "frost_resistance",
        "disease_resistance",
        "transportability"
    ]
    
    list_filter = [
        "category",
        "discount",
        "quantity",
        "rootstock",
        "ripening_period",
        "pollinators",
        "frost_resistance",
        "disease_resistance",
        "transportability"
    ]
    
    fieldsets = (
        (None, {
            'fields': ("name", "slug", "category", "description", "image")
        }),
        ("Ціноутворення", {
            'fields': ("price", "discount")
        }),
        ("Інвентаризація", {
            'fields': ("quantity",)
        }),
        ("Характеристики", {
            'fields': (
                "rootstock",
                "ripening_period",
                "fruit_weight",
                "pollinators",
                "frost_resistance",
                "disease_resistance",
                "transportability",
            )
        }),
    )
    
    ordering = ["name", "category"]

    def get_sell_price(self, obj):
        return obj.sell_price()  # Метод для вычисления цены со скидкой
    get_sell_price.short_description = 'Ціна зі знижкою'  # Название колонки в админке
