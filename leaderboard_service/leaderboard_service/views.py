#!/usr/bin/python3

# -*- coding:utf-8 -*-
"""

@author: forgotten_liu
@projectName: leaderboard_service
@file: views
@time: 2021/5/21 10:33
@IDE: PyCharm
@desc:

"""
from django.shortcuts import HttpResponse, render, redirect
from django.contrib import auth
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from leaderboard_service.models import *


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        user_name = request.POST.get('username', '')
        response = redirect('/upload/')
        response.set_cookie('username', user_name, 3600)
        return response


def upload(request):
    client_name = request.COOKIES.get('username', '')
    if client_name:
        if request.method == 'GET':
            username = request.COOKIES.get('username', '')
            return render(request, 'upload.html', {'username': username})
        if request.method == 'POST':
                score = request.POST.get('score', '')
                if score:
                    # 判断数据库内已存在分数,如果分数存在则更新，否则写入
                    exist_score = Score.objects.filter(client=client_name).first()
                    if exist_score and exist_score.score != score:
                        exist_score.score = score
                        exist_score.save()
                    else:
                        Score.objects.create(client=client_name, score=score)
                    # 排名表更新数据
                    Rank.objects.all().delete()
                    score_li = [score_obj.id for score_obj in Score.objects.all().order_by('-score')]
                    n = 1
                    for i in score_li:
                        Rank.objects.create(c_id_id=i, rank=n)
                        n = n + 1
                    return render(request, 'upload.html', {'success': "提交成功!"})
    else:
        return redirect('/login/')


def leaderboard(request):
    client_name = request.COOKIES.get('username', '')
    if client_name:
        context = {'scores': [{'ranking': score.rank.rank, 'client': score.client, 'score': score.score} for score in
                              Score.objects.all().order_by('-score')]}
        user_score = Score.objects.filter(client=client_name).first()
        user_score = {'ranking': user_score.rank.rank, 'score': user_score.score}
        if request.method == 'GET':
            return render(request, 'leaderboard.html', {'context': context, 'uscore': user_score, 'logname': client_name})
        if request.method == 'POST':
            start = int(request.POST.get('start', ''))
            end = int(request.POST.get('end', ''))
            context = {'scores': [{'ranking': score.rank.rank, 'client': score.client, 'score': score.score} for score in
                                  Score.objects.all().order_by('-score')[int(start) - 1:end]]}
            return render(request, 'leaderboard.html', {'context': context, 'uscore': user_score, 'logname': client_name})
    else:
        return redirect('/login/')