class MyString:
    def __init__(self, value=''):
        self.value = value  

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:

            print("The value must be a string.")
            
        

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        sentences = []
        new_sentence = []

        for char in self.value:
            if char in '.!?':
                if new_sentence:
                    sentences.append(''.join(new_sentence).strip())
                    new_sentence = []
            else:
                new_sentence.append(char)

        if new_sentence:  # Add the last sentence if there's any
            sentences.append(''.join(new_sentence).strip())

        return len([s for s in sentences if s])
