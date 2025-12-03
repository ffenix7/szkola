from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bs4 import Bootstrap
import secrets
from extensions import db
from db import Task
import os

def create_app():
    #app config
    app = Flask(__name__)
    Bootstrap(app)

    app.config['SECRET_KEY'] = secrets.token_urlsafe(16)

    #db config
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DATA_DIR = os.path.join(BASE_DIR, 'data')
    os.makedirs(DATA_DIR, exist_ok=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(DATA_DIR, 'tasks.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #extensions init
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Routes
    @app.route('/')
    def index():
        tasks = Task.query.all()
        tasks.sort(key=lambda t: (t.created_at), reverse=True)
        completed_tasks = sum(1 for task in tasks if task.completed)
        completion_rate = round((completed_tasks / len(tasks) * 100) if tasks else 0)
        return render_template('index.html', tasks=tasks, total_tasks=len(tasks), completed_tasks=completed_tasks, completion_rate=completion_rate)

    @app.route('/add', methods=['GET', 'POST'])
    def add_task():
        if request.method == 'POST':
            title = request.form.get('title', '').strip()
            description = request.form.get('description', '').strip()
            priority = request.form.get('priority', 'średni')

            if not title:
                flash('Tytuł zadania nie może być pusty!', 'danger')
                return redirect(url_for('add_task'))

            if priority not in ['niski', 'średni', 'wysoki']:
                priority = 'średni'

            task = Task(title=title, description=description, priority=priority)
            db.session.add(task)
            db.session.commit()

            flash(f'Zadanie "{title}" zostało dodane!', 'success')
            return redirect(url_for('index'))

        return render_template('add_task.html')

    @app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
    def edit_task(task_id):
        task = Task.query.get_or_404(task_id)

        if request.method == 'POST':
            title = request.form.get('title', '').strip()
            description = request.form.get('description', '').strip()
            priority = request.form.get('priority', 'średni')

            if not title:
                flash('Tytuł zadania nie może być pusty!', 'danger')
                return redirect(url_for('edit_task', task_id=task_id))

            if priority not in ['niski', 'średni', 'wysoki']:
                priority = 'średni'

            task.title = title
            task.description = description
            task.priority = priority

            db.session.commit()
            flash(f'Zadanie "{title}" zostało zaktualizowane!', 'success')
            return redirect(url_for('index'))

        return render_template('edit_task.html', task=task)

    @app.route('/delete/<int:task_id>')
    def delete_task(task_id):
        task = Task.query.get_or_404(task_id)
        title = task.title
        db.session.delete(task)
        db.session.commit()

        flash(f'Zadanie "{title}" zostało usunięte!', 'danger')
        return redirect(url_for('index'))

    @app.route('/toggle/<int:task_id>')
    def toggle_task(task_id):
        task = Task.query.get_or_404(task_id)
        task.completed = not task.completed
        db.session.commit()

        status = 'ukończone' if task.completed else 'nieukończone'
        flash(f'Zadanie "{task.title}" oznaczone jako {status}!', 'success')
        return redirect(url_for('index'))

    return app

if __name__ == '__main__':
    app = create_app()
    
    with app.app_context():
        db.create_all()
    app.run(debug=True)