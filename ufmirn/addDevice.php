<?php include_once "includes/head.php";?>






<div data-role="header" data-position="fixed"> <a href="index.php" data-icon="home">Home</a>
    <h1>Jarvis</h1>
    <a href="updateAndAct.php" data-icon="info">List&nbsp;&nbsp;&nbsp;&nbsp;</a> 
   </div>
  <!-- /header -->
  <div data-role="content"  ><!--content-->
  	<form action="insertIntoDb.php">
    <input type="hidden" name="status" value="0"/>
    <input type="hidden" name="sliderValue" value="0"/>
    	<ul data-role="listview">
        	<li><input type="text" name="name" value="Name"/>
            <li><label>Hardware Address:</label><br><br>
            	<select name="address" id="select-choice-1" data-theme="b" data-mini="true">
					<option value="1234">Room 1</option>
					<option value="5678">Room 2</option>
				</select>
            </li>
            <li><label>Port Number:</label>
            	<select name="pinNumber" id="select-choice-1" data-theme="b" data-mini="true">
					<?php
						for($i=0;$i<14;$i++)
							echo '<option value="'.$i.'">'.$i.'</option>';
					?>
                    
                </select>
                
            </li>
            <li>

	<label>Requires Slider</label>
	<select name="slider" id="flip-min" data-role="slider">

		<option value="0" selected>Nope</option>
   		<option value="1">Yep</option>
	</select>
            </li>
                        <li>
            	<div data-role="fieldcontain">
    <label for="name">command input</label>
    <input type="text" name="command" id="name" value="command"  />
</div>
            </li>
            <li>
            	<button type="submit">Submit</button>
            </li>

        </ul>
        
    </form>
  
  </div>

<?php include_once "includes/foot.php" ?>