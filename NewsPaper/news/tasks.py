from celery import shared_task
import datetime
from django.conf import settings
from news.models import Post, Category
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

@shared_task
def send_email_task(pk):
    post = Post.objects.get(pk=pk)
    title = post.title
    categories = post.postCategory.all()
    subscribers_emails = []
    for category in categories:
        subscribers_user = category.subscribers.all()
        for sub_user in subscribers_user:
            subscribers_emails.append(sub_user.email)

    html_content = (
        f'Новость: {post.title}<br>'
        f'<a href="{settings.SITE_URL}/post/{pk}">'
        f'Ссылка на новость</a>'
    )
    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email='varipaev.ser@yandex.ru',
        to=subscribers_emails)
    msg.attach_alternative(html_content, "text/html")
    msg.send()


@shared_task
def weekly_send_email_task():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(dataCreate__gte=last_week)
    categories = set(posts.values_list('postCategory__name', flat=True))
    subscribers = set(Category.objects.filter(name__in=categories).values_list('subscribers__email', flat=True))

    html_content = render_to_string(
        'daily_post.html',
        {
            'link': settings.SITE_URL,
            'post': posts,
        }
    )

    msg = EmailMultiAlternatives(subject='Статьи за неделю',
                                 body='',
                                 from_email='varipaev.ser@yandex.ru',
                                 to=subscribers)
    msg.attach_alternative(html_content, "text/html")
    msg.send()