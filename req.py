req = requests.delete('http://localhost:8000/api/fb_post/user/post/delete/v1/',
                    headers={'Authorization': 'Bearer kalyan1234'}, json={'user_id': 2, 'post_id': 9})