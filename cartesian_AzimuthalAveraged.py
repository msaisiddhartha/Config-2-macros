CFViewBackward(912)
mflow = ['4']

Viewnum = 1
for i in mflow:
    fis = 'C:/Users/msais/Box Sync/Thesis Work/Old Geometry_Done/Krain/te_stk/te_stk_111_SA_'+i+'kgs/'
    FileOpenProject(fis+'te_stk_111_SA_'+i+'kgs.run')
    SetTurboMode()
    OpenTurboModeStandard3DView()
    OpenTurboModeBladeToBladeView()
    OpenTurboModeBladeView()
    OpenTurboModeMeridionalView(0,0)
    ViewActivate('te_stk_111_SA_'+i+'kgs.run:'+str(Viewnum))
    Viewnum+=3
    ViewActivate(':'+str(Viewnum))
    Viewnum+=1
    QntFieldScalar('atan(Wt/Wm)')
    RprSection(0,0.045000002,0,0,0.1225,0,0,0,1 ,'Section 1',0 ,'',0)
    ViewActivate(':'+str(Viewnum))
    Viewnum+=1
    SelectPlotCurves('Section 1 on D6.I=1(0:1,0.714286:0.857143)')
    UpdateCurveType(0,1,1,0,0,0,1,2,0,1,1,0,0.4,4,1,1)
    PlotFctOfQnt()
    PlotOrdinateNormArcLen()
    VAxisLabelText('Normalized Span')
    HAxisLabelText('Rel. flow angle (rad)')
    LimitsFull()
    ActivePlotCurveOutput(fis+'MassAvg.dat' ,'Section 1 on D6.I=1(0:1,0.714286:0.857143)')


    fi = 'C:/Users/msais/Box Sync/Thesis Work/Old Geometry_Done/Multi-stage/Backsweep 30 deg_2/initial/initial_111_SA_'+i+'kgs/'
    FileOpenProject(fi+'initial_111_SA_'+i+'kgs.run')
    SetTurboMode()
    OpenTurboModeStandard3DView()
    OpenTurboModeBladeToBladeView()
    OpenTurboModeBladeView()
    OpenTurboModeMeridionalView(0,0)
    ViewActivate('initial_111_SA_'+i+'kgs.run:'+str(Viewnum))
    Viewnum+=3
    ViewActivate(':'+str(Viewnum))
    Viewnum+=1
    QntFieldScalar('atan(Wt/Wm)')
    RprSection(0,0.045000002,0,0,0.1225,0,0,0,1 ,'Section 1',0 ,'',0)
    ViewActivate(':'+str(Viewnum))
    Viewnum+=1
    SelectPlotCurves('Section 1 on D20.I=1(0:1,0.714286:0.857143)')
    UpdateCurveType(0,1,1,0,0,0,1,1,0,1,1,0,0.4,4,1,1)
    PlotFctOfQnt()
    PlotOrdinateNormArcLen()
    VAxisLabelText('Normalized Span')
    HAxisLabelText('Rel. flow angle (rad)')
    LimitsFull()
    ActivePlotCurveOutput(fi+'MassAvg.dat' ,'Section 1 on D20.I=1(0:1,0.714286:0.857143)')
    SelectPlotCurves('Section 1 on D20.I=1(0:1,0.714286:0.857143)')
    RenameCurve('Section 1 on D20.I=1(0:1,0.714286:0.857143)' ,'Multi-Stage')
    InsertNewCurveFromFile('Single-Stage' ,fis+'MassAvg.dat')
    FitOrdinate()
    FitAbscissa()
    SelectPlotCurves('Single-Stage')
    UpdateCurveType(0,0,0,0,0,0,1,2,0,0,0,0,0.4,4,1,1)
    AddToLegend('Single-Stage')
    AddToLegend('Multi-Stage')
    SetLegendTextType(10,12,1,0,1,0,0,1,0,0,0,0)
    SetLegendPosition(-0.461765,0.354944,0)
    SetNumecaLogo(0,0)
    Print(8,0,0,1,100,1920,1080,0 ,'C:/Users/msais/Box Sync/Thesis Work/Documentation/C7 3D CFD Analysis/Beta_inlet_'+i+'kgs.png' ,'',1,0,1)
    FileCloseProject()
    Viewnum+=1
