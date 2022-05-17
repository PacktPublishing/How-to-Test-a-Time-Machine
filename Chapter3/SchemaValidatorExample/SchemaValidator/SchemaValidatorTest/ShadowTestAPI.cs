using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using System.Net.Http;
using System.Collections.Generic;

namespace SchemaValidatorTest
{
	[TestClass]
	public class ShadowTestAPI {
		private HttpClient client = new HttpClient();

		public static IEnumerable<object[]> DataProvider() {
			object[][] callData = new object[][] {
				new object[]{"inputCall", "expectedOutput"} ,
				// insert more expected data 
			};
			return callData;
		}

		// We could use DynamicData (method) or DataSource (database/file...)
		[DataTestMethod]
		[DataRow("inputCall", "expectedOutput")]
		public async void compareData(String inputCall, String expectedOutput) {
			HttpContent content = new StringContent(inputCall);
			/* We could get expected from the data or make another call like the one below
			 HttpResponseMessage expected = await client.PostAsJsonAsync(“api1”, inputCall); */
			HttpResponseMessage actual = await client.PostAsync("api2", content);
			Assert.AreEqual(expectedOutput, actual, "The new API is returning wrong data");
		}
	}
}
