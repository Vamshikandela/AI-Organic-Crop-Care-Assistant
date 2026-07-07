def get_weather_advice(weather, language="Telugu"):

    weather = weather.lower()

    if language == "English":

        if "rain" in weather:
            return """
🌧️ During Heavy Rain:
- Ensure proper drainage to avoid waterlogging.
- Monitor crops for fungal diseases.
- Spray neem oil as an organic preventive measure.
"""

        elif "hot" in weather or "summer" in weather:
            return """
☀️ During Hot Weather:
- Apply mulching to retain soil moisture.
- Irrigate during early morning or evening.
- Keep the soil moist to reduce heat stress.
"""

        elif "cold" in weather or "winter" in weather:
            return """
❄️ During Cold Weather:
- Reduce irrigation frequency.
- Protect plant roots from excess moisture.
- Apply Jeevamrutham to improve soil health.
"""

        elif "cloud" in weather:
            return """
☁️ Cloudy Weather:
- Monitor crops for fungal infections.
- Ensure proper air circulation around plants.
"""

        else:
            return """
🌱 General Farming Tips:
- Use organic fertilizers.
- Maintain balanced irrigation.
- Inspect crops regularly for pests and diseases.
"""

    else:

        if "rain" in weather:
            return """
🌧️ భారీ వర్షాలు ఉన్నప్పుడు:
- నీరు నిల్వ ఉండకుండా డ్రైనేజ్ ఏర్పాటు చేయండి
- ఫంగస్ వ్యాధులు పెరగవచ్చు
- వేపనూనె స్ప్రే ఉపయోగించండి
"""

        elif "hot" in weather or "summer" in weather:
            return """
☀️ అధిక వేడి సమయంలో:
- మల్చింగ్ చేయండి
- ఉదయం లేదా సాయంత్రం నీరు ఇవ్వండి
- మొక్కలకు తేమ నిల్వ ఉంచండి
"""

        elif "cold" in weather or "winter" in weather:
            return """
❄️ చల్లని వాతావరణంలో:
- నీటి పరిమాణం తగ్గించండి
- వేర్లు పాడుకాకుండా జాగ్రత్తపడండి
- జీవామృతం ఉపయోగించండి
"""

        elif "cloud" in weather:
            return """
☁️ మేఘావృత వాతావరణం:
- ఫంగల్ వ్యాధులను పరిశీలించండి
- గాలి ప్రసరణ ఉండేలా చూడండి
"""

        else:
            return """
🌱 సాధారణ వాతావరణ సూచనలు:
- సేంద్రియ ఎరువులు వాడండి
- నీటి పరిమాణం సమతుల్యం ఉంచండి
- పంటను తరచుగా పరిశీలించండి
"""