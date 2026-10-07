class Solution:
    def getWordCharacters(self, s: str):
        wordCharacters = {}

        for character in s:
            characterCount = wordCharacters.get(character)

            if characterCount == None:
                characterCount = 1
            else:
                characterCount += 1
            
            wordCharacters[character] = characterCount

        return wordCharacters

    def isAnagram(self, s: str, t: str) -> bool:
        firstWordCharacters = self.getWordCharacters(s)
        secondWordCharacters = self.getWordCharacters(t)

        return firstWordCharacters == secondWordCharacters