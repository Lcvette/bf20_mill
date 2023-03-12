from qtpyvcp.widgets.qtdesigner import _DesignerPlugin

from bf20_mill_widgets.conversational.facing import FacingWidget
from bf20_mill_widgets.conversational.xy_coord import XYCoordWidget
from bf20_mill_widgets.conversational.hole_circle import HoleCircleWidget
from bf20_mill_widgets.conversational.int_line_edit import IntLineEdit
from bf20_mill_widgets.conversational.float_line_edit import FloatLineEdit



class FloatLineEditPlugin(_DesignerPlugin):
    def pluginClass(self):
        return FloatLineEdit


class IntLineEditPlugin(_DesignerPlugin):
    def pluginClass(self):
        return IntLineEdit


class HoleCircleWidgetPlugin(_DesignerPlugin):
    def pluginClass(self):
        return HoleCircleWidget


class XYCoordWidgetPlugin(_DesignerPlugin):
    def pluginClass(self):
        return XYCoordWidget


class FacingWidgetPlugin(_DesignerPlugin):
    def pluginClass(self):
        return FacingWidget
