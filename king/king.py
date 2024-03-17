# from art import logo


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

"""TODO: pastda yozilgan funksiyani hammadan so'rayman qanday ishlayotganini!!!"""
def shriftlash(text, shift_number, shriftlash_turi):
    result_text = ""
    if shriftlash_turi == "decode":
        shift_number *= -1
    for harf in text:
        if harf in alphabet:
            position = alphabet.index(harf)  # alphabetdagi harfni indexini oldim
            new_position = position + shift_number  # bunda alphabetdagi harfga shrift raqamni qo'shgandan keyingi harfni indexini oldim
            result_text += alphabet[new_position]
        else:
            result_text += harf
    print(f"Mana senga tanlagan {shriftlash_turi} bo'yicha yaratilgan text: {result_text}")


# print(logo)
# encode  hello ???!>
# decode
is_finished = False
while not is_finished:
    shriftlash_turi = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()  # hello
    shift = int(input("Type the shift number:\n"))  # 45

    # TODO: agar shift raqam alphabetdagi harflar sonidan katta bo'lsa, nima bo'lish kerak. Yordam % modulus belgisidan foydalansayiz bo'ladi.
    if len(text) >= len(alphabet) and shriftlash_turi == "encode":
        num = len(text) % len(alphabet)
        alphabet = alphabet * num

    shriftlash(text, shift, shriftlash_turi)
     # TODO: program tugagandan keyin yana so'rash yes yoki no degan savol bilan
    tugatish = input("Tugatish (ha yoki yo'q) :").lower()
    if tugatish == "ha":
        is_finished = True