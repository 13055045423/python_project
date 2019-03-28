from django.db import models

# Create your models here.
class Banzoufenlei(models.Model):
    banzouurl = models.CharField(max_length=255, blank=True, null=True)
    shangchuanshijian = models.CharField(max_length=255, blank=True, null=True)
    geshi = models.CharField(max_length=255, blank=True, null=True)
    shangchuanyonghu = models.CharField(max_length=255, blank=True, null=True)
    yuanchang = models.CharField(max_length=255, blank=True, null=True)
    banzouming = models.CharField(max_length=255, blank=True, null=True)
    zhonglei = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banzoufenlei'


class Gedancontentinfo(models.Model):
    danqubofangliang = models.CharField(max_length=255, blank=True, null=True)
    gequzuozhe = models.CharField(max_length=255, blank=True, null=True)
    gequurl = models.CharField(max_length=255, blank=True, null=True)
    gequmingcheng = models.CharField(max_length=255, blank=True, null=True)
    gequxuhao = models.CharField(max_length=255, blank=True, null=True)
    gequshuliang = models.CharField(max_length=255, blank=True, null=True)
    jianjie = models.CharField(max_length=255, blank=True, null=True)
    biaoqian = models.CharField(max_length=255, blank=True, null=True)
    shoucang = models.CharField(max_length=255, blank=True, null=True)
    bofangcishu = models.CharField(max_length=255, blank=True, null=True)
    chuangjianren = models.CharField(max_length=255, blank=True, null=True)
    chuangjianshijian = models.CharField(max_length=255, blank=True, null=True)
    gedan_title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gedancontentinfo'


class Gedaninfo(models.Model):
    gedanurl = models.CharField(max_length=255, blank=True, null=True)
    zuozhe = models.CharField(max_length=255, blank=True, null=True)
    gedanname = models.CharField(max_length=255, blank=True, null=True)
    bofangliang = models.CharField(max_length=255, blank=True, null=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gedaninfo'


class Yuanchuangcontent(models.Model):
    dianzanshu = models.CharField(max_length=255, blank=True, null=True)
    shoucangshu = models.CharField(max_length=255, blank=True, null=True)
    xiazaishu = models.CharField(max_length=255, blank=True, null=True)
    shangchuanshijian = models.CharField(max_length=255, blank=True, null=True)
    xiazaishezhi = models.CharField(max_length=255, blank=True, null=True)
    qufeng = models.CharField(max_length=255, blank=True, null=True)
    yuzhong = models.CharField(max_length=255, blank=True, null=True)
    fenlei = models.CharField(max_length=255, blank=True, null=True)
    hunsuo = models.CharField(max_length=255, blank=True, null=True)
    bianqu = models.CharField(max_length=255, blank=True, null=True)
    zuoqu = models.CharField(max_length=255, blank=True, null=True)
    zuoci = models.CharField(max_length=255, blank=True, null=True)
    yanchang = models.CharField(max_length=255, blank=True, null=True)
    mingzi = models.CharField(max_length=255, blank=True, null=True)
    zhonglei = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yuanchuangcontent'


class Yunachuangfenlei(models.Model):
    mokuai = models.CharField(max_length=255, blank=True, null=True)
    fenleiurl = models.CharField(max_length=255, blank=True, null=True)
    fenleiname = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yunachuangfenlei'