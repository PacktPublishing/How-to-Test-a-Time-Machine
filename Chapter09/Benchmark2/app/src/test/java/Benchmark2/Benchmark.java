package Benchmark2;
import org.testng.annotations.BeforeClass; 
import org.testng.annotations.AfterClass; 
import org.testng.annotations.Test; 

public class Benchmark { 
 long classStart;

 @BeforeClass 
 public void setUp() { 
    classStart = System.nanoTime();
    long threadID = Thread.currentThread().getId();
    System.out.println(String.format("Class starting on thread %s ...", threadID));
 } 

 @Test 
 public void test1Time() { 
    long testStart = System.nanoTime(); 
    long threadID = Thread.currentThread().getId();
    System.out.println(String.format("Starting test1 on thread %s", threadID)); 
    long testFinish = System.nanoTime();
    System.out.println(String.format("Test 1 took: %s nanoseconds", (testFinish - testStart)));
 } 

 @Test
 public void test2Time() {
   long testStart = System.nanoTime(); 
   long threadID = Thread.currentThread().getId();
   System.out.println(String.format("Starting test2 on thread %s", threadID)); 
   long testFinish = System.nanoTime();
   System.out.println(String.format("Test 2 took: %s nanoseconds", testFinish - testStart));
 }

 @AfterClass
 public void tearDown() { 
    long classFinish = System.nanoTime(); 
    System.out.println(String.format("Class took: %s nanoseconds", classFinish - classStart)); 
    System.out.println(String.format("or %s milliseconds", (classFinish - classStart) / 1e6));
 } 
} 