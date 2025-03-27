BEGIN
    INPUT Num1
    INPUT Num2
    INPUT MenuOption
    IF MenuOption = "Add" THEN
        Answer = Num1 + Num2
    ELSE
        Answer = Num1 - Num2
    ENDIF
    DISPLAY Answer
END
