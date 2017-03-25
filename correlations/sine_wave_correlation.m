clear all, clc, close all

% random signal
%B=(2*rand(1,500))+9;



%y1 = cumsum(rand(500,1));
%y1 = cumsum((2*rand(1,500)) + 9);

t = [0:1:530];
y1 = 10+sind(t);

% autocorrelation
%maxlag = length(y1);   % set a max lag value here
maxlag=530;
[c,lags] = xcorr(detrend(y1), maxlag, 'coeff');

m=detrend(y1);

%[d,lags] = corrcoef(detrend(y1), maxlag, 'biased');

%{
figure(1)
plot(y1)
xlabel('time','FontSize',14), ylabel('V','FontSize',14)
%axis([0 530 9 11]);
%}

for i=1:length(lags)
    xy(i,1)=lags(i);
    xy(i,2)=c(i);
end

figure(2)
% plot
hold on
plot(lags,c,'LineWidth',2), xlabel('\tau','FontSize',22), ylabel('correlation coefficient','FontSize',18)
plot([-500 500],[0 0],'k');
plot([0 0],[-1 1],'k');
axis([-530 530 -1 1]);

save tecplot_sine_correlation.dat xy -ascii

%{
figure(3)
%# plot
hold on
plot(lags,c,'LineWidth',2), xlabel('\tau','FontSize',22), ylabel('correlation coefficient','FontSize',18)
plot([-500 500],[0 0],'k');
plot([0 0],[-1 1],'k');
axis([0 530 -1 1]);
%}

%figure(2)
%plot(B)
% xlabel('time'), ylabel('V')

%figure(3)
%plot(m)