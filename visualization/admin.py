from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Category_sector, Category_industry, Stock, Stock_daily, Stock_intraday_1min

class StockAdmin(ImportExportModelAdmin):
    list_display   = ('exchange', 'symbol', 'company', 'date', 'ipoYear','category_sector','category_industry')
    list_filter    = ('exchange','category_sector', 'ipoYear')
    date_hierarchy = 'date'
    ordering       = ('exchange','symbol', 'company')
    search_fields  = ('exchange','symbol', 'company')

class Category_sectorAdmin(ImportExportModelAdmin):
    list_display   = ('id', 'sector')

class Category_industryAdmin(ImportExportModelAdmin):
    list_display   = ('id', 'industry')

class Stock_dailyAdmin(ImportExportModelAdmin):
    list_display   = ('id', 'date', 'symbol', 'open', 'high', 'low', 'close', 'volume')
    list_filter    = ('symbol',)
    ordering       = ('date',)
    search_fields  = ('symbol',)

class Stock_intraday_1minAdmin(ImportExportModelAdmin):
    list_display   = ('id', 'date', 'symbol', 'open', 'high', 'low', 'close', 'volume')
    list_filter    = ('symbol',)
    ordering       = ('date',)
    search_fields  = ('symbol',)

admin.site.register(Category_sector, Category_sectorAdmin)
admin.site.register(Category_industry, Category_industryAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Stock_daily, Stock_dailyAdmin)
admin.site.register(Stock_intraday_1min, Stock_intraday_1minAdmin)
