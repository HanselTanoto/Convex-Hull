# Pustaka _Convex-Hull_ Menggunakan Algoritma _Divide and Conquer_
## Deskripsi Singkat
Himpunan titik pada bidang planar (2D) dapat disebut _convex_ jika untuk sembarang 2 titik pada bidang tersebut, misalnya p dan q, seluruh segmen garis yang berakhir di p dan q berada pada himpunan tersebut. Atau dengan kata lain, _Convex hull_ adalah sebuah poligon yang tersusun dari subset himpunan titik sedemikian sehingga tidak ada titik dari himpunan awal yang berada di luar poligon tersebut dan jika digambarkan garis yang menghubungkan sembarang titik pada himpunan titik awal, tidak ada garis yang memotong garis batas luar dari poligon tersebut. 

Pustaka _Convex Hull_ ini memanfaatkan algoritma _divide and conquer_, lebih tepatnya algoritma _Quickhull_, untuk menghasilkan sebuah _convex hull_ dari suatu kumpulan data 2 dimensi yang dapat dianggap sebagai himpunan titik. Pustaka ini terletak pada _folder_ src dengan nama _file_ `myConvexHull.py`. Pustaka ini juga dilengkapi dengan _driver_ untuk mencoba penggunaan pustaka tersebut. Terdapat 2 _file driver_ yang terletak pada folder src yaitu _file_ `driver_Iris.py` yang merupakan _driver_ untuk dataset Iris saja dan _file_ `driver_General.py` yang dapat digunakan untuk 4 buah dataset. Empat dataset tersebut yaitu dataset _Iris_, _Wine_, _Digits_, dan _Breast Cancer_ yang diperoleh dari [scikit-learn](https://scikit-learn.org/stable/datasets/toy_dataset.html).

## _Requirement_ Program
1. Program ini menggunakan bahasa pemrograman __Python__
2. Program ini dapat dijalankan pada sistem operasi __Windows__
3. Program ini dapat dijalankan melalui __Command Prompt (cmd)__ dan __Windows Powershell__
4. _Driver_ pada pustaka ini menggunakan beberapa _library_ yang harus di-_install_ terlebih dahulu, yaitu __numpy__, __pandas__, __matplotlib__, dan __scikit-learn__.

## Cara Menggunakan Pustaka
1. Unduh _zip file_ dari _repository_ ini lalu di_extract_ atau _clone repository_ ini menggunakan _command_:
   ```
   git clone https://github.com/HanselTanoto/Convex-Hull.git
   ```
2. Salin file myConvexHull pada directory program yang ingin menggunakan pustaka ini.
3. _Import_ file pustaka ini pada program yang ingin menggunakaannya dengan mengetikkan `import myConvexHull`.
4. Penggunaan pustaka dapat dilakukan dengan mengetikkan `myConvexHull.myConvexHull(Array_of_Point)` dengan `Array_of_Point` adalah array titik-titik yang ingin dicari _convex hull_-nya. Baris kode tersebut akan mengembalikan sebuah objek dari kelas `myConvexHull`.
5. Garis-garis (pasangan titik) pembentuk _convex hull_ dapat diakses pada atribut `simplices` dari objek tersebut. 
Untuk lebih lengkapnya, dapat dilihat implementasi pada _file driver_ yaitu `driver_General.py` atau pada dokumentasi di _folder_ `doc`

## Cara Menggunakan Driver
1. Unduh _zip file_ dari _repository_ ini lalu di_extract_ atau _clone repository_ ini menggunakan _command_:
   ```
   git clone https://github.com/HanselTanoto/Convex-Hull.git
   ```
2. Buka terminal lalu ubah directory ke folder src pada program ini
3. _Install library_ yang terdapat pada _requirement_ program dengan _command_:
   ```
   pip install numpy
   pip install pandas
   pip install matplotlib
   pip install -U scikit-learn
   ```
4. Jalankan program _driver_ dengan mengetikkan _command_:
   ```
   python driver_General.py
   ```
   Saat pertama kali dijalankan, waktu menunggu mungkin akan lebih lama karena program akan me-_load_ dataset.
5. _User_ akan diminta memasukkan nomor pilihan dataset dan pasangan atribut.
6. Selanjutnya akan  muncul jendela berisi visualisasi dari _convex hull_.
7. Setelah menutup jendela gambar tadi, akan muncul konfirmasi pada layar terminal untuk melanjutkan atau tidak.
   - Ketik 'Y' atau 'y' untuk membuat _convex hull_ dari atribut yang lain untuk dataset yang sama.
   - Ketik 'N' atau 'n' untuk keluar dari program. 

## Author
[Hansel Valentino Tanoto](https://github.com/HanselTanoto) - K-01 / 13520046
