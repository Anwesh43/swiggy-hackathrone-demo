<?php

	#require_once "conn.php"
	
	$option = $_GET['option'];
	if(isset($_GET['data']))
		$data = $_GET['data'];
	if(isset($_POST['Restaurant_id']))
		$Restaurant_id = $_POST['Restaurant_id'];
		
	if(isset($_POST['item_id']))
		$item_id = $_POST['item_id'];
		
		
	
	switch($option)
	{
		case 'Locality':
				DummyLocalityData($data);
				break;
		case 'Restaurant':
				DummyFooddata($data);
				break;
		case 'Food':
				GetDummyFoodInfo($data);
				break;
		case 'ConfirmOrder':
				ConfirmOrder($Restaurant_id, $item_id);
				break;
		default:
				return;
		
	}
	
	function DummyLocalityData($LocalityName)
	{
		$output_array = array();
		$output_array[] = array('Restaurant' => "Lazeez" , 'Restaurant_id' => 1 );
		$output_array[] = array('Restaurant' => "SukhSagar" , 'Restaurant_id' => 2 );
		$output_array[] = array('Restaurant' => "KFC" , 'Restaurant_id' => 3 );
		$output_array[] = array('Restaurant' => "PizzaHut" , 'Restaurant_id' => 4 );
		$output_array[] = array('Restaurant' => "Grameen" , 'Restaurant_id' => 6940798 );
		$output_array[] = array('Restaurant' => "SOHOStreet" , 'Restaurant_id' => 6 );
		echo json_encode($output_array);
	}
	
	function DummyFooddata($Restaurant)
	{
		$output_array = array();
		$output_array[] = array('FoodItem' => "Dal Fry" , 'ItemId' => 5959936149 );
		$output_array[] = array('FoodItem' => "Plain Naan" , 'ItemId' => 5959936150 );
		$output_array[] = array('FoodItem' => "Paneer Butter Masala" , 'ItemId' => 5959936151 );
		$output_array[] = array('FoodItem' => "Navrathan Korma" , 'ItemId' => 5959936152 );
		$output_array[] = array('FoodItem' => "Kashmiri Pulao" , 'ItemId' => 5959936153 );
		$output_array[] = array('FoodItem' => "Lassi" , 'ItemId' => 5959936154 );
		echo json_encode($output_array);
	}
	
	
	
	function GetDummyFoodInfo($FoodInfo)
	{
		switch(strtolower($FoodInfo))
		{
			case 'dal fry':
			case 'dal':
				echo json_encode("110");
				break;
			case 'paneer butter masala':
			case 'paneer':
				echo json_encode("160");
				break;
			case 'plain naan':
				echo json_encode("40");
				break;
			case 'navrathan korma':
			case 'navratan korma':
				echo json_encode("170");
				break;
			case 'kashmiri pulao':
			case 'pulao':
				echo json_encode("140");
				break;
			case 'lassi':
				echo json_encode("40");
				break;
			default:
			    echo json_encode("-999");
				break;
		}
	}
	
	function ConfirmOrder($restaurant_id,$item_id)
	{
		$conn = mysqli_connect("localhost","root","","testmydb");
		$sql = "SELECT max(order_id) FROM `order_details` WHERE 1";
		$customerid = 0;
		$orderid = 0;
		
		$result = $conn->query($sql);
		if ($result->num_rows > 0) 
		{
			while($row = $result->fetch_assoc())
			{
				$orderid = $row['max(order_id)'] + 1;
				$t=time();
				$timestamp = date("Y-m-d",$t);
				$paymentstatus = 0;
				$customer_id = 1;
				$customer_lat = 0;
				$customer_long = 0;
				$customer_user_agent = "User Agent 1";
				$payment_method = "Swiggy Bank";
				
				$sql = "INSERT INTO `order_details` (`order_id`, `ordered_time`, `payment_status`, `customer_id`, `customer_lat`, `customer_lng`, `customer_user_agent`, `payment_method`, `restaurant_id`) VALUES ($orderid, '$timestamp', '0', $customerid, '0', '0','$customer_user_agent' , '$payment_method', '$restaurant_id');";
				//echo $sql;
				$result = $conn->query($sql);
				$colors = array("red", "green", "blue", "yellow");
				
								
				
				$itemidlist = json_decode(file_get_contents("./json.txt"));
				$itemid = $_POST['item_id'];
				
				$itemsql = "INSERT INTO `order_items` (`id`, `order_id`, `item_id`, `quantity`) VALUES (NULL, $orderid, '$itemid' , 1);";
				$result1 = $conn->query($itemsql);
				
				break;
			}
		}
		else
		{
			
		}
		echo  json_encode("true");

	}

?>