# current_actions = ["line", "circle", "square"]
# backup_actions = current_actions[:]
# current_actions.append("triangle")
# print("Current Actions:", current_actions)
# print("Backup Actions :", backup_actions)

#E-Commerce Cart SlicingA customer views their e-commerce shopping cart containing 6 items. They click a button to view "only the last 3 items added." Given cart = ["shoes", "shirt", "watch", "hat", "belt", "socks"], write a single line of code using negative list slicing to extract exactly the last 3 items.
# cart = ["shoes", "shirt", "watch", "hat", "belt", "socks"]
# last_three_items = cart[-3:]
# print(last_three_items)

#Inventory Sorting & Case SensitivityA warehouse management system runs .sort() on a list of product tags: tags = ["banana", "Vipia", "apple", "cherry", "vipin"]. Write down exactly what the list will look like after running tags.sort(), and explain how capital letters affect the sorting order.
# tags = ["banana", "Vipia", "apple", "cherry", "vipin"]
# tags.sort()
# print(tags)
# tags.sort(reverse=True)
# print(tags)

#An industrial IoT sensor records temperatures every single minute of an hour, resulting in a list of 60 items. You want to downsample this data to look at every 4th minute's reading. Given a list numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], write a slice expression that retrieves every 4th element starting from index 0.
#numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# every_fourth = numbers[::4]
# print(every_fourth)

#notifications = ["Like", "Comment"]
# Insert "New Follower" at index 0
# notifications.insert(0, "New Follower")
# print(notifications)

#log_data = ["Vipin", 25, "Jaipur", 302020, True, ["Test", 43, [23242, [234234]]]]
# Extracting the innermost tracking ID
# tracking_id = log_data[5][2][1][0]
# print("Tracking ID:", tracking_id) # Output: 234234
# Extracting the secondary log code
# log_code = log_data[5][2][0]
# print("Log Code:", log_code)       # Output: 23242

log_data = ["Vipin", 25, "Jaipur", 302020, True, ["Test", 43, [23242, [234234]]]]
print(log_data[5][2][1][0])







