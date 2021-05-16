float asd(float kl, float s) 
    float z
    z = kl + s    
    return z
end

float qwe(float kl, float s) 
    float z
    z = kl - s    
    return z
end

float x
float q
q = 2.2
x = 21.0 - q
x = asd(x, 2.0)
write(x)
x = 21.0 - q
x = qwe(x, 2.0)
write(x)
end
