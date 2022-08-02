import logging

from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_webhook
from bot.settings import (BOT_TOKEN, HEROKU_APP_NAME,
                          WEBHOOK_URL, WEBHOOK_PATH,
                          WEBAPP_HOST, WEBAPP_PORT)

bot = Bot(token="1614394875:AAH2iQCvs6_e3ob_t8CYuVEkuWtff2vvuWY")
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())
import os

 

button0 = InlineKeyboardButton(text="👋 Tutorial", callback_data="tutorial")
button1 = InlineKeyboardButton(text="Pengertian Arsip", callback_data="pengertian_arsip")
button2 = InlineKeyboardButton(text="Fungsi Arsip", callback_data="fungsi")
button3 = InlineKeyboardButton(text="Tujuan Arsip", callback_data="tujuan")
button4 = InlineKeyboardButton(text="Penggolongan Arsip", callback_data="penggolongan")
button5 = InlineKeyboardButton(text="Nilai Guna Arsip", callback_data="nilai")
button6 = InlineKeyboardButton(text="Daur Hidup Arsip", callback_data="daur")
button7= InlineKeyboardButton(text="Latihan Soal", callback_data="latihan")
button8 = InlineKeyboardButton(text="Tentang", callback_data="tentang")
keyboard_inline = InlineKeyboardMarkup().add(button0,button1, button2,button3,button4,button5,button6,button7,button8)

keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("👋 Kembali ke Menu!")


@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
 
    await message.reply("Halo! Selamat datang di Bot Kearsipan.\nPilih Menu dibawah ini ya👋", reply_markup=keyboard_inline)

@dp.callback_query_handler(text=["tutorial","pengertian_arsip", "fungsi","tujuan","penggolongan","nilai",'daur','latihan','tentang'])
async def random_value(call: types.CallbackQuery):
    if call.data == "tutorial":
        await call.message.answer("""Penggunaan Bot ini cukup mudah, click menu pada Botnya!""",reply_markup=keyboard1)
    if call.data == "pengertian_arsip":
        await call.message.answer("""
Pengertian Arsip.
Arsip dapat dikatakan sebagai sebuah kumpulan rekaman informasi dari kegiatan organisasi atau perusahaan. Biasanya rekaman tersebut digunakan juga untuk keperluan pengambilan keputusan pimpinan.

“Archive” merupakan kata arsip berasal dari Bahasa Inggris dan “Archium” berasal dari Bahasa Latin Kuno, artinya suatu tempat penyimpanan arsip pemerintah, dimana arsip sebagai tanda bukti, dokumen, atau warkat dengan keterangan tertentu.

Sementara itu, arti dari kearsipan sendiri yakni suatu kegiatan menyimpan surat atau dokumen. Kegiatan tersebut berkaitan dengan kegiatan penerimaan, pencatatan, pengiriman, serta pemusnahan surat dan dokumen. Kearsipan sangat penting dalam suatu organisasi atau perusahaan. Hal ini telah disadari oleh seluruh pihak yang terkait. Apabila suatu organisasi tidak melakukan kearsipan pasti akan menimbulkan permasalahan baru bagi organisasi atau perusahaan tersebut. Misalnya saja, ketika organisasi memiliki banyak surat atau dokumen, jika tidak ada kearsipan maka surat atau dokumen tersebut akan menumpuk dan itu akan menghambat proses pencarian sewaktu dibutuhkan. Ditambah lagi jika pimpinan sangat membutuhkan surat atau dokumen tersebut untuk urusan yang sangat penting, pasti sangatlah sulit mencarinya.
""",reply_markup=keyboard1)
    if call.data == "fungsi":
        await call.message.answer("""
Fungsi Arsip!
DILIHAT DARI KEGIATANNYA
1. Sebagai alat penyimpanan warkat;
2. Sebagai alat bantuan perpustakaan;
3. Penyimpanan warkat-warkat keputusan sesudah diambil, atau dasar dalam 
pengambilan atau penentian keputusan organisasi atau perusahaan;
4. Sebagai penyimpanan warkat secara teratur dan tetap demi kepentingan mengenai kemajuan perusahaan.

DILIHAT DARI SEGI PENANGANNAN KEARSIPANNYA
1. Dengan adanya arsip, aktifitas organisasi atau perusahaan akan berjalan dengan lancar;
2. Sebagai bukti-bukti tertulis jika terjadi masalah;
3. Sebagai sarana komunikasi secara tertulis;
4. Sebagai bahan dokumentasi;
5. Sebagai alat pengingat;
6. Sebagai alat penyimpanan warkat;
7. Sebagai alat bantu perpustakaan organisasi atau perusahaan jika memilikinya;
8. Sebagai bantuan bagi pimpinan dalam menentukan keputusan organisasiatau perusahaan

Dalam peraturan yang ditetap pemerintah juga terdapat pembagian fungsi arsip, antara lain sebagai berikut:
1. Fungsi Dinamis
Arsip dikatakan sebagai fungsi dinamis apabila penggunaannya dilakukan secara langsung dalam perencanaan, pelaksanaan, penyelenggaraan kegiatan organisasi atau perusahaan. 
2. Fungsi Statis
Arsip dikatakan sebagai fungsi statis apabila penggunaannya tidak dilakukan secara langsung dalam perencanaan, pelaksanaan, penyelenggaraan kegiatan organisasi atau perusahaan.
""",reply_markup=keyboard1)
    if call.data == "tujuan":
        await call.message.answer("""
Tujuan Arsip
Untuk melindungi dan menjamin bahan pertanggungjawaban tentang seluruh kegiatan organisasi atau perusahaan merupakan tujuan umum adanya arsip. Selain itu, adanya arsip juga dijadikan bahan dalam pengambilan keputusan pimpinan organisasi atau perusahaan. 
Oleh karena itu, sebagai wujud untuk merealisasikan tujuan arsip, setiap organisasi atau perusahaan sebaiknya melakukan pelaksanaan kearsipan harus:
1. Menyampaikan arsip dengan aman dan ditemukan dengan mudah jika diperlukan;
2. Menyiapkan arsip ketika diperlukan;
3. Mengumpulkan arsip-arsip yang berkaitan dengan masalah sebagai pelengkap.""",reply_markup=keyboard1)
    if call.data == "penggolongan":
        await call.message.answer("""
Penggolongan Arsip
BERDASARKAN KEASLIANNYA
1. Arsip asli yakni dokumen pertama yang dikerjakan dan dicetak dari mesin ketik atau printer dimana terdapat tandatangan asli dan legalisir asli didalamnya.
2. Arsip tembusan yakni dokumen kedua atau seterusnya dimana pembuatannya bersamaan dengan dokumen asli
3. Arsip salinan yakni dokumen dimana proses pembuatannya tidak bersamaan 
4. dengan dokumen asli, akan tetapo saling berkaitan dengan dokumen asli.

BERDASARKAN KEPENTINNGAN ARSIP
1. Arsip Tidak Penting Dokumen yang didalamnya hanya berisikan pemberitahuan informasi tertentu disebut dengan arsip tidak penting
2. Arsip biasa Dimana sebuah dokumen mempunyai nilai guna saat ini dan masih diperlukan pada waktu yang akan datang dalam jangka waktu 1-5 tahun
3. Arsip penting Dimana sebuah dokumen mempunyai nilai guna berhubungan dengan kegiatan masa lampau dan masa yang akan datang
4. Arsip vital Sebuah dokumen dimana dipakai sebagai pengingat dalam jangka waktu tidak terbatas (abadi)

BERDASARKAN FUNGSI ARSIP
1. Arsip dinamis
2. Arsip statis

BERDASARKAN KEPENTINNGAN ARSIP
1. Arsip tertutup
Sebuah arsip dimana dalam pengelolaan dan perlakuannya berlaku ketentuan tentang kerahasiaan disebut arsip tertutup.
2. Arsip terbuka
Sebuah arsip dimana dalam pengelolaan dan perlakuannya tidak berlaku ketentuan kerahasiaan dan boleh diketahui oleh orang lain
    """,reply_markup=keyboard1)
    if call.data == "nilai":
        await call.message.answer("""
Nilai Guna Arsip
Nilai Guna Primer, meliputi:
1. Nilai Guna Administrasi, dimana arsip digunakan pada kegunaan bagi Pelaksanaan tugas dan fungsi lembaga atau instansi pencipta arsip.
2. Nilai Guna Hukum, berisi bukti-bukti kekuasaan hukum atas hak dan kewajiban warga Negara dan pemerintah.
3. Nilai Guna Keuangan, berisi segala hal mengenai keuangan.
4. Nilai Guna Ilmiah dan Teknologi, mengandung data ilmiah dan teknologi sebagai akibat hasil penelitian.

Nilai Guna Sekunder, meliputi:
1. Nilai Guna Kebuktian, terdapat fakta beserta keterangan dan digunakan untuk menjelaskan mengenai perkembangan organisasi atau perusahaan mulai dari awal pembentukan hingga pengelolaannya. 
2. Nilai Guna Informasional, mempunyai nilai guna informasional untuk berbagai kepentingan penelitian tanpa adanya keterkaitan dengan organisasi atau perusahaan, seperti: orang, tempat, fenomena dan sebagainya.

""",reply_markup=keyboard1)
    if call.data == "sistem":
        await call.message.answer("""
Sistem Penyimpanan Arsip
1. Sistem Wilayah
Suatu sistem penataan arsip dengan menggunakan pembagian wilayah sebagai pedoman untuk menyimpan dan penemuan kembali arsip disebut dengan sistem wilayah. Pembagian wilayah tersebut dipisahkan sesuai dengan asal pengirim atau penerima surat.

2. Sistem Abjad
Suatu sistem penataan arsip dengan menggunakan petunjuk abjad sebagai pedoman untuk menyimpan dan penemuan kembali arsip disebut dengan sistem abjad. Surat akan disimpan berdasarkan nama orang/nama perusahaan/ nama organisasi yang menerima maupun mengirim surat

3. Sistem Kronologis
Suatu sistem penyimpanan dan penemuan kembali arsip berdasarkan tanggal, bulan atau tahun disebut Filing sistem kronologis. Kode penyimpanan dan penemuan kembali di sistem ini menggunakan tanggal, bulan atau tahun pembuatan surat atau tanggal surat pada barisan tanggal dalam arsip itu.

4. Sistem Subyek
Suatu pengelolaan arsip dari penyimpanan dan penemuan kembali arsip (arsip surat masuk maupun arsip surat keluar) berdasarkan subyek atau pokok masalah/perihal dari arsip disebut sistem penyimpanan subyek Penggunaannya banyak dipergunakan oleh instansi-instansi pemerintah yang besar dan luas di Indonesia.

5. Sistem Nomor/ Angka
Sistem penyimpanan arsip sesuai kode nomor yakni sebagai ganti dari nama orang atau badan disebut dengan sistem nomor (numeric filling system). Sistem ini merupakan sistem penyimpanan dan penemuan kembali arsip dengan menggunakan kode angka/nomor.
""")
    if call.data == "daur":
        await call.message.answer("""
Daur Hidup Arsip      
Manajemen kearsipan adalah sebuah kegiatan mengelola arsip, dimana sistem tersebut membentuk terdiri atas unsur-unsur saling berkaitan sehingga membentuk daur hidup arsip (life cycle of record).                           
                 """,reply_markup=keyboard1)
    if call.data == "latihan":
        await call.message.answer("""
Latihan Soal!

Berilah tanda silang (X) pada jawaban yang paling tepat!
1. Kegiatan menempatkan berkas dalam tempat penyimpanan disebut kegiatan ....
a. Pengkodean
b. Penampungan
c. Penelitian
d. Penyortiran 
e. Penyimpanan

2. Arsip yang masih dipergunakan terus menerus bagi kelangsungan pekerjaan dilingkungan unit pengolahan suatu organisasi, meruakan pengertian dari . . .
a. Arsip aktif
b. Arsip inaktif/pasif
c. Arsip statis
d. Arsip sekunder
e. Arsip Primer

3. Alat yang digunakan untuk memisahkan surat/warkat yang diterima, diproses, 
dikirimkan dan disimpan kedalam folder masing-masing disebut ... .
a. Alat sortir
b. Filling cabinet
c. Perforator
d. Label
e. Numerator

4. Folder yang mempunyai besi penggantung disebut ... .
a. Guide
b. Ordner
c. Hanging folder
d. Map snelhecter
e. Stopmap

5. Map arsip yang dilengkapi dengan daun penutup disebut ... .
a. Stopmap folio
b. Folder
c. Hanging folder
d. Snelhecter
e. Ordner

6. Sistem penyimpanan dan penemuan kembali arsip berdasarkan masalah/pokok isi 
surat disebut juga filling sistem ... .
a. Abjad
b. Nomor
c. Subjek
d. Kronologis
e. Wilayah

7. Sistem penyimpanan arsip ada 5 macam, kecuali … .
a. Sistem Abjad
b. Sistem Indeks
c. Sistem Subyek
d. Sistem Nomor
e. Sistem Wilayah

8. Perhatikan langkah-langkah berikut :
i. Mengindeks arsip yang akan dipinjam
ii. Menuju tempat penyimpanan
iii. Kenali arsip yang diminta atau yang diperlukan
iv. Telusuri dengan menggunankan kartu indeks
v. Menempatkan out slip di tempat arsip yang diambil
vi. Mengisi bon peminjam
vii. Menyerahkan arsip kepada yang memerlukan
Adapun langkah-langkah yang benar dalam menemukan kembali arsip yang disimpan 
pada sistem subjek ialah ....
a. i – ii – iii – iv – v – vi – vii
b. ii – iv – iii – i – vi – v – vii
c. iii – i – iv – ii – v – vi – vii
d. iii – i – iv – ii – vi – v – vii
e. iii – iv – ii – i – v – vi – vii

9. Kegiatan menempatkan berkas dalam tempat penyimpanan disebut kegiatan ....
a. Pengkodean
b. Penampungan
c. Penelitian
d. Penyimpanan
e. Penyortiran

10. Apotek Depok
Nama diatas jika disimpan menurut sistem abjad kodenya adalah ....
a. Ad
b. Ak
c. Dep
d. Ap
e. De""",reply_markup=keyboard1)
    if call.data == "tentang":
        await call.message.answer("""
Ini adalah Bot Kearsipan yang memudahkan penggunaan untuk mempelajari tentang kearsipan.
                                  """,reply_markup=keyboard1)
@dp.message_handler()
async def kb_answer(message: types.Message):
    if message.text == '👋 Kembali ke Menu!':
        await bot.send_message(message.chat.id, "Pilih menu!",reply_markup=keyboard_inline)
    else:
        await message.reply(f"Your message is: {message.text}")


def main():
    logging.basicConfig(level=logging.INFO)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
