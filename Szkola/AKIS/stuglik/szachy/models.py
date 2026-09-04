from flask_login import UserMixin
from extentions import db


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    ranking = db.Column(db.Integer, default=0, nullable=False)

    def __repr__(self):
        return f"<User {self.email}>"


class Player(db.Model):
    __bind_key__ = 'tournaments'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150))
    age = db.Column(db.Integer, nullable=False)
    ranking = db.Column(db.Integer, nullable=False, default=0)
    gender = db.Column(db.String(1), default='O')  # O = Open, K = Kobiety, M = Mężczyźni

    participants = db.relationship('TournamentParticipant', back_populates='player', cascade='all, delete-orphan')

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"<Player {self.full_name()}>"


class Tournament(db.Model):
    __bind_key__ = 'tournaments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(50), default='Open')
    selection_mode = db.Column(db.String(20), default='all')  # all | selected
    pairing_method = db.Column(db.String(20), default='ranking')  # name | age | ranking
    status = db.Column(db.String(20), default='not_started')  # not_started | in_progress | finished
    current_round = db.Column(db.Integer, default=0)

    participants = db.relationship('TournamentParticipant', back_populates='tournament', cascade='all, delete-orphan')
    rounds = db.relationship('Round', back_populates='tournament', cascade='all, delete-orphan', order_by='Round.number')

    def __repr__(self):
        return f"<Tournament {self.name} ({self.status})>"


class TournamentParticipant(db.Model):
    __bind_key__ = 'tournaments'

    id = db.Column(db.Integer, primary_key=True)
    tournament_id = db.Column(db.Integer, db.ForeignKey('tournament.id'), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    tournament = db.relationship('Tournament', back_populates='participants')
    player = db.relationship('Player', back_populates='participants')

    def __repr__(self):
        return f"<TournamentParticipant t={self.tournament_id} p={self.player_id} active={self.is_active}>"


class Round(db.Model):
    __bind_key__ = 'tournaments'

    id = db.Column(db.Integer, primary_key=True)
    tournament_id = db.Column(db.Integer, db.ForeignKey('tournament.id'), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending | completed

    tournament = db.relationship('Tournament', back_populates='rounds')
    matches = db.relationship('Match', back_populates='round', cascade='all, delete-orphan', order_by='Match.board_number')

    def __repr__(self):
        return f"<Round {self.number} t={self.tournament_id} {self.status}>"


class Match(db.Model):
    __bind_key__ = 'tournaments'

    id = db.Column(db.Integer, primary_key=True)
    round_id = db.Column(db.Integer, db.ForeignKey('round.id'), nullable=False)
    board_number = db.Column(db.Integer, nullable=False)
    white_player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    black_player_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    result = db.Column(db.String(20), default='pending')  # pending | white | black | bye

    round = db.relationship('Round', back_populates='matches')
    white_player = db.relationship('Player', foreign_keys=[white_player_id])
    black_player = db.relationship('Player', foreign_keys=[black_player_id])

    @property
    def winner_id(self):
        if self.result == 'white':
            return self.white_player_id
        if self.result == 'black':
            return self.black_player_id
        if self.result == 'bye':
            return self.white_player_id
        return None

    def __repr__(self):
        return f"<Match r={self.round_id} b={self.board_number} result={self.result}>"