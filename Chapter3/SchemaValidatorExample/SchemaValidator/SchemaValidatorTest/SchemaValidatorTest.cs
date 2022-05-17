using Newtonsoft.Json.Linq;
using Newtonsoft.Json.Schema;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using SchemaValidatorSrc;

namespace SchemaValidatorTest
{
	[TestClass]
	public class SchemaValidatorTest
	{
		private JObject readJson(string name)
		{
			return JObject.Parse(System.IO.File.ReadAllText(name));
		}

		private JSchema readSchema(string name)
		{
			return JSchema.Parse(System.IO.File.ReadAllText(name));
		}

		[TestMethod]
		public void validateEmptySchemaTest()
		{
			SchemaValidator schemaValidator = new SchemaValidator();
			Assert.IsTrue(schemaValidator.validate(readJson("example.json"), JSchema.Parse("{}")));
		}

		[TestMethod]
		public void validateEmptyObjectTest()
		{
			SchemaValidator schemaValidator = new SchemaValidator();
			Assert.IsFalse(schemaValidator.validate(JObject.Parse("{\"bad\":1}"), readSchema("schema.json")));
		}

		[TestMethod]
		public void validateTest()
		{
			SchemaValidator schemaValidator = new SchemaValidator();
			Assert.IsTrue(schemaValidator.validate(readJson("example.json"), readSchema("schema.json")));
		}
	}
}
