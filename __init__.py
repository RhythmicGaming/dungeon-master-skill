from mycroft import MycroftSkill, intent_file_handler


class DungeonMaster(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('master.dungeon.intent')
    def handle_master_dungeon(self, message):
        spell = message.data.get('spell')

        self.speak_dialog('master.dungeon', data={
            'spell': spell
        })


def create_skill():
    return DungeonMaster()

