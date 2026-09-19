# import_products.py — one-time script to import products from catalogue.js
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'comeiin.settings')
django.setup()

from products.models import Category, Product

# ---------- Your 22 products (from catalogue.js) ----------
PRODUCTS = [
    # (category, name, sku, short_description, description, image_file, kind, is_featured)
    ('Equipment', 'Microscopes & Imaging', 'CW-001',
     'Microscopes and laboratory imaging equipment for routine and educational laboratory work.',
     'Microscopes and laboratory imaging equipment for routine and educational laboratory work. Suitable for educational, clinical and research laboratories.',
     'CW-001-generated-v2.webp', 'range', True),

    ('Consumables', 'Microscope slides', 'CW-001-SLIDES',
     'Glass microscope slides supplied in a vacuum-sealed, moisture- and gas-impermeable liner.',
     'Width: 26 mm\nLength: 76 mm\nThickness: 1-1.2 mm\nPack quantity: 50 pieces per box\nPackaging: Vacuum-sealed, moisture- and gas-impermeable liner',
     'CW-001-SLIDES-generated-v2.webp', 'product', False),

    ('Equipment', 'Centrifuges', 'CW-002',
     'Laboratory centrifuges and sample-processing equipment.',
     'Laboratory centrifuges and sample-processing equipment for routine and specialised work.',
     'CW-002-generated-v2.webp', 'range', True),

    ('Liquid handling', 'Pipettes & Accessories', 'CW-005',
     'Pipettes, burettes and associated laboratory measuring equipment.',
     'Pipettes, burettes and associated laboratory measuring equipment.',
     'CW-005-generated-v2.webp', 'range', False),

    ('Equipment', 'Hot Plates & Stirrers', 'CW-007',
     'Hot plates, magnetic stirrers and laboratory mixing equipment.',
     'Hot plates, magnetic stirrers and laboratory mixing equipment for routine laboratory work.',
     'CW-007-generated-v2.webp', 'range', False),

    ('Equipment', 'Autoclaves & Sterilization', 'CW-008',
     'Autoclaves and laboratory sterilization equipment.',
     'Autoclaves and laboratory sterilization equipment for clinical and research laboratories.',
     'CW-008-generated-v2.webp', 'range', False),

    ('Equipment', 'Laboratory Refrigerators & Freezers', 'CW-009',
     'Laboratory cold-storage equipment for temperature-sensitive materials.',
     'Laboratory cold-storage equipment for temperature-sensitive materials and reagents.',
     'CW-009-generated-v2.webp', 'range', False),

    ('Consumables', 'Laboratory Plasticware', 'CW-014',
     'Laboratory plastic containers, racks, pipettes and storage products.',
     'Laboratory plastic containers, racks, pipettes and storage products for everyday laboratory use.',
     'CW-014-generated-v2.webp', 'range', True),

    ('Consumables', 'Universal specimen containers', 'CW-017',
     'Sterile universal specimen containers for sample collection.',
     'Sterility: Sterile\nCapacities: 30 ml, 40 ml, 60 ml and 120 ml\nPack quantity: 500 pieces per box',
     'CW-017-generated-v2.webp', 'product', True),

    ('Consumables', 'Test Tubes & Vacutainers', 'CW-018',
     'Test tubes, collection tubes and Vacutainer-style products.',
     'Test tubes, collection tubes and Vacutainer-style products for clinical and routine laboratory use.',
     'CW-018-generated-v2.webp', 'range', False),

    ('Liquid handling', 'Pipette Tips & Consumables', 'CW-019',
     'Pipette tips and disposable laboratory consumables.',
     'Pipette tips and disposable laboratory consumables for liquid handling.',
     'CW-019-generated-v2.webp', 'range', False),

    ('Consumables', 'Syringes & Needles', 'CW-022',
     'Laboratory syringes and associated sampling accessories.',
     'Laboratory syringes and associated sampling accessories for laboratory work.',
     'CW-022-generated-v2.webp', 'range', False),

    ('Consumables', 'Alcohol swabs', 'CW-023',
     'Individually packed sterile antiseptic wipes.',
     'Product type: Alcohol swabs\nSterility: Sterile\nPack quantity: 200 per box',
     'CW-023-generated-v2.webp', 'product', False),

    ('Consumables', 'Reagent Bottles & Storage', 'CW-024',
     'Reagent bottles and laboratory chemical/sample storage containers.',
     'Reagent bottles and laboratory chemical/sample storage containers for laboratory use.',
     'CW-024-generated-v2.webp', 'range', False),

    ('Equipment', 'Stirrers & Lab Mixers', 'CW-025',
     'Magnetic stirrers, stirrer hot plates, shaft stirrers, vortex mixers and mixing accessories.',
     'Magnetic stirrers, stirrer hot plates, shaft stirrers, vortex mixers and mixing accessories.',
     'CW-025-generated-v2.webp', 'range', False),

    ('Liquid handling', 'Pipettes & Burettes', 'CW-028',
     'Pipettes, fill pipettes, burettes and associated laboratory measuring equipment.',
     'Pipettes, fill pipettes, burettes and associated laboratory measuring equipment.',
     'CW-028-generated-v2.webp', 'range', False),

    ('Lab essentials', 'Dissection Kits & Tools', 'CW-029',
     'Dissection sets, boards, scissors, scalpels, needles, forceps and magnifiers.',
     'Dissection sets, boards, scissors, scalpels, needles, forceps and magnifiers for educational and research laboratories.',
     'CW-029-generated-v2.webp', 'range', False),

    ('Lab essentials', 'Stands, Racks & Supports', 'CW-030',
     'Retort and burette stands, tripods, test-tube racks, pipette stands and support systems.',
     'Retort and burette stands, tripods, test-tube racks, pipette stands and support systems.',
     'CW-030-generated-v2.webp', 'range', False),

    ('Lab essentials', 'Laboratory Metalware', 'CW-031',
     'Clamps, boss heads, tongs, spatulas, scoops and other laboratory metal tools.',
     'Clamps, boss heads, tongs, spatulas, scoops and other laboratory metal tools.',
     'CW-031-generated-v2.webp', 'range', False),

    ('Lab essentials', 'Laboratory Safety Gear', 'CW-032',
     'Lab coats, gloves, protective eyewear, reusable mats and laboratory PPE.',
     'Lab coats, gloves, protective eyewear, reusable mats and laboratory PPE for a safe working environment.',
     'CW-032-generated-v2.webp', 'range', False),

    ('Equipment', 'Digital fridge / freezer thermometer', 'CW-033',
     'Digital thermometer for monitoring fridge and freezer temperatures.',
     'Temperature range: -50 °C to +70 °C\nOrder unit: Each',
     'CW-033-generated-v2.webp', 'product', False),

    ('Lab essentials', 'Lab Cleaning Supplies', 'CW-034',
     'Brushes, detergents and cleaning tools designed for glassware, pipettes and laboratory equipment.',
     'Brushes, detergents and cleaning tools designed for glassware, pipettes and laboratory equipment.',
     'CW-034-generated-v2.webp', 'range', False),
]


def run():
    print("=" * 60)
    print("Importing Comeiin products...")
    print("=" * 60)

    created = 0
    updated = 0

    # 1) Categories
    categories = {}
    for cat_name in ['Equipment', 'Consumables', 'Liquid handling', 'Lab essentials']:
        cat, was_created = Category.objects.get_or_create(
            name=cat_name,
            defaults={
                'slug': cat_name.lower().replace(' ', '-'),
                'is_active': True,
            }
        )
        categories[cat_name] = cat
        print(f"  Category: {cat_name} {'(created)' if was_created else '(exists)'}")

    print()

    # 2) Products
    for (cat_name, name, sku, short_desc, description, image_file, kind, is_featured) in PRODUCTS:
        cat = categories[cat_name]

        # Determine slug from SKU (lowercase)
        slug = sku.lower()

        product, was_created = Product.objects.update_or_create(
            sku=sku,
            defaults={
                'category': cat,
                'name': name,
                'slug': slug,
                'short_description': short_desc,
                'description': description,
                'badge': cat_name,
                'is_featured': is_featured,
                'is_active': True,
                'stock': 100,
                'price': None,  # Price on request
            }
        )

        # Set image path manually — points to static file
        # We store the relative path so the API returns the right URL
        product.image.name = f'products/{image_file}'
        product.save()

        if was_created:
            created += 1
            print(f"  ✅ Created: {sku} — {name}")
        else:
            updated += 1
            print(f"  ↻ Updated: {sku} — {name}")

    print()
    print("=" * 60)
    print(f"DONE — {created} created, {updated} updated")
    print(f"Total products now: {Product.objects.filter(is_active=True).count()}")
    print("=" * 60)


if __name__ == '__main__':
    run()