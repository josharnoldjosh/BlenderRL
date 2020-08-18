from parlai.agents.transformer.transformer import TransformerGeneratorAgent
from custom.opt import opt as blender_opt


class Blender(TransformerGeneratorAgent):

    def __init__(self):
        super().__init__(blender_opt, None)

    def listen(self, utt):
        self.observe({'text': utt, 'episode_done': False})

    def speak(self):
        res = super().act()
        return res['text']


blender = Blender()
blender.reset()
blender.listen("Hey, how are you?")
utt = blender.speak()
print(utt)