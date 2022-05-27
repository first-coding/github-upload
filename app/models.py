from django.db import models
'''
智能病虫害识别系统 数据模型
'''
# 管理员表
class  Admin(models.Model):
    id= models.IntegerField(primary_key = True)
    name=models.CharField("用户名",default="",max_length=10)
    pwd=models.CharField("密码",default="",max_length=100)
    flag=models.CharField("标记",default="",max_length=10)  # 1 超级管理员，2 普通管理员
    class Meta:
        db_table="admin"


# 普通用户表
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name=models.CharField("用户名",default="",max_length=10)
    head = models.CharField("头像", default="", max_length=100)
    wxid = models.CharField("微信标识码", default="", max_length=100)
    ttscore = models.IntegerField("总积分", default=0)
    snscore = models.IntegerField("7天总积分", default=0)
    class Meta:
        db_table = "user"

# 日常任务表
class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    uid=models.IntegerField("用户id",null=True)
    rq=models.DateField("日期",null=True)
    qnd= models.IntegerField("签到分", default=0)
    stp= models.IntegerField("上传图片分", default=0)
    myd= models.IntegerField("每日一答分", default=0)
    fxf= models.IntegerField("分享分", default=0)

    class Meta:
        db_table = "task"

# 采集数据表
class Acdata(models.Model):
    id = models.IntegerField(primary_key=True)
    uid = models.IntegerField("用户id", null=True)
    addr=models.CharField("地点",default="",max_length=100)
    type = models.CharField("类别", default="", max_length=100)
    name = models.CharField("名称", default="", max_length=100)
    content = models.CharField("其他内容", default="", max_length=200)
    rq = models.DateField("日期", null=True)

    class Meta:
        db_table = "acdata"

# 采集数据表图片
class AcdataMd(models.Model):
    id = models.IntegerField(primary_key=True)
    aid = models.IntegerField("采集数据表id", null=True)
    mdpath = models.CharField("图片路径", default="", max_length=200)
    class Meta:
        db_table = "acdataMd"

# 关注问题
class Concerns(models.Model):
    id = models.IntegerField(primary_key=True)
    uid = models.IntegerField("用户id", null=True)
    qid = models.IntegerField("问答表id", null=True)
    class Meta:
        db_table = "concerns"

# 我的点赞
class Myfav(models.Model):
    id = models.IntegerField(primary_key=True)
    uid = models.IntegerField("用户id", null=True)
    qid = models.IntegerField("问答表id", null=True)
    class Meta:
        db_table = "myfav"



# 手册表
class Guide(models.Model):
    id = models.IntegerField(primary_key=True)
    bm = models.CharField("病虫药害编码", default="", max_length=100)
    name = models.CharField("病虫药害名称", default="", max_length=100)
    info = models.TextField("简介", default="")
    sgt = models.TextField("防治建议", default="")
    type = models.CharField("类别", default="", max_length=100)
    num = models.IntegerField("搜索次数", default=0)
    class Meta:
        db_table = "guide"



# 手册表图片
class GuideMd(models.Model):
    id = models.IntegerField(primary_key=True)
    gid = models.IntegerField("手册表id", null=True)
    mdpath = models.CharField("图片路径", default="", max_length=200)
    class Meta:
        db_table = "guideMd"


# 问答表
class Question(models.Model):
    id = models.IntegerField(primary_key=True)
    uid = models.IntegerField("用户id", null=True)
    qname = models.CharField("提问名称", default="", max_length=100)
    qcontent = models.CharField("问题", default="", max_length=500)
    qk = models.CharField("用肥用药情况", default="", max_length=500)
    mj = models.CharField("发生面积", default="", max_length=100)
    weather = models.CharField("天气情况", default="", max_length=100)
    rq = models.DateField("日期", null=True)
    addr = models.CharField("定位地址", default="", max_length=200)
    dznum = models.IntegerField("点赞数", default=0)
    scnum = models.IntegerField("浏览数", default=0)


    class Meta:
        db_table = "question"



# 问答表图片
class QuestionMd(models.Model):
    id = models.IntegerField(primary_key=True)
    qid = models.IntegerField("问答表id", null=True)
    mdpath = models.CharField("图片路径", default="", max_length=200)
    class Meta:
        db_table = "questionMd"


# 问答识别结果
class QAIR(models.Model):
    id = models.IntegerField(primary_key=True)
    qid = models.IntegerField("问答表id", null=True)
    r1 = models.CharField("结果1", default="", max_length=100)
    rd1 = models.CharField("结果1相似度", default="", max_length=100)
    r2 = models.CharField("结果2", default="", max_length=100)
    rd2 = models.CharField("结果2相似度", default="", max_length=100)
    r3 = models.CharField("结果3", default="", max_length=100)
    rd3 = models.CharField("结果3相似度", default="", max_length=100)
    class Meta:
        db_table = "qair"



# 回复表
class Reply(models.Model):
    id = models.IntegerField(primary_key=True)
    qid = models.IntegerField("问答表id", null=True)
    content = models.CharField("回复内容", default="", max_length=500)
    sj = models.DateTimeField("时间", null=True)
    dznum = models.IntegerField("点赞数", default=0)
    rid = models.IntegerField("回复的id", null=True)
    class Meta:
        db_table = "reply"
