using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Accord.Fuzzy;
using System.IO;

namespace RuleBasedSystem
{
	class ruleBasedSystem
	{
		static void Main(string[] args)
		{
			Database fdb = new Database();

			LinguisticVariable priority = new LinguisticVariable("Priority", 0, 100);

			LinguisticVariable steps = new LinguisticVariable("Steps", 0, 100);

			LinguisticVariable isNew = new LinguisticVariable("IsNew", 0, 100);

			LinguisticVariable isPassing = new LinguisticVariable("IsPassing", 0, 100);

			LinguisticVariable shouldExecute = new LinguisticVariable("MarkExecute", 0, 100);

			TrapezoidalFunction priorityLowFunction = new TrapezoidalFunction(20, 40, TrapezoidalFunction.EdgeType.Right);

			FuzzySet priorityLow = new FuzzySet("Low", priorityLowFunction);

			TrapezoidalFunction priorityMediumFunction = new TrapezoidalFunction(20, 40, 60, 80);

			FuzzySet priorityMedium = new FuzzySet("Medium", priorityMediumFunction);

			TrapezoidalFunction priorityHighFunction = new TrapezoidalFunction(60, 80, TrapezoidalFunction.EdgeType.Left);

			FuzzySet priorityHigh = new FuzzySet("High", priorityHighFunction);

			TrapezoidalFunction stepsLowFunction = new TrapezoidalFunction(0, 6, TrapezoidalFunction.EdgeType.Right);

			FuzzySet stepsLow = new FuzzySet("Low", stepsLowFunction);

			TrapezoidalFunction stepsMediumFunction = new TrapezoidalFunction(5, 9, 12, 15);

			FuzzySet stepsMedium = new FuzzySet("Medium", stepsMediumFunction);

			TrapezoidalFunction stepsHighFunction = new TrapezoidalFunction(10, 15, TrapezoidalFunction.EdgeType.Left);

			FuzzySet stepsHigh = new FuzzySet("High", stepsHighFunction);

			TrapezoidalFunction oldFunction = new TrapezoidalFunction(0, 30, TrapezoidalFunction.EdgeType.Right);

			FuzzySet ageOld = new FuzzySet("Old", oldFunction);

			TrapezoidalFunction ageMediumFunction = new TrapezoidalFunction(15, 50, 70, 90);

			FuzzySet ageMedium = new FuzzySet("Medium", ageMediumFunction);

			TrapezoidalFunction ageNewFunction = new TrapezoidalFunction(90, 100, TrapezoidalFunction.EdgeType.Left);

			FuzzySet ageNew = new FuzzySet("New", ageNewFunction);

			TrapezoidalFunction notPassFunction = new TrapezoidalFunction(10, 50, TrapezoidalFunction.EdgeType.Right);

			FuzzySet notPassing = new FuzzySet("Nope", notPassFunction);

			TrapezoidalFunction passingFunction = new TrapezoidalFunction(50, 90, TrapezoidalFunction.EdgeType.Left);

			FuzzySet passing = new FuzzySet("Yes", passingFunction);

			TrapezoidalFunction doNotExecuteFunction = new TrapezoidalFunction(10, 50, TrapezoidalFunction.EdgeType.Right);

			FuzzySet doNotExecute = new FuzzySet("Nope", doNotExecuteFunction);

			TrapezoidalFunction executeFunction = new TrapezoidalFunction(50, 90, TrapezoidalFunction.EdgeType.Left);

			FuzzySet execute = new FuzzySet("Yes", executeFunction);

			priority.AddLabel(priorityLow);

			priority.AddLabel(priorityMedium);

			priority.AddLabel(priorityHigh);

			steps.AddLabel(stepsLow);

			steps.AddLabel(stepsMedium);

			steps.AddLabel(stepsHigh);

			isNew.AddLabel(ageNew);

			isNew.AddLabel(ageMedium);

			isNew.AddLabel(ageOld);

			isPassing.AddLabel(passing);

			isPassing.AddLabel(notPassing);

			shouldExecute.AddLabel(execute);

			shouldExecute.AddLabel(doNotExecute);

			fdb.AddVariable(priority);

			fdb.AddVariable(steps);

			fdb.AddVariable(isNew);

			fdb.AddVariable(isPassing);

			fdb.AddVariable(shouldExecute);

			InferenceSystem IS = new InferenceSystem(fdb, new CentroidDefuzzifier(1000));

			IS.NewRule("Rule 1", "IF Priority IS High THEN MarkExecute IS Yes");

			IS.NewRule("Rule 2", "IF Priority IS Medium AND IsPassing IS Nope THEN MarkExecute IS Yes");

			IS.NewRule("Rule 3", "IF Priority IS Medium AND IsNew IS Medium then MarkExecute IS Yes");

			IS.NewRule("Rule 4", "IF Priority IS Low AND IsPassing IS Yes THEN MarkExecute IS Nope");

			IS.NewRule("Rule 5", "IF Priority IS Low AND IsNew IS Old THEN MarkExecute IS Nope");

			IS.NewRule("Rule 6", "IF Steps IS High AND IsPassing IS Nope THEN MarkExecute IS Yes");

			IS.NewRule("Rule 7", "IF Steps IS Low AND Priority IS Medium THEN MarkExecute IS Yes");

			IS.NewRule("Rule 8", "IF Steps IS High AND Priority IS Medium THEN MarkExecute IS Nope");

			// IS.SetInput("IsNew", 3);
			// IS.SetInput("Steps", 3);
			// IS.SetInput("Priority", 20);
			// IS.SetInput("IsPassing", 10);

			IS.SetInput("IsNew", 90);

			IS.SetInput("Priority", 90);

			IS.SetInput("Steps", 20);

			IS.SetInput("IsPassing", 90);

			/*try {

				float testCaseResult = IS.Evaluate("MarkExecute");
				Console.WriteLine("The test case should be " + testCaseResult + " executed.");
				Console.ReadKey();

			} catch (Exception e) {
				Console.WriteLine("We found an exception : " + e.Message);
				Console.ReadKey();

			}*/

			try {
				String[] lines = File.ReadAllLines(@"testcases.csv");
				StringBuilder testResults = new StringBuilder();
				foreach (String line in lines) {
					String[] test = line.Split(',');
					IS.SetInput("Priority", float.Parse(test[0]));
					IS.SetInput("Steps", float.Parse(test[1]));
					IS.SetInput("IsNew", float.Parse(test[2]));
					IS.SetInput("IsPassing", float.Parse(test[3]));
					float testCaseResult = IS.Evaluate("MarkExecute");
					testResults.Append(line).Append(',').Append(testCaseResult);
					testResults.Append(';').AppendLine();
				}
				File.WriteAllText("testResults.csv", testResults.ToString());

			}
			catch (Exception e) {

				Console.WriteLine("Exception found: " + e.Message);
				Console.ReadKey();
			}
		}
	}
}
