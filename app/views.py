from flask import render_template, flash, redirect, make_response
from app import app
from forms import PointsInRadiusForm
import geo
import StringIO
import csv
import string, random


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = PointsInRadiusForm()
    if form.validate_on_submit():
        res = geo.points_on_a_radius(form.latitude.data, form.longitude.data, form.radius.data, form.num_of_points.data)
        si = StringIO.StringIO()
        cw = csv.writer(si, )
        cw.writerow(['longitude', 'latitude'])
        cw.writerows(res)
        output = make_response(si.getvalue())
        output.headers["Content-Disposition"] = "attachment; filename=%s" % name_generator()
        output.headers["Content-type"] = "text/csv"
        output.headers["Location"] = "/"
        return output
    return render_template('index.html', form=form)


def name_generator():
    name = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(10)) + '.csv'
    return name