from django.contrib import admin
from .models import Program, NomorPaket, Event, Paket



class NomorPaketInline(admin.TabularInline):
    model = NomorPaket
    extra = 0

class ProgramAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['nama_program']}),
    ]
    inlines = [NomorPaketInline]
    list_display = ('nama_program', 'event_count')
    search_fields = ['nama_program']

admin.site.register(Program, ProgramAdmin)



class PaketInline(admin.TabularInline):
    model = Paket
    extra = 0

class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['nama_event', 'program', 'link_panduan', 'aktif']}),
        ('Jadwal', {'fields': ['jadwal', 'waktu_buka', 'waktu_mulai', 'waktu_selesai']}),
    ]
    actions = ['activate_program', 'deactivate_program']
    inlines = [PaketInline]
    list_filter = ['aktif']
    list_display = ('nama_event', 'link_panduan', 'aktif', 'paket_count', 'status')
    search_fields = ['nama_event']

admin.site.register(Event, EventAdmin)



class PaketAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['nama_paket', 'nomor_paket', 'event', 'bundel_soal']}),
        ('Jadwal', {'fields': ['open_time', 'close_time']}),
    ]
    list_display = ('nama_paket', 'event', 'bundel_soal', 'open_time_format', 'close_time_format',)
    search_fields = ['nama_paket']

admin.site.register(Paket, PaketAdmin)
