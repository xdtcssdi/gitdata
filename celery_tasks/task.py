from celery.task import task
from django.conf import settings
from django.core.mail import send_mail


# 用装饰器装饰发送邮件的函数
@task
def send_msg(email, randomCode):
    # send_mail的第一个参数为：主标题；
    # 第二个参数为：文本内容；
    # 第三个参数为发送源邮箱；
    # 第四个参数为一个列表或元组表示要发送给哪个邮箱可以是多个；
    # 第五个参数为：可以将html标签翻译如a标签中如果有href属性他的内容就可以被点击。
    # 注意：第二个参数和第五个参数不能同时存在，如果同时存在第五个参数会覆盖掉第二个参数中的内容。
    send_mail(
        "验证您的用户信息", '您已经注册账户成功，现在需要您访问如下链接：http://localhost:8000/check?code=' + randomCode,
        settings.EMAIL_HOST_USER, [email, ],
        html_message='您已经注册账户成功，现在需要您访问如下链接：http://localhost:8000/check?code=' + randomCode,
    )
