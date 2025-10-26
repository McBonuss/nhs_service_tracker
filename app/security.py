from functools import wraps
from flask_login import current_user
from flask import abort

def roles_required(*roles):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if not current_user.is_authenticated:
                abort(401)
            if not any(current_user.has_role(r) for r in roles):
                abort(403)
            return fn(*args, **kwargs)
        return wrapper
    return decorator
