from flask import Flask
from flask import Blueprint
from pymongo import MongoClient

from Routers.DreamRouter import DreamRouter
from Routers.DiaryRouter import DiaryRouter

from Controllers.Dreams import DreamsController
from Controllers.Diaries import DiariesController

from Models.Job import JobsModel
from Models.Dream import DreamsModel
from Models.Diary import DiaryModel


DREAMBP = "/dream"
DIARYBP = "/dream"
HOST = "0.0.0.0"
MONGOHOST = "localhost"
MONGOPORT = 27017


if __name__ == "__main__":
    # Запуск серверного приложения
    print("STARTING AN APPLICATION")
    app = Flask(__name__)

    # Создают раутинг
    bp_dream = Blueprint(DREAMBP, __name__)
    bp_diary = Blueprint(DIARYBP, __name__)
    router_dream = DreamRouter(bp_dream)
    router_diary = DiaryRouter(bp_diary)

    # Подключаем базу данных
    print("Начинаем инициализировать базу данных")
    client = MongoClient(MONGOHOST, MONGOPORT)
    db = client.db

    # TODO
    userid = 1

    # Контролеры
    dream_model = DreamsModel(client, userid)
    job_model = JobsModel(client, userid)
    diary_model = DiaryModel(client, userid)

    dream_controller = DreamsController(dream_model, job_model)
    diary_controller = DiariesController(diary_model)

    # Прописываем контролерам раутинг
    router_dream.route_dreams(dream_controller)
    router_diary.route_diary(diary_controller)
    app.register_blueprint(bp_dream, url_prefix=DREAMBP)
    app.register_blueprint(bp_diary, url_prefix=DIARYBP)

    print("Раутинг был закреплен со схемой")
    print(app.url_map)

    print("Инициализируем запуск")
    app.run(host="0.0.0.0")