msg_template = """ Hell0 {name}, 
Thank you for joining {website}.  We are very
happy to have you with us. 
""" # . format(name="Tonia", website= 'tonia.saba.com')

def format_msg(my_name="Justin", my_website="toniasaba.com"):
    my_msg = msg_template.format(name=my_name, website=my_website)
    return my_msg