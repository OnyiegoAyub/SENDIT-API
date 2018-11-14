# virt# where you create blueprint for v1
# # handles everything for models and views
#
# from flask_restful import Api
# from flask import Blueprint
#
# from .views.parcel_order import SingleOrder, AllOrders, CancelOrder, CreateOrders, UserOrders
# from .views.user_auth import SingleUser, AllUsers, CreateUsers
#
#
# # version the app using Blueprint
# blueprint_version1 = Blueprint('apiv1', __name__, url_prefix='/api/v1')
#
# api = Api(blueprint_version1)
#
# # api end points
# api.add_resource(AllOrders, "/parcels")
# api.add_resource(CreateOrders, "/parcels")
# api.add_resource(SingleOrder, "/parcels/<int:parcel_id>")
# api.add_resource(UserOrders, "/users/<int:user_id>/parcels")
# api.add_resource(CancelOrder, "/parcels/<int:parcel_id>/cancel")
# api.add_resource(SingleUser, "/users/<int:user_id>")
# api.add_resource(AllUsers, "/users")
# api.add_resource(CreateUsers, "/users")
