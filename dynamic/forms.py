from django import forms

from dynamic.models import FileExcel


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = FileExcel
        fields = ['pname', 'describle', 'excel']
        labels = {
            'pname': '项目名',
            'describle': '邮箱'
        }
