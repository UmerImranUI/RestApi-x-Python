import requests
import pandas as pd
'''
provided by: themoviedb.org
https://api.themoviedb.org/3/movie/550?api_key=1f2b75da7407cfa5d44def673a072696
GET
/movie/{movie_id}
api_key='1f2b75da7407cfa5d44def673a072696'
api_key_v4='eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxZjJiNzVkYTc0MDdjZmE1ZDQ0ZGVmNjczYTA3MjY5NiIsInN1YiI6IjYzYzkwZDNiNzBiNDQ0MDBjOGJmMTcxNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Edqw3aJGQGlW3942iht5qvUc9vEWOC1TV8N1AWScumY'
'''
# movie_id=500
api_ver=3
api_key='1f2b75da7407cfa5d44def673a072696'
# api_base_url=f'https://api.themoviedb.org/{api_ver}/'
# endpoint_path=f'movie/{movie_id}'
# endpoint=f"{api_base_url}{endpoint_path}?api_key={api_key}"

# r=requests.get(endpoint)
# print(r.text)




# movie_id=501
# api_ver=4
# api_key_v4='eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxZjJiNzVkYTc0MDdjZmE1ZDQ0ZGVmNjczYTA3MjY5NiIsInN1YiI6IjYzYzkwZDNiNzBiNDQ0MDBjOGJmMTcxNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Edqw3aJGQGlW3942iht5qvUc9vEWOC1TV8N1AWScumY'
# api_base_url=f'https://api.themoviedb.org/{api_ver}/'
# endpoint_path=f'movie/{movie_id}'
# endpoint=f"{api_base_url}{endpoint_path}"
# headers = {
#     'Authorization': f'Bearer {api_key_v4}',
#     'Content-Type': 'application/json;charset=utf-8'
# }
# r=requests.get(endpoint, headers=headers)
# print(r.text)






api_base_url=f'https://api.themoviedb.org/{api_ver}/'
endpoint_path=f'/search/movie'
search_query='The Matrix'
endpoint=f"{api_base_url}{endpoint_path}?api_key={api_key}&query={search_query}"
# print(endpoint)
r=requests.get(endpoint)
# print(r.json())
if r.status_code in range(200,299):
    data=r.json()
    results=data['results']
    if len(results)>0:
        # print(results[0].keys())
        movie_ids=set()
        for result in results:
            _id = result['id']
            # print(result['title'], _id)
            movie_ids.add(_id)
        # print(list(movie_ids))


output='movies.csv'
movie_data=[]
for movie_id in movie_ids:
    api_ver=3
    api_base_url=f'https://api.themoviedb.org/{api_ver}/'
    endpoint_path=f'movie/{movie_id}'
    endpoint=f"{api_base_url}{endpoint_path}?api_key={api_key}"
    r=requests.get(endpoint)
    if r.status_code in range(200,299):
        data=r.json()
        movie_data.append(data)
    
df= pd.DataFrame(movie_data)
print(df.head())
df.to_csv(output, index=False)

