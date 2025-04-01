# from flask import Flask, request, jsonify
# from flask_migrate import Migrate

# app = Flask(__name__)
# app.config.from_pyfile('config.py')
# db.init_app(app)
# jwt.init_app(app)
# migrate = Migrate(app, db)

# # Auth Routes
# @app.route('/api/auth/register', methods=['POST'])
# def register():
#     data = request.get_json()
#     user = User(email=data['email'], role=data.get('role', 'user'))
#     user.set_password(data['password'])
#     db.session.add(user)
#     db.session.commit()
#     return jsonify({'message': 'User created'}), 201

# @app.route('/api/auth/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     user = User.query.filter_by(email=data['email']).first()
#     if user and user.check_password(data['password']):
#         return jsonify({'token': generate_token(user)})
#     return jsonify({'error': 'Invalid credentials'}), 401

# # Artist Routes
# @app.route('/api/artists', methods=['POST'])
# @jwt_required()
# @roles_required('artist', 'admin')
# def create_artist_profile():
#     current_user = User.query.get(get_jwt_identity())
#     data = request.get_json()
#     artist = Artist(
#         user_id=current_user.id,
#         stage_name=data['stage_name'],
#         bio=data.get('bio'),
#         genre=data.get('genre')
#     )
#     db.session.add(artist)
#     db.session.commit()
#     return jsonify(artist.serialize()), 201

# # Event Routes
# @app.route('/api/events', methods=['GET'])
# def get_events():
#     events = Event.query.filter(Event.date_time > datetime.utcnow()).all()
#     return jsonify([e.serialize() for e in events])

# @app.route('/api/events', methods=['POST'])
# @jwt_required()
# @roles_required('venue', 'admin')
# def create_event():
#     data = request.get_json()
#     event = Event(
#         title=data['title'],
#         date_time=datetime.fromisoformat(data['date_time']),
#         venue_id=data['venue_id'],
#         artist_id=data['artist_id'],
#         price=data['price'],
#         tickets_available=data['tickets_available']
#     )
#     db.session.add(event)
#     db.session.commit()
#     return jsonify(event.serialize()), 201

# @app.route('/api/events', methods=['GET'])
# def get_events():
#     page = request.args.get('page', 1, type=int)
#     per_page = 20
#     events = Event.query.paginate(page=page, per_page=per_page)
#     return jsonify({
#         'events': [e.serialize() for e in events.items],
#         'page': events.page,
#         'total_pages': events.pages
#     })

# # Booking Routes
# @app.route('/api/bookings', methods=['POST'])
# @jwt_required()
# def create_booking():
#     data = request.get_json()
#     event = Event.query.get(data['event_id'])
    
#     if event.tickets_available < data['tickets']:
#         return jsonify({'error': 'Not enough tickets available'}), 400
    
#     booking = Booking(
#         user_id=get_jwt_identity(),
#         event_id=data['event_id'],
#         tickets=data['tickets'],
#         total_price=event.price * data['tickets']
#     )
    
#     event.tickets_available -= data['tickets']
#     db.session.add(booking)
#     db.session.commit()
#     return jsonify(booking.serialize()), 201