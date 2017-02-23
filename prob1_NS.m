% symbolic expression for NS for project 1b prob 1
% Sam friedman

syms xi1 xi2 V nu rho 
syms F(xi2)  % symbolic function of xi2
Gamma1 = sym('G1', [2,2]);
Gamma2 = sym('G2', [2,2]);
g11 = 1/(xi1^2 + xi2^2);
g22 = g11;
V = symfun(nu*1/(xi1^2 + xi2^2)*F, [xi1, xi2]);


% christoffel symbols, gamma
Gamma1(1,1) = 1/(xi1^2 + xi2^2) * xi1;
Gamma1(1,2) = 1/(xi1^2 + xi2^2) * xi2;
Gamma1(2,1) = 1/(xi1^2 + xi2^2) * xi1;
Gamma1(2,2) = 1/(xi1^2 + xi2^2) * -xi1;

Gamma2(1,1) = 1/(xi1^2 + xi2^2) * -xi2;
Gamma2(1,2) = 1/(xi1^2 + xi2^2) * xi1;
Gamma2(2,1) = 1/(xi1^2 + xi2^2) * xi1;
Gamma2(2,2) = 1/(xi1^2 + xi2^2) * xi2;

% NS equation
% syms p(xi1,xi2) 
% simplify(-V*diff(V,xi1) - V*V*G1(1,1) -1/rho*diff(p,xi1)*g11 + nu*g11*(...
%     diff(V,xi1,2) + diff(V,xi2,2) + diff(V,xi1)*(G1(1,1)-G1(2,2)) ...
%     + diff(V,xi2)*(2*G1(1,1)-G2(2,2)-G2(2,2))))
    
syms p(xi1, xi2)
LHS_1 = simplify(V*diff(V,xi1) + V*V*Gamma1(1,1));
RHS_1 = simplify(-1/rho*diff(p,xi1)*g11 + nu*g11*(...
    diff(V,xi1,2) + diff(V,xi2,2) + diff(V,xi1)*(Gamma1(1,1)-Gamma1(2,2)) ...
    + diff(V,xi2)*(2*Gamma1(1,2)-Gamma2(2,2)-Gamma2(2,2))));
LHS_2 = simplify(V*V*Gamma2(1,1));
RHS_2 = simplify(-1/rho*diff(p,xi2)*g22 + nu*g22*(2*diff(V,xi1)*Gamma2(1,1) ...
    + 2*diff(V,xi2)*Gamma2(1,2)));
NS_1 = simplify(LHS_1 - RHS_1);
NS_2 = simplify(LHS_2-RHS_2);
NS_Final = simplify(diff(NS_1,xi2)-diff(NS_2,xi1));
% NS_eqn = NS_Final/(nu^2*(xi1^2+xi2^2));
NS_eqn = NS_Final;
NS_aft_int = int(NS_eqn,xi2);
fctr = (2*nu)/(xi1^2 + xi2^2)^2;

% LHS_1 = simplify((v1*diff(v1,x1)+v1^2*Ga_1(1,1))/g_u(1,1));
% RHS_1 = simplify(nu*(diff(diff(v1,x1),x1)+diff(diff(v1,x2),x2)+diff(v1,x1)*(Ga_1(1,1)-Ga_1(2,2))+diff(v1,x2)*(2*Ga_1(1,2)-Ga_2(1,1)-Ga_2(2,2))));
% LHS_2 = simplify((v1)^2*Ga_2(1,1)/g_u(1,1));
% RHS_2 = simplify(2*nu*(diff(v1,x1)*Ga_2(1,1)+diff(v1,x2)*Ga_2(1,2)));
% NS_1 = simplify(LHS_1-RHS_1);
% NS_2 = simplify(LHS_2-RHS_2);
% NS_Final = simplify(diff(NS_1,x2)-diff(NS_2,x1));
% NS_eqn = NS_Final/(nu^2*(x1^2+x2^2));
% NS_aft_int = int(NS_eqn,x2);
