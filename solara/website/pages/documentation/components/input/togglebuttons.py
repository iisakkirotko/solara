"""
# ToggleButtons

ToggleButtons are in two flavours, for single, and for multiple selections.


"""

import solara
from solara.website.components import NoPage
from solara.website.utils import apidoc

title = "ToggleButtons"

Page = NoPage


__doc__ += "# ToggleButtonsSingle"
__doc__ += apidoc(solara.ToggleButtonsSingle.f)  # type: ignore
__doc__ += "# ToggleButtonsMultiple"
__doc__ += apidoc(solara.ToggleButtonsMultiple.f)  # type: ignore
