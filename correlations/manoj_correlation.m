%program to calculate cross correlation function for a sine wave

t = 0:1:500;
A = sind(t)';
figure(1)
plot(A)
%A = 9+2*rand(501,1);
A_shifted = zeros(length(A),1);
coerr_coeff = zeros(length(t),1);

for m = 0:length(t)-1
    A_shifted = zeros(length(A),1);
    A_shifted(1:length(t)-m,1) = A(m+1:length(A),1);
    total_sum=0;
    for n = 1:length(A_shifted)
        total_sum_num = sum(A.*A_shifted);
        total_sum_den = sum(A.*A);
        coerr_coeff(m+1) = total_sum_num/total_sum_den;
    end
end


figure(2)
plot(t,coerr_coeff)