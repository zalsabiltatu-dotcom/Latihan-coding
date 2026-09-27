public class Main {
    int age; 
    int berat;
    String nama;
    
    public Main(int age, int berat, String nama) {
        this.age = age;
        this.berat = berat;
        this.nama = nama;
    }

    public Main(int berat, String nama) {
        this(12, berat, nama);
    }

    public Main(String nama, int age) {
        this(age, 60, nama);
    }

    public Main(String nama) {
        this(12, 60, nama);
    }

    public void tampil() {
        System.out.println("umur saya " + age + " berat saya " + berat + " nama saya " + nama);
    }

    public static void main(String[] args) {
        Main ob1 = new Main(12, 40, "ulfa");
        Main ob2 = new Main(20, "Andi");
        Main ob3 = new Main("Budi", 22);
        Main ob4 = new Main("Siti");

        ob1.tampil();
        ob2.tampil();
        ob3.tampil();
        ob4.tampil();
    }
}