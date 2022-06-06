a = 0;
b = 4*pi;
x = linspace(a,b,100)
maxcount=100;
eps=0.001;
f=@(x)sin(x).*(x)-cos(x);
plot(x,f(x),'.',x,0*x,'-'); grid on
xlabel('x'); ylabel('y')
hold on
z = ginput(2); 
z1=z(1,1), z2=z(2,1); z=(z2-z1)/2+z1;
f1 = f(z1); f2=f(z2); y=f(z);
P = plot(z1,0,'*',z2,0,'*',z,0,'o');
flag = 0;
if f1*f2>0 'Плохие точки'
end;
end
i=0;
while(i<maxcount)
    z=(z2-z1)/2+z1;
    y=f(z);
    P=plot(z1,0,'*',z2,0,'*',z,0,'o');
    if abs(f(z))<eps
        flag = 1;
        break;
    end
    if y*f1<0
        z2=z;
    else 
        z1=z;
    end
    i=i+1;
end

if flag == 1
    plot(z1,0,'*',z2,0,'*',z,0,'o');
    disp("Найденный корень " + z);
end;

hold off
