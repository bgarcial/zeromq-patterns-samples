import zmq


zmq_VERSION      = zmq.zmq_version_info()
anAgentsIDENTITY = whateverHashOrHumanReadableSTRING
notMINE          = anAgentsIDENTITY

if     zmq_VERSION[0] < 4:
           print "ZMQ{0:} ver < than expected, will exit".format( zmq_VERSION )
aCTX = zmq.Context( 2 )                        # if performance boosting is needed

#SUB ---------------------------------------------------------------------------
aSUB = aCTX.socket( zmq.SUB )
aSUB.setsockopt(    zmq.LINGER,          0 )   # protect your agent
aSUB.setsockopt(    zmq.MAXMSGSIZE,      m )   # protect your agent from DoS
aSUB.setsockopt(    zmq.AFFINITY,        1 )   # protect your server resources
aSUB.setsockopt(    zmq.HEARTBEAT_IVL,   ivl ) #     set server helping Heartbeats
aSUB.setsockopt(    zmq.HEARTBEAT_TTL,   ttl ) #     set server helping Heartbeats
aSUB.setsockopt(    zmq.INVERT_MATCHING, 1 )   #   avoid server sending data back
aSUB.setsockopt(    zmq.SUBSCRIBE,       notMINE )  #  NEVER .recv()-s  data back
...
#SUB PERFORMANCE & RESOURCES TWEAKING DETAILS GO WAY BEYOND THE SCOPE OF THIS POST

aSUB.connect(      "tcp://localhost:5557" )

#PUSH --------------------------------------------------------------------------
aPUSH = aCTX.socket( zmq.PUSH )
...
#PUSH PERFORMANCE & RESOURCES TWEAKING DETAILS GO WAY BEYOND THE SCOPE OF THIS POST

#main loop ---------------------------------------------------------------------
pass; notSoftFLAG = True; anAgentSignsWithIdentityPREFIX = anAgentsIDENTITY
while notSoftFLAG:

    if aReasonToSendSomethingToServer:
       aPUSH.send( anAgentSignsWithIdentityPREFIX
                 + ":::"
                 + aMsgPAYLOAD,
                   zmq.DONTWAIT
                   )                          # inspect ZMQError
       ...
       pass

    if aSUB.poll( 100 ):
       message = aSUB.recv( zmq.DONTWAIT )    #  NEVER .recv()-s own data back
       ...
       pass


    if aReasonToFlagLoopEXIT:
       notSoftFLAG = False
       ...
       pass

    if ...:
       ...
       pass

#main loop ---------------------------------------------------------------------
pass

#########
# ALWAYS:
#          better using context-aware try:/except:/finally:

aRetCODE = [ aSOCK.close() for aSOCK in ( aSUB, aPUSH, ) ]
...

aCTX.term()
#   .term()
#########