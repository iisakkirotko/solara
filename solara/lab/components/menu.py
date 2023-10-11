from typing import Callable, Dict, List, Literal, Optional, Union, overload

import solara
from solara.components.component_vue import component_vue


@component_vue("menu.vue")
def MenuWidget(
    activator: List[solara.Element],
    show_menu: bool,
    on_show_menu: Optional[Callable] = None,
    children: List[solara.Element] = [],
    style: Optional[str] = None,
    context: bool = False,
    use_absolute: bool = True,
    close_on_content_click: bool = True,
):
    pass


@solara.component
def ClickMenu(
    activator: Union[solara.Element, List[solara.Element]],
    open: Union[solara.Reactive[bool], bool] = False,
    children: List[solara.Element] = [],
    style: Optional[Union[str, Dict[str, str]]] = None,
):
    """
    Show a pop-up menu by clicking on the `activator` element. The menu appears at the cursor position.

    ```solara
    import solara


    @solara.component
    def Page():
        image_url = "/static/public/beach.jpeg"
        image = solara.Image(image=image_url)

        with solara.lab.ClickMenu(activator=image):
            with solara.Column(gap="0px"):
                [solara.Button(f"Click me {i}!", text=True) for i in range(5)]

    ```


    ## Arguments

    * activator: Clicking on this element will open the menu. Accepts either a `solara.Element`, or a list of elements.
    * open: Controls and communicates the state of the menu. If True, the menu is open. If False, the menu is closed.
    * menu_contents: List of Elements to be contained in the menu.
    * style: CSS style to apply. Applied directly onto the `v-menu` component.
    """
    open = solara.use_reactive(open)
    style_flat = solara.util._flatten_style(style)

    if not isinstance(activator, list):
        activator = [activator]

    return MenuWidget(
        activator=activator,
        children=children,
        show_menu=open.value,
        on_show_menu=open.set,
        style=style_flat,
    )


@solara.component
def ContextMenu(
    activator: Union[solara.Element, List[solara.Element]],
    open: Union[solara.Reactive[bool], bool] = False,
    children: List[solara.Element] = [],
    style: Optional[Union[str, Dict[str, str]]] = None,
):
    """
    Show a context menu by triggering the contextmenu event on the `activator` element. The menu appears at the cursor position.

    A contextmenu event is typically triggered by clicking the right mouse button, or by pressing the context menu key.

    ```solara
    import solara


    @solara.component
    def Page():
        image_url = "/static/public/beach.jpeg"
        image = solara.Image(image=image_url)

        with solara.lab.ContextMenu(activator=image):
            with solara.Column(gap="0px"):
                [solara.Button(f"Click me {i}!", text=True) for i in range(5)]

    ```

    ## Arguments

    * activator: Clicking on this element will open the menu. Accepts either a `solara.Element`, or a list of elements.
    * open: Controls and communicates the state of the menu. If True, the menu is open. If False, the menu is closed.
    * children: List of Elements to be contained in the menu
    * style: CSS style to apply. Applied directly onto the `v-menu` component.
    """
    open = solara.use_reactive(open)
    style_flat = solara.util._flatten_style(style)

    if not isinstance(activator, list):
        activator = [activator]

    return MenuWidget(
        activator=activator,
        children=children,
        show_menu=open.value,
        on_show_menu=open.set,
        style=style_flat,
        context=True,
    )


@overload
def Menu(
    activator: Union[solara.Element, List[solara.Element]],
    close_on_content_click: Literal[True],
    open: Optional[Union[solara.Reactive[bool], bool]] = False,
    children: List[solara.Element] = [],
    style: Optional[Union[str, Dict[str, str]]] = None,
) -> solara.Element:
    ...


# If close_on_content_click is False, then the menu will be impossible to close.
# Thus when close_on_content_click is False, we require open to be reactive.
# This way the menu can be closed by setting open to False.
@overload
def Menu(
    activator: Union[solara.Element, List[solara.Element]],
    open: solara.Reactive[bool],
    close_on_content_click: Literal[False],
    children: List[solara.Element] = [],
    style: Optional[Union[str, Dict[str, str]]] = None,
) -> solara.Element:
    ...


@solara.component
def Menu(
    activator: Union[solara.Element, List[solara.Element]],
    open: Union[solara.Reactive[bool], bool] = False,
    close_on_content_click: bool = True,
    children: List[solara.Element] = [],
    style: Optional[Union[str, Dict[str, str]]] = None,
):
    """
    Show a pop-up menu by clicking on the `activator` element. The menu appears below the `activator` element.

    ```solara
    import solara


    @solara.component
    def Page():
        btn = solara.Button("Show suboptions")

        with solara.lab.Menu(activator=btn):
            with solara.Column(gap="0px"):
                [solara.Button(f"Click me {str(i)}!", text=True) for i in range(5)]

    ```

    ## Arguments

    * activator: Clicking on this element will open the menu. Accepts either a `solara.Element`, or a list of elements.
    * open: Controls and communicates the state of the menu. If True, the menu is open. If False, the menu is closed.
    * children: List of Elements to be contained in the menu
    * style: CSS style to apply. Applied directly onto the `v-menu` component.
    * close_on_content_click: If True, clicking on the menu contents will close the menu. If False, the menu will stay open.
    """
    open = solara.use_reactive(open)

    style_flat = solara.util._flatten_style(style)

    if not isinstance(activator, list):
        activator = [activator]

    return MenuWidget(
        activator=activator,
        children=children,
        show_menu=open.value,
        on_show_menu=open.set,
        style=style_flat,
        use_absolute=False,
        close_on_content_click=close_on_content_click,
    )
