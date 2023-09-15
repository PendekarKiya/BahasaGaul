meme = {
    'gabut' : 'ga ada kerjaan',
    'mager' : 'malas gerak',
    'ygy' : 'ya guys ya...',
    'kepo' : 'pengen tau aja',
    'mantul' : 'mantap betul',
    'gaje' : 'ga jelas'
}

for i in range (5):
    word = input("Ketik kata yang tidak Kamu mengerti: ")
    if word in meme.keys():
        print(meme[word])
    else:
        print("maaf, kata yang anda tulis tidak ada di kamus mohon coba sekali lagi")
