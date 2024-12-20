from django.forms import ModelForm
from djang_app.models import school



class schoolForm(ModelForm):
    
    class Meta:
        model = school
        fields = "__all__"
