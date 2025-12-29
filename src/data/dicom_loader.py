import os
import pydicom
import numpy as np
import cv2

class MedicalImageLoader:
    """
    Teknofest Sağlıkta Yapay Zeka Yarışması için profesyonel DICOM yükleyici.
    
    Özellikler:
    - DICOM okuma ve Metadata çıkarma
    - Hounsfield Unit (HU) dönüşümü
    - Pencereleme (Windowing) (Örn: Beyin, Akciğer, Kemik modları)
    - Normalizasyon (0-1 arası)
    """
    
    def __init__(self, data_path):
        self.data_path = data_path

    def read_dicom(self, file_path):
        """Tek bir DICOM dosyasını okur."""
        try:
            ds = pydicom.dcmread(file_path)
            # Piksel verisini HU değerlerine dönüştür (RescaleSlope/Intercept)
            image = ds.pixel_array.astype(np.float32)
            slope = getattr(ds, 'RescaleSlope', 1)
            intercept = getattr(ds, 'RescaleIntercept', 0)
            image = image * slope + intercept
            return image
        except Exception as e:
            print(f"Hata: {file_path} okunamadı. ({e})")
            return None

    def apply_windowing(self, image, center, width):
        """
        Tıbbi görüntüdeki belirli dokuları vurgulamak için pencereleme uygular.
        
        Args:
            center (int): Pencere merkezi (Level)
            width (int): Pencere genişliği (Width)
            
        Yaygın Değerler (HU):
            - Beyin: Center 40, Width 80
            - Akciğer: Center -600, Width 1500
            - Kemik: Center 400, Width 1800
        """
        lower_bound = center - (width / 2)
        upper_bound = center + (width / 2)
        
        image = np.clip(image, lower_bound, upper_bound)
        return image

    def normalize(self, image):
        """Görüntüyü 0-1 aralığına normalize eder."""
        min_val = np.min(image)
        max_val = np.max(image)
        if max_val - min_val != 0:
            return (image - min_val) / (max_val - min_val)
        return image

    def load_and_process(self, file_path, window_type='brain'):
        """Bir görüntü yükler, pencereleme yapar ve normalize eder."""
        img = self.read_dicom(file_path)
        if img is None: return None

        if window_type == 'brain':
            img = self.apply_windowing(img, 40, 80)
        elif window_type == 'lung':
            img = self.apply_windowing(img, -600, 1500)
        elif window_type == 'bone':
            img = self.apply_windowing(img, 400, 1800)
            
        img = self.normalize(img)
        return img

# Kullanım Örneği (Main bloğu sadece test içindir)
if __name__ == "__main__":
    print("MedicalImageLoader hazır. Projenize import edebilirsiniz.")
    # loader = MedicalImageLoader("./data/raw")
    # img = loader.load_and_process("sample.dcm", window_type="brain")
