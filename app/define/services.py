from PyDictionary import PyDictionary
import json

class DefineService:

    dictionary = PyDictionary()

    def __init__(self):
        return

    def meaning(self, word):
        definition = self.dictionary.meaning(word)
        """ Changes key names to lower case """
        if (definition is None):
            print('DEFINITION NOT FOUND')
            definition = {}
        else:
            if 'Adjective' in definition:
                definition['adjective'] = definition.pop('Adjective')
            if 'Adverb' in definition:
                definition['adverb'] = definition.pop('Adverb')
            if 'Noun' in definition:
                definition['noun'] = definition.pop('Noun')
            if 'Verb' in definition:
                definition['verb'] = definition.pop('Verb')
        return definition
