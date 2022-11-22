using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.EventSystems; // Required when using Event data.

public class Opendoor : MonoBehaviour, IPointerDownHandler
{
	public bool doorGoingUp;
	public float topReach;

	void OnMouseEnter()
	{
		doorGoingUp = true;
		Debug.Log("mousee");
	}
	public void OnPointerDown(PointerEventData eventData)
	{
		doorGoingUp = true;
		Debug.Log("mousep");
	}


	void OnMouseDown()
	{
		doorGoingUp = true;
		Debug.Log("moused");
	}

	// Start is called before the first frame update
	void Start()
    {        
    }

	// Update is called once per frame
	void Update()
	{
		GameObject door = GameObject.FindGameObjectWithTag("door");
		float y = door.gameObject.transform.position.y;
		float x = door.gameObject.transform.position.x;
		float z = door.gameObject.transform.position.z;
		if (doorGoingUp && door.gameObject.transform.position.y <= topReach)
		{
			y += 0.05f;
			door.gameObject.transform.position = new Vector3(x, y, z);
		}
	}
	

	void UnityApiMouseEvents()
	{
		Debug.Log("here");
		Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
		RaycastHit hit;
		if (Physics.Raycast(ray, out hit))
		{
			if (hit.rigidbody != null)
				hit.rigidbody.gameObject.SendMessage("OnMouseDown");
			else
				hit.collider.SendMessage("OnMouseDown");
		}

	}
}
