% system1_velocity_profile
function system1_velocity_profile()

zta1 = 12;
xi1_dim = [10, 15];
xi2_dim = [-0.8, 0.8];
graphNum = 2;
figure(graphNum);
plt = gca;
plt.ColorOrderIndex = 1;

    hold on
    if graphNum == 1
        for Re = [500, 750, 1000]  % reynolds number
        xi1 = 11;
        C = 2*Re - 10; %constant
        solinit = bvpinit(linspace(xi2_dim(1),xi2_dim(2),10),[-1, 1]);
        PhiFun = @(xi2,y) [y(2);(2*Re*y(1)^2-10*y(1)-6*xi2*y(2)-C)/(xi1^2+xi2^2)];
        PhiBC = @(ya,yb) [ya(1); yb(1)];
        sol = bvp4c(PhiFun,PhiBC,solinit);
        xi2 = linspace(xi2_dim(1),xi2_dim(2),20);
        y = deval(sol,xi2);
        
        % Plot value of F
        plot(-y(1,:),xi2,'LineWidth',2)
        title('F(\xi_2) in Concave Channel');
        velocity = sqrt(xi1^2+xi2.^2).*y(1,:);
        norm_vel = velocity/max(abs(velocity));
        end
        lg = legend('Re = 500','Re = 750', 'Re = 1000');
        set(lg,'FontSize',14,'LineWidth',2);
    elseif graphNum == 2
        for Re = [500, 750, 1000]  % reynolds number
        xi1 = 11;
        C = 2*Re - 10; %constant
        solinit = bvpinit(linspace(xi2_dim(1),xi2_dim(2),10),[-1, 1]);
        PhiFun = @(xi2,y) [y(2);(2*Re*y(1)^2-10*y(1)-6*xi2*y(2)-C)/(xi1^2+xi2^2)];
        PhiBC = @(ya,yb) [ya(1); yb(1)];
        sol = bvp4c(PhiFun,PhiBC,solinit);
        xi2 = linspace(xi2_dim(1),xi2_dim(2),20);
        y = -deval(sol,xi2);
        % Plot value of Phi
        velocity = sqrt(xi1^2+xi2.^2).*y(1,:);
        norm_vel = velocity/max(abs(velocity));
        plot(norm_vel,xi2,'LineWidth',2)
        end
        title('Normalized \Phi = F/F_{max} in Concave Channel');
        lg = legend('Re = 500','Re = 750', 'Re = 1000');
        set(lg,'FontSize',14,'LineWidth',2);
        
    else
%         plt.ColorOrderIndex = 1;
% Plot domain
            n = 15;
            xi = [linspace(10,15,n)', linspace(-.8,.8,n)'];
            % plot xi1 coordinates for a fixed xi2
            hold on
            for j = 1:size(xi,1)
                xi_tmp = [xi(:,1),xi(j,2)*ones(size(xi(:,1)))];
                x = [.5*xi_tmp(:,1).^2-.5*xi_tmp(:,2).^2, xi_tmp(:,1).*xi_tmp(:,2)];
                plot(plt, x(:,1),x(:,2),'k');
                %     axis([110,210,-20,20]);
            end
            % plot xi2 coordinates for a fixed xi1
            for j = 1:size(xi,1)
                x = [.5*xi(j,1).^2+.5*xi(:,2).^2, xi(j,1).*xi(:,2)];
                plot(plt, x(:,1),x(:,2),'k');
            end
        for xi1 = [11, 14]  % xi1 position
            plt.ColorOrderIndex = 1;

            for Re = [500, 750, 1000]  % reynolds number
            C = 2*Re - 10; %constant
            solinit = bvpinit(linspace(xi2_dim(1),xi2_dim(2),10),[-1, 1]);
            PhiFun = @(xi2,y) [y(2);(2*Re*y(1)^2-10*y(1)-6*xi2*y(2)-C)/(xi1^2+xi2^2)];
            PhiBC = @(ya,yb) [ya(1); yb(1)];
            sol = bvp4c(PhiFun,PhiBC,solinit);
            xi2 = linspace(xi2_dim(1),xi2_dim(2),20);
            y = deval(sol,xi2);
            % Plot in x-y coordinates overlayed on channel domain
           velocity = -sqrt(xi1^2+xi2.^2).*y(1,:);
            norm_vel = velocity/max(abs(velocity));
            norm_vel = norm_vel(:);
            xi2 = xi2(:);
            
            % Plot velocity profile over domain
            t = 1;
            Xi1 = norm_vel*t + xi1;
            xx = (0.5)*(Xi1.^2+xi2.^2);
            yy = Xi1.*xi2;
            h(Re) = plot(plt, xx, yy,'LineWidth',3);
            end

        end
        lg = legend([h(500),h(750),h(1000)], 'Re = 500','Re = 750','Re = 1000');
        set(lg,'FontSize',14,'LineWidth',2)
        title('Velocity Profile in Concave Channel');
        xlabel('x'); ylabel('y');
        % hold(plt,'off')
    end
    hold off
    
end



    function res = concave_cond_dim(ya,yb)
        res = [ya(1);yb(1)];
    end


    function dydx = concave_bvp_dim(xi2,y,xi1,C)
        dydx = [y(2);(2*xi2*y(1)^2-10*y(1)-6*xi2*y(2)-C)/(xi1^2+xi2^2)];
    end

    function plt = concave_domain(plt, n)
        % get x1, x2 coordinates from xi1, xi2
        xi = [linspace(15,20,n)', linspace(-.8,.8,n)'];
        % plot xi1 coordinates for a fixed xi2
        hold(plt,'on');
        for j = 1:size(xi,1)
            xi_tmp = [xi(:,1),xi(j,2)*ones(size(xi(:,1)))];
            x = [.5*xi_tmp(:,1).^2-.5*xi_tmp(:,2).^2, xi_tmp(:,1).*xi_tmp(:,2)];
            
            %     x = [.5*xi(:,1).^2-.5*xi(j,2).^2, xi(:,1).*xi(j,2)];
            plot(plt, x(:,1),x(:,2),'k');
            %     axis([110,210,-20,20]);
            %     pause(.0001);
        end
        % plot xi2 coordinates for a fixed xi1
        for j = 1:size(xi,1)
            x = [.5*xi(j,1).^2+.5*xi(:,2).^2, xi(j,1).*xi(:,2)];
            plot(plt, x(:,1),x(:,2),'k');
            %     pause(.0001);
        end
        
        xlabel('x'); ylabel('y');
        title('2D-Flow Through a Concave Curved Channel');
        hold(plt,'off');
        
    end