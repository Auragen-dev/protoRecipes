# -*- coding: utf-8 -*-
import json

class recipe:
    def __init__(self, id, title, ingredients, method):
        self.id = id
        self.title = title
        self.ingredients = ingredients
        self.method = method

    def getID(self):
        return self.id
    
    def getTitle(self):
        return self.title
    
    def getIngredients(self):
        return self.ingredients
    
    def getMethod(self):
        return self.method

    