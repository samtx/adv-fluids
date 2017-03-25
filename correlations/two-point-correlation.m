clear all, clc, close all

%# random signal
B=(2*rand(1,500))+9;

%y1 = cumsum(rand(500,1));
y1 = cumsum((2*rand(1,500)) + 9);

%# autocorrelation
%maxlag = length(y1);   %# set a max lag value here
maxlag=500;
[c,lags] = xcorr(detrend(y1), maxlag, 'coeff');

m=detrend(y1);

%[d,lags] = corrcoef(detrend(y1), maxlag, 'biased');

figure(1)
plot(B)
xlabel('time'), ylabel('V')

figure(2)
%# plot
hold on
plot(lags,c,'LineWidth',2), xlabel('\tau'), ylabel('correlation coefficient')
plot([-500 500],[0 0],'k');
plot([0 0],[-1 1],'k');
%axis([0 500 -1 1]);

figure(3)
%# plot
hold on
plot(lags,c,'LineWidth',2), xlabel('\tau'), ylabel('correlation coefficient')
plot([-500 500],[0 0],'k');
plot([0 0],[-1 1],'k');
axis([0 500 -1 1]);

%figure(2)
%plot(B)
% xlabel('time'), ylabel('V')

%figure(3)
%plot(m)