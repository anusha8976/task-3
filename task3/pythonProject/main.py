import matplotlib.pyplot as plt
import pandas as pd
#sample data
data = {
    'course':['c','c++','java','python','R'],
    'students enrolled':['40','15','30','50','20']
}
#create a dataframe from data
df=pd.DataFrame(data)
plt.bar(df['course'],df['students enrolled'], width=0.5, color="green")
plt.title('students intrest in programming lang')
          #label
plt.xlabel('course name')
plt.ylabel('no of student')
plt.legend('S')
#display the chart
plt.show()
import matplotlib.pyplot as plt
import pandas as pd
#sample data
data = {
    'course':['c','c++','java','python','R'],
    'students enrolled':['40','15','30','50','20']
}
#create a dataframe from data
df=pd.DataFrame(data)
plt.plot(df['course'],df['students enrolled'],  color="red")
plt.title('students intrest in programming lang')
          #label
plt.xlabel('course name')
plt.ylabel('no of student')
plt.legend('S')
#display the chart
plt.show()