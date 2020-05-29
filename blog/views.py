from django.shortcuts import render
from django.utils import timezone

#.はカレントディレクトリー、ここではblog.のかわりかな
from .models import Post

#404エラーが表示されるモジュール
from django.shortcuts import render, get_object_or_404
#PostForモデルの読み込み
from .forms import PostForm
#リダイレクト
from django.shortcuts import redirect

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #render→テンプレートの組み立て、パラメーター{"name":value}をテンプレートに渡す
    #redirect指定したURL に飛ぶ
    return render(request, 'blog/post_list.html', {'posts': posts})
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
    
def post_new(request):
    #request.postにデータが追加される
    #getでもできるっぽい
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            #validに引っかからなければ以下が実行される
            #フォームは保存するが、postモデルは保存していない、これはここでやる意味あるのか？最後のpost.saveだけじゃだめなのか？？
            post = form.save(commit=False)
            #htmlのフォーム内にautherがないので、userモデルから引っ張ってくる、publishd_dateも同様
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})