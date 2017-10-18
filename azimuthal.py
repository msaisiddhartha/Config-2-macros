CFViewBackward(912)
mflow = ['3','3.5','4']
DefaultsLoad('C:/Users/msais/Box Sync/Thesis Work/Old Geometry_Done/macro/def_settings.def')
FlowQuantites = ['Relative Mach Number']
Rnge = [[0,1.4]]
isolne_switch=[1]

Viewnum = 1
for i in mflow:
    fi = 'C:/Users/msais/Box Sync/Thesis Work/Old Geometry_Done/Krain/te_stk/te_stk_111_SA_'+i+'kgs/'
    FileOpenProject(fi+'te_stk_111_SA_'+i+'kgs.run')
    SetTurboMode()
    OpenTurboModeStandard3DView()
    OpenTurboModeBladeToBladeView()
    OpenTurboModeBladeView()
    OpenTurboModeMeridionalView(0,0)
    ViewActivate('te_stk_111_SA_'+i+'kgs.run:'+str(Viewnum))
    ViewActivate(':'+str(Viewnum+3))
    SetNumecaLogo(0,0)
    Limits(-1,0,-1,1)
    ViewOriginal()
    GmtToggleBoundary()

    fi = 'C:/Users/msais/Box Sync/Thesis Work/Old Geometry_Done/Multi-stage/Backsweep 30 deg_2/initial/initial_111_SA_'+i+'kgs/'
    FileOpenProject(fi+'initial_111_SA_'+i+'kgs.run')
    SetTurboMode()
    OpenTurboModeStandard3DView()
    OpenTurboModeBladeToBladeView()
    OpenTurboModeBladeView()
    OpenTurboModeMeridionalView(0,0)
    ViewActivate('initial_111_SA_'+i+'kgs.run:'+str(Viewnum+4))
    ViewActivate(':'+str(Viewnum+7))
    SetNumecaLogo(0,0)
    Limits(0,1,-1,1)
    ViewOriginal()
    GmtToggleBoundary()

    ViewActivate(':'+str(Viewnum+3))
    QntFieldScalar(FlowQuantites[0])
    SclContourStrip()
    RprRangeIn(Rnge[0][0], Rnge[0][1])
    RprColormap(0)
    DeleteIsoline()
    SclIsolineMulti(2,4,0,1.1,0.037931,1)

    ViewActivate(':'+str(Viewnum+7))
    QntFieldScalar(FlowQuantites[0])
    SclContourStrip()
    RprRangeIn(Rnge[0][0], Rnge[0][1])
    ColormapStripesOnly()
    DeleteIsoline()
    SclIsolineMulti(2,4,0,1.1,0.037931,1)
    DefaultColormapType(10,12,2,2,1,0,0,1,0,0,0,0,1,1,0.012,10,12,2,0,1,0,0,1,0,0,0,0,0,0,6,10,3,0,21,5,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1)

    Print(8,1,0,1,100,1148,693,0 ,'C:/Users/msais/Box Sync/Thesis Work/Documentation/C7 3D CFD Analysis/config2_relmach_mf'+str(i)+'kgs.png' ,'',1,1,1)
    Viewnum+=8
