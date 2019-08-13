from app import app_microblog, db
from app.models import User, Post

@app_microblog.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
