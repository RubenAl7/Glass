from flask import Blueprint

from services.lentes import create_lente_service, get_lentes_service, get_lente_service, update_lente_service, delete_lente_service

lente = Blueprint('lente',__name__)

@lente.route('/', methods = ['GET'])
def get_lentes():
    return get_lentes_service()

@lente.route('/<id>', methods = ['GET'])
def get_vaccine(id):
    return get_lente_service(id)


@lente.route('/', methods = ['POST'])
def create_vaccine():
    return create_lente_service()


@lente.route('/<id>', methods = ['PUT'])
def update_vaccine(id):
    return update_lente_service(id)


@lente.route('/<id>', methods = ['DELETE'])
def delete_vaccine(id):
    return delete_lente_service(id)