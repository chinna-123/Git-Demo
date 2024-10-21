from random import random

number_of_points = 100000;
rng('shuffle')
a = -10;
b = 10;
r = (b-a).*random(2,number_of_points);
r = reshape(r, [2,number_of_points]);
I = eye(2);
e1 = I(:,1); e2 = I(:,2);
theta = inf*ones(1,number_of_points);
rho = inf*ones(1,number_of_points);
for i=1:length(r(1,:))
   x = r(:,i);
   [theta(i),rho(i)] = cart2pol(x(1),x(2));        
end
figure
M=3;N=1; bins = 360;
subplot(M,N,1);
histogram(rad2deg(theta), bins)
title('Polar angle coordinate p.d.f');
subplot(M,N,2);
histogram(rho, bins);
title('Polar radius coordinate p.d.f');
subplot(M,N,3);
histogram(r(:));
title('The x-y cooridnates distrbution (p.d.f)');
Substituting the 3rd line: r = (b-a).*randn(2,number_of_points); with r = (b-a).*randn(2,number_of_points) +a ; will change the distribution of (x,y)
from normal to uniform.
