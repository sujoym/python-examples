x=[1,'1/2/2017','Green']
dates=[];
colors=[];
for row in x:
    color=x[2]
    dat=x[1]

    dates.append(dat);
    colors.append(color);
print(colors);
print(dates);

try:
    wCol= input('what is ur color: ');
    col=colors.index(wCol)
    theD=dates[col]
    print('The date is '+ theD + ' for color ' +wCol );

except Exception as e:
    print(e);
    print('Continuing')