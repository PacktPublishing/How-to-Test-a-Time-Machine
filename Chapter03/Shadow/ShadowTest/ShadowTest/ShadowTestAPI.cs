using System;
using System.Net.Http;
using System.Collections.Generic;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using System.Threading.Tasks;

namespace ShadowTest {

	[TestClass]
	public class ShadowTestAPI {
		private HttpClient client = new HttpClient();

		public static IEnumerable<object[]> DataProvider() {
			yield return new object[] { "42", "http://numbersapi.com/42?json" } ;
		}

		[DataTestMethod]
		[DynamicData(nameof(DataProvider), DynamicDataSourceType.Method)]
		public async Task compareData(String expectedOutput, String inputCall) {
			HttpResponseMessage actualResponse = await client.GetAsync(inputCall);
			String actualString = await actualResponse.Content.ReadAsStringAsync();
			Console.Out.WriteLine(actualString);
			Console.Out.WriteLine(expectedOutput);
			Assert.IsTrue(actualString.Contains(expectedOutput),
					 "The new API is returning wrong data");
		}
	}
}