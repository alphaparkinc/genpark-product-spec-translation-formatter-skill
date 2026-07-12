from client import ProductSpecTranslationFormatterClient
client = ProductSpecTranslationFormatterClient()
print(client.format_specs({"weight": "5"}, "th"))