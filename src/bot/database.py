STATUS_EMOJI = {
    "done": "✅",
    "not_done": "◻️",
}


DATABASE = {
    "reminder_list": [
        {
            "id": 0,
            "name": "Входящие",
            "icon": "📥",
            "sections": [
                {
                    "id": 0,
                    "name": "DEFAULT",
                    "reminders": [
                        {
                            "id": 0,
                            "tittle": "Закинуть стирку",
                            "description": "Только цветное белье",
                            "status": "done",
                        },
                        {
                            "id": 1,
                            "tittle": "Почистить обувь",
                            "description": "",
                            "status": "not_done",
                        },
                        {
                            "id": 2,
                            "tittle": "Купить крем для рук",
                            "description": "",
                            "status": "not_done",
                        },
                    ],
                },
            ],
        },
        {
            "id": 1,
            "name": "Следующие действия",
            "icon": "⏭️",
            "sections": [
                {
                    "id": 0,
                    "name": "DEFAULT",
                    "reminders": [
                        {
                            "id": 0,
                            "tittle": "Закинуть стирку",
                            "description": "Только цветное белье",
                            "status": "done",
                        },
                        {
                            "id": 1,
                            "tittle": "Почистить обувь",
                            "description": "",
                            "status": "not_done",
                        },
                        {
                            "id": 2,
                            "tittle": "Купить крем для рук",
                            "description": "",
                            "status": "not_done",
                        },
                    ],
                }
            ],
        },
        {
            "id": 2,
            "name": "Проекты",
            "icon": "👨‍💻",
            "sections": [
                {
                    "id": 0,
                    "name": "DEFAULT",
                    "reminders": [
                        {
                            "id": 0,
                            "tittle": "Закинуть стирку",
                            "description": "Только цветное белье",
                            "status": "done",
                        },
                        {
                            "id": 1,
                            "tittle": "Почистить обувь",
                            "description": "",
                            "status": "not_done",
                        },
                        {
                            "id": 2,
                            "tittle": "Купить крем для рук",
                            "description": "",
                            "status": "not_done",
                        },
                    ],
                },
                {
                    "id": 1,
                    "name": "Программирование",
                    "reminders": [
                        {
                            "id": 0,
                            "tittle": "Закинуть стирку",
                            "description": "Только цветное белье",
                            "status": "done",
                        },
                        {
                            "id": 1,
                            "tittle": "Почистить обувь",
                            "description": "",
                            "status": "not_done",
                        },
                        {
                            "id": 2,
                            "tittle": "Купить крем для рук",
                            "description": "",
                            "status": "not_done",
                        },
                    ],
                },
            ],
        },
        {
            "id": 3,
            "name": "Запланировано",
            "icon": "🗓️",
            "sections": [
                {
                    "id": 0,
                    "name": "DEFAULT",
                    "reminders": [
                        {
                            "id": 0,
                            "tittle": "Закинуть стирку",
                            "description": "Только цветное белье",
                            "status": "done",
                        },
                        {
                            "id": 1,
                            "tittle": "Почистить обувь",
                            "description": "",
                            "status": "not_done",
                        },
                        {
                            "id": 2,
                            "tittle": "Купить крем для рук",
                            "description": "",
                            "status": "not_done",
                        },
                    ],
                }
            ],
        },
        {
            "id": 4,
            "name": "Когда-нибудь",
            "icon": "🤷‍♂️",
            "sections": [
                {
                    "id": 0,
                    "name": "DEFAULT",
                    "reminders": [
                        {
                            "id": 0,
                            "tittle": "Закинуть стирку",
                            "description": "Только цветное белье",
                            "status": "done",
                        },
                        {
                            "id": 1,
                            "tittle": "Почистить обувь",
                            "description": "",
                            "status": "not_done",
                        },
                        {
                            "id": 2,
                            "tittle": "Купить крем для рук",
                            "description": "",
                            "status": "not_done",
                        },
                    ],
                }
            ],
        },
    ]
}


def get_sections_by_list_id(list_id: int) -> list:
    res = DATABASE.get("reminder_list")[list_id].get("sections")
    return res


def get_reminder_list_name_by_list_id(list_id: int) -> str:
    res = DATABASE.get("reminder_list")[list_id].get("name")
    return res


def get_section_name_by_list_id(list_id: int, section_id: int) -> str:
    res = DATABASE.get("reminder_list")[list_id].get("sections")[section_id].get("name")
    return res


def get_reminders_by_section_id(list_id: int, section_id: int) -> list:
    res = DATABASE.get("reminder_list")[list_id].get("sections")[section_id]
    return res
