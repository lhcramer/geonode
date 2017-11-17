# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2016 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

from django.contrib import admin

from geonode.base.admin import MediaTranslationAdmin, ResourceBaseAdminForm
from geonode.base.admin import metadata_batch_edit
from geonode.layers.models import Layer, Attribute, Style
from geonode.layers.models import LayerFile, UploadSession
from geonode.tasks.update import fix_layer_thumbnail


def fix_thumbnail(modeladmin, request, queryset):
    for layer in queryset:
            fix_layer_thumbnail.delay(object_id=layer.id)        
fix_thumbnail.short_description = "Fix Thumbnails"


def fix_thumbnail(modeladmin, request, queryset):
    for layer in queryset:
            fix_layer_thumbnail.delay(object_id=layer.id)        
fix_thumbnail.short_description = "Fix Thumbnails"


class AttributeInline(admin.TabularInline):
    model = Attribute


class LayerAdminForm(ResourceBaseAdminForm):

    class Meta:
        model = Layer
        fields = '__all__'


class LayerAdmin(MediaTranslationAdmin):
    list_display = (
        'id',
        'alternate',
        'service_type',
        'title',
        'date',
        'category',
<<<<<<< HEAD
        'is_published')
    list_display_links = ('id',)
    list_editable = ('title', 'category', 'is_published')
    list_filter = ('owner', 'category',
                   'restriction_code_type__identifier', 'date', 'date_type')
    search_fields = ('typename', 'title', 'abstract', 'purpose',)
=======
        'group',
        'is_approved',
        'is_published',
        'metadata_completeness')
    list_display_links = ('id',)
    list_editable = ('title', 'category', 'group', 'is_approved', 'is_published')
    list_filter = ('storeType', 'owner', 'category', 'group',
                   'restriction_code_type__identifier', 'date', 'date_type',
                   'is_approved', 'is_published')
    search_fields = ('alternate', 'title', 'abstract', 'purpose',
                     'is_approved', 'is_published',)
>>>>>>> e7605f5980062789a1dfe0321b74882a9af32ed6
    filter_horizontal = ('contacts',)
    date_hierarchy = 'date'
    readonly_fields = ('uuid', 'alternate', 'workspace')
    inlines = [AttributeInline]
    form = LayerAdminForm
<<<<<<< HEAD
    actions = [fix_thumbnail]
=======
    actions = [metadata_batch_edit]
>>>>>>> e7605f5980062789a1dfe0321b74882a9af32ed6


class AttributeAdmin(admin.ModelAdmin):
    model = Attribute
    list_display_links = ('id',)
    list_display = (
        'id',
        'layer',
        'attribute',
        'description',
        'attribute_label',
        'attribute_type',
        'display_order')
    list_filter = ('layer', 'attribute_type')
    search_fields = ('attribute', 'attribute_label',)


class StyleAdmin(admin.ModelAdmin):
    model = Style
    list_display_links = ('sld_title',)
    list_display = ('id', 'name', 'sld_title', 'workspace', 'sld_url')
    list_filter = ('workspace',)
    search_fields = ('name', 'workspace',)


class LayerFileInline(admin.TabularInline):
    model = LayerFile


class UploadSessionAdmin(admin.ModelAdmin):
    model = UploadSession
    list_display = ('date', 'user', 'processed')
    inlines = [LayerFileInline]


admin.site.register(Layer, LayerAdmin)
admin.site.register(Attribute, AttributeAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(UploadSession, UploadSessionAdmin)
