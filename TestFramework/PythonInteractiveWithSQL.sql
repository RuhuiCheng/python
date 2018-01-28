execute sp_execute_external_script 
@language = N'Python',
@script = N'
print(InputDataSet.SourceSql) 
OutputDataSet =InputDataSet
',
@input_data_1 = N'SELECT 
      [SourceSql] = cast(''1234567890123456789012345678901234567890123456789012345678901234567890ppp'' as nvarchar(max))'
WITH RESULT SETS ((python_version nvarchar(max)))
------------------------------------------------------------
------------------------------------------------------------
------------------------------------------------------------
DECLARE @TestCaseId INT =16
DECLARE @TestExecutionID int =89
DECLARE @IsMatched INT = 0

exec sp_execute_external_script 
@language =N'Python',
@script=N'
print(''Inputs---------->'')
print(''---@TestCaseId---'')
TestCaseId = TestCaseId+ 1
print(TestCaseId)
print(''---@TestExecutionID---'')
TestExecutionID = TestExecutionID + 1
print(TestExecutionID)
print(''---@IsMatched---'')
IsMatched = IsMatched +1
print(IsMatched)
',
@params = N'@TestCaseId INT, @TestExecutionID INT, @IsMatched INT OUTPUT',
@TestCaseId = @TestCaseId,
@TestExecutionID = @TestExecutionID,
@IsMatched = @IsMatched OUTPUT
select @TestCaseId,@TestExecutionID,@IsMatched 