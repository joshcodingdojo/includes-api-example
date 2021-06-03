from django.shortcuts import render
import requests
poke_api_url = "https://pokeapi.co/api/v2/pokemon"
# Create your views here.
def index(request): 
  r = requests.get(poke_api_url)
  json = r.json()
  print(json['results'])
  context = {
    "results": json['results']
  }
  return render(request, 'index.html', context)
