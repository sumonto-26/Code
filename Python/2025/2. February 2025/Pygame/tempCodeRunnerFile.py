    def color_change(c, incr_speed, decr_speed):
        if(c >= 254):
            while(c > 0): 
                c -= decr_speed
        elif(c <= 0):
            while(c < 254):
                c += incr_speed