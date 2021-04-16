declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)
@strp = constant [4 x i8] c"%d\0A\00"
@strs = constant [3 x i8] c"%d\00"
@x = global i32 0
define i32 @fun() nounwind {
%1 = load i32, i32* @x
%2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strp, i32 0, i32 0), i32 %1)
%x = alloca i32
store i32 3, i32* %x
%3 = load i32, i32* %x
%4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strp, i32 0, i32 0), i32 %3)
%5 = load i32, i32* %x
%fun = alloca i32
store i32 %5, i32* %fun
%6 = load i32, i32* %fun
ret i32 %6
}
@zosia = global i32 0
@ala = global i32 0
define i32 @alax() nounwind {
%ala = alloca i32
store i32 1234, i32* %ala
%1 = load i32, i32* %ala
%2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strp, i32 0, i32 0), i32 %1)
%3 = load i32, i32* %ala
%alax = alloca i32
store i32 %3, i32* %alax
%4 = load i32, i32* %alax
ret i32 %4
}
define i32 @main() nounwind{
%1 = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @strs, i32 0, i32 0), i32* @x)
%2 = call i32 @fun()
store i32 %2, i32* @zosia
%3 = load i32, i32* @zosia
%4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strp, i32 0, i32 0), i32 %3)
store i32 1, i32* @ala
%5 = load i32, i32* @ala
%6 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strp, i32 0, i32 0), i32 %5)
%7 = call i32 @alax()
store i32 %7, i32* @ala
%8 = load i32, i32* @ala
%9 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strp, i32 0, i32 0), i32 %8)
ret i32 0 }

