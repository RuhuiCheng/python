import pymssql

def run(TestCaseId,TestExecutionID):
    # print('TestCaseId-->'+str(TestCaseId))
    # print('TestExecutionID-->'+str(TestExecutionID))
    t = TCase(TestCaseId,TestExecutionID)
    return t.run()
    
class TCase:
    def __init__(self, TestCaseId, TestExecutionID):
        self.connAudit = pymssql.connect('YAMI-PC','EFECBI','fishing22','Audit')
        self.connVS3 = pymssql.connect('YAMI-PC','EFECBI','fishing22','USVS3')
        self.connDW = pymssql.connect('YAMI-PC','EFECBI','fishing22','ApolloEC')
        self.TestCaseId = TestCaseId
        self.TestExecutionID = TestExecutionID

    def run(self):
        cursor_aud = self.connAudit.cursor()
        cursor_aud.execute('SELECT [SourceSql],[DwSql] FROM [dbo].[TestCase] WHERE [TestCaseId] = %d',self.TestCaseId)
        row = cursor_aud.fetchone()
        self.connAudit.commit()
        self.connAudit.close()
        source_sql = 'select skey=checksum(*) from (' + row[0] +') as SourceSql'
        dw_sql = 'select dkey=checksum(*) from (' + row[1] +') as DWSql'
        #print(source_sql+'--'+dw_sql)
        cursor_vs3 = self.connVS3.cursor()
        cursor_vs3.execute(source_sql)
        vs3_data = cursor_vs3.fetchall()
        print(vs3_data)
        self.connVS3.commit()
        self.connVS3.close()

        cursor_dw = self.connDW.cursor()
        cursor_dw.execute(dw_sql)
        dw_data = cursor_dw.fetchall()
        print(dw_data)
        self.connDW.commit()
        self.connDW.close()
        diff_vs3 = set(vs3_data) - set(dw_data)
        diff_dw = set(dw_data) - set(vs3_data)
        
        # print('---------------------------------------------------------')
        # print(diff_vs3)
        # print(diff_dw)
        #return 1
