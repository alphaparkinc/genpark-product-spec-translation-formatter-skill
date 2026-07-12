class ProductSpecTranslationFormatterClient:
    def format_specs(self, specs: dict, locale: str) -> dict:
        return {"formatted_specs": {k: f"{v} formatted" for k, v in specs.items()}}