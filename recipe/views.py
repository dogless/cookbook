from django.shortcuts import render
from recipe.models import Recipe, Step

# Create your views here.
def index(request):
	return render(request, 'recipe/index.html')

def test(request):
	recipe = Recipe.objects.get(name="pbj")
	steps = recipe.step_set.all()

	print steps
	context = {
		'steps': steps,
	}
	return render(request, 'recipe/test.html', context)
