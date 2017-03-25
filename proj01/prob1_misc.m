syms xi1 xi2 x y
% x = 1/2 * (xi1^2 + xi2^2);
% y = xi1*xi2;

S = solve([x==(1/2)*(xi1^2+xi2^2), y==xi1*xi2],...
	[xi1, xi2], 'ReturnConditions', true);
S.x
S.y
S.conditions
S.parameters