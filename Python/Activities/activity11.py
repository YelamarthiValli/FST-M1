fruit_shop = {
    "apple": 15,
    "banana": 17,
    "orange": 20,
    "peaches": 25
}
 
key_to_check = input("What is the fruit you are looking for? ").lower()
 
if(key_to_check in fruit_shop):
    print("Yes, this fruit is available")
else:
    print("No, this fruit is not available")
