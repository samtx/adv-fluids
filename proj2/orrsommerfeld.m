% Matlab script to find global eigenvalues for Poiseuille flow
clear
N=120;
R=31965;
alpha=1;
% The collocation points are at ybar=cos(m*pi/(N-1)) for m=0..N-1
% Setup matrix t of Chebyshev polynomials and their derivatives at each collocation
% point
for m=N-2:-1:2
    ybar=cos(m*pi/(N-1));
    t=0.0;
    t(1,1)=1.0;
    t(1,2)=ybar;
    for ii=2:N-1
        t(1,ii+1)=2.0*ybar*t(1,ii)-t(1,ii-1);
    end
    for j=2:5
        t(j,1)=0.0;
        t(j,2)=t(j-1,1);
        t(j,3)=4.0*t(j-1,2);
        for k=4:N
            t(j,k)=2.0*(k-1.0)*t(j-1,k-1)+(k-1.0)/(k-3.0)*t(j,k-2);
        end
    end
    % Evaluate the base flow at value of ybar
    U=1.0-ybar^2.0;
    dU=-2.0*ybar;
    d2U=-2.0;
    % Setting up matrices of Orr-Sommerfeld equation
    for j=1:N
        a(N-m,j)=U*(t(3,j)-alpha^2*t(1,j))-d2U*t(1,j)-1.0/(1i*alpha*R)*(t(5,j)-2.0*alpha^2*t(3,j)+alpha^4.0*t(1,j));
        b(N-m,j)=t(3,j)-alpha^2*t(1,j);
    end
end

% Boundary conditions
for j=1:N
    a(1,j)=1.0;
    a(2,j)=(j-1.0)^2.0;
    a(N-1,j)=(-1.0)^(j-2.0)*(j-1.0)^2.0;
    a(N,j)=(-1.0)^(j-1.0);
    b(1,j)=0.0;
    b(2,j)=0.0;
    b(N-1,j)=0.0;
    b(N,j)=0.0;
end

% find eigenvalues c
[V,D]=eig(a,b);
% put eigenvalues into plottable form
realc = zeros(1,N);
imagc = zeros(1,N);
for j=1:N
    realc(j)=real(D(j,j));
    imagc(j)=imag(D(j,j));
end

plot(realc,imagc,'+',[0 1],[0 0],'MarkerSize',10)
xlabel('c_r','Fontsize',14);
ylabel('c_i','Fontsize',14);
axis([0 1 -1 0.1])

% Check if there are positive, finite c_i
max(imagc(~isinf(imagc)))>=0
