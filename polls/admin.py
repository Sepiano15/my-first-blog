from django.contrib import admin
from .models import Choice, Question
# Register your models here.
class ChoiceInline(admin.StackedInline):
    model = Choice  #Choice라는 모델을
    extra = 3       #3가지 선택하게 한다.

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    search_fields = ['question_text'] #텍스트 검색 추가
    list_filter = ['pub_date'] #요일 필터링 추가
    list_display = ('question_text', 'pub_date', 'was_published_recently') #Question리스트에서 출력될 정보 선택
    inlines = [ChoiceInline]  #Question 추가할 때 Choice모델 선택


admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
