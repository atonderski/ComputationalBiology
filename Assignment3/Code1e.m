alpha = 1;
beta = 0.5;
numIterations = 10^6;
N = 200;

%% Simulation
infectives = [];
runs = 100;
parfor iRun = 1:runs
  infectives = [infectives; RunSimulation(N, alpha, beta, numIterations)];
  
  fprintf('Completed run %d \n', iRun);
end

infectives = infectives(infectives > 0);

%% Plotting
clf;
hold on;
[bins, edges] = histcounts(infectives);
centers = (edges(1:end-1) + edges(2:end))/2;
centers = centers(bins > 0);
bins = bins(bins > 0);
% scale each bin with the expected average time spent for a step in this
% bin
bins = bins ./ (alpha .* centers .* (1 - centers) + beta .* centers);
bins = bins ./ sum(bins);
bar(centers, bins, 0.5);

x = min(infectives):.001:max(infectives);
norm = normpdf(x, mean(infectives), std(infectives));
norm = norm ./ max(norm) * max(bins);
plot(x, norm, 'LineWidth', 2);

r = alpha / beta;
Ns = 0:.001:1;
s = -(-1 + r - Ns.*r + (-1 + Ns).*r.*log(r-Ns.*r)) / r;
analytical = exp(-N * s(:));
plot(Ns, analytical * max(bins), 'LineWidth', 2);
xlabel('Normalized Population Size');
ylabel('Probability');
title(sprintf('Population distribution for N=%d, \\alpha=%.1f and \\beta=%.2f', N, alpha, beta))

legend('Numerical', 'Gaussian', 'Analytical');

xlim([0.35,0.65])
%xlim([0,0.5])