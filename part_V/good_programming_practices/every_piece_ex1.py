# IF YOU ARE READING THIS YOU ARE READING 
# AN OUTDATED VERSION OF THE BOOK.
# I am working with Amazon to resolve this.
# The new version is much better and has correctly formatted code examples
# In the book.
# Please email me at cory@theselftaughtprogrammer.io
# For an updated version

# WARNING this is an example and will not work

import twitter_api
import celebrity_list
import regular_list


def celebrity_data():
    api_key = '11330000aazzz22'
    return twitter_api.get_data(api_key, celebrity_list)


def people_data():
    api_key = '11330000aazzz22'
    return twitter_api.get_data(api_key, regular_list)
