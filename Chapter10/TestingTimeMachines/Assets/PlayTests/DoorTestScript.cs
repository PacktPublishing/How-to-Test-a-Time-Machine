using System.Collections;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.TestTools;
using UnityEngine.SceneManagement;

public class DoorTestScript
{
    // A Test behaves as an ordinary method
    [Test]
    public void NewTestScriptSimplePasses()
    {
		// Use the Assert class to test conditions
	}

	// A UnityTest behaves like a coroutine in Play Mode. In Edit Mode you can use
	// `yield return null;` to skip a frame.
	[UnityTest]
    public IEnumerator DoorTestScriptWithEnumeratorPasses()
    {
		SceneManager.LoadScene("TTM", LoadSceneMode.Single);
		yield return new WaitForDomainReload();
		GameObject door = GameObject.Find("Door");
		Vector3 position = door.transform.position;
		Debug.Log("Initial position " + door.transform.position);
		door.SendMessage("OnMouseDown");
		yield return new WaitForDomainReload();
		Assert.AreNotEqual(position, door.transform.position);
		Debug.Log("Final position " + door.transform.position);
		yield return null;
    }
}
