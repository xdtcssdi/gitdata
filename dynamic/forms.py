from django import forms

from dynamic.models import FileExcel, User


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = FileExcel
        fields = ['pname', 'describle', 'excel', 'user']
        exclude = ['user']
        labels = {
            'pname': '项目名',
            'describle': '邮箱',
            'user': '上传人'
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username': '用户名',
            'password': '密码'
        }

