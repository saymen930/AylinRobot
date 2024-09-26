import random

kelimeler = ["güzel, "bilmek", "soru", "iyileşmek", "gitmek", "zaman", "su", "çatlamak", "çılgın", "görmek",

              "tekrar", "çok", "gerçek", "para", "oyun", "çiçek", "şehir", "yükseliş", "savaş", "olmak", "yapmak",

              "güven", "ihtiyaç", "tedavi", "bir", "rahat", "soğuk", "orada", "kitap", "paylaş", "hesap", "beden",

              "arazi", "fazla", "sistem", "hoş", "geri çekilme", ​​"teknik", "yaklaşma", "salyangoz", "tarih", "açık", "kardeş",

              "ince", "diyor", "görüş", "karşılıklı", "vermek", "sahip olmak", "zaten", "adam", "dyar", "nokta", "tekrar", "bunlar",

              "kitap", "hata", "bul", "sen", "durum", "ileri", "enerji", "bak", "salatalık", "oyun", "kafa", "başla",

              "yakala", "birbirini", "yok", "uyku", "su", "kalp", "durum", "sağ", "orta", "diğer", "büyük", "yap",

              "yeni", "çok", "sor", "onlar", "açık", "o", "hap", "iris", "ağla", "çılgın", "saat", "bölüm",

              'birlik', 'kıdemli', 'ol', 'buzlu', 'içecek', 'onuncu', 'biber', 'ortalama', 'çok', 'yeşil', 'aylık', 'beğen', 'daha fazla ', 'elde etmek',

              'nihai', 'sadece', 'gel', 'yıllık', 'ver', 'dede', 'sonra', 'mümkün', 'yer', 'baba', 'adam', 'değil', 'her ',

              'istiyorum', 'yılan', 'dışarı çık', 'gör', 'gün', 'biz', 'git', 'çalış', 'ölüm', 'ara', 'eltun', 'bil', ' el ', 'zaman',

              'yarasa', 'çocuk', 'birincil', 'bak', 'iş', 'içinde', 'büyük', 'hayır', 'başlangıç', 'yol', 'doğru', 'fiil', 'sen ',

              'söz', 'yarat', 'iyi', 'kadın', 'evli', 'söyle', 'bul', 'söyle', 'gözlük', 'ihtiyaç', 'dünya',

              'kafa', 'zaman', 'parti', 'git', 'sen', 'onlar', 'yeni', 'ilk', 'diğer', 'cehennem', 'orta', 'susuz', 'gir', 'ülke',

              'sevmek', 'biraz', 'çətin', 'çıkmaq', 'yapay', 'koymak', 'tek', 'sistem', 'toplu', 'vergi', 'kim', 'inci', 'genç',

             'kapı', 'kitap', 'üstün', 'burada', 'gece', 'alan', 'berber', 'içki', 'gizli', 'uzun', 'kainat', 'bugün', 'fokus',

             'dost', 'soyisim', 'aile', 'üç', 'okumak','kişi', 'hərkəs', 'güç', 'bilmek', 'doğru', 'tam', 'gece', 'Emirbozan',

             'çevre', 'eski', 'arama', 'özelharekat', 'ahali', 'yakın', 'yol', 'boy', 'tarih', 'özellik', 'bölüm', 'şahsi', 'akıl',

             'kimse', 'temiz', 'batı', 'gereksiz', 'yakın', 'anlamak', 'yukarı', 'banka', 'kriz', 'ayak', 'taşımak', 'geri', 'toplu',

             'araba', 'madde', 'türk', 'nargile', 'görüldü', 'hava', 'sayı', 'farklı', 'qurup', 'otuz', 'bacı', 'dolmak', 'haber',

             'Allah', 'ayrıca', 'gelin', 'çin', 'sual', 'arka', 'kazanmak', 'yazı', 'ders', 'açık', 'öğrenmek', 'sürmek',

             'dil', 'şirket', 'kaynak', 'bitmek', 'program', 'devametmek', 'hareket', 'renk', 'açılmak', 'hak', 'inanmak',

             'çalmak', 'zaman', 'mahnı', 'qazet', 'yaratmak', 'yaşam', 'diyar', 'tanımak', 'yapışkan', 'doktor', 'gelir',

             'komando', 'zafer', 'dünya', 'film', 'üzeri', 'satıcı', 'kolluk', 'telefon', 'aydın', 'deniz', 'ikinci',

             'kalkmak', 'düzgün', 'karlı', 'gelir', 'keşkül', 'boyun', 'düşünce', 'milyon', 'oynamaq', 'değişmek', 'tütün',

             'yaratmak', 'ben', 'fikir', 'keçi', 'küfür', 'kurmak', 'fakt', 'buna', 'resim', 'ışıq', 'içmek',

             'hanım', 'hasta', 'ihtiyaç', 'nokta', 'yeto', 'hata', 'oyun', 'artmak', 'yeniden', 'şal', 'kısa', 'asta',

             'şan', 'kan', 'asla', 'ağıl', 'orada', 'dikkat', 'uzak', 'bilgisayar', 'gelecek', 'görünmek',

             'şekiliz', 'okul', 'dinlemek', 'uygun', 'dolar', 'passiv', 'tutku', 'unutmak', 'hırslı', 'gözlük', 'pis',

             'maşın', 'ağız', 'dünya', 'uygulamak', 'hala', 'örnek', 'azlık', 'bakmak', 'derece', 'mümkün', 'dondurma',

             'divar', 'onsuz', 'sene', 'ana', 'hastalık', 'öğrenci', 'televizor', 'kino', 'stul', 'ölmek', 'taksi', 'üst',

             'baş', 'mahnı', 'sevgi', 'enerji', 'üniversite', 'spor', 'türlü', 'cansız', 'balta', 'soyuducu', 'ölüm',

             'dertli', 'sağlam', 'inek', 'muz', 'hissetmek', 'nine', 'sabah', 'internet', 'teknik', 'dondurma',

             'merkez', 'orta', 'yerine', 'düz', 'kent', 'yorulmak', 'aşağı', 'cevab', 'yatmak', 'toprak', 'axşam',

             'sarı', 'götürmek', 'katılmak', 'yoksul', 'kurmak', 'ödemek', 'sanki', 'karın', 'hasta', 'şehir', 'kalkmak',

             'qara', 'qaynaq', 'hafta', 'künefe', 'hesap', 'latif', 'başka', 'davranış', 'mutfak', 'kent', 'bazar',

             'vacib', 'ayrı', 'qiymet', 'hakkında', 'kaldırmak', 'kola', 'tek', 'hazırlamak', 'ayna', 'sonunda', 'yavaş',

             'lazım', 'diyor', 'avrat', 'yallı', 'varlı', 'tar', 'arı', 'türkçe', 'satış', 'içeri', 'güzel', 'mahkum',

             'şenlik', 'acı', 'hayır', 'korumak', 'kat', 'ekonomi', 'genel', 'bildirmek', 'şeker', 'hayvan', 'sarqı',

             'yumurta', 'alma', 'plan', 'istemek', 'kerim', 'kriz', 'birlik',

             'kapalı'

             ]

def kelime_sec():

    return random.choice(kelimeler)
