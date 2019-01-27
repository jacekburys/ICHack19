from flask import jsonify, request

from . import api
from ..models.myendpoint import Myendpoint
from ..schemas.myendpoint import myendpoint_schema, myendpoints_schema


@api.route('/myendpoints', methods=['GET'])
def get_myendpoints():
    pass


@api.route('/myendpoints/<int:id>', methods=['GET'])
def get_myendpoint(id):
    pass
