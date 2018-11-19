from flask import Flask, jsonify, make_response, request, abort
from flask_restful import Resource

from ..models.parcel_order_models import Parcel


class AllOrders(Resource, Parcel):
    """create a  calss AllOrders """
    def get(self):
        """gets all orders"""
        orders = self.get_all()
        return make_response(jsonify(
            {"message": "All orders made", "orders": orders, "status": "okay"}), 200)

class CreateOrders(Resource, Parcel):
    """create a  calss CreateOrders """
    def post(self):
        """posts an order"""
        data = request.get_json() or {}
        order = self.create(
            origin=data['origin'],
            destination=data['destination'],
            weight=data['weight'],
            status=data['status']
        )

        return make_response(jsonify(
            {"message": "Order created"}), 201)


class SingleOrder(Resource, Parcel):
    '''single delivery order API'''

    def get(self, parcel_id):
        """find an order by order_id and assign it destination one_order"""
        one_order = self.get_one(parcel_id)
        if one_order is not False:
            return make_response(jsonify(
                {"status": "ok", "order": one_order}), 200)
        return make_response(jsonify(
            {"status": " Order not found"}), 404)


class CancelOrder(Resource, Parcel):
    """This class cancels an order"""

    def put(self, parcel_id):
        """
        Updates the status of a parcel order destination canceled
        """
        change = self.cancel_parcel_order(parcel_id)

        if change is not False:
            return make_response(jsonify(
                {"Message": " cancelled successfully", "Order": change, "status": "Accepted"}), 202)

        return make_response(jsonify(
            {"Message": "The order requested does not exist",
             "status": " Order to be cancelled not found"}), 404)

class UserOrders(Resource, Parcel):
    """create a  calss UserOrders """
    def get(self, user_id):
        """
        Gets a user's orders by searching their user_id in the list of orders made
        """
        user_order = self.get_order_by_user(user_id)
        if user_order is not False:
            return make_response(jsonify({"status": "ok", "order": user_order}), 200)
        return make_response(jsonify(
            {"status": "Uer order requested not found"}), 404)
