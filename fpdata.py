
class fpdata():
    def __init__(self, *args):
        # self.id = int(args[0]["id"])
        self.fp_id = str(args[0]["id"])
        self.fp_title = str(args[0]["title"])
        self.fp_res_org = str(args[0]["org_name"])
        self.fp_report_time = str(args[0]["report_time"])
        self.fp_stock_name = str(args[0]["stock_name"])
        self.fp_stock_code = str(args[0]["stock_code"])
        self.fp_source_id = str(args[0]["source_id"])
        self.fp_is_stock = str(args[0]["is_stock"])

    def toString(self):
        return self.fp_id  + ",   " + self.fp_title + ",   " + self.fp_res_org + ",  " + self.fp_report_time + ",  " + self.fp_stock_name + ",  " + self.fp_stock_code + ",  " + self.fp_source_id + ",  " + self.fp_is_stock

    def toArray(self):
        return (self.fp_id, self.fp_title, self.fp_res_org, self.fp_report_time, self.fp_stock_name, self.fp_stock_code, self.fp_source_id, self.fp_is_stock)