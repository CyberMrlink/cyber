import random
import sys
import time
g = "\033[32;1m" 
gt = "\033[0;32m" 
bt = "\033[34;1m" 
b = "\033[36;1m" 
m = "\033[31;1m" 
c = "\033[0m" 
p = "\033[37;1m" 
u = "\033[35;1m" 
M = "\033[3;1m" 
k = "\033[33;1m" 
kt = "\033[0;33m" 
a = "\033[30;1m" 
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#kecepatan mengetik
        time.sleep(random.random() * 0.1)
mengetik('MRLINKERRORSYSTEM,\n')
mengetik('Selamat Datang Di Bucin Error system')
mengetik('SAYA DISINI INGIN BUCIN UNTUK KALIAN')
mengetik('Cinta adalah saat kamu kehilangan suatu rasa dan romantika akan tetapi kamu masih bisa tetap peduli pada dirinya.')
mengetik('Aku bahagia karena kamu, maka ijinkanlah aku untuk terus berada di hatimu selamanya.Dengan mencintaimu aku tidak pernah merasa takut, selama kau dan aku masih berada di bawah langit yang sama.Kau tidak pernah jauh dariku, walaupun aku pergi kamu selalu ada mengikutiku. Karena kamu selalu di hatiku, yang jauh hanyalah raga kita, dan bukan hati kita.Cinta hanyalah sebuah ungkapan dari rasa sayang semata, tapi dengan perbuatan itu akan membuktikan bahwa cinta itu memang ada.Hanya perlu waktu semenit untuk menyukaimu, sebulan untuk mencintaimu. Akan tetapi perlu waktu seumur hidup untuk melupakanmu.Kata kata yang lemah dan beradap dapat melembutkan hati manusia yang kerasnya seperti batu.Dalam hal percintaan, janganlah hanya menunggu orang yang tepat menghampiri kehidupanmu. Sebaiknya jadilah orang yang tepat yang menghampiri hidup seseorang.Hanya cinta yang bisa memudar dengan seiringnya waktu, tetapi hanya kasih sayang yang akan terus abadi.Wahai kekasihku, seberat apapun beban yang tengah kita hadapi. Percayalah, aku akan selalu ada untuk memikulnya bersamamu.Aku memang tidak bisa membaca pkiranmu namun aku bisa mencintaimu dengan segenap hatiku.Cinta tidak hanya tatapan satu sama lain tapi bisa memandang ke luar bersama, dan ke arah yang sama.Hidupku akan terasa rapuh jika itu tanpa dirimu.Aku tak pernah jauh darimu, karena aku selalu berada di dalam hatimu.Jatuh dan gagal itu merupakan hal yang sudah biasa namun  jatuh pada satu hati itu baru hal yang luar biasa, dan itu hanya kepadamu.Cinta adalah ketika kita merasakan adanya getaran suatu rasa yang tidak bisa diungkapkan dengan kata-kata.Jika kau bersamaku maka akan kuberikan cinta sejatiku untukmu selamanya.Lebih baik memilih orang yang mencintai kita dengan tulus daripada memilih orang yang kita cintai, dan lebih baik melihat pada orang yang berkorban demi kita daripada harus berkorban namun sia².Mungkin aku lahir di dunia ini untuk mencintaimu dan kau terlahir di dunia untuk kucintai.Cinta sejati adalah ketika hatimu dan pikiranmu mengatakan hal yang sama dengan dirinya.Jangan jadikan keindahannya sebagai alasanmu untuk mencintainya, tapi jadikanlah mencintai itu sebagai alasanmu untuk melihat keindahannya.Cintailah seseorang atas dasar siapa dia sekarang dan bukan siapa dia sebelumnya, kisah kelam tidak perlu diungkit kembali kalau kamu bernar-benar mencintai dirinya dengan setulus hatimu.Jika kamu tulus mencintai dirinya,janganlah pernah kau hiasi matanya dengan air mata,telinganya dengan dusta, dan hatinya dengan luka.Cinta itu memang buta, karena cinta tidak bisa dilihat oleh mata namun cinta itu tentang rasa.Di dunia ini tak hanya ada satu cinta namun banyak hingga tak terkira, tapi cinta itu hanya cinta biasa jika tanpa adanya ketulusan.Ketika dia telah bersungguh-sungguh mencintaimu dan menyayangimu, dia pasti tidak akan sempat memikirkan untuk memberikan hatinya untuk orang lain.Mungkin kau tak pernah tau, bahwa sesungguhnya rasa ini selalu hadir untukmu.Aku mencintaimu seperti setiap kali aku bernafas. Bila tiba saatnya aku berhenti bernafas, kau tahu bahwa itu adalah cinta terakhirku.Saat kamu mampu membuat aku tersenyum bahagia, itulah salah satu dari banyak hal yang aku suka dari dirimu.Mencintai dan dicintai adalah suatu anugerah dari Tuhan, tapi cinta yang sejati bukanlah sekedar ucapan namun disertai dengan pengorbanan.Cinta bukan hanya tentang memberi kebahagian namun berani berkata jujur jika ada suatu keputusan yang salah.Jika suatu saat jarak memisahkan kita, satu hal yang perlu kamu percaya dariku. Akan kujaga cinta ini hanya untukmu.Lembutnya hatimu mampu meluluhkan hatiku, akupun tersadar bahwa aku telah jatuh cinta padamu.Aku hanyalah manusia biasa yang tidak sempurna, namun kau telah membuatku sempurna dengan segenap cinta yang kau bawa.Cintaku padamu bagaikan garam di lautan yang luas, walaupun tidak terlihat namun akan selalu ada untuk selamanya.Mungkin aku telah ditakdirkan menjadi buta, buta untuk melihat wanita lain selain dirimu seorang.Mataku terpejam bukannya untuk mengabaikanmu namun hanya ingin melihatmu lebih dalam.Aku tidak mau menjadi yang nomor satu di hatimu, yang aku mau hanya ada aku seorang di dalam hatimu.Mencintaimu membuatku mengerti akan rasa sakit dan bahagia, dan mengerti arti memiliki dan dimiliki. Serta komitmen dan kesetiaan.Kata banyak orang cinta itu tidak harus memiliki, namun semua orang berhak untuk memiliki rasa cinta.Saat kita pertama kali bertemu, kamu selalu ada di hatiku. Waktu berjalan bersama bayangmu, aku ingin selalu dekat dengan dirimu.')
import random
import curses

s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

snk_x = sw/4
snk_y = sh/2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

food = [sh/2, sw/2]
w.addch(food[0], food[1], curses.ACS_PI)

key = curses.KEY_RIGHT

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0, sh] or snake[0][1]  in [0, sw] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')

    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
