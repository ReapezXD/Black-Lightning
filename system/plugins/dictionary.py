from system.Config.utils import Variable
from PyDictionary import PyDictionary

from system.decorators import on_cmd
from system import (
    app,
    COMMAND_HELP,
    HNDLR
)

mean = ""

@on_cmd(["dict", "define", "meaning"])
@on_cmd(["dict", "define", "meaning"], sudo=True, sudo_ids=Variable.SUDO_IDS)
async def dc(client, message):
    if  not message.text:
        await message.edit_message_text("**How could i define nothing?**")
        return
    txt = message.text.split()[1]
    meana = PyDictionary()
    meaning = meana.meaning(txt)
    for i in meaning:
        mean += "\n" + i
    await app.send_message(message.chat_id, f"__Meaning__{mean}")
   
COMMAND_HELP.update({
    "dictionary": f"`{HNDLR}dict or define or meaning`",
    "dictionary's help": "**Gets the meanign of that word from dictonary**"
})