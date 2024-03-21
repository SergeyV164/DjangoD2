from django import template

register = template.Library()

bad_words = ['text', 'bigtext', 'verybigtext', 'альбом', 'лиги', 'поколение']

@register.filter()
def censor(value):
   words = value.split()
   censor_list = []

   for word in words:
      if word.lower() in bad_words:
         censor_word = word[0] + '*' * (len(word) - 1)
         censor_list.append(censor_word)
      else:
         censor_list.append(word)

   return ' '.join(censor_list)