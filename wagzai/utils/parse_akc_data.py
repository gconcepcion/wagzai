import csv


def load_breed_info():
    breeds = []

    akc_data = "data/akc/akc-data-latest.csv"

    with open(akc_data, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            akc_breed = row["breed"]
            description = row["description"] or ""
            temperament = row["temperament"].split(",") if row["temperament"] else []
            popularity = int(row["popularity"]) if row["popularity"] else None
            min_height = float(row["min_height"]) if row["min_height"] else None
            max_height = float(row["max_height"]) if row["max_height"] else None
            min_weight = float(row["min_weight"]) if row["min_weight"] else None
            max_weight = float(row["max_weight"]) if row["max_weight"] else None
            min_expectancy = (
                float(row["min_expectancy"]) if row["min_expectancy"] else None
            )
            max_expectancy = (
                float(row["max_expectancy"]) if row["max_expectancy"] else None
            )
            group = row["group"] or ""
            grooming_frequency_value = (
                float(row["grooming_frequency_value"])
                if row["grooming_frequency_value"]
                else None
            )
            grooming_frequency_category = row["grooming_frequency_category"] or ""
            shedding_value = (
                float(row["shedding_value"]) if row["shedding_value"] else None
            )
            shedding_category = row["shedding_category"] or ""
            energy_level_value = (
                float(row["energy_level_value"]) if row["energy_level_value"] else None
            )
            energy_level_category = row["energy_level_category"] or ""
            trainability_value = (
                float(row["trainability_value"]) if row["trainability_value"] else None
            )
            trainability_category = row["trainability_category"] or ""
            demeanor_value = (
                float(row["demeanor_value"]) if row["demeanor_value"] else None
            )
            demeanor_category = row["demeanor_category"] or ""

            breed_info = {
                "breed": akc_breed,
                "description": description,
                "temperament": temperament,
                "popularity": popularity,
                "min_height": min_height,
                "max_height": max_height,
                "min_weight": min_weight,
                "max_weight": max_weight,
                "min_expectancy": min_expectancy,
                "max_expectancy": max_expectancy,
                "group": group,
                "grooming_frequency": {
                    "value": grooming_frequency_value,
                    "category": grooming_frequency_category,
                },
                "shedding": {"value": shedding_value, "category": shedding_category},
                "energy_level": {
                    "value": energy_level_value,
                    "category": energy_level_category,
                },
                "trainability": {
                    "value": trainability_value,
                    "category": trainability_category,
                },
                "demeanor": {"value": demeanor_value, "category": demeanor_category},
            }
            breeds.append(breed_info)

    return breeds
