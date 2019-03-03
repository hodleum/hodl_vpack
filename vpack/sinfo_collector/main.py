from flask import Flask
from flask_restplus import Resource, Api
from psutil import *

app = Flask(__name__)
api = Api(app)


@api.route('/sys/space')
class SysHDD(Resource):
    @api.doc(responses={200: 'Successfully gathered information'})
    def get(self):
        """Getter of HDD Space:
        Returns JSON: {'code':int-code, 'data':{'percentage':<float>, 'sav': <int>, 'sfi': <int>}

        if dsk.percent <= 95:
            code = 0
        else:
            code = 1

        """
        dsk = disk_usage("/")
        if dsk.percent <= 95:
            dco = 0
        else:
            dco = 1

        return {"code": dco, "data": {"percentage": dsk.percent, "sav": dsk.free, "sfi": dsk.used}}


@api.route('/sys/sclist')
class ScList(Resource):
    @api.doc(responces={200: "OK", 598: "SCList is empty", 500: "SCList cannot be collected."})
    def get(self):
        """
        Returns JSON: {'code':<if not users: return 0 | else return 1>, "data": {"ulist":<list of users>}}
        """

if __name__ == '__main__':
    app.run(debug=True)
