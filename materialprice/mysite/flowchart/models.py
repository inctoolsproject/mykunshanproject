from django.db import models


# Create your models here.
class Flowchart(models.Model):
    # num = models.IntegerField(default=0,verbose_name="第幾式")
    part_name = models.CharField(max_length=32,verbose_name="品名")
    mold_num = models.CharField(max_length=32,verbose_name="模號")
    cust_name = models.CharField(max_length=32,verbose_name="客戶名稱")
    # remarks = models.CharField(max_length=200)
    def __str__(self):
        return self.part_name
    class Meta:
        verbose_name = "生產工藝流程卡"
        verbose_name_plural = "生產工藝流程卡"

#
class Flowchartprocess(models.Model):
    # num = models.IntegerField(default=0,verbose_name="第幾式")
    process_name = models.CharField(max_length=32,verbose_name="工序")
    flowchart = models.ForeignKey(Flowchart, on_delete=models.CASCADE)
    process_desc = models.CharField(max_length=128,verbose_name="過程描述")
    # remarks = models.CharField(max_length=200)
    def __str__(self):
        return self.process_name
    class Meta:
        verbose_name = "流程"
        verbose_name_plural = "流程"
