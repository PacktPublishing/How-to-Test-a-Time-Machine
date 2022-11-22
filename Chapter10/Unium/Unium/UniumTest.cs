using System;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using NUnit.Framework;
using System.Threading.Tasks;
using Unium.Helpers;

namespace Unium
{
	[TestFixture]
	public class UniumTest
	{
			[Test]
			public async Task CheckDoorBehaviour()
			{

				using (var u = new WebsocketHelper())
				{
					// connect to game 
					await u.Connect(Test.TestConfig.WS);
					dynamic camera = await u.Get("/q/scene/XRRig");
					await u.Get("/q/scene/XRRig.transform.position={\"x\":1, \"y\":1, \"z\":1}");
					await u.Get("/q/scene/XRRig.transform.position={\"x\":180, \"y\":1, \"z\":1}");

					dynamic doorPosition = await u.Get("/q/Scene/Door.transform.position");
					await u.Get("/q/scene/Door.SendMessage(OnMouseDown)");
					dynamic doorPosition2 = await u.Get("/q/Scene/Door.transform.position");
					Assert.AreNotEqual(doorPosition, doorPosition2);
				}
			}
		
	}
}