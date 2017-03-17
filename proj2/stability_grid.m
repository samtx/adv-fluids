N = 121; % chebyshev poly
n = 75;
r = [5000, 7000];
a = [0.6, 1.2];
rr = linspace(r(1),r(2),n);
aa = linspace(a(1),a(2),n);
[RR,AA] = meshgrid(rr,aa);
CC = zeros(n,n);
for i = 1:n
    fprintf('i = %d\n',i);
    parfor j = 1:n
        CC(i,j) = calc_orrsommerfeld(aa(i),rr(j),N);
    end
end
surf(RR,AA,CC);