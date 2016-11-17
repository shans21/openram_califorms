#!/usr/bin/env python2.7
"Run a regresion test the library cells for DRC"

import unittest
from testutils import header
import sys,os
sys.path.append(os.path.join(sys.path[0],"../.."))
sys.path.append(os.path.join(sys.path[0],".."))
import globals
import debug
import calibre


class no_blockages_test(unittest.TestCase):

    def runTest(self):
        globals.init_openram("config_{0}".format(OPTS.tech_name))

        import design
        import router

        class gdscell(design.design):
            """
            A generic GDS design that we can route on.
            """
            def __init__(self, name):
                #design.design.__init__(self, name)
                debug.info(2, "Create {0} object".format(name))
                self.name = name
                self.gds_file = name + ".gds"
                self.sp_file = name + ".sp"                                
                design.hierarchy_layout.layout.__init__(self, name)
                design.hierarchy_spice.spice.__init__(self, name)
            
        class routing(design.design):
            """
            A generic GDS design that we can route on.
            """
            def __init__(self, name, gdsname):
                design.design.__init__(self, name)
                debug.info(2, "Create {0} object".format(name))

                cell = gdscell(gdsname)
                self.add_inst(name=gdsname,
                              mod=cell,
                              offset=[0,0])
                self.connect_inst([])
                
                r=router.router(gdsname+".gds")
                layer_stack =("metal1","via1","metal2")
                path=r.route(layer_stack,src="A",dest="B")
                r.rg.view()
                
                self.add_wire(layer_stack,path)

        
        r = routing("test1", "A_to_B_no_blockages")
        self.local_check(r)
        
        r = routing("A_to_B_m1m2_blockages")
        self.local_check(r)
        
        r = routing("A_to_B_m1m2_same_layer_pins")
        self.local_check(r)
        
        r = routing("A_to_B_m1m2_diff_layer_pins")
        self.local_check(r)
        
        # fails if there are any DRC errors on any cells
        self.assertEqual(drc_errors, 0)
        globals.end_openram()


    def local_check(self, r):
        tempgds = OPTS.openram_temp + "temp.gds"
        r.gds_write(tempgds)
        self.assertFalse(calibre.run_drc(r.name, tempgds))
        os.remove(tempgds)
        assert(0)

                             


# instantiate a copy of the class to actually run the test
if __name__ == "__main__":
    (OPTS, args) = globals.parse_args()
    del sys.argv[1:]
    header(__file__, OPTS.tech_name)
    unittest.main()