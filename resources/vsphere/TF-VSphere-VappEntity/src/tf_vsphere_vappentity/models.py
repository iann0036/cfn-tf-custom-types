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
    ContainerId: Optional[str]
    CustomAttributes: Optional[Sequence["_CustomAttributesDefinition"]]
    Id: Optional[str]
    StartAction: Optional[str]
    StartDelay: Optional[float]
    StartOrder: Optional[float]
    StopAction: Optional[str]
    StopDelay: Optional[float]
    Tags: Optional[Sequence[str]]
    TargetId: Optional[str]
    WaitForGuest: Optional[bool]

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
            ContainerId=json_data.get("ContainerId"),
            CustomAttributes=deserialize_list(json_data.get("CustomAttributes"), CustomAttributesDefinition),
            Id=json_data.get("Id"),
            StartAction=json_data.get("StartAction"),
            StartDelay=json_data.get("StartDelay"),
            StartOrder=json_data.get("StartOrder"),
            StopAction=json_data.get("StopAction"),
            StopDelay=json_data.get("StopDelay"),
            Tags=json_data.get("Tags"),
            TargetId=json_data.get("TargetId"),
            WaitForGuest=json_data.get("WaitForGuest"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CustomAttributesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomAttributesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomAttributesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomAttributesDefinition = CustomAttributesDefinition


