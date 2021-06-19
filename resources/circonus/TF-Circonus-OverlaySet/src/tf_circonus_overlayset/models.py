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
    GraphCid: Optional[str]
    Id: Optional[str]
    Title: Optional[str]
    Overlays: Optional[Sequence["_OverlaysDefinition"]]

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
            GraphCid=json_data.get("GraphCid"),
            Id=json_data.get("Id"),
            Title=json_data.get("Title"),
            Overlays=deserialize_list(json_data.get("Overlays"), OverlaysDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class OverlaysDefinition(BaseModel):
    Id: Optional[str]
    DataOpts: Optional[Sequence["_DataOptsDefinition"]]
    UiSpecs: Optional[Sequence["_UiSpecsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OverlaysDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OverlaysDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            DataOpts=deserialize_list(json_data.get("DataOpts"), DataOptsDefinition),
            UiSpecs=deserialize_list(json_data.get("UiSpecs"), UiSpecsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OverlaysDefinition = OverlaysDefinition


@dataclass
class DataOptsDefinition(BaseModel):
    GraphTitle: Optional[str]
    GraphUuid: Optional[str]
    XShift: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataOptsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataOptsDefinition"]:
        if not json_data:
            return None
        return cls(
            GraphTitle=json_data.get("GraphTitle"),
            GraphUuid=json_data.get("GraphUuid"),
            XShift=json_data.get("XShift"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataOptsDefinition = DataOptsDefinition


@dataclass
class UiSpecsDefinition(BaseModel):
    Decouple: Optional[bool]
    Id: Optional[str]
    Label: Optional[str]
    Type: Optional[str]
    Z: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UiSpecsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UiSpecsDefinition"]:
        if not json_data:
            return None
        return cls(
            Decouple=json_data.get("Decouple"),
            Id=json_data.get("Id"),
            Label=json_data.get("Label"),
            Type=json_data.get("Type"),
            Z=json_data.get("Z"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UiSpecsDefinition = UiSpecsDefinition


