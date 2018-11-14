from app import db
from models import Post

# t = Tag.query.first()
# print(t)
# post1 = Post.query.filter(Post.id == 1)
# print(post1)
# post1=post1.first()
# post1.tags
# print(post1.tags)

p = Post(title="test1", body="body1")

print(p)
print(p.slug)
