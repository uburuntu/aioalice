from copy import deepcopy

META = {
    "locale": "ru-RU",
    "timezone": "Europe/Moscow",
    "client_id": "ru.yandex.searchplugin/5.80 (Samsung Galaxy; Android 4.4)"
}

MARKUP = {
    "dangerous_context": True
}

REQUEST = {
    "command": "где поесть",
    "original_utterance": "Алиса где поесть",
    "type": "SimpleUtterance",
    "payload": {}
}

REQUEST_DANGEROUS = deepcopy(REQUEST)
REQUEST_DANGEROUS["markup"] = {
    "dangerous_context": True
}

BASE_SESSION = {
    "message_id": 4,
    "session_id": "2eac4854-fce721f3-b845abba-20d60",
    "user_id": "AC9WC3DF6FCE052E45A4566A48E6B7193774B84814CE49A922E163B8B29881DC"
}

SESSION = deepcopy(BASE_SESSION)
SESSION.update({
    "new": True,
    "skill_id": "3ad36498-f5rd-4079-a14b-788652932056",
})

TTS = "Здравствуйте! Это мы, хоров+одо в+еды."

RESPONSE_BUTTON = {
    "title": "Надпись на кнопке",
    "payload": {},
    "url": "https://responseexample.com/",
    "hide": True
}

RESPONSE = {
    "text": "Здравствуйте! Это мы, хороводоведы.",
    "tts": TTS,
    "buttons": [RESPONSE_BUTTON],
    "end_session": False
}

RESPONSE2 = {
    'text': 'Response Text',
    'buttons': [
        {
            'title': 'Hi!',
            'hide': True
        }
    ],
    'end_session': False
}

ALICE_REQUEST = {
    "meta": {
        "locale": "ru-RU",
        "timezone": "Europe/Moscow",
        "client_id": "ru.yandex.searchplugin/5.80 (Samsung Galaxy; Android 4.4)"
    },
    "request": {
        "command": "где ближайшее отделение",
        "original_utterance": "Алиса спроси у Сбербанка где ближайшее отделение",
        "type": "SimpleUtterance",
        "markup": {
            "dangerous_context": True
        },
        "payload": {}
    },
    "session": SESSION,
    "version": "1.0"
}

ALICE_RESPONSE = {
    "response": {
        "text": "Здравствуйте! Это мы, хороводоведы.",
        "tts": TTS,
        "end_session": False
    },
    "session": BASE_SESSION,
    "session_state": {},
    "user_state_update": {},
    "application_state": {},
    "version": "1.0"
}

ALICE_RESPONSE_WITH_BUTTONS = deepcopy(ALICE_RESPONSE)
ALICE_RESPONSE_WITH_BUTTONS["response"]["buttons"] = [
    {
        "title": "Надпись на кнопке",
        "payload": {},
        "url": "https://example.com/",
        "hide": True
    },
    {
        "title": "Надпись на кнопке1",
        "payload": {'key': 'value'},
        "url": "https://ya.com/",
        "hide": False
    },
]

RESPONSE_TEXT = 'Здравствуйте! Это мы, хороводоведы.'
EXPECTED_RESPONSE = {
    "response": {
        "text": RESPONSE_TEXT,
        "end_session": False
    },
    "session": BASE_SESSION,
    "session_state": {},
    "user_state_update": {},
    "application_state": {},
    "version": "1.0"
}

BUTTON_TEXT = "Надпись на кнопке 3"
URL = 'https://example.com/'
EXPECTED_RESPONSE_WITH_BUTTONS = deepcopy(EXPECTED_RESPONSE)
EXPECTED_RESPONSE_WITH_BUTTONS['response'].update({
    'tts': TTS,
    'buttons': [
        {
            'title': BUTTON_TEXT,
            'url': URL,
            'hide': True
        }
    ]
})

UPLOADED_IMAGE = {
    "id": '1234567890/qwerty',
    "origUrl": 'http://example.com'
}

MB_PAYLOAD = {'mediabutton': True, 'key': 'smth'}
MEDIA_BUTTON = {
    "text": BUTTON_TEXT,
    "url": URL,
    "payload": deepcopy(MB_PAYLOAD)
}

IMAGE_ID = '1027858/46r960da47f60207e924'

IMAGE = {
    "image_id": IMAGE_ID,
    "title": "Заголовок",
    "description": "Описание",
    "button": deepcopy(MEDIA_BUTTON)
}

CARD_HEADER_TEXT = 'Click here to see more'
FOOTER_TEXT = 'Click here to see more'
FOOTER = {
    'text': FOOTER_TEXT,
    'button': deepcopy(MEDIA_BUTTON)
}

CARD_TITLE = 'Заголовок'
CARD_DESCR = 'Описание'

EXPECTED_CARD_BIG_IMAGE_JSON = {
    "type": "BigImage",
    "image_id": IMAGE_ID,
    "title": CARD_TITLE,
    "description": CARD_DESCR,
    "button": deepcopy(MEDIA_BUTTON),
}

EXPECTED_CARD_ITEMS_LIST_JSON = {
    "type": "ItemsList",
    "header": {"text": CARD_HEADER_TEXT},
    "items": [deepcopy(IMAGE)],
    "footer": deepcopy(FOOTER),
}

EXPECTED_ALICE_RESPONSE_BIG_IMAGE_WITH_BUTTON = {
    "response": {
        "text": RESPONSE_TEXT,
        "card": deepcopy(EXPECTED_CARD_BIG_IMAGE_JSON),
        "buttons": [RESPONSE_BUTTON],
        "end_session": False
    },
    "session": BASE_SESSION,
    "session_state": {},
    "user_state_update": {},
    "application_state": {},
    "version": "1.0"
}

EXPECTED_ALICE_RESPONSE_ITEMS_LIST_WITH_BUTTON = {
    "response": {
        "text": RESPONSE_TEXT,
        "card": deepcopy(EXPECTED_CARD_ITEMS_LIST_JSON),
        "buttons": [RESPONSE_BUTTON],
        "end_session": False
    },
    "session": BASE_SESSION,
    "version": "1.0"
}

DATA_FROM_STATION = {
    'meta': {
        'client_id': 'ru.yandex.quasar.services/1.0 (Yandex Station; android 6.0.1)',
        'flags': [
            'no_cards_support'
        ],
        'locale': 'ru-RU',
        'timezone': 'Europe/Moscow'
    },
    'request': {
        'command': '',
        'original_utterance': 'запусти навык qwerty',
        'type': 'SimpleUtterance'
    },
    'session': {
        'message_id': 0,
        'new': True,
        'session_id': '618709-bb99dd92-82c4f626-442a4',
        'skill_id': '94d16-a32f-4932-9f5e-354d31f71998',
        'user_id': 'CFC516B0EC123B86C78532BCEC1C33CBF05D54EF15C8001B52628EF49F580'
    },
    "session_state": {},
    "user_state_update": {},
    "application_state": {},
    'version': '1.0'
}

ENTITY_TOKEN = {
    "start": 2,
    "end": 6
}

ENTITY_VALUE = {
    "house_number": "16",
    "street": "льва толстого"
}

ENTITY = {
    "tokens": ENTITY_TOKEN,
    "type": "YANDEX.GEO",
    "value": ENTITY_VALUE
}

ENTITY_INTEGER = {
    "tokens": {
        "start": 5,
        "end": 6
    },
    "type": "YANDEX.NUMBER",
    "value": 16
}

NLU = {
    "tokens": [
        "закажи",
        "пиццу",
        "на",
        "льва",
        "толстого",
        "16",
        "на",
        "завтра"
    ],
    "entities": [
        ENTITY,
        {
            "tokens": {
                "start": 3,
                "end": 5
            },
            "type": "YANDEX.FIO",
            "value": {
                "first_name": "лев",
                "last_name": "толстой"
            }
        },
        ENTITY_INTEGER,
        {
            "tokens": {
                "start": 6,
                "end": 8
            },
            "type": "YANDEX.DATETIME",
            "value": {
                "day": 1,
                "day_is_relative": True
            }
        }
    ]
}

REQUEST_WITH_NLU = {
    "meta": {
        "locale": "ru-RU",
        "timezone": "Europe/Moscow",
        "client_id": "ru.yandex.searchplugin/5.80 (Samsung Galaxy; Android 4.4)"
    },
    "request": {
        "command": "закажи пиццу на улицу льва толстого, 16 на завтра",
        "original_utterance": "закажи пиццу на улицу льва толстого, 16 на завтра",
        "type": "SimpleUtterance",
        "markup": {
            "dangerous_context": True
        },
        "payload": {},
        "nlu": NLU,
    },
    "session": {
        "new": True,
        "message_id": 4,
        "session_id": "2eac4854-fce721f3-b845abba-20d60",
        "skill_id": "3ad36498-f5rd-4079-a14b-788652932056",
        "user_id": "AC9WC3DF6FCE052E45A4566A48E6B7193774B84814CE49A922E163B8B29881DC"
    },
    "version": "1.0"
}

PING_REQUEST_1 = {
    'meta': {
        'client_id': 'ru.yandex.searchplugin/7.16 (none none; android 4.4.2)',
        'interfaces': {
            'screen': {}
        },
        'locale': 'ru-RU',
        'timezone': 'UTC'
    },
    'request': {
        'command': 'ping',
        'nlu': {
            'entities': [],
            'tokens': ['ping']
        },
        'original_utterance': 'ping',
        'type': 'SimpleUtterance'
    },
    'session': {
        'message_id': 0,
        'new': True,
        'session_id': '33234b1a-b8254783-45161bd7-3475df',
        'skill_id': '94d12322-a36f-4922-1f5e-364d31f77998',
        'user_id': '30395B6231A36EADCF17D4AF2707BF2D3A8E6AA48E5CD34A30365C1E642A9F9B'
    },
    'version': '1.0'
}

REQUEST_NEW_INTERFACES = {
    'meta': {
        'client_id': 'ru.yandex.searchplugin/7.16 (none none; android 4.4.2)',
        'interfaces': {
            'account_linking': {},
            'payments': {},
            'screen': {}
        },
        'locale': 'ru-RU',
        'timezone': 'UTC'
    },
    'request': {
        'command': '',
        'nlu': {
            'entities': [],
            'tokens': [],
        },
        'original_utterance': '',
        'type': 'SimpleUtterance',
    },
    'session': {
        'message_id': 0,
        'new': True,
        'session_id': 'aa6be578-34b9d8f7-e2f013b9-5c3b058d',
        'skill_id': '94d16422-a32f-4932-9f5e-354d31f71998',
        'user_id': '30397B6278A36EADCF17D4AF2707BF2C3A8E6BA48E5CD34A30365C1E628A9F9B'
    },
    'version': '1.0'
}

REQUEST_WITH_EXTRA_KWARGS = {
    'meta': {
        'client_id': 'JS/1.0',
        'locale': 'ru_RU',
        'timezone': 'Europe/Moscow',
        'interfaces': {
            'screen': {},
        },
        '_city_ru': 'Москва',
    },
    'request': {
        'command': '',
        'original_utterance': 'Запусти навык qwerty',
        'type': 'SimpleUtterance',
        'nlu': {
            'tokens': ['запусти', 'навык', 'qwerty'],
            'entities': [],
        },
    },
    'session': {
        'session_id': '4b124ca8-19c4-4ec5-75ca-24f96ef5718e',
        'user_id': '8e4156d21488cac9b7a7175a9374e63a74bb6ddd46cfbe34cf9dfb60c30c7bfb',
        'skill_id': 'f5f39790-2ee1-4744-8345-ee8229dadd58',
        'new': True,
        'message_id': 0,
        'deploy_tokens': {},
    },
    'version': '1.0',
}

REQUEST_W_EXTRA_KW_NEW = {
    'meta': {
        'client_id': 'MailRu-VC/1.0',
        'locale': 'ru_RU',
        'timezone': 'Europe/Moscow',
        'interfaces': {
            'screen': {},
        },
        '_city_ru': 'Москва',
    },
    'request': {
        'command': '',
        'original_utterance': 'Включи навык абракадабра',
        'type': 'SimpleUtterance',
        'nlu': {
            'tokens': ['включи',
                       'навык',
                       'абракадабра'],
            'entities': [],
        }
    },
    'session': {
        'session_id': 'a6dcdc42-92b8-4076-9bae-fced146bb1b2',
        'user_id': 'f67490185d2080870a55490310dcd14007ddad00eb330dd4e3356a8bac77d13f',
        'skill_id': 'efe83b82-c63e-4035-afa4-80ebed0973c8',
        'new': True,
        'message_id': 0,
        'user': {
            'user_id': 'bfe750f47d3548c13d46fa35a461dcdb49c5ab340e6f62097a77b2e023c7a4af',
        },
        'application': {
            'application_id': 'f67490185d2080870a55490310dcd14007ddad00eb330dd4e3356a8bac77d13f',
            'application_type': 'mobile',
        },
    },
    'state': {
        'session': {},
        'user': {},
    },
    'version': '1.0',
}

YANDEX_ALICE_REQUEST_EXAMPLE = {
  "meta": {
    "locale": "ru-RU",
    "timezone": "Europe/Moscow",
    "client_id": "ru.yandex.searchplugin/5.80 (Samsung Galaxy; Android 4.4)",
    "interfaces": {
      "screen": {},
      "account_linking": {}
    }
  },
  "request": {
    "command": "закажи пиццу на улицу льва толстого 16 на завтра",
    "original_utterance": "закажи пиццу на улицу льва толстого, 16 на завтра",
    "type": "SimpleUtterance",
    "markup": {
      "dangerous_context": True
    },
    "payload": {},
    "nlu": {
      "tokens": [
        "закажи",
        "пиццу",
        "на",
        "льва",
        "толстого",
        "16",
        "на",
        "завтра"
      ],
      "entities": [
        {
          "tokens": {
            "start": 2,
            "end": 6
          },
          "type": "YANDEX.GEO",
          "value": {
            "house_number": "16",
            "street": "льва толстого"
          }
        },
        {
          "tokens": {
            "start": 3,
            "end": 5
          },
          "type": "YANDEX.FIO",
          "value": {
            "first_name": "лев",
            "last_name": "толстой"
          }
        },
        {
          "tokens": {
            "start": 5,
            "end": 6
          },
          "type": "YANDEX.NUMBER",
          "value": 16
        },
        {
          "tokens": {
            "start": 6,
            "end": 8
          },
          "type": "YANDEX.DATETIME",
          "value": {
            "day": 1,
            "day_is_relative": True
          }
        }
      ]
    }
  },
  "session": {
    "message_id": 0,
    "session_id": "2eac4854-fce721f3-b845abba-20d60",
    "skill_id": "3ad36498-f5rd-4079-a14b-788652932056",
    "user_id": "47C73714B580ED2469056E71081159529FFC676A4E5B059D629A819E857DC2F8",
    "user": {
      "user_id": "6C91DA5198D1758C6A9F63A7C5CDDF09359F683B13A18A151FBF4C8B092BB0C2",
      "access_token": "AgAAAAAB4vpbAAApoR1oaCd5yR6eiXSHqOGT8dT"
    },
    "application": {
      "application_id": "47C73714B580ED2469056E71081159529FFC676A4E5B059D629A819E857DC2F8"
    },
    "new": True
  },
  "version": "1.0"
}
