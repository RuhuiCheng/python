# Run python in sqlserver
1. Enable the external script execution feature by running
    ```sql
    EXEC sp_configure  'external scripts enabled', 1
    RECONFIGURE WITH OVERRIDE
    ```
2. Restart the server.
    Ensure SQL Server Launchpad service avaliable
3. config python path to enviroment variables
    + C:\Program Files\Microsoft SQL Server\MSSQL14.MSSQLSERVER\PYTHON_SERVICES
    + C:\Program Files\Microsoft SQL Server\MSSQL14.MSSQLSERVER\PYTHON_SERVICES\Scripts
4. TO open CMD run as administrator
    + pip install pymssql
    + view packages that have been installed (conda list)
5. Adjust the outbound rule of firewall
    + Block network access for R local user accounts in SQL Server instance MSSQLSERVER
6. Give users permission to run external scripts
    ```sql
    USE <database_name>
    GO
    GRANT EXECUTE ANY EXTERNAL SCRIPT  TO [UserName]
    ```
7. If you need to run scripts from a remote data        science client, and you are using Windows           authentication, there are additional                considerations. These worker accounts must be       given permission to sign in to the SQL Server       instance on your behalf.
    ```SQL
    Security --> Logins -->to add SQLRUserGroup
    ```
8. Give your users read, write, or data definition      language (DDL) permissions to databases
    ```sql
    /*For example, the following Transact-SQL statement gives the SQL login MySQLLogin the rights to run T-SQL queries in the ML_Samples database. To run this statement, the SQL login must already exist in the security context of the server.*/
    
    USE ML_Samples
    GO
    EXEC sp_addrolemember 'db_datareader', 'MySQLLogin'
    ```
# MyPython
Python related projects
https://docs.microsoft.com/en-us/sql/advanced-analytics/python/install-additional-python-packages-on-sql-server

http://blog.csdn.net/sqlserverdiscovery/article/details/54428282
# conn tran issue
https://github.com/pymssql/pymssql/issues/460
