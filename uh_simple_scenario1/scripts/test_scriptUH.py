#!/usr/bin/python

import time

import roslib
roslib.load_manifest('cob_script_server')
import rospy

from simple_script_server import script

import tf
from geometry_msgs.msg import *

class GraspScript(script):
		
	def Initialize(self):
		# initialize components (not needed for simulation)
		self.sss.init("tray")
		self.sss.init("torso")
		self.sss.init("arm")
		self.sss.init("sdh")
		self.sss.init("base")
		
		# move to initial positions
		handle01 = self.sss.move("arm","folded",False)
		self.sss.move("torso","home",False)
		self.sss.move("sdh","home",False)
		self.sss.move("tray","down")
		handle01.wait()
		if not self.sss.parse:
			print "Please localize the robot with rviz"
		self.sss.wait_for_input()
		#self.sss.move("base","home")
	
	def AttentionSeeking(self):
		self.sss.move("base", "livingroom")
		self.sss.set_light("red")
		self.sss.sleep(1)		
		self.sss.set_light("blue")
		self.sss.sleep(1)
		self.sss.set_light("red")
		self.sss.sleep(1)
		self.sss.set_light("blue")
		self.sss.sleep(1)		
		self.sss.move("arm", "intermediateback")
		self.sss.move("arm", "intermediatefront")
		#keep on waving till it finish the speech
		self.sss.move("arm", "wave", False) #False for no blocking
		self.sss.move_base_direct("base",[0,0,0.05,1]) #xvel, yvel,orientation vel on Z-axis, sec
		self.sss.say(["Hello Alex"], False)
		self.sss.set_light([0,0,0])
		self.sss.sleep(1)
		self.sss.move_base_direct("base",[0,0,-0.05,2])		
		self.sss.set_light("yellow")
		self.sss.move("arm", "wave", False)		
		self.sss.sleep(1)
		self.sss.set_light([0,0,0])
		self.sss.sleep(1)
		self.sss.move_base_direct("base",[0,0,0.05,2])
		self.sss.set_light("yellow")
		self.sss.sleep(1)
		self.sss.set_light([0,0,0])
		self.sss.sleep(1)
		self.sss.move_base_direct("base",[0,0,-0.05,1])		
		self.sss.set_light("yellow")
		self.sss.sleep(1)
		self.sss.say(["there is some one at the door for you"])
		handleIntFront = self.sss.move("arm", "intermediatefront",False)
		self.sss.set_light([0,0,0])
		self.sss.sleep(1)
		self.sss.set_light("yellow")
		self.sss.sleep(1)
		self.sss.set_light([0,0,0])
		self.sss.sleep(1)
		self.sss.set_light("yellow")
		self.sss.sleep(1)
		self.sss.set_light([0,0,0])
		self.sss.sleep(1)
		self.sss.set_light("yellow")
		self.sss.sleep(1)
		handleIntFront.wait();
		self.sss.move("arm", "intermediateback", False)
		self.sss.move("sdh","point", False)
		self.sss.set_light([0,0,0])
		self.sss.sleep(1)
		self.sss.set_light("yellow")
		self.sss.sleep(1)
		self.sss.set_light([0,0,0])
		self.sss.sleep(1)
		self.sss.set_light("yellow")
		self.sss.sleep(1)
		self.sss.set_light([0,0,0])
		self.sss.sleep(1)
		self.sss.set_light("yellow")
		self.sss.sleep(1)
		self.sss.move("sdh", "cylclosed")
		self.sss.move("arm", "folded")
		self.sss.move("tray","up")
		self.sss.move("tray","down")
		self.sss.move("torso","left")
		self.sss.move("torso","home")

	def Run(self): 
		self.AttentionSeeking()

if __name__ == "__main__":
	SCRIPT = GraspScript()
	SCRIPT.Start()
