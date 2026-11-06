import json
import sys

import yaml


with open("reports/metrics.json", encoding="utf-8") as metrics_file:
    f1 = json.load(metrics_file)["f1"]
with open("params.yaml", encoding="utf-8") as params_file:
    threshold = yaml.safe_load(params_file)["validation"]["seuil_f1"]

print(f"F1 = {f1} | seuil = {threshold}")
if f1 < threshold:
    print("ECHEC : modele refuse")
    sys.exit(1)
print("OK : modele accepte")
