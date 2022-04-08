print('Ibu memberi perintah "Beli 1 Botol Susu"')
print('Anak menjawab, "Ok"')
print('Anak pergi ke toko')
print('Apakah susu ada?')

pilihan = ['ada']
jawaban = input('ada?')
if (jawaban in pilihan) :
    print('Anak mengecek harganya, cukup')
    print('apakah ada telur?')

    pilihan = ['ada']
    jawaban = input('ada?')
    if (jawaban in pilihan):
        print('Anak membeli satu botol susu dan 6 butir telur')
    else:
        print('Anak membeli satu botol susu')
else:
    print('Anak tidak jadi membeli susu')
print('Menyerahkan hasil belanjaan kepada ibu')