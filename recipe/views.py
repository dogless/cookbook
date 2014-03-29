from django.shortcuts import render
from recipe.models import Recipe, Step

# Create your views here.
def index(request):
	recipes = Recipe.objects.all()

	context = {
		'recipes': recipes,
	}
	return render(request, 'recipe/index.html', context)

def search(request):
	context = {'recipes' : []}
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		recipes = Recipe.objects.filter(name__icontains=q)
		context = {
			'recipes': recipes
		}
	return render(request, 'recipe/search.html', context)

def recipe(request, number):
	recipe = Recipe.objects.get(id=number)
	steps = recipe.step_set.all()

	context = {
		'recipe': recipe,
		'steps': steps,
	}
	return render(request, 'recipe/recipe.html', context)
