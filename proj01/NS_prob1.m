% syms x1 x2 f(x2) nu
% v1 = nu*((x1^2+x2^2)^2)*f(x2);  %velocity
% g_d = [1/(x1^2+x2^2)^2,0;0,1/(x1^2+x2^2)^2]; %covariant metric coefficients
% g_u = [(x1^2+x2^2)^2,0;0,(x1^2+x2^2)^2];  %contravarialt metric coefficients
% 
% Ga_1 = 2*[-x1 -x2;-x2 x1]/(x1^2+x2^2);
% Ga_2 = 2*[x2 -x1;-x1 -x2]/(x1^2+x2^2);
% LHS_1 = simplify((v1*diff(v1,x1)+v1^2*Ga_1(1,1))/g_u(1,1));
% RHS_1 = simplify(nu*(diff(diff(v1,x1),x1)+diff(diff(v1,x2),x2)+diff(v1,x1)*(Ga_1(1,1)-Ga_1(2,2))+diff(v1,x2)*(2*Ga_1(1,2)-Ga_2(1,1)-Ga_2(2,2))));
% LHS_2 = simplify((v1)^2*Ga_2(1,1)/g_u(1,1));
% RHS_2 = simplify(2*nu*(diff(v1,x1)*Ga_2(1,1)+diff(v1,x2)*Ga_2(1,2)));
% NS_1 = simplify(LHS_1-RHS_1);
% NS_2 = simplify(LHS_2-RHS_2);
% NS_Final = simplify(diff(NS_1,x2)-diff(NS_2,x1));
% NS_eqn = NS_Final/(nu^2*(x1^2+x2^2));
% NS_aft_int = int(NS_eqn,x2);


v1 = nu/((x1^2+x2^2)^2)*f(x2);  %velocity
% g_d = [1/(x1^2+x2^2)^2,0;0,1/(x1^2+x2^2)^2]; %covariant metric coefficients
g_u = [1/(x1^2+x2^2)^2,0;0,1/(x1^2+x2^2)^2];  %contravarialt metric coefficients

Ga_1 = [x1 x2;x2 -x1]/(x1^2+x2^2);
Ga_2 = [-x2 x1;x1 x2]/(x1^2+x2^2);

LHS_1 = simplify((v1*diff(v1,x1)+v1^2*Ga_1(1,1))/g_u(1,1));
RHS_1 = simplify(nu*(diff(diff(v1,x1),x1)+diff(diff(v1,x2),x2)+diff(v1,x1)*(Ga_1(1,1)-Ga_1(2,2))+diff(v1,x2)*(2*Ga_1(1,2)-Ga_2(1,1)-Ga_2(2,2))));
LHS_2 = simplify((v1)^2*Ga_2(1,1)/g_u(1,1));
RHS_2 = simplify(2*nu*(diff(v1,x1)*Ga_2(1,1)+diff(v1,x2)*Ga_2(1,2)));
NS_1 = simplify(LHS_1-RHS_1);
NS_2 = simplify(LHS_2-RHS_2);
NS_Final = simplify(diff(NS_1,x2)-diff(NS_2,x1));
NS_eqn = NS_Final/(nu^2*(x1^2+x2^2));
NS_aft_int = int(NS_eqn,x2);