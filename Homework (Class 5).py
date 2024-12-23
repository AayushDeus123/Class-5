print('Types of clothes required for specific seasons')
w = input('Enter the weather: ').strip().lower()
if w == 'summer':
    print('(Body) Cotton T-shirt\n(Legs) Shorts\n(Feet) Sandals or Slippers')
elif w == 'winter':
    print('(Body) Jacket or Sweater (Gloves if needed)\n(Legs) Pants or Jeans\n(Feet) Shoes or Boots')
elif w == 'spring':
    print('(Body) Linen T-shirt\n(Legs) Shorts or Pants\n(Feet) Sandals or Slippers')
elif w == 'autumn':
    print('(Body) Cotton Shirt or T-Shirt\n(Legs) Joggers or Trousers\n(Feet) Shoes or Sandals')
elif w == 'monsoon':
    print('(Body) Raincoat\n(Legs) Rain Pants\n(Feet) Boots')
else:
    print('Did you mean\nSummer?\nWinter?\nSpring?\nAutumn?\nMonsoon?\nPlease choose from the above')