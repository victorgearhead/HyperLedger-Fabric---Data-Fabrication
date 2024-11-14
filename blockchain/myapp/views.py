from django.shortcuts import render, redirect
from .forms import DataForm
import json
import os


def submit_data(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            data = {
                'AGE': form.cleaned_data['age'],
                'BMI': form.cleaned_data['bmi'],
                'APPID': form.cleaned_data['appid'],
                'SEX': form.cleaned_data['sex'],
                'WRIST': form.cleaned_data['wrist'],
                'HEIGHT': form.cleaned_data['height'],
                'WAIST': form.cleaned_data['waist'],
                'CURRENT ADDRESS': form.cleaned_data['current_address'],
                'HIP': form.cleaned_data['hip'],
                'WEIGHT': form.cleaned_data['weight'],
                'शरीरिक संगठन(Body Frame)?': form.cleaned_data['body_frame'],
                'शरीर संहनन(Body Bulk)?': form.cleaned_data['body_bulk'],
                'शारीरिक संहनन (मांसपेशीय)Body Build (Musculature)?': form.cleaned_data['musculature'],
                'माथे की लंबाई(Forehead Length)?': form.cleaned_data['forehead_length'],
                'नाखून बनावट(Nails Texture)?': form.cleaned_data['nails_texture'],
                'नाखुनो का रंग(Nails Colour)?': form.cleaned_data['nails_colour'],
                'उंगली के नाखुन का आकार(Finger Nail Size)?': form.cleaned_data['fingernail_size'],
                'त्वचा की उपस्थिति(Skin Appearance)?': form.cleaned_data['skin_appearance'],
                'त्वचा का रंग/आभा(Skin Colour/Complexion)?': form.cleaned_data['skin_colour'],
                'त्वचा की प्रकृति(Skin Nature)?': form.cleaned_data['skin_nature'],
                'त्वचा की बनावट(Skin Texture)?': form.cleaned_data['skin_texture'],
                'बालों की बनावट(Hair Texture), बालों की प्रकृति(Hair Nature)?': form.cleaned_data['hair_texture'],
                'बालों की प्रकृति(Hair Nature)?': form.cleaned_data['hair_nature'],
                'क्या आप देखते हैं कि आपके पास है?(Do you observe you have?)?': form.cleaned_data['observe_condition'],
                'आपकी भूख कैसी है?(नियमितता)(How is your appetite?(Regularity, Frequency, Amount))?': form.cleaned_data['appetite'],
                'स्वाद वरीयता(Taste Preference)?': form.cleaned_data['taste_preference'],
                'क्या आप अपने द्वारा खाए गए भोजन की मात्रा को पचा पा रहे हैं?(Are you able to digest the amount of food consumed by you?)': form.cleaned_data['digestibility'],
                'क्या आप वसा से भरपूर भोजन लेना पसंद करते हैं जैसे(Do you prefer to take food rich in fats like)?': form.cleaned_data['fat_food_preference'],
                'क्या आपके शरीर का तापमान सामान्य रहता है?(Does your body temperature in general remains ?)': form.cleaned_data['body_temperature'],
                'आपके पसीने के बारे में कैसे है?(How about your Perspiration?)': form.cleaned_data['perspiration'],
                'आपकी नींद कैसी है?(राशि)(How about your sleep ?(amount))': form.cleaned_data['sleep'],
                'क्या आपको बिस्तर पर जाने के तुरंत बाद नींद आती है?(Do you get sleep immediately after going to bed ?)': form.cleaned_data['sleep_immediately'],
                'नींद की गुणवत्ता(Quality of Sleep)?': form.cleaned_data['sleep_quality'],
                'आपकी शौच प्रवृत्तीआदतों के बारे में कैसे है ?(How about your bowel habits?)': form.cleaned_data['bowel_habits'],
                'शौच के प्रति आपकी प्रवृत्ती केसी है? (अधिकतर)(Do you tend to have ?)': form.cleaned_data['stool_preference'],
                'मल प्रवृत्ती कैसी होती है अधिकतर(Stool Consistency)?': form.cleaned_data['stool_consistency'],
                'आपके शरीर के वजन में परिवर्तन के बारे में आप कैसे?(How about changes in your body weight ?)': form.cleaned_data['body_weight_change'],
                'क्या आपके शरीर से दुर्गंध आती है?(Do you have body odor ?)': form.cleaned_data['body_odour'],
                'आप कौन सा मौसम पसंद करते हैं?(Which weather do you prefer ?)': form.cleaned_data['weather_preference'],
                'आपको किस मौसम में स्वास्थ्य समस्याएं होती हैं?(In which weather do you have health problems ?)': form.cleaned_data['health_in_weather'],
                'आप कितनी बार बीमार पड़ते हैं?(How frequently do you fall ill?)': form.cleaned_data['illness_frequency'],
                'यदि आप बीमार पड़ते हैं तो क्या आप आसानी से ठीक हो जाते हैं?(If you fall ill do you get cured easily?)': form.cleaned_data['recovery'],
                'बोलने की मात्रा(Amount of speaking)?': form.cleaned_data['speaking_amount'],
                'आवाज की गुणवत्ता(Quality of voice)?': form.cleaned_data['voice_quality'],
                'बोलने की गति/शैली(Speed/Style of Speaking)?': form.cleaned_data['speaking_speed'],
                'स्वैच्छिक और अनैच्छिक गतियां(Voluntary and Involuntary Movements)?- हाथ की गति(Hand), टाँगों की गति(Leg), आइब्रो मूवमेंट(Eyebrow), कंधे की गति(Shoulder)-समग्र आंदोलन(Overall)': form.cleaned_data['movements'],
                'मानसिक शक्ति(Mental Strength)?': form.cleaned_data['mental_strength'],
                'आप कितनी बार थकान महसूस करते हैं?(How frequently you feel tired?)': form.cleaned_data['tiredness'],
                'आप कितनी जल्दी चीजों को याद कर सकते हैं?(How quickly you can memorize things?)': form.cleaned_data['memorization_speed'],
                'आप कितने भुलक्कड़ हैं?(How forget ful you are?)': form.cleaned_data['forgetfulness'],
                'आपकी मेमोरी रिटेंशन पावर कैसी है?(How is your memory retention power?)': form.cleaned_data['memory_retention'],
                'क्या आप है एक…(Are you a…)?': form.cleaned_data['is_you'],
                'क्या आपको पसंद है?(Do you like to ?)': form.cleaned_data['preference'],
                'DOCTOR_Prakriti': form.cleaned_data['doctor_prakriti'],
                'Kapha': form.cleaned_data['kapha'],
                'Pitta': form.cleaned_data['pitta'],
                'Vata': form.cleaned_data['vata'],
                'NOTE': form.cleaned_data['note'],
                'APP_Prakarti': form.cleaned_data['app_prakarti'],
            }

            file_path = os.path.join('data', 'submitted_data.json')

            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            with open(file_path, 'w',encoding='utf-8') as json_file:
                json.dump(data, json_file,ensure_ascii=False, indent=4)

            return redirect('success')  # Redirect to a success page
    else:
        form = DataForm()

    return render(request, 'myapp/form.html', {'form': form})


def success(request):
    return render(request, 'myapp/success.html')
