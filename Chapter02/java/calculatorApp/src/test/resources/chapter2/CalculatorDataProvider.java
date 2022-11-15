package chapter2;

import java.util.ArrayList;
import java.util.stream.Stream;

import org.junit.jupiter.api.extension.ExtensionContext;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.ArgumentsProvider;

public class CalculatorDataProvider implements ArgumentsProvider {
    /**
    * Represents the data which is expected to pass.
    * data[X][0] = first number to add for the Xth entry
    * data[X][1] = second number to add for the Xth entry
    * data[X][2] = result of the add method for the Xth entry
    **/
    public static Object[][] goodData () 
    {
        // 3 + 4 = 7
        Object[][] data = new Object[3][3];
        data[0][0] = 3;
        data[0][1] = 4;
        data[0][2] = 7;
        // 0 + 0 = 0
        data[1][0] = 0;
        data[1][1] = 0;
        data[1][2] = 0;
        // 1 + 2147483646 = 2147483647
        data[2][0] = 1;
        data[2][1] = 2147483646;
        data[2][2] = 2147483647;
        return data;
    }
    /**
    * Represents the data that is expected to throw an exception
    * data[X][0] = first number to add for the Xth entry
    * data[X][1] = second number to add for the Xth entry
    * No need for Data[X][3] as we will not expect result
    **/
    public static Object[][] exceptionData() 
    {
        // 2147483647 + 2147483647
        Object[][] data = new Object[3][3];
        data[0][0] = 2147483647; // or Integer.MAX_VALUE
        data[0][1] = 2147483647;
        // -2147483648 + -2147483648
        data[1][0] = -2147483648; // or Integer.MIN_VALUE
        data[1][1] = -2147483648;
        // 2 + 2147483646 > 2147483647
        data[2][0] = 2;
        data[2][1] = 2147483646;     
        return data;
    }

    @Override
    public Stream<? extends Arguments> provideArguments(ExtensionContext context) throws Exception {
        Arguments[] argList;
        int length = 0;
        if (context.getTestMethod().toString().contains("Exception")) {
            length = exceptionData().length;
            argList = new Arguments[length];
            for (int i= 0; i<length ; i++) {
                argList[i] = Arguments.of(exceptionData()[i]);
            }
        } else {
            length = goodData().length;
            argList = new Arguments[length];
            for (int i= 0; i<length ; i++) {
                argList[i] = Arguments.of(goodData()[i]);
            }
        }
        return Stream.of(argList);
    }
}
