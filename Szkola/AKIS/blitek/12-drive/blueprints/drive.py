from flask import Blueprint, render_template, request, redirect, url_for, abort, flash
from flask_login import login_required, current_user
from extensions import db
from models import User, Folder

drive_bp = Blueprint('drive', __name__)

def get_folder_or_404(folder_id):
    if folder_id is None:
        return None
    folder = db.session.query(Folder).filter_by(id=folder_id, owner_id=current_user.id).first()
    if folder is None:
        abort(404)
    return folder

@drive_bp.get('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('drive.dashboard'))
    return redirect(url_for('auth.login_get'))

@drive_bp.get('/dashboard')
@login_required
def dashboard():
    folderid = request.args.get('folderid', type=int)
    current_folder = get_folder_or_404(folderid)
    parent_id = current_folder.id if current_folder else None
    folders = Folder.query.filter_by(owner_id=current_user.id, parent_id=parent_id).all()
    return render_template(
        'dashboard.html',
        user=current_user,
        title='Dashboard',
        current_folder=current_folder,
        folders=folders
    )

@drive_bp.post('/folders')
@login_required
def create_folder():
    parent = request.form.get('parent', type=int)
    name = (request.form.get('name') or '').strip()

    if not name:
        flash('Nazwa folderu nie może być pusta.', 'danger')
        return redirect(url_for('drive.dashboard', folderid=parent))

    new_folder = Folder(name=name, owner_id=current_user.id, parent_id=parent)
    db.session.add(new_folder)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        flash('Wystąpił błąd podczas tworzenia folderu. Upewnij się, że nazwa jest unikalna w tym katalogu.', 'danger')
        return redirect(url_for('drive.dashboard', folderid=parent))
    
    flash('Folder został utworzony.', 'success')
    return redirect(url_for('drive.dashboard', folderid=parent))
