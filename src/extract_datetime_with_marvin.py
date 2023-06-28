from marvin import ai_model
import pydantic
from typing import Optional
import json


@ai_model
class  YearMonthDayHourMinuteNotation(pydantic.BaseModel):
    year: int
    month: int
    day: int
    hour: int
    minute: int



chat_history = 'Userは自分のメールアドレスを教え、長期的な関係を求めている旨を伝えます。初回の会合に2万円を預かりたいと要求し、その後は対等に折半することを提案します。Agentはそれに同意し、名古屋駅周辺での待ち合わせを提案します。Userは6月16日の午後2時に矢場町公園で会うことを提案し、Agentはそれに同意します。'


res = YearMonthDayHourMinuteNotation(chat_history).json(indent = 2)

import pdb;pdb.set_trace()

json.loads(res)
print(res)
