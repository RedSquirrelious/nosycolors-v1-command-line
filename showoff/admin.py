from django.contrib import admin

# Register your models here.
from .models import Target, Tweet



class TweetInline(admin.StackedInline):
	extra = 3
	model = Tweet



class TargetAdmin(admin.ModelAdmin):
	fieldsets = [(None, {'fields': ['target_name']}),]
	inlines = [TweetInline]

	# list_display = ['tweet_text', 'tweet_date', 'was_tweeted_in_last_7_days']
	search_fields = ['target_name']



# class TweetAdmin(admin.ModelAdmin):
# 	fieldsets = [(None, {'fields': ['tweet_text']}), ('Date Information', {'fields': ['tweet_date']})]
# 	inlines = [TweetInline]

# 	list_display = ['tweet_text', 'tweet_date', 'was_tweeted_in_last_7_days']

# 	list_filter = ['tweet_date']

# 	search_fields = ['tweet_text']




admin.site.register(Target, TargetAdmin)

# admin.site.register(Tweet, TweetAdmin)

admin.site.register(Tweet)