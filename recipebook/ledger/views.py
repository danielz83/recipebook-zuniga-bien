from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def recipes_list(request):
    ctx = {
        "recipes": [
            {
                "name": "Recipe 1",
                "link": "/recipe/1"
            },
            {
                "name": "Recipe 2",
                "link": "/recipe/2"
            }
        ]
    }
    return render(request, 'ledger/recipes_list.html', ctx)

def recipe_detail(request, num:int =1):
    recipe_1 = {
        "name": "Recipe 1",
        "ingredients": [
            {
                "name": "tomato",
                "quantity": "3pcs"
            },
            {
                "name": "onion",
                "quantity": "1pc"
            },
            {
                "name": "pork",
                "quantity": "1kg"
            },
            {
                "name": "water",
                "quantity": "1L"
            },
            {
                "name": "sinigang mix",
                "quantity": "1 packet"
            }
        ],
        "link": "/recipe/1"
    }
    recipe_2 = {
        "name": "Recipe 2",
        "ingredients": [
            {
                "name": "garlic",
                "quantity": "1 head"
            },
            {
                "name": "onion",
                "quantity": "1pc"
            },
            {
                "name": "vinegar",
                "quantity": "1/2cup"
            },
            {
                "name": "water",
                "quantity": "1 cup"
            },
            {
                "name": "salt",
                "quantity": "1 tablespoon"
            },
            {
                "name": "whole black peppers",
                "quantity": "1 tablespoon"
            },
            {
                "name": "pork",
                "quantity": "1 kilo"
            }
        ],
        "link": "/recipe/2"
    }
    ctx = {}
    if num == 1:
        ctx = recipe_1
    if num == 2:
        ctx = recipe_2

    return render(request, 'ledger/recipe.html', ctx)
