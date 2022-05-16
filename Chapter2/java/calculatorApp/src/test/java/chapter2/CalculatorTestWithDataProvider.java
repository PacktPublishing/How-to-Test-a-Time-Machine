package chapter2;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ArgumentsSource;

public class CalculatorTestWithDataProvider {
    
    /**
    * Test normal scenarios
    **/
    @ParameterizedTest
    @ArgumentsSource(CalculatorDataProvider.class)
    public void TestAdd (int first, int second, int result) {
        Calculator calculator = new Calculator();
        assertEquals(result, calculator.confusingAdd(first, second));
    }

    /**
    * Test exceptions
    **/
    @ParameterizedTest
    @ArgumentsSource(CalculatorDataProvider.class)
    public void TestExceptionsAdd(int first, int second) 
    {
        Calculator calculator = new Calculator();
        assertThrows(IndexOutOfBoundsException.class, () -> { calculator.confusingAdd(first, second);});
    }
}
