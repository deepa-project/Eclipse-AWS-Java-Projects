import time;
import sys;
print(time.asctime());

def annual_increase(x,y):
        for i in range(0,15):
            print("your weight for year %s is %s" % (i,x));
            x=x+y;    
    
def annual_decrease(x,y):
        for i in range(0,15):
            print("your weight for year %s is %s" % (i,x));
            x=x-y;  

x=80;
y=0.165;
z=x*y;
for i in range(1,15):
      print("year %s : my weight on moon is %s kgs" %(i, z));  
print("Enter your wwight :");
your_weight=int(sys.stdin.readline());
print("\nEnter your average annual increase in weight");
your_average_annual_weight_increase=int(sys.stdin.readline());
annual_increase(your_weight,your_average_annual_weight_increase);
annual_decrease(your_weight, your_average_annual_weight_increase);

