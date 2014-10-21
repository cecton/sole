import xmlrpclib


def connect(url, database, login, password):
    odoo_common = xmlrpclib.ServerProxy(url + '/xmlrpc/common',
                                            allow_none=True)
    odoo = xmlrpclib.ServerProxy(url + '/xmlrpc/object',
                                     allow_none=True)
    uid = odoo_common.login(database, login, password)
    def make_proxy(model, method, *base_args):
        return lambda *args, **kwargs: \
            odoo.execute_kw(database, uid, password,
                                model, method, (base_args + args), kwargs)
    return make_proxy
