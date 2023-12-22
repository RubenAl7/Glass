from flask import request, Response
from bson import json_util, ObjectId
from config.mongodb import mongo

'''Registro de lentes'''
def create_lente_service():
    data = request.get_json()
    registro = data.get("registro", None)
    modelo = data.get("modelo")
    fecha = data.get("fecha", None)
    if registro:
        Response = mongo.db.lentes.insert_one(
            {
                "registro": registro, 
                "modelo": modelo, 
                "fecha": fecha
            }
        )
        result = {
            "id": str(Response.inserted_id),
            "registro":registro,
            "modelo": modelo,
            "fecha": fecha,
            "status":False,
        }
        return result
    else:
        return "Invalid payload", 400 



'''Obtiene los lente'''
def get_lente_service(id):
    data = mongo.db.lentes.find()
    result = json_util.dumps(data)
    return Response(result, mimetype="application/json")

'''Obtienene un lente'''
def get_lente(id):
    data = mongo.db.lentes.fin_one({"_id":ObjectId(id)})
    result = json_util.dumps(data)
    return Response(result, mimetype="application/json")

'''Actualizacion de lente'''
def update_lente(id):
    data = request.get_json()
    if len(data) == 0:
        return "No hay datos para actualizar", 400

    response = mongo.db.lentes.update_one({"_id": ObjectId(id)}, {"$set": data})

    if response.modified_count >= 1:
        return "El lente ha sido actualizado correctamente", 200
    else:
        return "El lente no fue encontrado", 404

'''Eliminar un lente'''
def delete_lente(id):
    response = mongo.db.lentes.delete_one({"_id": ObjectId(id)})
    if response.deleted_count >= 1:
        return "El lente ha sido eliminado correctamente", 200
    else:
        return "El lente no fue encontrado", 404