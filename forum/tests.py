from django.test import TestCase
from django.test import TestCase, Client
import os
import requests
import json
from forum.models import UserProfile, Module, PostManage, Post, StarContent, Comment
from forum.views import *;


class UserProfileTest(TestCase):
    def setUp(self):
        UserProfile.objects.create(name="Guo", sex="male", is_muted=False, user_id=1)
        UserProfile.objects.create(name="SomeOne", sex="female", is_muted=True, user_id=2)

    def test_create_and_delete_new_user(self):
        """ check if users can be create and delete"""
        guo = UserProfile.objects.get(name="Guo")
        guo.is_muted = True
        # Remember to delete your new user after insert it into database
        self.assertEqual(guo.save(), None, "fail to create this new user")
        self.assert_(UserProfile.objects.get(name="Guo").delete(), " cannot find the user, unable to delete")

    def test_set_follower_list(self):
        """check if the follower set can be successfully established"""
        guo = UserProfile.objects.get(name="Guo")
        someone = UserProfile.objects.get(name="SomeOne")
        follow_list = [str(someone.user_id)]
        guo.set_follow_by_list(follow_list[0])
        self.assertIn(str(someone.user_id), guo.get_follow_by_list(), " The User is Not in your follower list")


class HttpTest(TestCase):
    # user data need to be changed
    user = "1234567"
    host = "http://127.0.0.1:8000/forum"
    false = False
    true = True
    null = None
    token = None
    POST = "POST"
    GET = "GET"
    DELETE = "DELETE"
    PUT = "PUT"
    headers = {'content-Type': 'application/json', 'Accept': '*/*'}
    # login data need to be changed
    login_data = json.dumps({"phone": user,
                             "pwd": "e10adc3949ba59abbe56e057f20f883e",
                             "login_type": 0,
                             "identifier": "",
                             "role": 0})



    def setUp(self):
        login = None
        login_content = []
        try:
            login = requests.post(self.host + "/login", data=self.login_data, headers=self.headers)
            login_content = eval(login.content.decode("utf-8"))
        except:
            self.assert_(False, "failed to pass basic login, due to connection overtime")
        if login_content["code"] == 0:
            self.assert_(True, "login success")
            token = login_content["data"]["token"]
            print("token:" + token)
        else:
            print("login fail")
        if not token:
            self.assert_(False, "login anomaly")
            raise Exception("login error")
        self.headers["user-token"] = token

    def test(self, method, url, body_data=None, query_string=None, rest_query_string=None):
        if query_string:
            url = self.host + url + (
                str(rest_query_string) if rest_query_string is not None else "") + "?" + query_string
        else:
            url = self.host + url + (str(rest_query_string) if rest_query_string is not None else "")
        if method in [self.POST, self.DELETE, self.PUT] and body_data:
            body_data = json.dumps(body_data)
        response_data = requests.request(method, url, data=body_data, headers=self.headers)
        response_data = response_data.content.decode("utf-8")
        if response_data.find("\"code\": 0") != -1:
            print(url + " success!")
        else:
            print(url + " failed!" + response_data)

        self.assert_( self.test(self.GET, "/check_token/", rest_query_string=self.token),"token test failed" )
        self.assert_( self.test(self.GET, "/get/child"), "get test failed")

    def test_user_login(self):
        self.assert_(user_login(request=None), " failed to test none set ")
