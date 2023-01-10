from django.db import models
from django.core.exceptions import ValidationError

from django.utils import timezone

#最小値、最大値を指定する。(例えば、金額の場合、0円よりも小さい値を入力されてはいけない。そういう時はMinValueValidatorを使う。)
from django.core.validators import MinValueValidator,MaxValueValidator


#契約状況
AGGREEMENT  = [
        ("契約中"   , "契約中"  ),
        ("解約済み" , "解約済み"),
        ("初期分析" , "初期分析"),
        ]


# 担当者テーブル
class Manager(models.Model):
    name    = models.CharField(verbose_name="担当者名",max_length=10)

    def __str__(self):
        return self.name

# 店舗テーブル
class Store(models.Model):

    #独自の主キーを指定する。(手動で入れる主キーであればeditable=Falseを指定すると管理サイトから指定できない。)
    id      = models.CharField(verbose_name="店舗ID", primary_key=True, max_length=30)

    name    = models.CharField(verbose_name="店舗名",max_length=30)
    manager = models.ForeignKey(Manager, verbose_name="担当者", on_delete=models.CASCADE)

    #選択肢から選ぶ場合はchoicesを用意する。これでこれ以外の文字列はDBには保存されない。
    status  = models.CharField(verbose_name="契約ステータス",choices=AGGREEMENT, max_length=4)
    date    = models.DateField(verbose_name="契約日")

    def __str__(self):
        return self.name


#TODO:独自のバリデーション
def check_day(value):
    if value.day != 1:
        raise ValidationError( "日付が1日ではありません" , params={'value': value}, )


# 店舗データテーブル
class StoreData(models.Model):

    #対象店舗と年月で重複した記録を許さない場合、このようにunique_togetherを使う。
    class Meta:
        unique_together = ("store","date")

    store   = models.ForeignKey(Store,verbose_name="店舗",on_delete=models.CASCADE)

    #TODO:年月だけ記録したい場合は、バリデーション時に日付を1にして保存する。
    date    = models.DateField(verbose_name="記録年月", validators=[check_day])

    #TODO:後に店舗に紐づくデータを取得したい場合はここでモデルメソッドを使用する。

    def get_sale(self):
        return Sale.objects.filter(store_data=self.id) 






    #各テーブルに
    def __str__(self):
        return self.store.name + " : " +  str(self.date)


#売上テーブル
class Sale(models.Model):

    pc          = models.IntegerField(verbose_name="PC"     , validators=[MinValueValidator(0)])
    phone       = models.IntegerField(verbose_name="スマホ" , validators=[MinValueValidator(0)])
    app         = models.IntegerField(verbose_name="アプリ" , validators=[MinValueValidator(0)])
    store_data  = models.OneToOneField(StoreData, verbose_name="データ", on_delete=models.CASCADE)


#売上件数テーブル
class SaleAmount(models.Model):

    pc          = models.IntegerField(verbose_name="PC"     , validators=[MinValueValidator(0)])
    phone       = models.IntegerField(verbose_name="スマホ" , validators=[MinValueValidator(0)])
    app         = models.IntegerField(verbose_name="アプリ" , validators=[MinValueValidator(0)])
    store_data  = models.OneToOneField(StoreData, verbose_name="データ", on_delete=models.CASCADE)


#アクセス人数テーブル
class Access(models.Model):

    pc          = models.IntegerField(verbose_name="PC"     , validators=[MinValueValidator(0)])
    phone       = models.IntegerField(verbose_name="スマホ" , validators=[MinValueValidator(0)])
    app         = models.IntegerField(verbose_name="アプリ" , validators=[MinValueValidator(0)])
    store_data  = models.OneToOneField(StoreData, verbose_name="データ", on_delete=models.CASCADE)



#転換率テーブル
class ConversionRate(models.Model):

    pc          = models.FloatField(verbose_name="PC"       , validators=[MinValueValidator(0),MaxValueValidator(100)])
    phone       = models.FloatField(verbose_name="スマホ"   , validators=[MinValueValidator(0),MaxValueValidator(100)])
    app         = models.FloatField(verbose_name="アプリ"   , validators=[MinValueValidator(0),MaxValueValidator(100)])
    store_data  = models.OneToOneField(StoreData, verbose_name="データ", on_delete=models.CASCADE)




