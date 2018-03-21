function ns = RunSimulation(N, alpha, beta, nIterations)
    ns = zeros(nIterations, 1);
    ns(1) = 1 - beta / alpha;
    for i=2:nIterations
        n = ns(i-1);
        prob_increase = alpha * (1 - n) * n;
        prob_decrease = beta * n;
        % Normalize probabilities since we don't care about the situation where nothing changes
        prob_norm_factor = prob_decrease + prob_increase;
        if rand() < prob_increase / prob_norm_factor
            ns(i) = n + 1 / N;
        else
            ns(i) = n - 1 / N;
        end
        if n < 1 / N
            fprintf("Exctintion for N=%d after %d\n", N, i);
            break
        end
    end
end