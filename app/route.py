from celery.result import AsyncResult
from flask import jsonify, render_template, request

from app.app import app
from app.task import *


@app.route('/')
def home():
    return "Welcome to Report Service"

@app.route('/health')
def health():
    return jsonify({"state":"healthy"})

@app.route('/report',methods=["POST"])
def report_generator():
    async_result = report.delay()
    return jsonify({"report_id":async_result.id})

@app.route('/report/<report_id>')
def get_report(report_id):
    res = AsyncResult(report_id,app=celery)
    return jsonify({"id":res.id,"result":res.result,"state":res.state})
