from django.shortcuts import render

posts = [
	{
		'author': 'Азамат Мурдалов',
		'title': 'Первый пост',
		'content': 'Контент первого поста',
		'date_posted': 'Август 27, 2018'
	},
	{
		'author': 'Ислам Баталов',
		'title': 'Второй пост',
		'content': 'Контент второго поста',
		'date_posted': 'Август 28, 2018'
	}
]


def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)


def about(request):
	return render(request, 'blog/about.html', {'title': 'Обо мне'})