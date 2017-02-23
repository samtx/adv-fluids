% Plots for project 1, advanced fluids, MEEN 622
% Sam Friedman, 2/7/2017
% 

% get x1, x2 coordinates from xi1, xi2
n = 200;
xi = [linspace(15,20,n)', linspace(-.8,.8,n)'];

clf
hold on

% plot xi1 coordinates for a fixed xi2
for j = 1:size(xi,1)
    xi_tmp = [xi(:,1),xi(j,2)*ones(size(xi(:,1)))];
    x = [.5*xi_tmp(:,1).^2-.5*xi_tmp(:,2).^2, xi_tmp(:,1).*xi_tmp(:,2)];

%     x = [.5*xi(:,1).^2-.5*xi(j,2).^2, xi(:,1).*xi(j,2)];
    plt = plot(x(:,1),x(:,2),'k');
    axis([110,210,-20,20]);
    pause(.0001);
end

% plot xi2 coordinates for a fixed xi1
for j = 1:size(xi,1)
    x = [.5*xi(j,1).^2+.5*xi(:,2).^2, xi(j,1).*xi(:,2)];
    plt = plot(x(:,1),x(:,2),'k');
    pause(.0001);
end

xlabel('X_1'); ylabel('X_2');
% xlim([40,120]);

title('2D-Flow Through a Concave Curved Channel');
% plot x