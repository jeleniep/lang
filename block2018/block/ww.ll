; ModuleID = 'block.c'
source_filename = "block.c"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@.str = private unnamed_addr constant [6 x i8] c"%d %f\00", align 1
@.str.1 = private unnamed_addr constant [3 x i8] c"%d\00", align 1

; Function Attrs: noinline nounwind optnone uwtable
define i32 @f1(i32, i32, float) #0 {
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  %6 = alloca float, align 4
  %7 = alloca i32, align 4
  store i32 %0, i32* %4, align 4
  store i32 %1, i32* %5, align 4
  store float %2, float* %6, align 4
  %8 = load i32, i32* %4, align 4
  %9 = load float, float* %6, align 4
  %10 = fptosi float %9 to i32
  %11 = add nsw i32 %8, %10
  store i32 %11, i32* %7, align 4
  %12 = load i32, i32* %7, align 4
  %13 = icmp slt i32 %12, 2
  br i1 %13, label %14, label %15

; <label>:14:                                     ; preds = %3
  store i32 2, i32* %7, align 4
  br label %18

; <label>:15:                                     ; preds = %3
  %16 = load i32, i32* %5, align 4
  %17 = sub nsw i32 1, %16
  store i32 %17, i32* %7, align 4
  br label %18

; <label>:18:                                     ; preds = %15, %14
  %19 = load i32, i32* %4, align 4
  %20 = sub nsw i32 12, %19
  store i32 %20, i32* %7, align 4
  %21 = load i32, i32* %7, align 4
  ret i32 %21
}

; Function Attrs: noinline nounwind optnone uwtable
define i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  %4 = alloca float, align 4
  %5 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 1, i32* %2, align 4
  store i32 0, i32* %3, align 4
  store i32 0, i32* %3, align 4
  br label %6

; <label>:6:                                      ; preds = %15, %0
  %7 = load i32, i32* %3, align 4
  %8 = load i32, i32* %2, align 4
  %9 = icmp slt i32 %7, %8
  br i1 %9, label %10, label %18

; <label>:10:                                     ; preds = %6
  store float 1.230000e+02, float* %4, align 4
  %11 = load i32, i32* %2, align 4
  %12 = load float, float* %4, align 4
  %13 = fpext float %12 to double
  %14 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([6 x i8], [6 x i8]* @.str, i32 0, i32 0), i32 %11, double %13)
  br label %15

; <label>:15:                                     ; preds = %10
  %16 = load i32, i32* %3, align 4
  %17 = add nsw i32 %16, 1
  store i32 %17, i32* %3, align 4
  br label %6

; <label>:18:                                     ; preds = %6
  %19 = load i32, i32* %2, align 4
  %20 = call i32 @f1(i32 1, i32 %19, float 3.000000e+00)
  store i32 %20, i32* %5, align 4
  %21 = load i32, i32* %5, align 4
  %22 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.1, i32 0, i32 0), i32 %21)
  %23 = load i32, i32* %1, align 4
  ret i32 %23
}

declare i32 @printf(i8*, ...) #1

attributes #0 = { noinline nounwind optnone uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.module.flags = !{!0}
!llvm.ident = !{!1}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{!"clang version 6.0.0-1ubuntu2 (tags/RELEASE_600/final)"}
