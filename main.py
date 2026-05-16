import datetime
import time

def get_current_time_data():
    """
    Simulates reading sensor data (e.g., ambient light, time) from the device.
    This data is processed locally, without external network requests.
    """
    now = datetime.datetime.now()
    print(f"[{now.strftime('%H:%M:%S')}] Simulating sensor input: Current local time is {now.hour} o'clock.")
    return now.hour

def offline_decision_model(hour):
    """
    This function represents a simple 'offline model' running on an edge device.
    It makes a decision based *only* on local input, without needing cloud processing.
    This is the core concept of an 'offline AI model' as discussed in the article.
    """
    if 6 <= hour < 12:
        return "Günaydın! (Good Morning!) - Yeni Güne Merhaba!"
    elif 12 <= hour < 18:
        return "İyi Öğleden Sonraları! (Good Afternoon!) - Verimli Çalışmalar!"
    elif 18 <= hour < 22:
        return "İyi Akşamlar! (Good Evening!) - Keyifli Bir Akşam Dileriz!"
    else:
        return "İyi Geceler! (Good Night!) - Huzurlu Uykular!"

def display_on_digital_sign(message):
    """
    Simulates displaying a message on a digital sign, an example edge device.
    """
    print("-" * 30)
    print(f"DİJİTAL TABELA (DIGITAL SIGN): {message}")
    print("-" * 30)
    print("\n")

if __name__ == "__main__":
    print("Çevrimdışı Dijital Tabela Simülasyonu Başlatılıyor...")
    print("Starting Offline Digital Sign Simulation...\n")

    # The core loop demonstrating the offline model in action
    # The 'model' (offline_decision_model) makes decisions solely based on local data.
    for _ in range(3): # Run a few times to show dynamic behavior over a short period
        current_hour = get_current_time_data() # Get local data (simulated sensor input)
        sign_message = offline_decision_model(current_hour) # Make decision locally, on the 'edge'
        display_on_digital_sign(sign_message) # Display result on the 'device'
        time.sleep(2) # Wait a bit before next update

    print("Simülasyon Tamamlandı. (Simulation Complete.)")
