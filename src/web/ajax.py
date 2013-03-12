# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from datetime import datetime
import json
from zen.dataprocess.filters import brdate


def index(resp,texto):
    data=datetime.now()
    dct={"data":brdate(data),
         "texto":"resp: "+texto}
    js=json.dumps(dct)
    resp.write(js)

