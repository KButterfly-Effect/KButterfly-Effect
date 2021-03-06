from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    title_tag = models.CharField(max_length=20) # 요약 태그
    hashtag = models.TextField(max_length=30)  #해시 태그, 여러개하면 할때마다 띄워쓰기 시키기
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(auto_now=False)
    body = models.TextField()
    image = models.ImageField(upload_to="post/",null=True)
    shared= models.IntegerField(default=0) #공유된 수
    like_user_set = models.ManyToManyField(User, blank=True, related_name='likes_user_set',through='Like')
    after_dead=models.BooleanField(default=False) #데드라인이후 포스팅에 좋아요, 공유횟수가 개인 에코점수로 넘어간지 확인

    @property
    def like_count(self):
        return self.like_user_set.count()

#좋아요 모델
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together =(('user', 'post'))
