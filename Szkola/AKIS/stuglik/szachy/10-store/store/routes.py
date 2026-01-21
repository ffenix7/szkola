from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required

from extentions import db
from models import Player, Tournament, TournamentParticipant, Round, Match
from . import store_bp
from .forms import TournamentForm, PlayerForm, ParticipantSelectionForm


def _sort_players(players, pairing_method):
    if pairing_method == 'age':
        return sorted(players, key=lambda p: (p.age, p.last_name, p.first_name))
    if pairing_method == 'ranking':
        return sorted(players, key=lambda p: (-p.ranking, p.last_name, p.first_name))
    return sorted(players, key=lambda p: (p.last_name, p.first_name))


def _set_selection_choices(form):
    players = Player.query.order_by(Player.last_name, Player.first_name).all()
    form.player_ids.choices = [(p.id, f"{p.last_name} {p.first_name} ({p.ranking})") for p in players]
    return players


def _create_round_matches(round_obj, player_ids, pairing_method):
    if not player_ids:
        return []
    players = Player.query.filter(Player.id.in_(player_ids)).all()
    ordered = _sort_players(players, pairing_method)
    matches = []
    board_no = 1
    for idx in range(0, len(ordered), 2):
        white = ordered[idx]
        black = ordered[idx + 1] if idx + 1 < len(ordered) else None
        result = 'bye' if black is None else 'pending'
        match = Match(
            round=round_obj,
            board_number=board_no,
            white_player_id=white.id,
            black_player_id=black.id if black else None,
            result=result
        )
        matches.append(match)
        board_no += 1
    db.session.add_all(matches)
    return matches


def _refresh_active_participants(tournament, winners):
    winner_set = set(winners)
    for participant in tournament.participants:
        participant.is_active = participant.player_id in winner_set


def _clear_rounds(tournament):
    for round_obj in list(tournament.rounds):
        db.session.delete(round_obj)


def _replace_participants(tournament, player_ids):
    for participant in list(tournament.participants):
        db.session.delete(participant)
    for pid in player_ids:
        db.session.add(TournamentParticipant(tournament_id=tournament.id, player_id=pid, is_active=True))


@store_bp.route('/')
@login_required
def index():
    tournaments = Tournament.query.order_by(Tournament.id.desc()).all()
    players = Player.query.order_by(Player.last_name, Player.first_name).all()
    create_form = TournamentForm()
    player_form = PlayerForm()
    return render_template(
        'store/index.html',
        title='Turnieje szachowe',
        tournaments=tournaments,
        players=players,
        create_form=create_form,
        player_form=player_form
    )


@store_bp.route('/create', methods=['POST'])
@login_required
def create_tournament():
    form = TournamentForm()
    if form.validate_on_submit():
        tournament = Tournament(
            name=form.name.data,
            category=form.category.data,
            selection_mode=form.selection_mode.data,
            pairing_method=form.pairing_method.data,
            status='not_started'
        )
        db.session.add(tournament)
        db.session.commit()
        flash('Turniej został utworzony.', 'success')
        return redirect(url_for('tournaments.detail', tournament_id=tournament.id))
    flash('Nie udało się utworzyć turnieju. Sprawdź dane.', 'danger')
    return redirect(url_for('tournaments.index'))


@store_bp.route('/players', methods=['POST'])
@login_required
def add_player():
    form = PlayerForm()
    if form.validate_on_submit():
        player = Player(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            age=form.age.data,
            ranking=form.ranking.data,
            gender=form.gender.data
        )
        db.session.add(player)
        db.session.commit()
        flash('Dodano zawodnika do puli.', 'success')
    else:
        flash('Nie udało się dodać zawodnika. Sprawdź dane.', 'danger')
    return redirect(request.referrer or url_for('tournaments.index'))


@store_bp.route('/<int:tournament_id>', methods=['GET', 'POST'])
@login_required
def detail(tournament_id):
    tournament = Tournament.query.get_or_404(tournament_id)
    selection_form = ParticipantSelectionForm()
    players = _set_selection_choices(selection_form)
    selection_form.player_ids.data = [p.player_id for p in tournament.participants if p.is_active]
    player_form = PlayerForm()
    edit_form = TournamentForm(obj=tournament)

    if player_form.validate_on_submit():
        player = Player(
            first_name=player_form.first_name.data,
            last_name=player_form.last_name.data,
            email=player_form.email.data,
            age=player_form.age.data,
            ranking=player_form.ranking.data,
            gender=player_form.gender.data
        )
        db.session.add(player)
        db.session.commit()
        # Add to tournament
        participant = TournamentParticipant(tournament_id=tournament.id, player_id=player.id, is_active=True)
        db.session.add(participant)
        db.session.commit()
        flash('Zawodnik dodany do turnieju!', 'success')
        return redirect(url_for('tournaments.detail', tournament_id=tournament.id))

    return render_template(
        'store/detail.html',
        title=f'Turniej {tournament.name}',
        tournament=tournament,
        selection_form=selection_form,
        players=players,
        player_form=player_form,
        edit_form=edit_form
    )


@store_bp.route('/<int:tournament_id>/participants', methods=['POST'])
@login_required
def update_participants(tournament_id):
    tournament = Tournament.query.get_or_404(tournament_id)
    form = ParticipantSelectionForm()
    players = _set_selection_choices(form)
    chosen_ids = []
    if tournament.selection_mode == 'all':
        chosen_ids = [p.id for p in players]
    elif form.validate_on_submit():
        chosen_ids = form.player_ids.data
    else:
        flash('Nie wybrano uczestników.', 'warning')
        return redirect(url_for('tournaments.detail', tournament_id=tournament.id))

    _replace_participants(tournament, chosen_ids)

    tournament.status = 'not_started'
    tournament.current_round = 0
    _clear_rounds(tournament)
    db.session.commit()
    flash('Zaktualizowano listę uczestników.', 'success')
    return redirect(url_for('tournaments.detail', tournament_id=tournament.id))


@store_bp.route('/<int:tournament_id>/start', methods=['POST'])
@login_required
def start_tournament(tournament_id):
    tournament = Tournament.query.get_or_404(tournament_id)
    if tournament.selection_mode == 'all':
        all_players = Player.query.order_by(Player.last_name, Player.first_name).all()
        _replace_participants(tournament, [p.id for p in all_players])
        db.session.flush()
    active_ids = [p.player_id for p in tournament.participants]
    if len(active_ids) < 2:
        flash('Potrzeba co najmniej dwóch uczestników, aby rozpocząć turniej.', 'warning')
        return redirect(url_for('tournaments.detail', tournament_id=tournament.id))

    _clear_rounds(tournament)

    round_obj = Round(tournament_id=tournament.id, number=1, status='pending')
    db.session.add(round_obj)
    db.session.flush()
    _create_round_matches(round_obj, active_ids, tournament.pairing_method)

    tournament.status = 'in_progress'
    tournament.current_round = 1
    db.session.commit()
    flash('Rozpoczęto turniej i wygenerowano rundę 1.', 'success')
    return redirect(url_for('tournaments.detail', tournament_id=tournament.id))


@store_bp.route('/<int:tournament_id>/round/<int:round_id>/results', methods=['POST'])
@login_required
def submit_results(tournament_id, round_id):
    round_obj = Round.query.get_or_404(round_id)
    if round_obj.tournament_id != tournament_id:
        flash('Nie znaleziono takiej rundy w tym turnieju.', 'danger')
        return redirect(url_for('tournaments.detail', tournament_id=tournament_id))
    tournament = round_obj.tournament
    winners = []

    for match in round_obj.matches:
        if match.result == 'bye':
            winners.append(match.white_player_id)
            continue
        field_name = f"result_{match.id}"
        result_value = request.form.get(field_name)
        if result_value not in ['white', 'black']:
            flash('Uzupełnij wyniki wszystkich partii.', 'warning')
            return redirect(url_for('tournaments.detail', tournament_id=tournament.id))
        match.result = result_value
        winners.append(match.white_player_id if result_value == 'white' else match.black_player_id)

    round_obj.status = 'completed'
    _refresh_active_participants(tournament, winners)

    if len(winners) > 1:
        next_round = Round(tournament_id=tournament.id, number=round_obj.number + 1, status='pending')
        db.session.add(next_round)
        db.session.flush()
        _create_round_matches(next_round, winners, tournament.pairing_method)
        tournament.status = 'in_progress'
        tournament.current_round = next_round.number
    else:
        tournament.status = 'finished'
        tournament.current_round = round_obj.number

    db.session.commit()
    flash('Zapisano wyniki rundy.', 'success')
    return redirect(url_for('tournaments.detail', tournament_id=tournament.id))


@store_bp.route('/<int:tournament_id>/edit', methods=['POST'])
@login_required
def edit_tournament(tournament_id):
    tournament = Tournament.query.get_or_404(tournament_id)
    form = TournamentForm()
    if form.validate_on_submit():
        tournament.name = form.name.data
        tournament.category = form.category.data
        tournament.selection_mode = form.selection_mode.data
        tournament.pairing_method = form.pairing_method.data
        db.session.commit()
        flash('Zapisano zmiany turnieju.', 'success')
    else:
        flash('Nie udało się zapisać zmian turnieju.', 'danger')
    return redirect(url_for('tournaments.detail', tournament_id=tournament.id))


@store_bp.route('/<int:tournament_id>/delete', methods=['POST'])
@login_required
def delete_tournament(tournament_id):
    tournament = Tournament.query.get_or_404(tournament_id)
    db.session.delete(tournament)
    db.session.commit()
    flash('Turniej został usunięty.', 'info')
    return redirect(url_for('tournaments.index'))