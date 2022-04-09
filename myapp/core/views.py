from flask import render_template, request, Blueprint
from myapp.models import Note

core = Blueprint('core', __name__)

@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    notes = Note.query.order_by(Note.date.desc()).paginate(page=page, per_page=5)
    return render_template('index.html', notes=notes)

@core.route('/info')
def info():
    return render_template('info.html')