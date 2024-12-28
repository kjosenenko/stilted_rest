from django.contrib import admin
from .models import Member
from bands.managers import BandManager
from .managers import MemberManager

class MemberAdmin(admin.ModelAdmin):
  
  def get_queryset(self, request):
    if request.user.is_superuser:
      return Member.objects.all()
    else: 
      band = BandManager.find_by_name("Stilted")
      return MemberManager.band_members(band)

admin.site.register(Member, MemberAdmin)
