// #include <iostream>
// #include <iomanip>
// using namespace std;

// int main() {
//     int jumlah_buku = 3;
//     int harga_buku = 45000;
//     int jumlah_pulpen = 2;
//     int harga_pulpen = 7500;
//     int jumlah_tas = 1;
//     int harga_tas = 120000;
//     double Diskon = 0.1;

//     double total_belanja = (jumlah_buku * harga_buku) + (jumlah_pulpen * harga_pulpen) + (jumlah_tas * harga_tas);
//     std::cout << "Total belanja: Rp " << std::fixed << std::setprecision(0) << total_belanja << std::endl;

//     total_belanja -= total_belanja * Diskon;
//     std::cout << "Total belanja setelah diskon: Rp " << std::fixed << std::setprecision(0) << total_belanja << std::endl;

//     return 0;
// }



// #include <iostream>
// using namespace std;

// int main() {
//     int tabungan = 50000;
//     tabungan *= 3;
//     tabungan -= 30000;
//     tabungan += 50000;

//     std::cout << "Total tabungan: Rp " << tabungan << std::endl;
//     return 0;
// }



// #include <iostream>
// using namespace std;

//   int main() {
// int umur = 18;
//     if (umur >= 17) 
//         std::cout << "Anda sudah cukup umur untuk membuat KTP." << std::endl;
//     return 0;
//   }



//   #include <iostream>
// using namespace std;

//   int main() {
// int umur = 18;
//     if (umur >= 17) 
//        cout << "Anda sudah cukup umur untuk membuat KTP." << endl;
//     else
//         cout << "Anda belum cukup umur untuk membuat KTP." << endl;
//     return 0;
//   }



// #include <iostream>
// using namespace std;

// int main() {
// int nilai = 85;
//     if (nilai == 100) 
//         cout << "Nilai Anda sempurna." << endl;
//     else if (nilai >= 75) 
//         cout << "Anda lulus." << endl;
//     else 
//         cout << "Anda tidak lulus." << endl;
//     return 0;
// }



// #include <iostream>
// using namespace std; 

// int main() {
//     int nilai = 85;
//     if (nilai >= 90) 
//         cout << "Nilai Anda A." << endl;
//     else if (nilai >= 80) 
//         cout << "Nilai Anda B." << endl;
//     else if (nilai >= 70) 
//         cout << "Nilai Anda C." << endl;
//     else 
//         cout << "Nilai Anda D." << endl;
//     return 0;
// }



#include <iostream>
using namespace std;

int main() {
    int nilai = 90;

    switch (nilai / 10) {
        case 10:
        case 9:
            cout << "Nilai Anda A." << endl;
            break;

        case 8:
            cout << "Nilai Anda B." << endl;
            break;

        case 7:
            cout << "Nilai Anda C." << endl;
            break;

        default:
            cout << "Nilai Anda D." << endl;
    }

    return 0;
}