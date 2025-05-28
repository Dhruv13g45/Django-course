from django.shortcuts import render,redirect
from .models import TweetModel
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def show_all_tweet(request):
    
    if request.method == 'POST':
        all_tweets = TweetModel.objects.all()
        tweet_title = request.POST.get('tweet_title')
        tweet_message = request.POST.get('tweet_message')
        tweet_user = request.user
        print(tweet_user)
        TweetModel.objects.create(tweet_title = tweet_title, tweet_message = tweet_message,user = tweet_user)
        print("success")
        return redirect('show_all_tweet')
    else:
        all_tweets = TweetModel.objects.all()
    return render(request, 'index.html',{'all_tweets' : all_tweets})


def create_new_tweet(request):
    current_user = request.user
    return render(request, 'newTweet.html',{'user':current_user})


def delete_tweet(request,tweetid):
    record = TweetModel.objects.get(id=tweetid)
    record.delete()
    return redirect('show_all_tweet')


def edit_tweet(request,tweetid):
    if request.method == 'POST':
        tweet = TweetModel.objects.get(id=tweetid)
        tweet.tweet_title = request.POST.get("tweet_title")
        tweet.tweet_message = request.POST.get('tweet_message')
        tweet.user = request.user
        tweet.save()
        return redirect("show_all_tweet")
    else:
        tweet = TweetModel.objects.get(id=tweetid)
    return render(request,'showSingleTweet.html', {'tweet':tweet})


def display_registor_route(request):
    
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username = name)

        if user.exists():
            messages.info(request, "User already exsits.")
            return redirect('/register/')

        new_user = User.objects.create(username = name,password = password)
        new_user.set_password(password)
        new_user.save()
        return redirect("/login/")
    
    return render(request,'registor.html')

def display_login_route(request):

    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=name, password=password)
        if user is None:
            return redirect('/register/')
        else:
            login(request,user)
            return redirect('show_all_tweet')
    return render(request,'login.html')


def display_logout_route(request):
    logout(request)
    return redirect('show_all_tweet')