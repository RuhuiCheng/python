--Lead (The processing of CCA[Promoter] follow up Lead)
SELECT TOP (1000) 
       [Salesforce_id]
	   ,[Promoter_Comments__c]
FROM [SFNewOrg].[dbo].[Lead] with(nolock)
where [IsDeleted] = 0
and Promoter_Comments__c is not null
and Promoter_Comments__c <>'comment:;bookingDate:;bookingTime:;'
order by First_Assign_Date__c desc

--Oppt(The processing of CCA[Promoter] follow up Opportunity)
SELECT TOP (1000) 
      [Salesforce_Id]
	  ,[Promoter_Comments__c]
FROM [SFNewOrg].[dbo].[Opportunity]
where IsDeleted = 0 
and [Promoter_Comments__c] is not null

--Refund
SELECT TOP (1000) 
	  [Salesforce_Id]
	  ,Description__c --Still need to add to VS3
FROM [SFNewOrg].[dbo].[RefundRequest]

--Activity(The processing of course consultant follow up student)
select 
	Comments --Still need to add to VS3
FROM [SFNewOrg].[dbo].[Task]
  
select 
	Description --Still need to add to VS3
FROM [SFNewOrg].[dbo].[Event]

--NPS(For student survey)