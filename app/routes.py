from flask import Blueprint, jsonify, request
from .models import Article
from . import db

api = Blueprint('api', __name__)

@api.route('/articles', methods=['GET'])
def get_articles():
    articles = Article.query.all()
    return jsonify([{"id": article.id, "title": article.title} for article in articles])

@api.route('/articles', methods=['POST'])
def add_article():
    data = request.json
    new_article = Article(title=data['title'])
    db.session.add(new_article)
    db.session.commit()
    return jsonify({"id": new_article.id, "title": new_article.title}), 201
