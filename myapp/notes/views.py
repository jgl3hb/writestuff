from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import Note
from myapp.notes.forms import NoteForm

notes = Blueprint('notes', __name__)

@notes.route('/create', methods=['GET', 'POST'])
@login_required
def create_note():
    form = NoteForm()
    if form.validate_on_submit():
        note = Note(title=form.title.data, text=form.text.data, user_id=current_user.id)
        db.session.add(note)
        db.session.commit()
        flash('Note Created')
        print('Note was created')
        return redirect(url_for('core.index'))
    return render_template('create_note.html', form=form)

    @notes.route('/<int:note_id>')
def note(note_id):
    note = Note.query.get_or_404(note_id) 
    return render_template('note.html', title=note.title, date=note.date, post=note)