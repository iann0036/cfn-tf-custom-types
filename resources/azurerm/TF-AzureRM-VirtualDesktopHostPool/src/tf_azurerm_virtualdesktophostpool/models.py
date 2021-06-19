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
    CustomRdpProperties: Optional[str]
    Description: Optional[str]
    FriendlyName: Optional[str]
    Id: Optional[str]
    LoadBalancerType: Optional[str]
    Location: Optional[str]
    MaximumSessionsAllowed: Optional[float]
    Name: Optional[str]
    PersonalDesktopAssignmentType: Optional[str]
    PreferredAppGroupType: Optional[str]
    ResourceGroupName: Optional[str]
    StartVmOnConnect: Optional[bool]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Type: Optional[str]
    ValidateEnvironment: Optional[bool]
    RegistrationInfo: Optional[Sequence["_RegistrationInfoDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            CustomRdpProperties=json_data.get("CustomRdpProperties"),
            Description=json_data.get("Description"),
            FriendlyName=json_data.get("FriendlyName"),
            Id=json_data.get("Id"),
            LoadBalancerType=json_data.get("LoadBalancerType"),
            Location=json_data.get("Location"),
            MaximumSessionsAllowed=json_data.get("MaximumSessionsAllowed"),
            Name=json_data.get("Name"),
            PersonalDesktopAssignmentType=json_data.get("PersonalDesktopAssignmentType"),
            PreferredAppGroupType=json_data.get("PreferredAppGroupType"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            StartVmOnConnect=json_data.get("StartVmOnConnect"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Type=json_data.get("Type"),
            ValidateEnvironment=json_data.get("ValidateEnvironment"),
            RegistrationInfo=deserialize_list(json_data.get("RegistrationInfo"), RegistrationInfoDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class RegistrationInfoDefinition(BaseModel):
    ExpirationDate: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RegistrationInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RegistrationInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            ExpirationDate=json_data.get("ExpirationDate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RegistrationInfoDefinition = RegistrationInfoDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


