from email.headerregistry import ContentTypeHeader
from settings import *
from .buttons import *
from .States import *
from models.users import User

@dp.message_handler(commands=['start', 'restart'])
async def start(message: types.Message):
    id = str(message.chat.id)
    message.bot.user_data[id] = User(id, "@" + message.chat.username, message.chat.first_name) # Создание модели пользователя и

    await bot.send_message(
        message.chat.id,
        "🇷🇺️ Уважаемый {0.first_name} ❗\n"
        "Внимательно читайте и делайте что вам пишут, и проблем не будет.\n"
        "Нажми НАЧАТЬ  на кнопке снизу👇️и мы начнем\n"
        .format(message.from_user), reply_markup=keyboard1)


# -------------------------------------------- Блок для выбора типа работ

@dp.callback_query_handler(lambda call: call.data == 'st.start')
async def Type_of_subject_entry(call: types.CallbackQuery):

    await bot.send_message(
        call.message.chat.id,
        "Выберите предмет с которой вам нужна помощь👇️\n"
        .format(call.message.from_user), reply_markup=type_of_subject)


@dp.callback_query_handler(text_contains='tps.')
async def Type_of_work_entry(call: types.CallbackQuery):

    await bot.send_message(
        call.message.chat.id,
        "Выберите тип работ с которой вам нужна помощь👇️\n"
        .format(call.message.from_user), reply_markup=type_of_work)

    id = str(call.message.chat.id)
    call.bot.user_data[id].Type_of_subject = str(call.data) # user's kind of subject

# --------------------------------------------

@dp.callback_query_handler(text_contains='tpw.')
async def Date(call):

    await Form.Type_of_work.set()

    if call.data == "tpw.Экзамен":
        await bot.send_message(call.message.chat.id,
                       "Напишите дату проведения экзамена👇"
                       .format(call.message.from_user))

    if call.data == "tpw.Консультация":
        await bot.send_message(call.message.chat.id,
                       "Напишите дату к которой нужно провести консультацию👇"
                       .format(call.message.from_user))

    if call.data == "tpw.Домашняя_работа": # уточнить по поводу формулировки
        await bot.send_message(call.message.chat.id,
                       "Напишите дату к которой нужно провести консультацию👇"
                       .format(call.message.from_user))

    id = str(call.message.chat.id)
    call.bot.user_data[id].Type_of_work = str(call.data) # user's kind of work

    await Form.next()


@dp.message_handler(state=Form.Date)
async def Time_handler(message: types.Message, state: FSMContext):
    if message.text not in ["/start", "/restart"]:

        UDate = message.text

        id = str(message.chat.id)
        message.bot.user_data[id].Date = UDate

        if bot.user_data[id].Type_of_work == "tpw.Экзамен":
            await bot.send_message(
                message.chat.id,
                "Напишите время проведения экзамена👇\n")

        elif bot.user_data[id].Type_of_work == "tpw.Консультация":
            await bot.send_message(
                message.chat.id,
                "Напишите время проведения консультации👇\n")

        elif bot.user_data[id].Type_of_work == "tpw.Домашняя_работа":
            await bot.send_message(
                message.chat.id,
                "Напишите время проведения консультации👇\n")

        await Form.next()
    else:
        await state.finish()


@dp.message_handler(state=Form.Time)
async def Tasks_handler(message: types.Message, state: FSMContext):
    if message.text not in ["/start", "/restart"]:

        UTime = message.text

        id = str(message.chat.id)
        message.bot.user_data[id].Time = UTime

        if bot.user_data[id].Type_of_work == "tpw.Экзамен":
            await bot.send_message(
                message.chat.id,
                "Напишите количество задач на экзамене\n")

        elif bot.user_data[id].Type_of_work == "tpw.Консультация":
            await bot.send_message(
                message.chat.id,
                "Напишите тему консультации или отправьте 1 фото\n")

        elif bot.user_data[id].Type_of_work == "tpw.Домашняя_работа":
            await bot.send_message(
                message.chat.id,
                "Напишите сколько задач нужно разобрать или отправьте 1 фото👇\n")

        await Form.next()
    else:
        await state.finish()


@dp.message_handler(state=Form.Tasks, content_types=['text', 'document', 'photo'])
async def Htowrite_handler(message: types.Message, state: FSMContext):
    if message.text not in ["/start", "/restart"]:

        try:
            idphoto = message.photo[-1].file_id
            id = str(message.chat.id)
            bot.user_data[id].Photos = idphoto

        except:
            UTasks = message.text
            id = str(message.chat.id)
            message.bot.user_data[id].Tasks = UTasks


        if bot.user_data[id].Type_of_work == "tpw.Экзамен":
            await bot.send_message(
                message.chat.id,
                "Напишите сколько времени дают на решение задач👇\n")

        elif bot.user_data[id].Type_of_work == "tpw.Консультация":
            await bot.send_message(
                message.chat.id,
                "Напишите сколько примерно времени понадобиться на решение задач👇\n")

        elif bot.user_data[id].Type_of_work == "tpw.Домашняя_работа":
            await bot.send_message(
                message.chat.id,
                "Напишите сколько примерно времени понадобиться на решение задач👇\n")

        await Form.next()
    else:
        await state.finish()


@dp.message_handler(state=Form.Htowrite) # Присабачить фото
async def Lectur_handler(message, state: FSMContext):
    if message.text not in ["/start", "/restart"]:

        UHours_to_write = message.text
        id = str(message.chat.id)
        message.bot.user_data[id].Hours_to_write = UHours_to_write

        if bot.user_data[id].Type_of_work == "tpw.Экзамен":
            await bot.send_message(
                message.chat.id,
                "Напишите фамилию лектора👇\n")

        elif bot.user_data[id].Type_of_work == "tpw.Консультация":
            await bot.send_message(
                message.chat.id,
                "Напишите фамилию лектора👇\n")

        elif bot.user_data[id].Type_of_work == "tpw.Домашняя_работа":
            await bot.send_message(
                message.chat.id,
                "Напишите фамилию лектора👇\n")

        await Form.next()
    else:
        await state.finish()


@dp.message_handler(state=Form.Lectur)
async def Info_handler(message: types.Message, state: FSMContext):
    if message.text not in ["/start", "/restart"]:

        ULectur = message.text

        id = str(message.chat.id)
        message.bot.user_data[id].Lectur = ULectur

        await bot.send_message(
            message.chat.id,
            "️Напишите дополнительную информацию которую стоит знать прежде чем мы свяжемся с вами :)")
        await Form.next()
    else:
        await state.finish()


@dp.callback_query_handler(text_contains='tpwd.')
async def Type_of_work_entry(call: types.CallbackQuery):

        await bot.send_message(
            call.message.chat.id,
            "️Опишите вашу проблему или задачу с которой вам нужна помощь")

        await Form.Info.set()


@dp.message_handler(state=Form.Info)
async def End_handler(message: types.Message, state: FSMContext):
    if message.text not in ["/start", "/restart"]:

        UInfo = message.text

        id = str(message.chat.id)
        message.bot.user_data[id].Info = UInfo

        bot.user_data[id].Type_of_subject = str(bot.user_data[id].Type_of_subject[4:]) # user's kind of subject
        bot.user_data[id].Type_of_work = str(bot.user_data[id].Type_of_work[4:]) # user's kind of work

        json_data = check_n_load_json(BASE_JSON_FILEPATH)

        if id in json_data:
            try:
                message.bot.user_data[id].Count = int(json_data[id]["Count"].split()[-1]) + 1
            except:
                message.bot.user_data[id].Count = 1
        else:
            message.bot.user_data[id].Count = 1


        # Отправка владельцу
        await bot.send_message(
            config['meid']['id1'],
            bot.user_data[id].to_str())

        await bot.send_message(
            config['meid']['id2'],
            bot.user_data[id].to_str())

        try:
            await bot.send_photo(
                config['meid']['id1'],
                bot.user_data[id].Photos)

            await bot.send_photo(
                config['meid']['id2'],
                bot.user_data[id].Photos)
        except:
            pass


        with open(BASE_JSON_FILEPATH, "w", encoding='utf-8') as file:
            # Добавление пользователя в БД
            json_data.update(bot.user_data[id].to_dict())
            # Запись в файд
            json.dump(json_data, file, indent=4, ensure_ascii=False)


        await bot.send_message(
            message.chat.id,
            "️Спасибо, что выбрали нас, в скором времени наш специалист свяжется с вами\n\n"
            "+Inf\n"
            "Базовая цена экзаменационной задачи - от 1500 рублей.\n\n"

            "Почему от? Если хочешь быть выше в очереди на решение, то можно с доплатой за срочность к основной сумме.\n"
            " - То есть буду решать раньше, чем тем, кто внёс доплату за срочность меньше.\n\n"

            "Так как я не всем желающим смогу решить, поэтому за 1-3 дня составлю список из 3 ребят, кому успеваю решить,\n"
            "а остальным верну их оплату/оставлю по их желанию до экзамена, вдруг кто-то не скинет задачи и очередь продвинется вперёд.\n\n"

            "В доплату за срочность (от 500 рублей) также будет входить помощь с теоретической частью билета\n\n"

            "Если не скидываешь условие задачи, деньги возвращаю.\n\n"

            "2202 2016 3632 9266")

        await state.finish()
    else:
        await state.finish()

@dp.message_handler(content_types='text')
async def start(message: types.Message):
    if message.text == "/all_inf":
        if str(message.chat.id) == str(config['meid']['id']):
            with open("settings/user_data.json", "rb") as fileJson:
                df = pd.read_json(fileJson)
                df.to_csv(r"settings/user_data.csv", index=False)
                with open("settings/user_data.csv", "rb") as fileCSV:
                    await bot.send_document(config['meid']['id'], fileCSV)

        else:
            await bot.send_message(
                message.chat.id,
                "Вас разве это попросили сделать⁉️")

            await bot.delete_message(message.chat.id, message.message_id)
            await asyncio.sleep(5)
            await bot.delete_message(message.chat.id, message.message_id + 1)





