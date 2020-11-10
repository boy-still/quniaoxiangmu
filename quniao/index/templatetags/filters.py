from django.template import Library
register = Library()
@register.filter
def get_value(d, key):
    lists=[]
    for i in d:
        lists.append(int(i[key]))
        print(int(i[key]))
        #lists.append(int(i[key]))

    return lists

