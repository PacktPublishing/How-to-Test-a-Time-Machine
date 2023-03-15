using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace UnitTestProject1
{
	[TestClass]
	public class UnitTest1
	{
		[TestMethod]
		[Priority(2)]
		public void TestMethod1()
		{
			Assert.Fail();
		}

		[TestMethod]
		[Priority(1)]
		public void TestMethod2()
		{
			Assert.Fail();
		}

		[TestMethod]
		[Priority(3)]
		public void TestMethod3()
		{
			Assert.Fail();
		}

		[TestMethod]
		[Priority(1)]
		public void TestMethod4()
		{
			Assert.Fail();
		}
	}
}
