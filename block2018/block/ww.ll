; ModuleID = 'block.c'
source_filename = "block.c"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

sas = global i32 0, align 4
@.str = private unnamed_addr constant [6 x i8] c"%d %f\00", align 1

; Function Attrs: noinline nounwind optnone uwtable
define i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca double, align 8
  %4 = alloca float, align 4
  store i32 0, i32* %1, align 4
  store i32 97563, i32* sas, align 4
  %5 = load i32, i32* sas, align 4
  %6 = add nsw i32 1, %5
  store i32 %6, i32* %2, align 4
  store double 0.000000e+00, double* %3, align 8
  br label %7

; <label>:7:                                      ; preds = %12, %0
  %8 = load double, double* %3, align 8
  %9 = load i32, i32* %2, align 4
  %10 = sitofp i32 %9 to double
  %11 = fcmp olt double %8, %10
  br i1 %11, label %12, label %19

; <label>:12:                                     ; preds = %7
  store float 1.230000e+02, float* %4, align 4
  %13 = load i32, i32* %2, align 4
  %14 = load float, float* %4, align 4
  %15 = fpext float %14 to double
  %16 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([6 x i8], [6 x i8]* @.str, i32 0, i32 0), i32 %13, double %15)
  %17 = load double, double* %3, align 8
  %18 = fadd double %17, 1.000000e+00
  store double %18, double* %3, align 8
  br label %7

; <label>:19:                                     ; preds = %7
  %20 = load i32, i32* %1, align 4
  ret i32 %20
}

declare i32 @printf(i8*, ...) #1

attributes #0 = { noinline nounwind optnone uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.module.flags = !{!0}
!llvm.ident = !{!1}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{!"clang version 6.0.0-1ubuntu2 (tags/RELEASE_600/final)"}
