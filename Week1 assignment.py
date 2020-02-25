def date_sorter():
    
    datelist = []
    type1 = r'(\d{1,2})[/-](\d{1,2})[/-](\d{2,4})'
    type2 = r'((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec))[a-z]*[.]?[- ](\d{1,2})[,]?[- ](\d{4})'
    type3 = r'(\d{1,2}) ((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec))[a-z]*[.,]? (\d{4})'
    type4 = r'((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec))[a-z]* (\d{1,2})[a-z]{2}[,] (\d{4})'
    type5 = r'((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec))[a-z]*[,]? (\d{4})'
    type6 = r'(\d{1,2})[/](\d{4})'
    type7 = r'\d{4}'
    
    month_dict = {'Jan': '01', 'Feb': '02' ,'Mar': '03','Apr':'04','May':'05','Jun':'06',
                  'Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}
    count = 0
    for s in df:
        count = count + 1             # Using count just in case if some error occurs, so to check that error (optional)
        if len(re.findall(type1,s)) != 0:
            date = list(re.findall(type1,s)[0])       # Using list because without list it is a tuple, and we cannot modify tuple
            if len(date[0]) == 1:
                date[0] = "0"+date[0]
            if len(date[1]) == 1:
                date[1] = "0"+date[1]
            if len(date[2]) == 2:
                date[2] = "19"+date[2]
            datelist.append(date[2]+date[0]+date[1])
            
        elif len(re.findall(type2,s)) != 0:
            date = list(re.findall(type2,s)[0])
            if len(date[2]) == 2:
                date[2] = "19"+date[2]
            if len(date[1]) == 1:
                date[1] = "0"+date[1]
            date[0] = month_dict[date[0]]
            datelist.append(date[2]+date[0]+date[1])
            
        elif len(re.findall(type3,s)) != 0:
            date = list(re.findall(type3,s)[0])
            if len(date[2]) == 2:
                date[2] = "19"+date[2]
            if len(date[0]) == 1:
                date[0] = "0"+date[0]
            date[1] = month_dict[date[1]]  
            datelist.append(date[2]+date[1]+date[0])
            
        elif len(re.findall(type4,s)) != 0:
            date = list(re.findall(type4,s)[0])
            if len(date[2]) == 2:
                date[2] = "19"+date[2]
            if len(date[1]) == 1:
                date[1] = "0"+date[1]
            date[0] = month_dict[date[0]]  
            datelist.append(date[2]+date[0]+date[1])   
            
        elif len(re.findall(type5,s)) != 0:
            date = list(re.findall(type5,s)[0])
            if len(date[1]) == 2:
                date[1] = "19"+date[1]
            date[0] = month_dict[date[0]]  
            datelist.append(date[1]+date[0]+"01")  
            
        elif len(re.findall(type6,s)) != 0:
            date = list(re.findall(type6,s)[0])
            if len(date[1]) == 2:
                date[1] = "19"+date[1]
            if len(date[0]) == 1:
                date[0] = "0"+date[0]
            datelist.append(date[1]+date[0]+"01") 
            
        elif len(re.findall(type7,s)) != 0:
            date = re.findall(type7,s)[0]
            if len(date) == 2:
                date = "19"+date
            datelist.append(date+"01"+"01")
            
        else:
            print(s)
    
    dates = pd.Series(datelist)
    dates.sort_values(inplace=True)
    order = pd.Series(dates.index)
    
    return order
date_sorter()
