import json
import random
from flask import Flask, request, jsonify
from flask_restx import Resource, Api
from xml.etree.ElementTree import parse
import re
import pandas as pd
from string import punctuation


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


def make_response_bring(a,b,list):
    
    
    response = {
        "version": "2.0",
        "resultCode": "OK",
        "output": {
            "RCP_NM": "",
            "RCP_PARTS":"",
            "RCP_METHOD1": "",
            "RCP_METHOD2": "",
            "RCP_METHOD3": "",
            "RCP_METHOD4": "",
            "RCP_METHOD5": "",
            "RCP_METHOD6": "",
            "RCP_METHOD7": "",
            "RCP_METHOD8": "",
            "RCP_METHOD9": ""
        }
    }
    response['output']['RCP_NM'] = a
    response['output']['RCP_PARTS'] = b
    
    for i in range(len(list)):
        response['output']['RCP_METHOD'+str(i+1)] = list[i]

    return response




def make_response_recipe(a,b,list):
    
    
    response = {
        "version": "2.0",
        "resultCode": "OK",
        "output": {
            "rcp_nm": "",
            "rcp_parts": "",
            "rcp_method1": "",
            "rcp_method2": "",
            "rcp_method3": "",
            "rcp_method4": "",
            "rcp_method5": "",
            "rcp_method6": "",
            "rcp_method7": "",
            "rcp_method8": "",
            "rcp_method9": ""
        }
    }
    response['output']['rcp_nm'] = a
    response['output']['rcp_parts'] = b
    
    for i in range(len(list)):
        response['output']['rcp_method'+str(i+1)] = list[i]

    return response



def make_clear(method):
    
    alphabet = ['a','b','c']
    
    for i in alphabet:
        method = method.replace(i,"")
    
    
    for i in range(1,19):
        method = method.replace(str(i)+".","  " + str(i)+ ",")
        
    method = method.replace("\n","")
    method = method.replace(". ",".")
    
    list = method.split(".")
    
    return list





def Recipe_Name_Find(Text):
    
    path="./"
    tree=parse(path+"1000.xml")
    root=tree.getroot()
    
    df=[]
    for element in root.findall("row"):
        name=element.findtext("RCP_NM") # 레시피 이름
        ingredient=element.findtext("RCP_PARTS_DTLS") # 레시피 재료
    
        Method = ""
    
        for M in range(1,19):
            if M < 10:
                Temp = element.findtext("MANUAL0"+ str(M)) #메뉴얼 통합 1
                Method = Method + Temp
            else: 
                Temp = element.findtext("MANUAL"+ str(M)) # 메뉴얼 통합 2
                Method = Method + Temp   

        df.append({"요리명":name, "재료":ingredient,"요리법":Method})
        
    df=pd.DataFrame(df)
    Alphabet = ["a","b","c"] # 요리법에 들어있는 영어를 제거 하기 위함 

    for i in range(1,19):
        df['요리법'] =df['요리법'].apply(lambda x: x.replace(str(i)+".",'')) # 번호 제거
    for j in Alphabet:
        df['요리법'] =df['요리법'].apply(lambda x: x.replace(j,'')) # 영문자 제거

    df['요리법'] = df['요리법'].apply(lambda x: x.replace('\n','')) # 줄 제거 
    df['재료'] = df['재료'].apply(lambda x: x.replace("\n",',')) # 줄 제거
    df['재료'] = df['재료'].apply(lambda x: x.replace(',',', ')) # 공백추가
    df['재료'] = df['재료'].apply(lambda x: x.replace('g',"그램")) # 가끔씩 그램을 g로 읽어서 바꿈.
    regex = r"\([^\)]*\)"
    for i in range(len(df)):
        df['재료'][i] = re.sub(regex,'',df['재료'][i])
    
    recipe=df[df['요리명'] == Text]
    recipe.to_json('test.json',orient='table')

    return_list = []
    rcp_nm = recipe['요리명'].values[0]
    rcp_parts = recipe['재료'].values[0]
    rcp_method = recipe['요리법'].values[0]

    List = [rcp_nm,rcp_parts,rcp_method]

    for i in List:
        return_list.append(i)

    return return_list


app = Flask(__name__)
api = Api(app)


class Getparams(Resource):
    def post(self):
        data = request.get_json() # json road 는 이렇게~
        print(data)

        find_ingredients = []
        rcp = []
        rcp_list = []
        select = 0 

        # data['action']['parameters']['ingredient_one']['value'] 이런식으로 접근할때 'iingredient_one' 이 없으면 접근할 수 없이 에러 나요
        
        if 'ingredient_one' in data['action']['parameters']:
            find_ingredients.append(data['action']['parameters']['ingredient_one']['value'])
            SELECT = 1 
        if 'ingredient_two' in data['action']['parameters']:
            find_ingredients.append(data['action']['parameters']['ingredient_two']['value'])
            SELECT = 1
        if 'ingredient_three' in data['action']['parameters']:
            find_ingredients.append(data['action']['parameters']['ingredient_three']['value'])
            SELECT = 1

            
        if "rcp_name" in data["action"]["parameters"]:
            rcp.append(data['action']['parameters']['rcp_name']['value'])
            SELECT = 2

        
                 
        if SELECT ==1:
            recipe_recommendation = RecipeRecommendation(target_path)
            result = recipe_recommendation.find_recipe(find_ingredients)

            name = result['dish']
            method = result['method']
            method = make_clear(method)
            
            rcp_list = Recipe_Name_Find(name)

            rcp_parts = rcp_list[1]

            
            response = make_response_bring(name, rcp_parts, method)



            return jsonify(response) 
        

        if SELECT ==2:
            
            rcp_list = Recipe_Name_Find(rcp[0])
            
            rcp_name = rcp_list[0] # 요리명 
            rcp_ingredients = rcp_list[1] # 요리재료
            rcp_method = rcp_list[2] # 조리법
            method = make_clear(rcp_method) #조리법 깔끔하게 

            response = make_response_recipe(rcp_name,rcp_ingredients,method)

            return jsonify(response) 


            


api.add_resource(Getparams, '/bring.ingredients','/bring.cusines')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)  # 이건 그냥 수정하면 알아서 재실행 하게 하는거.  있으면 편함
