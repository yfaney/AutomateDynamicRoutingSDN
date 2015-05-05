#!/usr/bin/python
# Copyright (c) Younghwan Jang, 2014-2015
# You can copy, reuse, modify whatever you want but...
# I want you to specify where it is from.(It is not by force, but a recommendation)

"""Custom topology example

Two directly connected switches plus a host for each switch:

                  +-- switch2 --+
   host1 --- switch1           switch4 --- host2
   host4          +-- switch3 --+
			 |
		  	host3

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        leftHost = self.addHost( 'h1' )
        rightHost = self.addHost( 'h2' )
	host3 = self.addHost( 'h3' )
	host4 = self.addHost( 'h4' )
        switch1 = self.addSwitch( 's1' )
        switch2 = self.addSwitch( 's2' )
        switch3 = self.addSwitch( 's3' )
        switch4 = self.addSwitch( 's4' )

        # Add links
        self.addLink( leftHost, switch1 )
        self.addLink( host4, switch1 )
        self.addLink( switch1, switch2 )
        self.addLink( switch1, switch3 )
        self.addLink( switch3, host3 )
        self.addLink( switch2, switch4 )
        self.addLink( switch3, switch4 )
        self.addLink( switch4, rightHost )


topos = { 'mytopo': ( lambda: MyTopo() ) }