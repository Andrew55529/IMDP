clear
a=0;
b=4*pi;
x = linspace(a,b,100);
h = 0.001; maxcount = 1000; eps = 0.001;
f=@(x)sin(x).*(x)-cos(x);
y = f(x);
plot(x,f(x),'.',x,0*x,'-'); grid on
xlabel('x'); ylabel('y')
hold on
ylim([min(y),max(y)]);
z = ginput(1);
x1=z(1);
i=0;
while(i<maxcount)
    yh=(f(x1+h)-f(x1))/h;
    x2=x1-f(x1)/yh;
    L=line([x2,x2],[0,f(x2)]);
    set(L,'LineStyle','-.')
    x1=x2;
    delete(L)
    if abs(f(x2))<eps break; end;
    i=i+1;
end
P=plot(x,f(x1)+yh*(x-x1),':',x1,f(x1),'*',x2,0,'*',x2,f(x2),'o')
hold off
