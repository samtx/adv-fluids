      program correlations

        implicit none
        integer :: i, n, t, tau, max_lag
        real :: sum_num, sum_denom
        real, dimension(n) :: y1, y2
        real, dimension(max_lag) :: rho, lags
        parameter, real :: pi = 3.141592653589793
        
         C Generate sine wave
         do t = 1, n
            y1(t) = sin(t)
         end do
         
         C Loop over tau
         do tau = 0, max_lag-1
         
            C Shift the signal by tau
            y2(:) = 0.0
            y2(1:n-tau) = y1(tau:n)
    
            C Perform the correlations
            sum_num = 0.0
            sum_denom = 0.0
            do i = 1,n
                sum_num = sum_num + y1(i)*y2(i)
                sum_denom = sum_denom + y1(i)*y1(i)
            end do    
            rho(tau+1) = sum_num / sum_denom
            lags(tau+1) = tau
            
         end do
      end program