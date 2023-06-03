from deep_translator import MyMemoryTranslator
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


authenticator = IAMAuthenticator("aqZ6tgIGiAKXZ4EAqmFqeRH8qOE_IptEJoDtLiJhiGKI")
language_translator = LanguageTranslatorV3(
    version="2018-05-01", authenticator=authenticator
)

language_translator.set_service_url(
    "https://api.us-south.language-translator.watson.cloud.ibm.com/instances/807e6aaf-b701-427d-9826-e67805e5e323"
)


def english_to_french(english_text):
    """write the code here"""
    translation = language_translator.translate(
        text=english_text, model_id="en-fr"
    ).get_result()
    french_text = translation["translations"][0]["translation"]

    return french_text


def french_to_english(french_text):
    """write the code"""
    translation = language_translator.translate(
        text=french_text, model_id="fr-en"
    ).get_result()
    english_text = translation["translations"][0]["translation"]
    return english_text
