

class DiaryRouter:
    def __init__(self, bp):
        self.bp = bp

    def route_diary(self, controller):
        self.bp.route("/", methods=["GET"])(controller.get)
        self.bp.route("/", methods=["POST"])(controller.store)
        self.bp.route("/<int: dreamid>/job/<int: jobid>", methods=["POST"])(controller.get)
        self.bp.route("/<int: dreamid>/job/<int: jobid>", methods=["UPDATE"])(controller.get)
        self.bp.route("/<int: dreamid>/job/<int: jobid>", methods=["DELETE"])(controller.get)
