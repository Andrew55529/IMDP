clear
a = 0;
b = 4*pi;
x = linspace(a,b,100)
h = 0.001;
maxcount=100;
eps=0.001;
f=@(x)sin(x).*(x)-cos(x);
plot(x,f(x),'.',x,0*x,'-'); grid on
xlabel('x'); ylabel('y')
hold on
z = ginput(2); 
z1=z(1,1), z2=z(2,1);
f1 = f(z1); f2=f(z2); z=(z1+z2)/2; y=f(z);
P = plot(z1,0,'*',z2,0,'*',z,0,'o');
if f1*f2>0 
    'Error'
end
i=0;
while(i<maxcount)
    z=(z1+z2)/2; y=f(z);
    P=plot(z1,0,'*',z2,0,'*',z,0,'o');
    if abs(f(z))<eps
        break;
    end
    if y*f1<0
        z2=z;
    else 
        z1=z;
    end
    i=i+1;
end
hold off