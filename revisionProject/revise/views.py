from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def first(request):
    # return render(request,'./first.html')
    # return HttpResponse("hello world")
    name=request.GET.get("name",'krishna')
    age=request.GET.get("age",24)
    gender=request.GET.get("gender",'male')
    data={"student_name":name,"student_age":age,"gender":gender}
    return  JsonResponse(data,status=200)

movies_data = [
    {
        "id": 1,
        "movie_name": "Inception",
        "release_year": 2010,
        "genre": "Sci-Fi",
        "rating": 6.5,
        "director": "Christopher Nolan"
    },
    {
        "id": 2,
        "movie_name": "Baahubali: The Beginning",
        "release_year": 2015,
        "genre": "Action / Drama",
        "rating": 7.0,
        "director": "S. S. Rajamouli"
    },
    {
        "id": 3,
        "movie_name": "Interstellar",
        "release_year": 2014,
        "genre": "Sci-Fi",
        "rating": 9.6,
        "director": "Christopher Nolan"
    },
    {
        "id": 4,
        "movie_name": "KGF: Chapter 1",
        "release_year": 2018,
        "genre": "Action",
        "rating": 7.2,
        "director": "Prashanth Neel"
    },
    {
        "id": 5,
        "movie_name": "Avengers: Endgame",
        "release_year": 2019,
        "genre": "Action / Fantasy",
        "rating": 6.4,
        "director": "Russo Brothers"
    }
]

def movies(request):
    filtered_list=[]
    r1=float(request.GET.get("r1"))
    r2=float(request.GET.get("r2"))
    for movie in movies_data:
        if movie["rating"]>r1 and movie["rating"]<r2:
            filtered_list.append(movie)
    return JsonResponse({"data":filtered_list})
