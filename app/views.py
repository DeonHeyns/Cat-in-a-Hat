import StringIO
import csv
import string
import random
import json

from flask import render_template, make_response
from app import app
from forms import PointsInRadiusForm
import geo


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    form = PointsInRadiusForm()
    app.logger.info('serving up the homepage')
    return render_template('index.html', form=form)


@app.route('/points', methods=['GET', 'POST'])
def points():
    form = PointsInRadiusForm()
    if form.validate_on_submit():
        app.logger.info('user submitted: Latitude: {0}, Longitude: {1}, Radius: {2}, Number of Points: {3}'
                        .format(form.latitude.data, form.longitude.data, form.radius.data, form.num_of_points.data))
        res = geo.points_on_a_radius(form.latitude.data, form.longitude.data, form.radius.data, form.num_of_points.data)
        app.logger.info('obtained results')
        app.logger.info('writing to csv')
        si = StringIO.StringIO()
        cw = csv.writer(si)
        cw.writerow(['longitude', 'latitude'])
        cw.writerows(res)
        output = make_response(si.getvalue())
        output.headers["Content-Disposition"] = "attachment; filename=%s" % name_generator()
        output.headers["Content-type"] = "text/csv"
        output.headers["Location"] = "/"
        app.logger.info('returning the results')
        return output


@app.route('/raw-points/<latitude>/<longitude>/<radius>/<points>')
def raw_points(latitude, longitude, radius, points):
    res = geo.points_on_a_radius(float(latitude), float(longitude), float(radius), int(points))
    p = [Point(x[0], x[1]).__dict__ for x in res]
    p = json.dumps(p)
    output = make_response(p)
    output.headers["Content-type"] = "application/json"
    return output


def name_generator():
    name = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(10)) + '.csv'
    return name


class Point(object):
    def __init__(self, lon, lat):
        self.lat = lat
        self.lon = lon