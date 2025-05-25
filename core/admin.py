from django.contrib import admin
from core.models import Repository, Commit

# Register your models here.


@admin.register(Repository)
class RepositoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Commit)
class CommitAdmin(admin.ModelAdmin):
    pass
