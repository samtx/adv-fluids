        PROGRAM CORRELATIONS
        
        IMPLICIT NONE
        INTEGER I, N, T, TAU, MAX_LAG
        REAL SUM_NUM, SUM_DENOM
        REAL Y1(500), Y2(500)
        REAL RHO(500), LAGS(500)
        REAL PI
        
        OPEN(UNIT=1,FILE='OUTPUT.TXT')
        
        PI = 3.141592653589793
        MAX_LAG = 500
        N = 500
        
C       GENERATE SINE WAVE
        DO T = 1, N
            Y1(T) = SIN(FLOAT(T))
        END DO
         
C       LOOP OVER TAU
        DO TAU = 0, MAX_LAG-1
         
C       SHIFT THE SIGNAL BY TAU
        Y2(1:N) = 0.0
        Y2(1:N-TAU) = Y1(TAU:N)
        
C       PERFORM THE CORRELATIONS
            SUM_NUM = 0.0
            SUM_DENOM = 0.0
            DO I = 1,N
                SUM_NUM = SUM_NUM + Y1(I)*Y2(I)
                SUM_DENOM = SUM_DENOM + Y1(I)*Y1(I)
            END DO    
            RHO(TAU+1) = SUM_NUM / SUM_DENOM
            LAGS(TAU+1) = TAU
            
            
        END DO
100     FORMAT(I6, F12.7)
C       WRITE RESULTS TO FILE
        DO I = 1,MAX_LAG
            WRITE(UNIT=1, FMT=100) LAGS(I), RHO(I)
        END DO
        
        CLOSE(UNIT=1)
        
        END PROGRAM