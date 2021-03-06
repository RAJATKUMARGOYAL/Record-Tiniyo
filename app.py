from flask import Flask
from tiniyo.voice_response import VoiceResponse
from xmlhelp import tiniyoml


app = Flask(__name__)


@app.route('/voicecall-record/tiniyo', methods=['GET', 'POST'])
def record():
    response = VoiceResponse()
    response.record(
        record="record-from-tiniyo",
        recording_status_callback="https://ensh0ghfhpwu.x.pipedream.net/",
        recording_status_callback_event='complete',
        max_length='10',
        playBeep="false",
        timeout='5'
    )
    return tiniyoml(response)


if __name__ == '__main__':
    app.run()
