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
    x1=x1-f(x1)/yh;
    L=line([x1,x1],[0,f(x1)]);
    set(L,'LineStyle','-.')
    delete(L)
    if abs(f(x1))<eps break; end;
    i=i+1;
end
plot(x,f(x1)+yh*(x-x1),':',x1,f(x1),'*',x1,0,'*',x1,f(x1),'o')
disp("Найденный корень " + x1)
hold off

