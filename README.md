# Hajriansah_F55121046_UAS_PAA2

Analisis Bubble sort dan insertion sort

A. Bubble Sort:
   1. Worst Case terjadi ketika elemen-elemen dalam array terurut secara terbalik atau dalam urutan terbalik. Dalam kasus ini, algoritma akan melakukan iterasi penuh dan pertukaran pada setiap pasangan elemen hingga mencapai urutan yang benar. Kompleksitas waktu worst case bubble sort adalah O(n^2), di mana n adalah jumlah elemen dalam array.
   2. Best Case terjadi ketika elemen-elemen dalam array sudah dalam urutan yang benar. Dalam kasus ini, algoritma akan melakukan iterasi penuh, tetapi tidak ada pertukaran yang perlu dilakukan karena elemen sudah dalam urutan yang benar. Kompleksitas waktu best case bubble sort adalah O(n), di mana n adalah jumlah elemen dalam array.
   3. Average Case pada bubble sort dapat dianggap sebagai kasus ketika elemen-elemen dalam array tersebar secara acak. Dalam kasus ini, algoritma akan melakukan beberapa iterasi dan pertukaran untuk mendapatkan urutan yang benar. Kompleksitas waktu average case bubble sort adalah O(n^2), di mana n adalah jumlah elemen dalam array.
      
B. Insertion Sort:
   1. Worst Case terjadi ketika elemen-elemen dalam array terurut secara terbalik atau dalam urutan terbalik. Dalam kasus ini, setiap elemen harus disisipkan ke posisi yang benar dengan memindahkan elemen-elemen lain ke kanan. Kompleksitas waktu worst case insertion sort adalah O(n^2), di mana n adalah jumlah elemen dalam array.
   2. Best Case terjadi ketika elemen-elemen dalam array sudah dalam urutan yang benar. Dalam kasus ini, algoritma hanya perlu memeriksa setiap elemen satu kali tanpa perlu memindahkan elemen mana pun. Kompleksitas waktu best case insertion sort adalah O(n), di mana n adalah jumlah elemen dalam array.
   3. Average Case pada insertion sort dapat dianggap sebagai kasus ketika elemen-elemen dalam array tersebar secara acak. Dalam kasus ini, algoritma harus memeriksa setiap elemen dan memindahkan beberapa elemen untuk menyisipkan setiap elemen pada posisi yang benar. Kompleksitas waktu average case insertion sort adalah O(n^2), di mana n adalah jumlah elemen dalam array.

Analisis TSP dan Dijkstra

A. TSP
   1. Worst case terjadi ketika semua kemungkinan kombinasi jalur diuji. Sebagai contoh, jika terdapat N node dalam graf, maka terdapat N! kemungkinan jalur yang harus diperiksa. Oleh karena itu, kompleksitas waktu algoritma TSP adalah O(N!).
   2. Best Case terjadi ketika graf hanya memiliki 2 node, yaitu start node dan end node. Dalam hal ini, algoritma TSP akan langsung menghasilkan jalur yang optimal tanpa perlu melakukan perhitungan tambahan. Oleh karena itu, kompleksitas waktu algoritma TSP dalam best case adalah O(1).
   3. Average Case atau rata-rata kasus terjadi ketika graf memiliki node yang tersebar dengan berbagai kemungkinan koneksi. Kompleksitas waktu algoritma TSP adalah O(N!), di mana N adalah jumlah node dalam graf. Oleh karena itu, waktu eksekusi algoritma TSP cenderung meningkat secara eksponensial seiring bertambahnya jumlah node.

B. Dijkstra
   1.  Worst Case terjadi ketika setiap node dihubungkan dengan semua node lainnya dalam graf. Dalam kasus ini, Dijkstra harus mengunjungi setiap node dan memeriksa semua kemungkinan jalur. Oleh karena itu, kompleksitas waktu algoritma Dijkstra adalah O(N^2), di mana N adalah jumlah node dalam graf.
   2.  Best Case terjadi ketika start node dan end node berada dalam satu komponen terhubung langsung tanpa ada node lain di antaranya. Dalam hal ini, Dijkstra hanya perlu memeriksa langsung jalur antara start node dan end node tanpa melibatkan node lain. Oleh karena itu, kompleksitas waktu algoritma Dijkstra dalam best case adalah O(1).
   3.  Average Case algoritma Dijkstra tergantung pada struktur graf dan panjang jalur terpendek antara start node dan end node. Jika graf jarang terhubung dan panjang jalur terpendek relatif pendek, maka algoritma Dijkstra dapat berjalan dengan cepat. Namun, jika graf padat terhubung dan panjang jalur terpendek relatif panjang, waktu eksekusi Dijkstra akan meningkat. Kompleksitas waktu algoritma Dijkstra adalah O(N^2), di mana N adalah jumlah node dalam graf.


