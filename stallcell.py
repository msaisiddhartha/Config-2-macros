
CFViewBackward(912)
mf = '3'
quant = 'Vr'
b2b = 0.9

fi = 'C:/Users/msais/Box Sync/Thesis Work/Old Geometry_Done/Krain/te_stk/te_stk_111_SA_'+mf+'kgs/'
FileOpenProject(fi+'te_stk_111_SA_'+mf+'kgs.run')
GmtRepetitionToggle()
GmtRepetitionNumber(23)
SelectFromProject('row 1_hub_(r.p.m. -22345)' ,'row 1_shroud' ,'row 1_blade_(r.p.m. -22345)')
GmtToggleBoundary()
CutPlaneSave(b2b,0,0,1,0,0,2)
SelectFromProject('CUT1')
GmtToggleBoundary()
ViewPlaneZ()
QntFieldScalar(quant)
SclContourStrip()
ColormapStripesOnly()
RprRangeIn(-80,260)
RprColormap(0)
ViewZoomAll(1)
Print(8,0,0,1,100,1920,1080,0 ,fi+quant+'_'+str(b2b)+'b2b_stall.png' ,'',1,0,1)
#FileCloseProject()
Limits(-1,0,-1,1)
SetCamera(0.0198781,0.00954631,-1.22266,0.0198781,0.00954631,0.0361362,1,0,0,0.50352,0.50352)

fi = 'C:/Users/msais/Box Sync/Thesis Work/Old Geometry_Done/Multi-stage/Backsweep 30 deg_2/initial/initial_111_SA_'+mf+'kgs/'
FileOpenProject(fi+'initial_111_SA_'+mf+'kgs.run')
GmtRepetitionToggle()
GmtRepetitionNumber(23)
SelectFromProject('row 1_hub_(r.p.m. -22345)' ,'row 1_shroud' ,'row 1_blade_(r.p.m. -22345)')
GmtToggleBoundary()
SelectFromProject('row 2_hub_(r.p.m. 0)' ,'row 2_shroud' ,'row 2_blade')
GmtToggleBoundary()
SelectFromProject('row 3_hub_(r.p.m. -22345)' ,'row 3_shroud_(r.p.m. -22345)' ,'row 3_blade_(r.p.m. -22345)')
GmtToggleBoundary()
CutPlaneSave(b2b,0,0,1,0,0,2)
SelectFromProject('CUT1')
GmtToggleBoundary()
ViewPlaneZ()
QntFieldScalar(quant)
SclContourStrip()
ColormapStripesOnly()
RprRangeIn(-80,260)
ColormapLabelTextType(10,12,2,2,1,0,0,1,0,0,0,0)
ColormapTicksNumberTextType(10,12,2,0,1,0,0,1,0,0,0,0)
ViewZoomAll(1)
Print(8,0,0,1,100,1920,1080,0 ,fi+quant+'_'+str(b2b)+'b2b_stall.png' ,'',1,0,1)
Limits(0,1,-1,1)
SetCamera(0.0241594,0.0101337,-1.22266,0.0241594,0.0101337,0.0361362,1,0,0,0.50352,0.50352)

Print(8,1,0,1,100,1148,693,0 ,'C:/Users/msais/Box Sync/Thesis Work/Documentation/C7 3D CFD Analysis/config2_stallcomp_b2b'+str(b2b)+'_mf'+mf+'kgs.png' ,'',1,1,1)