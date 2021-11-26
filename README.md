## Team members

#### Ju Sang Han , Department of Information System, wntkdgks4076@gmail.com 

#### Lee Won Seok, Department of Information System, lws1516@naver.com

#### Lee Jun I , Department of Information System, lji123ji-@naver.com 

#### Valiukenas, Airidas Tomas , Department of Program System, airidas.valiukenas@ktu.edu

#### Kouadio, Laura, Department of Electronics and Computer Science , laura.kouaio@ensea.fr 

## Title
#### AI Cooking manager - Ghost CookKing

## Introduction

####  AI cooking assistant - Ghost CookKing - is a dish recipe recommendation system and will let us know the cooking steps. So to speak, we are trying to make a service that acts like a kitchen assistant. A User of LG signature appliance can use an application called 'Signature Kitchen Suite'. One of this application's function is that a user can see what's in his refrigerator. We can import the list of ingredients from refrigerator. We will use Kaggle's recipe dataset or a recipebox dataset that nicely scraped from websites. From now we're considering relu softmax method but it can be changed. Using the recipe dataset, ingredients and classification system, Ghost CookKing will make a suggestion based on existing ingredients and user's command, and let us know what to buy more to cook that dish. Moreover, when you start cooking, you will be informed of the cooking process step by step. If possible, it will be improved by automatic adjustment of of fire or oven.

![latex2](https://user-images.githubusercontent.com/95012070/143515817-ffef0ab8-f775-468a-bd44-f2d2394b812b.png){: width="100" height="100"}

## DATASET
식품의약품안전처의 레시피 과정 정보 OpenAPI를 요청해 CSV 파일로 데이터전처리를 하였음.

## Methodology
KOGPT-2는 머신러닝 알고리즘을 활용해 입력된 샘플 텍스트를 구문론적, 문법적 정보 등의 일관성을 갖춘 텍스트로 생성하는 자연어 처리 모델이다. 한국어로 학습된 오픈소스 기반 GPT-2 모델인 KoGPT-2는 질문에 대한 응답 생성, 문장 완성, 챗봇 등 한국어 해석이 필요한 여러 애플리케이션의 머신러닝 성능을 향상시킬 수 있다. (GPT-2는 주어진 텍스트의 다음 단어를 잘 예측할 수 있도록 학습된 언어모델이며 문장 생성에 최적화 되어 있습니다.)


## References
1. 식품의약안전처 공공데이터: https://www.foodsafetykorea.go.kr/apiMain.do
2. KoGPT2: https://github.com/SKT-AI/KoGPT2
