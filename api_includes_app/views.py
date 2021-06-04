from django.shortcuts import render
import requests
poke_api_url = "https://pokeapi.co/api/v2/pokemon"
# Create your views here.
def index(request):
  r = requests.get(poke_api_url)
  r = r.json()
  results = r['results']
  context = {
    "pokemon": results
  }
  return render(request, 'index.html', context)

def contact(request):
  return render(request, 'contact.html')