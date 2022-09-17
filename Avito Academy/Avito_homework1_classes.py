class CountVectorizer:
    """
    - метод fit_transform
        принимает текстовый корпус
        возвращает терм-документную матрицу
    - метод get_feature_names
        ничего не принимает
        возвращает список фичей (уникальных слов из корпуса)
    """
    def get_features(self, text_corpus: list) -> list:
        features = list(set((' '.join(text_corpus).lower()).split()))
        return features

    def fit_transform(self, text_corpus: list) -> list:
        self.corpus = text_corpus
        features = self.get_features(text_corpus)
        term_matrix = [[0 for i in range(len(features))] for j in range(len(text_corpus))]

        for k in range(len(text_corpus)):
            for word in text_corpus[k].split():
                sentence = ''.join(text_corpus[k]).lower()
                low_word = word.lower()
                term_matrix[k][features.index(low_word)] = sentence.count(low_word)

        return term_matrix

    def get_feature_names(self) -> list:
        return self.get_features(self.corpus)


corpus = [
    'Crock Pot Pasta Never boil pasta again',
    'Pasta Pomodoro Fresh ingredients Parmesan to taste'
]

vectorizer = CountVectorizer()
count_matrix = vectorizer.fit_transform(corpus)

print(vectorizer.get_feature_names())
print(count_matrix)
