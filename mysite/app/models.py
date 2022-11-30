from django.db import models


class Top(models.Model):
    title = models.CharField(verbose_name='題名', max_length=200)

    def __str__(self):
        return self.title


class ListOf(models.Model):
    top = models.ForeignKey(Top, on_delete=models.CASCADE)
    element = models.CharField(verbose_name='項目', max_length=200)

    def __str__(self):
        return self.element


class NoticeDetail(models.Model):
    list = models.ForeignKey(ListOf, on_delete=models.CASCADE)
    order_day = models.DateTimeField(verbose_name="順番用", auto_now_add=True)
    day = models.DateField(verbose_name="登録日時", auto_now_add=True)
    notice = models.CharField(verbose_name='お知らせ', max_length=200)
    image = models.ImageField(verbose_name='写真（画像）',upload_to='images/')

    def __str__(self):
        return self.notice



class ReplyDetail(models.Model):
    Top = models.ForeignKey(Top, on_delete=models.CASCADE)
    order_day = models.DateTimeField(verbose_name="順番用", auto_now_add=True)
    day = models.DateField(verbose_name="登録日時", auto_now_add=True)
    reply_title = models.CharField(verbose_name="返信内容", max_length=200)
    reply = models.DateField(default=False, verbose_name="返信用封筒はいつまでですか")
    image = models.ImageField(verbose_name='写真（画像）', upload_to='images/')

    def __str__(self):
        return self.reply_title
