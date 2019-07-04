import django.db.models
import django.forms
import django.forms.fields

import gfklookupwidget.widgets


class GfkLookupField(django.db.models.PositiveIntegerField):

    def __init__(self, content_type_field_name=None, *args, **kwargs):

        self.content_type_field_name = content_type_field_name
        super(GfkLookupField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': GfkLookupFormField,
            'content_type_field_name': self.content_type_field_name,
            'parent_field': self,
        }
        defaults.update(kwargs)
        return super(GfkLookupField, self).formfield(**defaults)


class GfkLookupFormField(django.forms.IntegerField):

    def __init__(self, content_type_field_name, parent_field, *args, **kwargs):
        kwargs['widget'] = gfklookupwidget.widgets.GfkLookupWidget(
            # Pass-through for the GfkLookupField.
            content_type_field_name=content_type_field_name,
            parent_field=parent_field,
        )
        return super(GfkLookupFormField, self).__init__(*args, **kwargs)


try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^gfklookupwidget\.fields\.GfkLookupField"])
except:
    pass
