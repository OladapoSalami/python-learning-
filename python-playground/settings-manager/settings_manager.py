# Test 1: Create dictionary and add initial values
test_settings = {'theme': 'dark', 'font_size': '12px'}

def add_setting(settings, new_setting):
    key, value = new_setting
    key, value = key.lower(), value.lower()
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, update_data):
    key, value = update_data
    key, value = key.lower(), value.lower()
    if key not in settings:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
    settings[key] = value
    return f"Setting '{key}' updated to '{value}' successfully!"

def delete_setting(settings, key):
    key = key.lower()
    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    return "Setting not found!"

def view_settings(dictionary):
    if len(dictionary) == 0:
        return "No settings available."
    else:
        entries = ""
        for item in dictionary.items():
            entry = item[0].capitalize() + ": " + item[1] + "\n"
            entries += entry
        return "Current User Settings:\n" + entries
               
# add_setting(test_settings, ('EMOJI', 'SMALL'))

# update_setting(test_settings, ('EMOJI', 'SMALL'))

# delete_setting(test_settings, 'THEME')

view_settings(test_settings)

print(view_settings(test_settings))
