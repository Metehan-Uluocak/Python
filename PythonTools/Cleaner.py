import os
import shutil
import time

def temizle():
    try:
        # %temp% dizini
        temp_dizin = os.environ.get('TEMP') or os.environ.get('TMP')

        for file in os.listdir(temp_dizin):
            dosya_yolu = os.path.join(temp_dizin, file)
            try:
                if os.path.isfile(dosya_yolu):
                    time.sleep(1)
                    os.unlink(dosya_yolu)
                elif os.path.isdir(dosya_yolu):
                    shutil.rmtree(dosya_yolu)
            except Exception as e:
                print(f"{dosya_yolu} silinirken hata oluştu: {e}")

        # Prefetch dosyaları
        check = input("Prefetch dosyasi temizlensin mi?(Y/n) ")
        if check == "Y" or check == "y":
            prefetch_dizin = "C:\\Windows\\Prefetch"
            for file in os.listdir(prefetch_dizin):
                dosya_yolu = os.path.join(prefetch_dizin, file)
                try:
                    if os.path.isfile(dosya_yolu):
                        os.unlink(dosya_yolu)
                except Exception as e:
                    print(f"{dosya_yolu} silinirken hata oluştu: {e}")

        # Çöp kutusu
        os.system('rd /s /q C:\\$Recycle.Bin')

        # Başka gereksiz dosyaların bulunduğu dizinleri ekleyebilirsiniz.
        # Örneğin: gereksiz_dizin = "C:\\path\\to\\gereksiz_dizin"
        # shutil.rmtree(gereksiz_dizin)

        print("Gereksiz dosyalar başarıyla temizlendi.")
    except Exception as e:
        print(f"Temizleme işlemi sırasında bir hata oluştu: {e}")

temizle()
