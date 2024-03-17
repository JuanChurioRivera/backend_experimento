import	pyodbc


class azure_con:
    def __init__(self):
        self.server = 'umng-experiment.database.windows.net'
        self.database = 'datos-experimentos'
        self.username = 'JuanChurio'
        self.password = 'UmngExperimento4$'
        self.driver = 'ODBC Driver 18 for SQL Server'
        self.connection_string = f'Driver={self.driver};Server=tcp:umng-experiment.database.windows.net,1433;Database=datos-experimentos;Uid=JuanChurio;Pwd={self.password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
        self._con = pyodbc.connect(self.connection_string)
        print("1")
        
    def getTable(self):
        cur = self._con.cursor()
        query  = 'SELECT * FROM DatosExperimento;'
        cur.execute(query)
        result = str(cur.fetchall())
        return result
    
    def insertRow(self,CONDITION_A,CONDITION_B,GRAPH,timeTaken,Error,controlCondition,timePer):
        
        cur = self._con.cursor()
        query  = "INSERT INTO DatosExperimento (CONDITION_A,CONDITION_B,GRAPH,timeTaken,Error,controlCondition,timePer) VALUES (?, ?, ?,?,?,?,?);"
        cur.execute(query, (CONDITION_A, CONDITION_B, GRAPH,timeTaken,Error,controlCondition,timePer))
        self._con.commit()
        return {"status": "success", "message": "Row inserted"}
        
       
    
# myazure = azure_con()
# print(myazure.getTable())
    
