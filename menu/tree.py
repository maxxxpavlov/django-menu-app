from menu.models import MenuTree


def filterByParent(elements, parent):
    return list(filter(lambda x: x["parent"] == parent, elements))


def infiltrate(root: list, elements):
    if len(root) == 0:
        return []
    rootCopy = root.copy()
    for element in rootCopy:
        element['children'] = infiltrate(
            filterByParent(elements, element['id']), elements)
    return rootCopy


def setShownFlagTrue(elements):
    for element in elements:
        element['shown'] = True
    return elements


def inflitrateShownFlag(elements: list, selectedElementId: int, had=False):
    hasSelectedElementInRoot = False
    for element in elements:
        if element['id'] == selectedElementId:
            hasSelectedElementInRoot = True
            element['selected'] = True
            setShownFlagTrue(elements)
            setShownFlagTrue(element["children"])
        else:
            _, hasNow = inflitrateShownFlag(
                element['children'], selectedElementId)
            if had or hasNow:
                setShownFlagTrue(elements)
                had = True
    return elements, hasSelectedElementInRoot or had


def getMenuTree(menuName: str, selectedElementId=None):
    elements = MenuTree.objects.filter(menuName=menuName).values()
    root = filterByParent(elements, None)
    for element in root:
        element["shown"] = True  # all root element are always shown
    infiltratedTree = infiltrate(root, elements)
    if selectedElementId is not None:
        infiltratedTree, _ = inflitrateShownFlag(
            infiltratedTree, selectedElementId)
    return infiltratedTree
