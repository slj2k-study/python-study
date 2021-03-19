import json
from flask import Flask, request, make_response
from datetime import datetime
import time
import pytz
import requests

def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-974853239138-1873692512450-PMPTmlDdZTxmi6NFgw6zHSsz"

app = Flask(__name__)

def get_datetime(weekday=None):
    asia_seoul = datetime.fromtimestamp(time.time(), pytz.timezone('Asia/Seoul'))
    t = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']

    if weekday is None:
        fmt = "%Y-%m-%d %H:%M:%S"
        s = asia_seoul.strftime(fmt)
        return s
    else:
        return t[asia_seoul.today().weekday()]


def get_answer(user_query):
    with open('searchlog.log', 'a') as f:  # 유저 검색어는 로그로 저장, 시간 / 검색어만 저장
        f.write(str(get_datetime())+','+user_query+'\n')

    raw_user_query = user_query
    user_query = raw_user_query.replace(" ", "")

    answer_dict = {
        'hello': 'hi there',
        '요일': 'Asia/Seoul 현재 ' + str(get_datetime()) + '입니다. 오늘은 ' + str(get_datetime('weekday')) + '입니다.',
        '전화번호': '\n회사 번호 :  02-000-000. \n 고객 콜센터: 080-1544-0000',
    }

    if user_query == '' or None:
        return "앗.. 아무것도 안쓰셨거나.. 혹은 아직 해석 불가 글자에요. 아직 그정도로 똑똑하진 않아요."
    elif user_query in answer_dict.keys():  # 결과 있으면 리턴
        return answer_dict[user_query]
    else:

        for now_key in answer_dict.keys():  # 키에서 먼저 찾고
            if now_key.find(user_query) != -1:
                return "연관 단어인 '" + now_key + "'에 대한 답변입니다.\n" + now_key + ' : ' + answer_dict[now_key]

        for now_key in answer_dict.keys():  # 키가 없으면 본문에 검색
            if answer_dict[now_key].find(raw_user_query[1:]) != -1:
                return "관련이 있나 모르겠지만 답변 내용에" + answer_dict[now_key] + '가 있네요.\n' + now_key + '에 대한 답변이에요.'

    return user_query + "은(는) 없는 질문입니다."


def event_handler(event_type, slack_event):
    channel = slack_event["event"]["channel"]
    string_slack_event = str(slack_event)
    if string_slack_event.find("{'type': 'user', 'user_id': ") != -1:  # 멘션으로 호출
        try:
            user_query = slack_event['event']['blocks'][0]['elements'][0]['elements'][1]['text']
            answer = get_answer(user_query)
            post_message(myToken, channel, answer)
            return make_response("ok", 200, )
        except IndexError:
            pass
    elif string_slack_event.find("'channel_type': 'im'") != -1:  # 다이렉트로 호출
        try:
            if slack_event['event']['client_msg_id']:
                user_query = slack_event['event']['text']
                answer = get_answer(user_query)
                post_message(myToken, channel, answer)
                return make_response("ok", 200, )
        except IndexError:
            pass
        except KeyError:
            pass

    message = "[%s] cannot find event handler" % event_type
    return make_response(message, 200, {"X-Slack-No-Retry": 1})


@app.route('/', methods=['POST'])
def hello_there():
    slack_event = json.loads(request.data)
    if "challenge" in slack_event:
        return make_response(slack_event["challenge"], 200, {"content_type": "application/json"})
    if "event" in slack_event:
        event_type = slack_event["event"]["type"]
        return event_handler(event_type, slack_event)
    return make_response("There are no slack request events", 404, {"X-Slack-No-Retry": 1})


if __name__ == '__main__':
    app.run(debug=True)