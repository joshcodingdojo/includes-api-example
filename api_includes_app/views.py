from django.shortcuts import render
poke_api_url = "https://pokeapi.co/api/v2/pokemon"
# Create your views here.
def index(request): 
  return render(request, 'index.html')
