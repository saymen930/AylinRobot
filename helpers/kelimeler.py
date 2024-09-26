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

             'çevre', 'eski', 'arama', 'yaşma', 'əhali', 'yaxın', 'yol', 'bəy', 'tarix', 'özellik', 'bölüm', 'şəxsi', 'ağıl',

             'kimsə', 'pak', 'baş', 'gerek', 'yaxın', 'anlamaq', 'yuxarı', 'banka', 'kriz', 'ayak', 'daşımaq', 'geri', 'toplu',

             'maşın', 'maddə', 'türk', 'qəlyan', 'görüldü', 'hava', 'sayı', 'farklı', 'qrup', 'otaq', 'bacı', 'dolmaq', 'xəbər',

             'allah', 'ayrıca', 'gələn', 'çin', 'sual', 'arxa', 'qazanmaq', 'yazı', 'dərs', 'açıq', 'öyrənmək', 'sürmək',

             'dil', 'şirkət', 'qaynaq', 'bitmək', 'program', 'devametmek', 'hareket', 'rəng', 'açılmaq', 'hak', 'inanmaq',

             'çalmaq', 'zaman', 'mahnı', 'qazet', 'yaratmaq', 'yaxşı', 'dəyər', 'tanımaq', 'kley', 'doxdur', 'gəlir',

             'hərbiçi', 'zəfər', 'dünya', 'kino', 'üzere', 'satıcı', 'zolaq', 'telefon', 'aydın', 'dəniz', 'ikinci',

             'qalxmaq', 'düzgün', 'qarlı', 'gəlir', 'keçən', 'boyun', 'düşüncə', 'milyon', 'oynamaq', 'dəyişmək', 'tütün',

             'yaratmaq', 'xallı', 'fikir', 'keçmək', 'söyüş', 'qurmaq', 'fakt', 'buna', 'rəsim', 'ışıq', 'içmək',

             'xanım', 'xəstə', 'ehtiyac', 'nöktə', 'yönlü', 'xəta', 'oyun', 'artmak', 'yenidən', 'şar', 'qısa', 'asta',

             'şan', 'qan', 'əsla', 'ağıl', 'orada', 'diqqət', 'uzaq', 'bilgisayar', 'gələcək', 'görünmək',

             'şəkil', 'oğul', 'dinləmək', 'uyğun', 'manat', 'passiv', 'dəqiq', 'unutmaq', 'cəld', 'eynək', 'pis',

             'maşın', 'ağız', 'dünya', 'uygulamak', 'xala', 'örnek', 'azlıq', 'baxmaq', 'dərəcə', 'mümkün', 'dondurma',

             'divar', 'onsuz', 'sənə', 'ana', 'xəstəlik', 'öğrenci', 'televizor', 'kino', 'stul', 'ölmək', 'taksi', 'üst',

             'baş', 'mahnı', 'sevgi', 'enerji', 'üniversite', 'spor', 'türlü', 'cansız', 'balta', 'soyuducu', 'ölüm',

             'dərdli', 'sağlam', 'inək', 'banan', 'hissetmek', 'nənə', 'sabah', 'internet', 'texnik', 'dondurma',

             'mərkəz', 'orta', 'yerinə', 'düz', 'kənd', 'yorulmaq', 'aşağı', 'cavab', 'yatmaq', 'torpaq', '', 'axşam',

             'sarı', 'götürmek', 'qatılmaq', 'yoxsul', 'qurmaq', 'ödəmək', 'sanki', 'qarın', 'xəstə', 'şəhər', 'qalxmaq',

             'qara', 'qaynaq', 'həftə', 'lənpə', 'hesab', 'lətif', 'başqa', 'davranış', 'mutfak', 'kent', 'bazar',

             'vacib', 'ayrı', 'qiymət', 'hakkında', 'qaldırmaq', 'kola', 'tək', 'hazırlamaq', 'ayna', 'sonunda', 'yavaş',

             'lazım', 'dəyər', 'arvad', 'yallı', 'varlı', 'tar', 'arı', 'təkcə', 'satış', 'içəri', 'qoğal', 'məhkum',

             'şənlik', 'acı', 'xeyir', 'qorumaq', 'qat', 'ekonomi', 'genel', 'bildirmək', 'şəkər', 'heyvan', 'sarqı',

             'yumurta', 'alma', 'plan', 'istəmək', 'kərim', 'kriz', 'birlik',

             'qapanmaq'

             ]

def kelime_sec():

    return random.choice(kelimeler)
