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
    DevicesMax: Optional[float]
    DevicesMin: Optional[float]
    Facilities: Optional[Sequence[str]]
    Id: Optional[str]
    MaxBidPrice: Optional[float]
    ProjectId: Optional[str]
    WaitForDevices: Optional[bool]
    InstanceParameters: Optional[Sequence["_InstanceParametersDefinition"]]
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
            DevicesMax=json_data.get("DevicesMax"),
            DevicesMin=json_data.get("DevicesMin"),
            Facilities=json_data.get("Facilities"),
            Id=json_data.get("Id"),
            MaxBidPrice=json_data.get("MaxBidPrice"),
            ProjectId=json_data.get("ProjectId"),
            WaitForDevices=json_data.get("WaitForDevices"),
            InstanceParameters=deserialize_list(json_data.get("InstanceParameters"), InstanceParametersDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class InstanceParametersDefinition(BaseModel):
    AlwaysPxe: Optional[bool]
    BillingCycle: Optional[str]
    Customdata: Optional[str]
    Description: Optional[str]
    Features: Optional[Sequence[str]]
    Hostname: Optional[str]
    IpxeScriptUrl: Optional[str]
    Locked: Optional[str]
    OperatingSystem: Optional[str]
    Plan: Optional[str]
    ProjectSshKeys: Optional[Sequence[str]]
    Tags: Optional[Sequence[str]]
    UserSshKeys: Optional[Sequence[str]]
    Userdata: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            AlwaysPxe=json_data.get("AlwaysPxe"),
            BillingCycle=json_data.get("BillingCycle"),
            Customdata=json_data.get("Customdata"),
            Description=json_data.get("Description"),
            Features=json_data.get("Features"),
            Hostname=json_data.get("Hostname"),
            IpxeScriptUrl=json_data.get("IpxeScriptUrl"),
            Locked=json_data.get("Locked"),
            OperatingSystem=json_data.get("OperatingSystem"),
            Plan=json_data.get("Plan"),
            ProjectSshKeys=json_data.get("ProjectSshKeys"),
            Tags=json_data.get("Tags"),
            UserSshKeys=json_data.get("UserSshKeys"),
            Userdata=json_data.get("Userdata"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceParametersDefinition = InstanceParametersDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


