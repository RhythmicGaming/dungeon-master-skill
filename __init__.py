from mycroft import MycroftSkill, intent_file_handler
import requests

class DungeonMaster(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('master.dungeon.intent')
    def handle_master_dungeon(self, message):
        spell = str(message.data.get('spell'))
        spell = spell.replace(" ", "-")
        url = "http://dnd5eapi.co/api/spells/" + spell
        url = url + "/"
        try:
            resp = requests.get(url)
            description = (resp.json()["desc"])
            description = description[0].strip("'['")
            final = description.strip("']'")
            skilloutput = str(final)
            print(skilloutput)
        except:
            skilloutput = "the dm does not know the spell" + spell

        data = {'skilloutput' : skilloutput,
                'spell': spell
                }
        self.speak_dialog(skilloutput, data)


def create_skill():
    return DungeonMaster()
