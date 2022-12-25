from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.recipe import Recipe, recipe_list

class RecipeListResource(Resource):
    # get all the recipes
    def get(self):

        data = []

        for recipe in recipe_list:
            if recipe.is_publish is True:
                data.append(recipe.data)

        return {'data': data}, HTTPStatus.OK

    # create a recipe
    def post(self):
        data = request.get_json()

        recipe = Recipe(name = data['name'], 
                        description = data['description'], 
                        num_of_servings = data['num_of_servings'], 
                        cook_time = data['cook_time'], 
                        directions = data['directions'])
        
        recipe_list.append((recipe))

        return recipe.data, HTTPStatus.CREATED


# Getting a single resource
class RecipeResource(Resource):

    def get(self, recipe_id):
        recipe = next((recipe for recipe in recipe_list if recipe.id == recipe_id and 
                        recipe.is_publish == True), None)

        if recipe is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

        
        return recipe.data, HTTPStatus.OK

    def put(self, recipe_id):
        data = request.get_json()

        recipe = next((recipe for recipe in recipe_list if recipe.id == recipe_id), 
                        None)
        
        if recipe is None:
            return{'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

        recipe.name = data['name']
        recipe.description = data['description']
        recipe.number_of_servings = data['num_of_servings']
        recipe.cook_time = data['cook_time']
        recipe.directions = data['directions']

        return recipe.data, HTTPStatus.OK



# publish and unpublish recipes i.e update recipes before publishing
class RecipePublishResource(Resource):

    def put(self, recipe_id):
        recipe = next((recipe for recipe in recipe_list if recipe.id == recipe_id), None)

        if recipe is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

        recipe.is_publish = True
        
        return {}, HTTPStatus.NO_CONTENT

    def delete(self, recipe_id):
        recipe = next((recipe for recipe in recipe_list if recipe.id == recipe_id), None)

        if recipe is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

        recipe.is_publish = False

        return {}, HTTPStatus.NO_CONTENT