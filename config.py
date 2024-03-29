"""
config_example.py. Данные со значениями должны быть обязательно указаны.
Списки снизу можно дополнять своими данными.
"""
import discord,time

settings = {
    'token': 'TOKEN',
    'app_id': 977280463792115833, # Application ID вашего бота.
    'key': 'Ключ some-random-api.md',
    'weather_key': 'Ключ openweathermap.org',
    'support_invite': 'https://discord.gg/wX6CxW8J', # Ссылка на сервер поддержки.
    'owner_id': 754719910256574646, # ID владельца.
    'server': 796449686986424340, # Сервер логов.
    'log_channel': 797188770184429608, # Канал логирования.
    'perm_scope': 8, # Permission Integer.
    'outages': 797188770184429608, # ID канала с оповещениями о сбоях.
    'github_channel': 940317991483080765, # ID канала обновлений репозитория.
    'idea_channel': 797183341513277460, # ID канала, в который будут публиковаться идеи.
    'curr_version': "0.9 Alpha [ARTAMON EDITION]", # Текущая версия MadBot.
    'cmd-log-id': 797188770184429608,
    'developers': [560529834325966858]
}

started_at = int( # Время запуска бота. Не изменять.
    time.mktime(
        discord.utils.utcnow().timetuple()
    ) + 10800
) 
lastcommand = "Ещё ни разу команды не использовались."
used_commands = 0 # Счетчик использованных команд. Не трогать.

cogs = [ # Список cog'ов.
    "cogs.entartaiment",
    "cogs.moderation",
    "cogs.tools",
    "cogs.developerzone"
]

errload_cogs = [
    
]

blacklist = [ # ID сервера/участника, который в ЧС бота.
    
]
supports = [ # ID сотрудников поддержки.
    
]
verified = [ # ID верифицированных серверов/участников.
    
]
beta_testers = [ # ID серверов, учавствующих в бета-тесте.
    
]
bug_hunters = [ # ID баг-хантеров.
    
]
bug_terminators = [ # ID баг-терминаторов.
    
]
testserver = [ # Тестовые сервера в формате discord.Object(id=ID).
     
]
shutted_down = [ # Названия слеш-команд, которые должны быть отключены.

]


slap_gifs = [ # Гифки шлёпа.
    "https://cdn.discordapp.com/attachments/707201738255368194/847553281852702770/tenor_1.gif",
    "https://cdn.discordapp.com/attachments/707201738255368194/847553382339182642/tenor_2.gif",
    "https://cdn.discordapp.com/attachments/707201738255368194/847553413319098418/tenor_3.gif",
    "https://cdn.discordapp.com/attachments/707201738255368194/847553484949553202/tenor_4.gif",
    "https://cdn.discordapp.com/attachments/707201738255368194/847553521683529758/tenor_5.gif",
    "https://cdn.discordapp.com/attachments/707201738255368194/847553545632612443/tenor_6.gif",
    "https://cdn.discordapp.com/attachments/707201738255368194/847553662780047421/tenor_12.gif",
    "https://cdn.discordapp.com/attachments/707201738255368194/847554139943731250/tenor_23.gif",
    "https://cdn.discordapp.com/attachments/707201738255368194/847554219648352266/tenor_24.gif"
]
kiss_gifs = [ # Гифки поцелуя.
    "https://i.imgur.com/a66k9c7.gif",
    "https://cdn.discordapp.com/attachments/956616897363869796/967834319160750111/animesher.com_kiss-anime-love-tender-kiss-766612.gif",
    "https://cdn.discordapp.com/attachments/956616897363869796/967834665568305162/d0cd64030f383d56e7edc54a484d4b8d.gif",
    "https://cdn.discordapp.com/attachments/956616897363869796/967834666021310534/giphy.gif",
    "https://cdn.discordapp.com/attachments/956616897363869796/967834666277175296/kiss-anime.gif",
    "https://cdn.discordapp.com/attachments/956616897363869796/967834666709164123/tumblr_0cd93127b3eee8352ca2a5a66349bcdb_0d2f4ba2_500.gif"
]
hit_gifs = [ # Гифки удара.
    "https://cdn.discordapp.com/attachments/956616897363869796/967842754828861470/2ce5a017f6556ff103bce87b273b89b7.gif",
    "https://cdn.discordapp.com/attachments/956616897363869796/967842755147624468/anime.gif",
    "https://cdn.discordapp.com/attachments/956616897363869796/967842755697049600/anime-hit.gif",
    "https://cdn.discordapp.com/attachments/956616897363869796/967842755978100786/animesher.com_hitting-toradora-funny-1701058.gif",
    "https://cdn.discordapp.com/attachments/956616897363869796/967842756288475277/head-hit-anime.gif",
    "https://cdn.discordapp.com/attachments/956616897363869796/967842756590444624/hit.gif",
    "https://cdn.discordapp.com/attachments/956616897363869796/967842756875673710/hit-anime.gif",
    "https://cdn.discordapp.com/attachments/956616897363869796/967842757148278864/hit-head-anime.gif"
]
