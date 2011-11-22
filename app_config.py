import os
try:
    config_module_name = os.environ.get('BATTY_CONFIG_MODULE', 'batty_config')
    batty_conf = __import__(config_module_name)
except:
    raise Exception('Undefined Bikini Configuration....')

def get_config():
    """API to retrieve webapp config
    app config needs to be always retrived using this API
    """
    return batty_conf._config
