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
    AdditionalTags: Optional[Sequence["_AdditionalTagsDefinition"]]
    ExternalId: Optional[str]
    ForceSave: Optional[bool]
    HostnameTags: Optional[Sequence[str]]
    Id: Optional[str]
    Name: Optional[str]
    RoleArn: Optional[str]
    Service: Optional[str]
    ServiceRefreshRateInMinutes: Optional[float]

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
            AdditionalTags=deserialize_list(json_data.get("AdditionalTags"), AdditionalTagsDefinition),
            ExternalId=json_data.get("ExternalId"),
            ForceSave=json_data.get("ForceSave"),
            HostnameTags=json_data.get("HostnameTags"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            RoleArn=json_data.get("RoleArn"),
            Service=json_data.get("Service"),
            ServiceRefreshRateInMinutes=json_data.get("ServiceRefreshRateInMinutes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AdditionalTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdditionalTagsDefinition = AdditionalTagsDefinition

