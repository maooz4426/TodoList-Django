from django.db import models

#カテゴリモデル
class Category(models.Model):
    #カテゴリ名
    name = models.CharField(max_length=255)
    #カテゴリを設定した人
    author = models.ForeignKey(
        'auth.User',on_delete=models.CASCADE,
    )
    #作成日
    created_at = models.DateTimeField(auto_now_add=True)
    #更新日
    updated_at = models.DateTimeField(auto_now=True)

    #これ入れないと管理画面でcategoryobjectgって名前になる
    def __str__(self):
        return self.name

class Task(models.Model):
    #タスク名
    title = models.CharField(max_length=255)
    # タスクを設定した人
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    #カテゴリ（外部キー参照)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT
    )
    #完了確認
    completed = models.BooleanField(default=False)
    #締切日
    deadline = models.DateTimeField()
    #タスク作成日
    created_at = models.DateTimeField(auto_now_add=True)
    #タスク完了日
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
