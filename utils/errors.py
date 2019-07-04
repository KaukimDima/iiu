from django.shortcuts import render


def 404(request, context): return render(request, 'page_404.html', context)
