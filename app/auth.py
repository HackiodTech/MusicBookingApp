from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from functools import wraps

jwt = JWTManager()

def roles_required(*roles):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            current_user = User.query.get(get_jwt_identity())
            if current_user.role not in roles:
                return {'error': 'Insufficient permissions'}, 403
            return fn(*args, **kwargs)
        return decorator
    return wrapper

# Token generation in login route
def generate_token(user):
    return create_access_token(identity=user.id, 
                             additional_claims={'role': user.role})