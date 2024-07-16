from lib.post import Post

"""
Post constructs with an id, title, contents, views, and account id
"""
def test_post_constructs():
    post = Post(1, 'Big Post', 'Biggest post possible', 0, 1)
    assert post.id == 1
    assert post.title == 'Big Post'
    assert post.contents == 'Biggest post possible'
    assert post.views == 0
    assert post.account_id == 1

"""
We can format posts to strings nicely
"""
def test_posts_format_nicely():
    post = Post(1, 'Big Post', 'Biggest post possible', 0, 1)
    assert str(post) == 'Post(1, Big Post, Biggest post possible, 0, 1)'
