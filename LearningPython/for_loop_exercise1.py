found_coins=20;
magic_coins=70;
number_of_days=365;
stolen_coins=3;
coins=found_coins;
for week in range(1,52):
    coins=coins + magic_coins - stolen_coins;
    print('week %s = %s' %(week, coins));
    