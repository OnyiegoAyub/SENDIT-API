

class Parcel:
    """Create parcel class"""
    users = []
    parcels = []

    def create(self, origin, destination, weight, status):
        """Create new parcel delivery order"""
        parcel = {"user_id": len(Parcel.parcels) + 1,
                  "origin": origin, "parcel_id": len(Parcel.parcels) + 1,
                  "destination": destination,
                  "weight": weight,
                  "status": status}
        Parcel.parcels.append(parcel)
        return parcel

    def get_all(self):
        """method calling all parcels"""
        return Parcel.parcels

    def get_one(self, parcel_id):
        """method calling single parcel"""
        for parcel in Parcel.parcels:
            if parcel["parcel_id"] == parcel_id:
                return parcel

            return False

    def cancel_parcel_order(self, parcel_id):
        """method cancelling a parcel order"""
        for parcel in Parcel.parcels:
            if parcel["parcel_id"] == parcel_id:
                parcel['status'] == "Cancelled"
                return parcel
            return False

    def get_order_by_user(self, user_id):
        """method for getting a user's parcel order"""
        for user in Parcel.parcels:
            if user["user_id"] == user_id:
                return user
            return False
