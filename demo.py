from text_handling.text_handling import TextHandling


def main():
    text = "Hola, mundo!"
    print(f"Original text: {text}")
    print(f"Reversed text: {TextHandling.reverse(text)}")
    print(f"Uppercase text: {TextHandling.to_upper(text)}")
    print(f"Vowel count: {TextHandling.count_vowels(text)}")
    concatenated = TextHandling.concat("Hola", "Mundo")
    print(f"Concatenated text: {concatenated}")


if __name__ == "__main__":
    main()