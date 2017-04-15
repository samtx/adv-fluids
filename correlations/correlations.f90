program correlations

implicit none
integer :: i, n, t, tau, max_lag
real :: sum_num, sum_denom
real, dimension(500) :: y1, y2
real, dimension(500) :: rho, lags
real :: pi = 3.141592653589793

open(unit=1,file='output5.txt')

max_lag = 500
n = 500

! ! Generate sine wave
! do t = 1, n
!     y1(t) = sin(pi/180.0 * float(t))
! end do
 
! Generate sine wave with random fluctuations and nonzero mean 
! do t = 1, n
!     y1(t) = 30 + 10*sin(pi/180.0 * float(t)) + (rand()*6 - 3)
! end do

! ! Generate random fluctuations with nonzero mean 
! do t = 1, n
!     y1(t) = 10 + float(t) + (rand()*2 - 1)
! end do

! ! Generate random fluctuations with zero mean 
! do t = 1, n
!     y1(t) = float(t) + (rand()*2 - 1)
! end do

! Generate sine wave with random fluctuations and zero mean 
do t = 1, n
    y1(t) = 10*sin(pi/180.0 * float(t)) + (rand()*4 - 3)
end do

! Loop over tau
do tau = 0, max_lag-1
 
    ! Shift the signal by tau
    y2(:) = 0.0
    y2(1:n-tau) = y1(tau:n)

    ! Perform the correlations
    sum_num = 0.0
    sum_denom = 0.0
    do i = 1,n
        sum_num = sum_num + y1(i)*y2(i)
        sum_denom = sum_denom + y1(i)*y1(i)
    end do    
    rho(tau+1) = sum_num / sum_denom
    lags(tau+1) = tau
    
end do

! Write results to file
do i = 1,max_lag
    write(unit=1, fmt="(F5.1, F12.7)") lags(i), rho(i)
end do

close(unit=1)

end program