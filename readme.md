## NotifyMe

NotifyMe - сервис, позволяющий легко и быстро оправлять уведомления через сообщения ВКонтакте посредством выполнения всего одного запроса.

### Получение токена

Токен предоставляет собой средство авторизации для запроса на отправку уведомления. Для получения токена необходимо отправить сообщение с текстом `token` в [сообщения группы](http://vk.com/ntfyme). В ответном сообщении вам будет выслан токен. Если до этого у вас уже имелся токен, то его действие аннулируется.
![](http://img.dedol.ru/notifyme_token.png)

### Отправка уведомлений

После получения токена можно перейти непосредственно к отправке уведомлений. Чтобы отправить уведомление необходимо выполнить GET-запрос на адрес `http://notify.dedol.ru/send`, передав следующие параметры:

| Параметр | Тип | Описание |
|---|---|---|
| **user**  | целое число | Идентификатор пользователя ВКонтакте (ID), которому будет отправлено уведомление. |
| **token**  | строка | Средство авторизации, уникальная последовательность для каждого пользователя. |
| **text**  | строка | Текст отправляемого уведомления. |

В ответ будет возвращен json-объект, содержащий следующие поля:

| Ключ | Описание |
|---|---|
| **status**  | Результат выполнения запроса, принимает значения `ok` или `error`. |
| **error_msg**  | Описание полученной ошибки, возвращается только в том случае, если поле `status` имеет значение `error`. Расшифровка полученных значений описана ниже. |

### Возможные ошибки

| Код | Описание |
|---|---|
| **Bad Request** | Переданы не все требуемые параметры. |
| **Unknown user** | Пользователь, которому отправляется уведомление, не выпускал токен, поэтому он не может получать уведомления. |
| **Invalid token** | Неверный токен для текущего пользователя. После выпуска нового токена, все выпущенные ранее перестают работать. |
| **Sending error** | Ошибка отправки уведомления. Попробуйте выполнить запрос чуть позже. |

### Список команд для сообщений

Полный список и описание команд, которые можно отправить в [сообщения сообщества](http://vk.com/ntfyme):

| Команда | Описание |
|---|---|
| **token** | Выпускает новый токен, старый токен, если он имелся, перестанет работать. |
| **user** | Возвращает ваш ID ВКонтакте, который необходим для отправки запроса. |
| **stat** | Возвращает статистику использования сервиса. |
