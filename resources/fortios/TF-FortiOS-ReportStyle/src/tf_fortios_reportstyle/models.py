# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

from cloudformation_cli_python_lib.interface import (
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class ResourceHandlerRequest(BaseResourceHandlerRequest):
    # pylint: disable=invalid-name
    desiredResourceState: Optional["ResourceModel"]
    previousResourceState: Optional["ResourceModel"]


@dataclass
class ResourceModel(BaseModel):
    tfcfnid: Optional[str]
    Align: Optional[str]
    BgColor: Optional[str]
    BorderBottom: Optional[str]
    BorderLeft: Optional[str]
    BorderRight: Optional[str]
    BorderTop: Optional[str]
    ColumnGap: Optional[str]
    ColumnSpan: Optional[str]
    FgColor: Optional[str]
    FontFamily: Optional[str]
    FontSize: Optional[str]
    FontStyle: Optional[str]
    FontWeight: Optional[str]
    Height: Optional[str]
    Id: Optional[str]
    LineHeight: Optional[str]
    MarginBottom: Optional[str]
    MarginLeft: Optional[str]
    MarginRight: Optional[str]
    MarginTop: Optional[str]
    Name: Optional[str]
    Options: Optional[str]
    PaddingBottom: Optional[str]
    PaddingLeft: Optional[str]
    PaddingRight: Optional[str]
    PaddingTop: Optional[str]
    Vdomparam: Optional[str]
    Width: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Align=json_data.get("Align"),
            BgColor=json_data.get("BgColor"),
            BorderBottom=json_data.get("BorderBottom"),
            BorderLeft=json_data.get("BorderLeft"),
            BorderRight=json_data.get("BorderRight"),
            BorderTop=json_data.get("BorderTop"),
            ColumnGap=json_data.get("ColumnGap"),
            ColumnSpan=json_data.get("ColumnSpan"),
            FgColor=json_data.get("FgColor"),
            FontFamily=json_data.get("FontFamily"),
            FontSize=json_data.get("FontSize"),
            FontStyle=json_data.get("FontStyle"),
            FontWeight=json_data.get("FontWeight"),
            Height=json_data.get("Height"),
            Id=json_data.get("Id"),
            LineHeight=json_data.get("LineHeight"),
            MarginBottom=json_data.get("MarginBottom"),
            MarginLeft=json_data.get("MarginLeft"),
            MarginRight=json_data.get("MarginRight"),
            MarginTop=json_data.get("MarginTop"),
            Name=json_data.get("Name"),
            Options=json_data.get("Options"),
            PaddingBottom=json_data.get("PaddingBottom"),
            PaddingLeft=json_data.get("PaddingLeft"),
            PaddingRight=json_data.get("PaddingRight"),
            PaddingTop=json_data.get("PaddingTop"),
            Vdomparam=json_data.get("Vdomparam"),
            Width=json_data.get("Width"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


