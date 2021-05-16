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
q = qwe(1240.0, 1231.0)
x = 12.0 - q
q = (asd(5.0, 0.0) + asd(0.0, 2.0)) / qwe(12.0, 2.0) * 2.0
q = 2.0
write(x)
write(q)
end
