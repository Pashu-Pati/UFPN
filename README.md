привет! Я JavaScript Developer c 4-летним опытом работы. В большинстве проектов, где я был частью команды, для разработки пользовательского интерфейса мы использовали библиотеку React. В этой статье я расскажу, как выстраивать процесс подготовки React Junior Developer’ов к работе в их первом проекте. Информация будет полезна менторам по React и тем, кто собирается учить эту библиотеку. Также, считаю, материал пригодится тем, кто работает с Angular или Vue.

Недавно я сам был на испытательном сроке в своей первой компании. И еще хорошо помню, как было нелегко структурировать все новые знания и, что важнее, понять, как их применить. Особые сложности возникали, когда я сталкивался с процессными моментами. Что такое pull request? Что значит «перевести статус таски в done»? Это сейчас все понятно и просто. А в начале пути так не казалось. Новому сотруднику недостаточно быть технически подкованным. Также важно уметь коммуницировать с другими разработчиками и понимать детали работы в проекте. У меня был опыт менторства новых сотрудников, и мне хотелось бы им поделиться. Но сначала опишу, как я строил свою коммуникацию с интерном. А дальше уже перейдем к более технической части статьи.


Иллюстрация Алины Самолюк

Все задания, которые представлены ниже, стоит делать последовательно. Это поможет интерну сфокусироваться и не выполнять несколько задач одновременно. Переходить к следующему заданию следует только в том случае, если ментор уверен, что интерн разобрался с текущим. Каждое утро у меня с интернами был митинг, где им надо было ответить на три вопроса:

Что ты делал вчера и с какими трудностями столкнулся?
Что собираешься делать сегодня?
Что тебя блокирует?
Сколько времени стоит уделять каждому пункту — индивидуально. Все зависит от нескольких факторов: срочности внедрения сотрудника в проект, уровня подготовки интерна, желаемого уровня подготовки интерна и так далее.

А теперь переходим к основным моментам, на которые стоит обратить внимание при подготовке React Junior Developer’а к работе в его первом проекте. Это мои пункты. В комментариях оставляйте то, что, по вашему мнению, можно или стоит добавить.

1. Документация по React
Зачастую молодые специалисты не любят читать документацию. Но документация по React — это must read. Она достаточно проста и информативна, структурирована, тут есть отличные практические примеры. Не стоит от интерна ожидать, что он сразу же освоит все темы. Достаточно пройтись по трем разделам: основные понятия, продвинутые темы и хуки. Главная цель — понять общие моменты, как можно делать и как лучше делать.

2. Работа с таск-менеджером
Обучаем работе с таск-менеджером (Jira, Trello, etc.). Рассказываем, какие виды заданий существуют (feature, bug), какой может быть статус задания (in progress, done). Учим интерна давать эстимейты своим задачам. Ничего страшного, если он не будет попадать в сроки. В данном случае отрицательный опыт может даже больше дать, чем положительный. В основном интерны занижают оценку. Если джуниор будет тратить времени и ресурсов больше, чем оценил изначально, то следующий раз более ответственно подойдет к эстимейту и, что важнее, более детально будет продумывать, как следует выполнить задание.

3. Работа с Git
Если интерн не знаком с Git (GitHub, Bitbucket, etc.), то стоит провести небольшую лекцию. Объясняем основные моменты: локальный и удаленный репозиторий, ветки, коммиты и так далее. После этого, чтобы закрепить полученную информацию, можно почитать статью. Также нужно выбрать, как будете проверять результат работы интерна. Мне нравится такой подход:

клонируем репозиторий (главная ветка master);
создаем новую ветку от master;
начинаем работу в новой ветке;
после завершения задания делаем коммит и пушим изменения в удаленный репозиторий;
создаем pull request в master и добавляем ментора в reviewers;
ментор и интерн обсуждают, что стоит исправить.
Как мы помним, стоит заложить фундамент. Проверяем pull requests. Обращаем внимание на название веток, коммитов, переменных, форматирование кода.

4. Написать To-Do List App
От теории к практике. Для того чтобы интерн не заскучал, начинаем писать код. Стоит постепенно усложнять задачу. Сначала мы реализовываем самый базовый функционал. Достаточно сделать следующие фичи:

поиск;
свитчер;
добавление новых todos;
изменение todos;
удаление todos.
Если в команде есть верстальщик, то не делайте акцент на верстке и стилях. Лучше сэкономить время и больше разобраться с React. Я рекомендую использовать для стилей React Bootstrap или Material-UI. Эти библиотеки предоставляют различные компоненты, в том числе Switcher. И интерн может сфокусироваться на логике, а не на презентации.

Зачастую Junior-разработчики уделяют стилям очень много внимания. Я рекомендую менторам, как только они в pull request увидят много изменений, которые относятся к стилям, сразу же просить переделать и использовать готовые компоненты.

5. Записать демо с кратким обзором сделанной работы
Мой любимый пункт. Это как первый шаг к развитию самопрезентации. Для джунов не всегда легко начинать говорить на английском. А это хороший повод сделать это.
Мои рекомендации по демо:

оно должно быть на английском;
screen recording (запись монитора, демонстрация фич с комментированием);
структура демо: вступление, обзор каждой фичи, завершение;
показать в разных браузерах (Chrome, Firefox, Safari);
продолжительность 3–5 минут;
показывать только функционал (не код).
6. Добавить Redux в проект
Да, есть хуки. Но я даже не знаю, сколько времени понадобится, чтобы заменить Redux во всех существующих приложениях. Наверное, тогда уже не будет и хуков. Да и вряд ли все будут делать это.

Читаем документацию по Redux, смотрим курсы, обсуждаем с интерном сложные моменты. Переносим локальный стэйт в глобальный стор. Добавляем экшены, редюсер, подключаем стор.

7. Добавить тесты в проект (Jest/Enzyme)
Важно, чтобы интерн понял: тесты нужны. Стоит показать примеры почему. Вот неплохая статья об этом. В итоге разработчик как минимум перестанет писать большие функции, которые сложно будет тестировать. А в лучшем случае — перейдет на TDD.

Сначала следует почитать документацию Jest. После этого будет полезным посмотреть более практичные примеры, как писать тесты для React-компонентов, reducer’ов и action’ов.

После того как интерн закончит теоретическую часть по тестам, переходите к практике. Покрываем тестами редюсеры, экшены и компоненты. Не стоит делать акцент на snapshots. Со своего опыта могу сказать, что они не сильно полезны. Почитайте здесь более детально, почему лучше не использовать snapshots вообще.

8. Пагинация
Постепенно усложняем приложение. Добавляем пагинацию. Не делаем акцент на верстке. Можно использовать готовый компонент, например bootstrap.
Так. Что-то не складывается. Для реалистичного использования пагинации нужен бэкенд с базой данных, где будет возможность получать, удалять, обновлять todos. Можно использовать мой. Вот ссылка на репозиторий.

Еще полезно добавить возможность переключения количества todos на страничке.

9. Авторизация
Форму регистрации и авторизации можно добавить в модальном окне. Но, для того чтобы охватить больше тем, эти формы надо разметить на различных страничках приложения. Для этого подключите роутер. Теперь вместо одной странички у нас целых три (todo lists, login, sign-up). Можно также добавить валидацию для форм регистрации и входа. Formik — неплохая библиотека, которая упрощает работу с формами. Еще интересное задание — добавить авторизацию с помощью Facebook или Instagram.

10. Сокеты
Шанс для ментора показать, почему нужно отписываться от подписок в componentWillUnmount. Интерну стоит записать демо, где он покажет, как в одном браузере добавляет новую to-do, а в другом она сразу же появляется.

11. Локализация
Локализация приносит пользу бизнесу. Хоть английский и популярный язык, но все же не стоит терять возможность привлечь клиентов, которые не знают его. В среднем добавление локализации не требует многих ресурсов. Для интерна будет полезным получить опыт работы с библиотеками, которые упрощают внедрение локализации. i18next — неплохое решения для React-приложений.

12. Улучшаем производительность
Это не очень легкое задание для джуна. Но в несложном проекте вполне реализуемое. Стоит обратить внимание на React.memo, PureComponent, React.useCallback, React.useMemo и так далее. Например, сосредотачиваемся на том, чтобы при изменении состояния одной todo не было re-render всех остальных. Добавляем возможность показать одновременно больше 1000 todos на страничке. Записываем демо, где сравниваем результаты производительности до и после. Вот ссылка, как проверять перформанс React-приложения.

Бонус
Переписать все на TypeScript. Он набирает популярность и является одним из самых быстрорастущих языков программирования по частоте использования в новых проектах. TypeScript расширяет возможности JavaScript. Главный плюс — это статическая типизация. Она позволяет снизить вероятность ошибки. В общем, благодаря переходу на TypeScript можно ускорить процесс разработки и отладки, легче будет расширять проект.

Итак, для JavaScript-разработчика TypeScript — это уже почти обязательная тема для изучения. Но этот пункт можно отложить на потом, поскольку пока еще многие проекты не используют этот язык.

Заключение
Надеюсь, эта статья была полезна и интересна. Безусловно, есть темы, которые также необходимо пройти новому специалисту, чтобы лучше ориентироваться в экосистеме React и легко интегрироваться в проект, но я старался выделить основные моменты и сделать материал максимально практичным.
