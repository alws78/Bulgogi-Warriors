import json
import random
from flask import Flask,request,jsonify
from flask_restx import Resource, Api

class RecipeRecommendation():

    def __init__(self, data_path):
        self.default_ingredients = {'물', ''}
        self.recipes = self._load_index(data_path)
        self.non_recipe = '적합한 레시피가 없습니다.\n 다시 시도해주세요.'

    def _load_index(self, data_path):
        '''
        요리 정보 json 파일 경로에서 데이터를 읽고 인덱싱

        :param data_path: 요리 정보 json 파일 경로
        :return: 인덱싱된 요리 리스트
        '''
        with open(data_path, "r", encoding='utf-8') as f:
            json_data = json.load(f)
        recipes = []
        for row in json_data['COOKRCP01']['row']:
            name = row["RCP_NM"]
            ingredient = row["RCP_PARTS_DTLS"]
            method = ""
            for i in range(1, 19):
                if i < 10:
                    mamula = row["MANUAL0" + str(i)]
                else:
                    mamula = row["MANUAL" + str(i)]
                method += mamula + "\n"

            method = method.strip()
            cooking_ingredients = ingredient.replace('\n', ', ')
            cooking_ingredients = [i.strip().split(' ')[0].split('(')[0] for i in cooking_ingredients.split(',')]

            cooking_ingredients = set(cooking_ingredients) - self.default_ingredients
            recipes.append({"dish": name, "ingredient": ingredient, "method": method, 'index': cooking_ingredients})
        return recipes

    def _find_recipe(self, find_ingredients):
        '''
        유사 요리 탐색
        요리 재료의 교집합이 가장 높은 조리법 중 랜덤으로 하나 선택
        :param find_ingredients: 사용자 검색 요리 재료
        :return: 추천 요리법
        '''
        find_ingredients = set(find_ingredients)
        result_ingredients = {}
        for recipe in self.recipes:
            recipe_ingredients = recipe['index']
            intersection = len(recipe_ingredients & find_ingredients)
            if intersection == 0:
                continue
            if intersection in result_ingredients:
                result_ingredients[intersection].append(recipe)
            else:
                result_ingredients[intersection] = [recipe]
        top_index = sorted(result_ingredients.keys(), reverse=True)[0]
        result_ingredient_list = result_ingredients[top_index]
        return random.choice(result_ingredient_list)

    def find_recipe(self, find_ingredients):
        '''
        추천 요리 반환
        :param find_ingredients: 사용자 검색 요리 재료
        :return: 추천 요리명과 요리법
        '''
        rec_recipe = self._find_recipe(find_ingredients)
        return rec_recipe

target_path = "./1000.json"
recipe_recommendation = RecipeRecommendation(target_path)

find_ingredients = ['고구마죽', '', '']
recipe_recommendation = RecipeRecommendation(target_path)
result = recipe_recommendation.find_recipe(find_ingredients)
print(result)

def make_response(a,b):
    response = {
        "version": "2.0",
        "resultCode": "OK",
        "output": {
            "RCP_NM": "",
            "RCP_METHOD": "",
        }
    }
    response['output']['RCP_NM'] = a
    response['output']['RCP_METHOD'] = b
    
    return response

app = Flask(__name__)
api = Api(app)

class Getparams(Resource):
    def post(self):
        data = request.get_json()
    
        ingredient1 = data['action']['parameters']['ingredient_one']['value']
        ingredient2 = data['action']['parameters']['ingredient_two']['value']
        ingredient3 = data['action']['parameters']['ingredient_three']['value']
        target_path = "./1000.json"
        recipe_recommendation = RecipeRecommendation(target_path)   
        find_ingredients = [ingredient1,ingredient2, ingredient3]
        recipe_recommendation = RecipeRecommendation(target_path)
        result = recipe_recommendation.find_recipe(find_ingredients)
        
        name = result['dish']
        method = result['method']
        
        response = make_response(name,method)
        
        return jsonfy(response)
    
api.add_resource(Getparams,'/bring.ingredients')    

if __name__ == "__main__":
    app.run()