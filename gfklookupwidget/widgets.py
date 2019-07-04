import json

from random import randint

try:
    from django.urls import reverse, NoReverseMatch
except ImportError:
    from django.core.urlresolvers import reverse, NoReverseMatch
import django.contrib.admin.templatetags.admin_static
import django.forms


class GfkLookupWidget(django.forms.Widget):

    def __init__(self, *args, **kwargs):
   
        self.ct_field_name = kwargs.pop('content_type_field_name')
        self.parent_field = kwargs.pop('parent_field')

        super(GfkLookupWidget, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None):
        model = self.parent_field.model
        ct_field = self.parent_field.model._meta.get_field(self.ct_field_name)
        choices = ct_field.get_choices()

     
        urls = {}
        for type_id, type_name in choices:
            if not type_id:
                continue

            content_type = django.contrib.contenttypes.models\
                .ContentType.objects.get(id=type_id)


            try:
                url = reverse(
                    'admin:{app}_{model}_changelist'.format(
                        app=content_type.app_label,
                        model=content_type.model))
            except NoReverseMatch:
 
                continue

            urls[type_name] = url

        if value is None:
            value = ""


        return django.utils.safestring.mark_safe("""
            <input class="vForeignKeyRawIdAdminField" id="id_{name}" name="{name}" value="{value}" type="text" />
            <a id="lookup_id_{name}" class="related-lookup gfklookup" onclick="return gfklookupwidget_{uniq}_click(django.jQuery, this, event);"></a>
            <script type="text/javascript">
                if (typeof(gfklookupwidget_{uniq}_click) == 'undefined') {{
                    function gfklookupwidget_{uniq}_click($, element, event) {{
                        if (event) {{
                            event.preventDefault();
                        }}

                        var urls = {urls};
                        var $this = $(element);
                        var ct_field_name = "{ct_field_name}";

                        var prefix = "";
                        var id = $this.attr('id');
                        if (id.indexOf('-')) {{
                            ct_field_name = id.substring(0, id.lastIndexOf('-') + 1).replace('lookup_id_', '') + ct_field_name;
                        }}

                        var selected = $('select[name="'+ct_field_name+'"]').find('option:selected');
                        var content_type_id = selected.val();
                        var content_type = selected.text();

                        if (!content_type) {{
                            alert('No content type found for GenericForeignKey lookup.');
                            return false;
                        }}

                        if (!content_type_id) {{
                            alert('You must select: '+ct_field_name+'.');
                            return false;
                        }}

                        $this.attr('href', urls[content_type]);

                        return showRelatedObjectLookupPopup(element);
                    }}
                }}
            </script>
        """.format(
            uniq='{:X}'.format(randint(1, 1000000)),
            name=name,
            value=value,
            urls=json.dumps(urls),
            ct_field_name=self.ct_field_name,
        ))
