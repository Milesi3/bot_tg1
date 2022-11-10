def find(update, context):
    update.message.reply_text(f"Введите фамилию для поиска\n"
                              f"Для остановки нажмите /stop")
    return 1


def add_row(update, context):
    update.message.reply_text(f"Введите фамилию, имя, телефон и комментарий через пробел\n"
                              f"Для остановки нажмите /stop")
    return 1


def deleterow(update, context):
    update.message.reply_text(f"Введите индекс для удаления \n"
                              f"Для остановки нажмите /stop")

    return 1