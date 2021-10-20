import tornado.web
import os
from tornado.options import define, options
from model.models import Array

define("port", default=8888, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            # example: GET http://127.0.0.1:8888/array/id:1
            (r'/array/id:(\d*)', ArrayGet),
            # example: POST http://127.0.0.1:8888/array/array:[11,9,1,5,2,13,4,24,5,9,8]
            (r'/array/array:\[([\d|,]*)\]', ArrayPost),
        ]
        settings = dict(
            title=u"Array Handler",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=False,
            debug=True,
        )
        super(Application, self).__init__(handlers, **settings)


class ArrayGet(tornado.web.RequestHandler):
    async def get(self, id):
        try:
            array = Array.get_by_id(self, int(id))

            response = {"id": array.id,
                        "array": array.array,
                        "result_array": array.result_array,
                        "date_of_creation": array.date_of_creation.strftime("%m/%d/%Y, %H:%M:%S")}
            self.write(response)
        except AttributeError as e:
            print(e)
            response = {"result": "ERROR"}
            self.write(response)


class ArrayPost(tornado.web.RequestHandler):
    async def post(self, array):
        try:
            list_array = [int(x) for x in array.split(",")]
            sorted_array = sorted(list_array)

            new_array = Array.save(self, list_array, sorted_array)

            response = {"result": "OK",
                        "id": str(new_array.id)}
            self.write(response)
        except Exception as e:
            print(e)
            response = {"result": "ERROR"}
            self.write(response)


if __name__ == "__main__":
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
