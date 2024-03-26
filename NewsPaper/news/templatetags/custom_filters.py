from django import template

register = template.Library()

@register.filter()
def censor(value):
    cheak_word = value.split()

    for word in cheak_word:
        if word[0].lower() == "p":
            id_word = cheak_word.index(word)
            cen_word = word[0]

            for i in range(len(word)-1):
                cen_word+= "*"

            cheak_word.remove(word)
            cheak_word.insert(id_word, cen_word)

    value = " ".join(cheak_word)
    return f'{value}'
