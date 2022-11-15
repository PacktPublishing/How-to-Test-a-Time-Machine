using System;
using Newtonsoft.Json.Linq;
using Newtonsoft.Json.Schema;
using System.Collections.Generic;

namespace SchemaValidatorSrc
{
	public class SchemaValidator
	{
		// Retrieving schema from before and object from the response...
		public bool validate(JObject toValidate, JSchema schema)
		{
			IList<string> messages;
			bool valid = toValidate.IsValid(schema, out messages);
			foreach (string message in messages)
			{
				Console.WriteLine(message);
			}
			/* Instead of writing in console we may want to raise an exception here with the message list*/
			return valid;
		}

		static public void Main(String[] args)
		{
			Console.WriteLine("Schema Validator, use test");
		}
	}
}
