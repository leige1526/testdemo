from quote.db.dbhandle import DbHandle


class DbCustomerOp:
    def __init__(self):
        self.db_handle = DbHandle('localhost', 3306, 'quote', 'root', '123456', 'utf8')

    def delete_customer_account(self,para):
        self.db_handle.sql_modify("delete from tb_customer where customerNO = %s",para)

# db=DbCustomerOp()
# db.delete_customer_account('00001111333')