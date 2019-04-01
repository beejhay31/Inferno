print ('I am inferno storm')
data=pd.read_csv('Salary_Data.csv')
data=pd.read_csv('Salary_Data.csv')
data.head(10)
data.head(10)
YearsExperience	Salary
0	1.1	39343.0
1	1.3	46205.0
2	1.5	37731.0
3	2.0	43525.0
4	2.2	39891.0
5	2.9	56642.0
6	3.0	60150.0
7	3.2	54445.0
8	3.2	64445.0
9	3.7	57189.0
x=data['YearsExperience']
y=data['Salary']
x.head(10)
x=data['YearsExperience']
y=data['Salary']
x.head(10)
0    1.1
1    1.3
2    1.5
3    2.0
4    2.2
5    2.9
6    3.0
7    3.2
8    3.2
9    3.7
Name: YearsExperience, dtype: float64
y.head(10)
y.head(10)
0    39343.0
1    46205.0
2    37731.0
3    43525.0
4    39891.0
5    56642.0
6    60150.0
7    54445.0
8    64445.0
9    57189.0
Name: Salary, dtype: float64
plt.scatter(x,y, color='red', label='Scatter plot')
plt.xlabel('YearsExperience')
plt.ylabel('Salary')
plt.legend()
plt.show()
plt.scatter(x,y, color='red', label='Scatter plot')
plt.xlabel('YearsExperience')
plt.ylabel('Salary')
plt.legend()
plt.show()

mean_x=np.mean(x)
mean_y=np.mean(y)
mean_x
mean_x=np.mean(x)
mean_y=np.mean(y)
mean_x
5.3133333333333335
mean_y
mean_y
76003.0
n=len(x)
n
30
top=0
bottom=0
for i in range(n):
    top += np.sum((x[i]-mean_x)*(y[i]-mean_y))
    bottom += (x[i]-mean_x)**2
a=top/bottom
b=mean_y-(a*mean_x)
a.round(),a
(9450.0, 9449.9623214550775)
b.round(),b
(25792.0, 25792.200198668688)
y_pred=b+a*x
y_pred
0      36187.158752
1      38077.151217
2      39967.143681
3      44692.124842
4      46582.117306
5      53197.090931
6      54142.087163
7      56032.079627
8      56032.079627
9      60757.060788
10     62647.053252
11     63592.049484
12     63592.049484
13     64537.045717
14     68317.030645
15     72097.015574
16     73987.008038
17     75877.000502
18     81546.977895
19     82491.974127
20     90051.943985
21     92886.932681
22    100446.902538
23    103281.891235
24    108006.872395
25    110841.861092
26    115566.842252
27    116511.838485
28    123126.812110
29    125016.804574
Name: YearsExperience, dtype: float64
plt.plot(x,y_pred, color='blue', label='Regession Line')
plt.scatter(x,y, color='red', label='Actual Data')
plt.xlabel('YearsExperience')
plt.ylabel('Salary')
plt.legend()
plt.show()


