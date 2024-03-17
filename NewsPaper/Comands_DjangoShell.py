python manage.py shell
from news.models import *

#Создал два юзера
u1 = User.objects.create_user(username='Vladimir')
u1
<User: Vladimir>
u2 = User.objects.create_user(username='Julia')
u2
<User: Julia>

#Создал два автора
Author.objects.create(authorUser=u1)
<Author: Author object (1)>
Author.objects.create(authorUser=u2)
<Author: Author object (2)>

#Создал 4 категории
Category.objects.create(name='Sport')
<Category: Category object (1)>
Category.objects.create(name='Music')
<Category: Category object (2)>
Category.objects.create(name='Cars')
<Category: Category object (3)>
Category.objects.create(name='Beauty')
<Category: Category object (4)>
author1 = Author.objects.get(id=1)
author1
<Author: Author object (1)>
author2 = Author.objects.get(id=2)
author2
<Author: Author object (2)>

#Создал посты
Post.objects.create(author=author1, categoryType='NW', title='Финал лиги чемпионов', text='bigtext')
<Post: Post object (1)>
Post.objects.create(author=author2, categoryType='AR', title='Новое поколение авто', text='verybigtext')
<Post: Post object (2)>
Post.objects.create(author=author1, categoryType='AR', title='Новый альбом', text='text')
<Post: Post object (3)>

#Присвоил постам категории
Post.objects.get(id=1).postCategory.add(Category.objects.get(id=1))
Post.objects.get(id=2).postCategory.add(Category.objects.get(id=1))
Post.objects.get(id=2).postCategory.add(Category.objects.get(id=3))
Post.objects.get(id=3).postCategory.add(Category.objects.get(id=2))

#Создал 4 комментария к постам
Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).authorUser, text='sometext')
<Comment: Comment object (1)>
Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=2).authorUser, text='anytext')
<Comment: Comment object (2)>
Comment.objects.create(commentPost=Post.objects.get(id=2), commentUser=Author.objects.get(id=1).authorUser, text='text')
<Comment: Comment object (3)>
Comment.objects.create(commentPost=Post.objects.get(id=3), commentUser=Author.objects.get(id=2).authorUser, text='bigtext')
<Comment: Comment object (4)>

#Лайки и дизлайки к комментариям + корректировка рейтинга
Comment.objects.get(id=1).like()
Comment.objects.get(id=1).dislike()
Comment.objects.get(id=1).dislike()
Comment.objects.get(id=1).dislike()
Comment.objects.get(id=1).rating
-2
Comment.objects.get(id=2).like()
Comment.objects.get(id=2).like()
Comment.objects.get(id=2).like()
Comment.objects.get(id=2).like()
Comment.objects.get(id=2).dislike()
Comment.objects.get(id=2).dislike()
Comment.objects.get(id=2).rating
2
Comment.objects.get(id=3).dislike()
Comment.objects.get(id=3).dislike()
Comment.objects.get(id=3).dislike()
Comment.objects.get(id=3).dislike()
Comment.objects.get(id=3).like()
Comment.objects.get(id=3).rating
-3
Comment.objects.get(id=4).dislike()
Comment.objects.get(id=4).like()
Comment.objects.get(id=4).like()
Comment.objects.get(id=4).like()
Comment.objects.get(id=4).like()
Comment.objects.get(id=4).like()
Comment.objects.get(id=4).like()
Comment.objects.get(id=4).dislike()
Comment.objects.get(id=4).rating
4

#Лайки и дизлайки к постам + корректировка рейтинга
Post.objects.get(id=1).like()
Post.objects.get(id=1).like()
Post.objects.get(id=1).like()
Post.objects.get(id=1).like()
Post.objects.get(id=1).like()
Post.objects.get(id=1).like()
Post.objects.get(id=1).dislike()
Post.objects.get(id=1).rating
5
Post.objects.get(id=2).dislike()
Post.objects.get(id=2).dislike()
Post.objects.get(id=2).dislike()
Post.objects.get(id=2).dislike()
Post.objects.get(id=2).dislike()
Post.objects.get(id=2).dislike()
Post.objects.get(id=2).like()
Post.objects.get(id=2).like()
Post.objects.get(id=2).rating
-4
Post.objects.get(id=3).dislike()
Post.objects.get(id=3).like()
Post.objects.get(id=3).like()
Post.objects.get(id=3).like()
Post.objects.get(id=3).like()
Post.objects.get(id=3).like()
Post.objects.get(id=3).like()
Post.objects.get(id=3).like()
Post.objects.get(id=3).like()
Post.objects.get(id=3).like()
Post.objects.get(id=3).like()
Post.objects.get(id=3).rating
9

# Обновляю рейтинг пользователей
a = Author.objects.get(id=1)
a.update_rating()
a.ratingAuthor
37
b = Author.objects.get(id=2)
b.update_rating()
b.ratingAuthor
-6

# Вывод лучшего пользователя
bestUser = Author.objects.order_by('-ratingAuthor')[:1]
bestUser
<QuerySet [<Author: Author object (1)>]>
>>> for i in bestUser:
...     i.ratingAuthor
...     i.authorUser.username
...
37
'Vladimir'

# Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
bestPost = Post.objects.order_by('-rating')[:1]
bestPost
<QuerySet [<Post: Post object (3)>]>
for i in bestPost:
...     i.dataCreate
...     i.author.authorUser.username
...     i.rating
...     i.title
...     i.preview()
...
datetime.datetime(2024, 3, 17, 8, 3, 15, 427991, tzinfo=datetime.timezone.utc)
'Vladimir'
9
'Новый альбом'
'text...'

#Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
bestPost
<QuerySet [<Post: Post object (3)>]>
post = Post.objects.get(id=3)
post.comment_set.all()
<QuerySet [<Comment: Comment object (4)>]>
post.comment_set.values('dateCreation', 'commentUser', 'text', 'rating')
<QuerySet [{'dateCreation': datetime.datetime(2024, 3, 17, 8, 28, 26, 390899, tzinfo=datetime.timezone.utc), 'commentUser': 4, 'text': 'bigtext', 'rating': 4}]>










