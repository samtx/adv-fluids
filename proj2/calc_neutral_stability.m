% alogrithm to plot neutral stability curve
% INPUTS
%   alpha = starting alpha
%   R     = starting Reynolds number
%   N      = degree of Chebyshev polynomial to use
%   step   = step size to use
%   tol    = tolerance to find c_i=0
alpha = .74;
R = 13000;
N = 121;
step = [250, .005];
tol = [0.1, 1e-4];
maxiter = 1000;
R_cutoff = 10000;

i = 1;
R_init = R;
R_opt = optimset('TolX',tol(1));
alpha_opt =optimset('TolX',tol(2));
R_step = step(1);
alpha_step = step(2);

print_results = @(R, alpha) fprintf('R = %6i,  alpha = %8.6f \n',[R, alpha]);
    
    while R >= R_cutoff && i < maxiter
        f = @(alpha) calc_orrsommerfeld(alpha, R, N);
        [alpha,fval,exitflag,output]  = fzero(f, alpha, alpha_opt); 
        if exitflag > 0 % root found
            neutStab(i,1:2) = [R, alpha]; %#ok<*SAGROW>
            i = i + 1;
            print_results(R, alpha);
            R = R - R_step;
        end
    end
    
    fprintf('... switch to f(R) ...\n');
    while R < R_cutoff && i < maxiter
        f = @(R) calc_orrsommerfeld(alpha, R, N);
        [R,fval,exitflag,output]  = fzero(f, R, R_opt); 
        if exitflag > 0 % root found
            neutStab(i,1:2) = [R, alpha]; 
            i = i + 1;
            print_results(R, alpha);
            alpha = alpha + alpha_step;
        else
            break
%             alpha_step = -alpha_step;  %reverse step
        end
    end
    
    fprintf('... switch back to f(alpha) ...\n');
    while R < R_init && i < maxiter
        f = @(alpha) calc_orrsommerfeld(alpha, R, N);
        [alpha,fval,exitflag,output]  = fzero(f, alpha, alpha_opt); 
        if exitflag > 0 % root found
            neutStab(i,1:2) = [R, alpha]; 
            i = i + 1;
            print_results(R, alpha);
            R = R + R_step;
        end
    end

% plot neutral stability curve
fig = plot(neutStab(:,1), neutStab(:,2));
axis([0,100000, 0.4, 1.2]);
xlabel('Reynolds Number');
ylabel('Frequency \alpha');




