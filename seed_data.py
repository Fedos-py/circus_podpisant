from models import Source, db
from seed_catalog_extra import EXTRA_VK_GROUPS, EXTRA_WEBSITES

# Данные собраны из официального каталога филиалов Росгосцирка (circus.ru/kontakty/filialy/)
# и открытых страниц цирков. VK-ссылки — публичные сообщества, указанные на сайтах или в соцсетях.

WEBSITES = [
    {
        "name": "Росгосцирк — официальный портал",
        "url": "https://www.circus.ru",
        "city": "Москва",
        "region": "Москва",
        "organization": "Росгосцирк",
        "description": "Единый портал: афиша, гастрольный график, каталог филиалов.",
    },
    {
        "name": "Астраханский государственный цирк",
        "url": "https://www.circus-astrahan.ru",
        "city": "Астрахань",
        "region": "Астраханская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Большой Санкт-Петербургский государственный цирк",
        "url": "https://www.circus.spb.ru",
        "city": "Санкт-Петербург",
        "region": "Санкт-Петербург",
        "organization": "Росгосцирк",
        "description": "Цирк на Фонтанке.",
    },
    {
        "name": "Шапито «Цирк в Автово»",
        "url": "https://www.circus-avtovo.ru",
        "city": "Санкт-Петербург",
        "region": "Санкт-Петербург",
        "organization": "Росгосцирк",
    },
    {
        "name": "Брянский государственный цирк",
        "url": "https://www.circus-bryansk.ru",
        "city": "Брянск",
        "region": "Брянская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Владивостокский государственный цирк",
        "url": "https://www.circus-vladivostok.ru",
        "city": "Владивосток",
        "region": "Приморский край",
        "organization": "Росгосцирк",
    },
    {
        "name": "Волгоградский государственный цирк",
        "url": "https://www.circus-volgograd.ru",
        "city": "Волгоград",
        "region": "Волгоградская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Воронежский государственный цирк",
        "url": "https://www.circus-voronezh.ru",
        "city": "Воронеж",
        "region": "Воронежская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Екатеринбургский государственный цирк",
        "url": "https://www.circus-ekaterinburg.ru",
        "city": "Екатеринбург",
        "region": "Свердловская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Ивановский государственный цирк",
        "url": "https://www.circus-ivanovo.ru",
        "city": "Иваново",
        "region": "Ивановская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Иркутский государственный цирк",
        "url": "https://www.circus-irkutsk.ru",
        "city": "Иркутск",
        "region": "Иркутская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Казанский государственный цирк",
        "url": "https://kazan-circus.ru",
        "city": "Казань",
        "region": "Республика Татарстан",
        "organization": "Росгосцирк",
    },
    {
        "name": "Кемеровский государственный цирк",
        "url": "https://www.circus-kemerovo.ru",
        "city": "Кемерово",
        "region": "Кемеровская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Кировский государственный цирк",
        "url": "https://www.circus-kirov.ru",
        "city": "Киров",
        "region": "Кировская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Кисловодский государственный цирк",
        "url": "https://www.circus-kislovodsk.ru",
        "city": "Кисловодск",
        "region": "Ставропольский край",
        "organization": "Росгосцирк",
    },
    {
        "name": "Костромской государственный цирк",
        "url": "https://www.circus-kostroma.ru",
        "city": "Кострома",
        "region": "Костромская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Красноярский государственный цирк",
        "url": "https://www.circus-krasnoyarsk.ru",
        "city": "Красноярск",
        "region": "Красноярский край",
        "organization": "Росгосцирк",
    },
    {
        "name": "Курский государственный цирк",
        "url": "https://www.circus-kursk.ru",
        "city": "Курск",
        "region": "Курская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Магнитогорский государственный цирк",
        "url": "https://www.circus-magnitogorsk.ru",
        "city": "Магнитогорск",
        "region": "Челябинская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Московский цирк Никулина на Цветном бульваре",
        "url": "https://www.nikulinacirkus.com",
        "city": "Москва",
        "region": "Москва",
        "organization": "Росгосцирк",
    },
    {
        "name": "Большой Московский государственный цирк на проспекте Вернадского",
        "url": "https://www.vernadsky-cirk.com",
        "city": "Москва",
        "region": "Москва",
        "organization": "Росгосцирк",
    },
    {
        "name": "Цирк-шапито «Радуга» — страница на портале Росгосцирка",
        "url": "https://www.circus.ru/kontakty/filialy/?qa=%D0%BC",
        "city": "Москва",
        "region": "Москва",
        "organization": "Росгосцирк",
        "description": "Отдельного сайта нет; контакты на портале Росгосцирка.",
    },
    {
        "name": "Нижегородский государственный цирк",
        "url": "https://www.circus-nnovgorod.ru",
        "city": "Нижний Новгород",
        "region": "Нижегородская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Нижнетагильский государственный цирк",
        "url": "https://www.circus-ntagil.ru",
        "city": "Нижний Тагил",
        "region": "Свердловская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Новокузнецкий государственный цирк",
        "url": "https://www.circus-novokuznetsk.ru",
        "city": "Новокузнецк",
        "region": "Кемеровская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Новосибирский государственный цирк",
        "url": "https://www.circus-novosibirsk.ru",
        "city": "Новосибирск",
        "region": "Новосибирская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Омский государственный цирк",
        "url": "https://www.circus-omsk.ru",
        "city": "Омск",
        "region": "Омская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Оренбургский государственный цирк",
        "url": "https://www.circus-orenburg.ru",
        "city": "Оренбург",
        "region": "Оренбургская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Пензенский государственный цирк",
        "url": "https://www.circus-penza.ru",
        "city": "Пенза",
        "region": "Пензенская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Пермский государственный цирк",
        "url": "https://www.circus-perm.ru",
        "city": "Пермь",
        "region": "Пермский край",
        "organization": "Росгосцирк",
    },
    {
        "name": "Ростовский государственный цирк",
        "url": "https://www.circus-rostov.ru",
        "city": "Ростов-на-Дону",
        "region": "Ростовская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Цирк-шапито «Азовье» (Таганрог)",
        "url": "https://circus-taganrog.ru",
        "city": "Таганрог",
        "region": "Ростовская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Рязанский государственный цирк",
        "url": "https://www.circus-ryazan.ru",
        "city": "Рязань",
        "region": "Рязанская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Самарский государственный цирк",
        "url": "https://www.circus-samara.ru",
        "city": "Самара",
        "region": "Самарская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Саратовский государственный цирк",
        "url": "https://www.circus-saratov.ru",
        "city": "Саратов",
        "region": "Саратовская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Севастопольский цирк",
        "url": "https://www.circus-sevastopol.ru",
        "city": "Севастополь",
        "region": "Севастополь",
        "organization": "Росгосцирк",
    },
    {
        "name": "Симферопольский государственный цирк им. Б. Тезикова",
        "url": "https://www.circtezikova.ru",
        "city": "Симферополь",
        "region": "Республика Крым",
        "organization": "Росгосцирк",
    },
    {
        "name": "Сочинский государственный цирк",
        "url": "https://www.circus-sochi.ru",
        "city": "Сочи",
        "region": "Краснодарский край",
        "organization": "Росгосцирк",
    },
    {
        "name": "Ставропольский государственный цирк",
        "url": "https://www.circus-stavropol.ru",
        "city": "Ставрополь",
        "region": "Ставропольский край",
        "organization": "Росгосцирк",
    },
    {
        "name": "Тверской государственный цирк",
        "url": "https://www.circus-tver.ru",
        "city": "Тверь",
        "region": "Тверская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Тульский государственный цирк",
        "url": "https://www.circus-tula.ru",
        "city": "Тула",
        "region": "Тульская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Тюменский государственный цирк",
        "url": "https://www.circus-tyumen.ru",
        "city": "Тюмень",
        "region": "Тюменская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Уфимский государственный цирк",
        "url": "https://www.circus-ufa.ru",
        "city": "Уфа",
        "region": "Республика Башкортостан",
        "organization": "Росгосцирк",
    },
    {
        "name": "Челябинский государственный цирк",
        "url": "https://www.circus-chelyabinsk.ru",
        "city": "Челябинск",
        "region": "Челябинская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Ярославский государственный цирк",
        "url": "https://www.circus-yaroslavl.ru",
        "city": "Ярославль",
        "region": "Ярославская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Государственный цирк Республики Саха (Якутия)",
        "url": "https://www.diamond-circus.ru",
        "city": "Якутск",
        "region": "Республика Саха (Якутия)",
        "organization": "Росгосцирк",
        "description": "Алмазный цирк.",
    },
    {
        "name": "Королевский цирк — продюсерский центр Гии Эрадзе",
        "url": "https://royalcircus.ru",
        "city": None,
        "region": None,
        "organization": "Гастрольный коллектив",
        "description": "Гастролирующие шоу на площадках Росгосцирка.",
    },
    {
        "name": "Цирк на воде «Шевченко Шоу»",
        "url": "https://www.aqua-circus.ru",
        "city": None,
        "region": None,
        "organization": "Гастрольный коллектив",
        "description": "Выездной цирк на воде, гастроли по России.",
    },
]

VK_GROUPS = [
    {
        "name": "Росгосцирк",
        "url": "https://vk.com/rosgoscirc",
        "city": "Москва",
        "region": "Москва",
        "organization": "Росгосцирк",
        "description": "Официальное сообщество Российской государственной цирковой компании.",
    },
    {
        "name": "Московский цирк Никулина на Цветном бульваре",
        "url": "https://vk.com/circusnikulin",
        "city": "Москва",
        "region": "Москва",
        "organization": "Росгосцирк",
    },
    {
        "name": "Большой Московский цирк на проспекте Вернадского",
        "url": "https://vk.com/vernadsky_circus",
        "city": "Москва",
        "region": "Москва",
        "organization": "Росгосцирк",
    },
    {
        "name": "Цирк-шапито «Радуга»",
        "url": "https://vk.com/circus_raduga",
        "city": "Москва",
        "region": "Москва",
        "organization": "Росгосцирк",
    },
    {
        "name": "Большой Санкт-Петербургский государственный цирк",
        "url": "https://vk.com/circusciniselli",
        "city": "Санкт-Петербург",
        "region": "Санкт-Петербург",
        "organization": "Росгосцирк",
        "description": "Цирк на Фонтанке.",
    },
    {
        "name": "Шапито «Цирк в Автово»",
        "url": "https://vk.com/circus_avtovo",
        "city": "Санкт-Петербург",
        "region": "Санкт-Петербург",
        "organization": "Росгосцирк",
    },
    {
        "name": "Астраханский государственный цирк",
        "url": "https://vk.com/circus_astrakhan",
        "city": "Астрахань",
        "region": "Астраханская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Брянский государственный цирк",
        "url": "https://vk.com/circus_bryansk",
        "city": "Брянск",
        "region": "Брянская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Владивостокский государственный цирк",
        "url": "https://vk.com/circus_vladivostok",
        "city": "Владивосток",
        "region": "Приморский край",
        "organization": "Росгосцирк",
    },
    {
        "name": "Волгоградский государственный цирк",
        "url": "https://vk.com/circus_volgograd",
        "city": "Волгоград",
        "region": "Волгоградская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Воронежский государственный цирк",
        "url": "https://vk.com/circus_voronezh",
        "city": "Воронеж",
        "region": "Воронежская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Екатеринбургский государственный цирк",
        "url": "https://vk.com/circus_ekb",
        "city": "Екатеринбург",
        "region": "Свердловская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Ивановский государственный цирк",
        "url": "https://vk.com/circus_ivanovo",
        "city": "Иваново",
        "region": "Ивановская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Иркутский государственный цирк",
        "url": "https://vk.com/circus_irkutsk",
        "city": "Иркутск",
        "region": "Иркутская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Казанский государственный цирк",
        "url": "https://vk.com/kazan_circus",
        "city": "Казань",
        "region": "Республика Татарстан",
        "organization": "Росгосцирк",
    },
    {
        "name": "Кемеровский государственный цирк",
        "url": "https://vk.com/circus_kemerovo",
        "city": "Кемерово",
        "region": "Кемеровская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Кировский государственный цирк",
        "url": "https://vk.com/circus_kirov",
        "city": "Киров",
        "region": "Кировская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Кисловодский государственный цирк",
        "url": "https://vk.com/circus_kislovodsk",
        "city": "Кисловодск",
        "region": "Ставропольский край",
        "organization": "Росгосцирк",
    },
    {
        "name": "Костромской государственный цирк",
        "url": "https://vk.com/circus_kostroma",
        "city": "Кострома",
        "region": "Костромская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Красноярский государственный цирк",
        "url": "https://vk.com/circus_krasnoyarsk",
        "city": "Красноярск",
        "region": "Красноярский край",
        "organization": "Росгосцирк",
    },
    {
        "name": "Курский государственный цирк",
        "url": "https://vk.com/circus_kursk",
        "city": "Курск",
        "region": "Курская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Магнитогорский государственный цирк",
        "url": "https://vk.com/circus_magnitogorsk",
        "city": "Магнитогорск",
        "region": "Челябинская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Нижегородский государственный цирк",
        "url": "https://vk.com/circus_nnovgorod",
        "city": "Нижний Новгород",
        "region": "Нижегородская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Нижнетагильский государственный цирк",
        "url": "https://vk.com/circus_ntagil",
        "city": "Нижний Тагил",
        "region": "Свердловская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Новокузнецкий государственный цирк",
        "url": "https://vk.com/circus_novokuznetsk",
        "city": "Новокузнецк",
        "region": "Кемеровская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Новосибирский государственный цирк",
        "url": "https://vk.com/circus_novosibirsk",
        "city": "Новосибирск",
        "region": "Новосибирская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Омский государственный цирк",
        "url": "https://vk.com/circus_omsk",
        "city": "Омск",
        "region": "Омская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Оренбургский государственный цирк",
        "url": "https://vk.com/circus_orenburg",
        "city": "Оренбург",
        "region": "Оренбургская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Пензенский государственный цирк",
        "url": "https://vk.com/circus_penza",
        "city": "Пенза",
        "region": "Пензенская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Пермский государственный цирк",
        "url": "https://vk.com/circus_perm",
        "city": "Пермь",
        "region": "Пермский край",
        "organization": "Росгосцирк",
    },
    {
        "name": "Ростовский государственный цирк",
        "url": "https://vk.com/circus_rostov",
        "city": "Ростов-на-Дону",
        "region": "Ростовская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Рязанский государственный цирк",
        "url": "https://vk.com/circus_ryazan",
        "city": "Рязань",
        "region": "Рязанская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Самарский государственный цирк",
        "url": "https://vk.com/circus_samara",
        "city": "Самара",
        "region": "Самарская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Саратовский государственный цирк",
        "url": "https://vk.com/circus_saratov",
        "city": "Саратов",
        "region": "Саратовская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Севастопольский цирк",
        "url": "https://vk.com/circus_sevastopol",
        "city": "Севастополь",
        "region": "Севастополь",
        "organization": "Росгосцирк",
    },
    {
        "name": "Симферопольский госцирк им. Б. Тезикова",
        "url": "https://vk.com/club85540620",
        "city": "Симферополь",
        "region": "Республика Крым",
        "organization": "Росгосцирк",
        "description": "Официальная страница цирка им. Б. Тезикова.",
    },
    {
        "name": "Сочинский государственный цирк",
        "url": "https://vk.com/circus_sochi",
        "city": "Сочи",
        "region": "Краснодарский край",
        "organization": "Росгосцирк",
    },
    {
        "name": "Ставропольский государственный цирк",
        "url": "https://vk.com/circus_stavropol",
        "city": "Ставрополь",
        "region": "Ставропольский край",
        "organization": "Росгосцирк",
    },
    {
        "name": "Тверской государственный цирк",
        "url": "https://vk.com/circus_tver",
        "city": "Тверь",
        "region": "Тверская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Тульский государственный цирк",
        "url": "https://vk.com/circus_tula",
        "city": "Тула",
        "region": "Тульская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Тюменский государственный цирк",
        "url": "https://vk.com/circus_tyumen",
        "city": "Тюмень",
        "region": "Тюменская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Уфимский государственный цирк",
        "url": "https://vk.com/circus_ufa",
        "city": "Уфа",
        "region": "Республика Башкортостан",
        "organization": "Росгосцирк",
    },
    {
        "name": "Челябинский государственный цирк",
        "url": "https://vk.com/circus_chelyabinsk",
        "city": "Челябинск",
        "region": "Челябинская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Ярославский государственный цирк",
        "url": "https://vk.com/circus_yaroslavl",
        "city": "Ярославль",
        "region": "Ярославская область",
        "organization": "Росгосцирк",
    },
    {
        "name": "Государственный цирк Республики Саха (Якутия)",
        "url": "https://vk.com/diamond_circus",
        "city": "Якутск",
        "region": "Республика Саха (Якутия)",
        "organization": "Росгосцирк",
        "description": "Алмазный цирк.",
    },
    {
        "name": "Королевский цирк — продюсерский центр Гии Эрадзе",
        "url": "https://vk.com/royalcircusgiaeradze",
        "city": None,
        "region": None,
        "organization": "Гастрольный коллектив",
    },
    {
        "name": "Цирк на воде «Шевченко Шоу»",
        "url": "https://vk.com/aquacircus",
        "city": None,
        "region": None,
        "organization": "Гастрольный коллектив",
    },
    {
        "name": "Цирк-шапито «Азовье» (Таганрог)",
        "url": "https://vk.com/circus_taganrog",
        "city": "Таганрог",
        "region": "Ростовская область",
        "organization": "Росгосцирк",
    },
]


def _normalize_url(url):
    normalized = url.strip().rstrip("/")
    if normalized.startswith("http://"):
        normalized = "https://" + normalized[7:]
    return normalized


def _all_catalog_items():
    for item in WEBSITES + EXTRA_WEBSITES:
        yield Source.WEBSITE, item
    for item in VK_GROUPS + EXTRA_VK_GROUPS:
        yield Source.VK, item


def seed_database():
    """Добавляет в БД только новые URL (идемпотентно)."""
    existing_urls = {
        _normalize_url(source.url).lower() for source in Source.query.all()
    }
    added = 0

    for source_type, item in _all_catalog_items():
        url = _normalize_url(item["url"])
        if url.lower() in existing_urls:
            continue
        db.session.add(
            Source(
                name=item["name"],
                source_type=source_type,
                url=url,
                city=item.get("city"),
                region=item.get("region"),
                organization=item.get("organization"),
                description=item.get("description"),
                verification_status=item.get(
                    "verification_status", Source.STATUS_VERIFIED
                ),
                discovery_method=item.get("discovery_method", "manual"),
            )
        )
        existing_urls.add(url.lower())
        added += 1

    db.session.commit()
    return added


if __name__ == "__main__":
    from app import app

    with app.app_context():
        db.create_all()
        count = seed_database()
        total = Source.query.count()
        websites = Source.query.filter_by(source_type=Source.WEBSITE).count()
        vk = Source.query.filter_by(source_type=Source.VK).count()
        print("Добавлено новых записей:", count)
        print("Всего в базе:", total, f"(сайты: {websites}, VK: {vk})")
