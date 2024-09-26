from flask import (
    Blueprint,
    render_template,
    redirect,
    request,
)

from flask_login import current_user, login_required
from funlab import models
from .. import forms

module = Blueprint("course", __name__, url_prefix="/course")
@module.route("/", methods=["GET", "POST"])
def index():
    course = models.Course.objects()
    return render_template("/course/index.html", course=course)