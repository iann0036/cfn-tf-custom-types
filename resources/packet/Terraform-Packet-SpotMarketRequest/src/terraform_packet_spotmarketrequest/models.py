# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    DevicesMax: Optional[float]
    DevicesMin: Optional[float]
    Facilities: Optional[Sequence[str]]
    MaxBidPrice: Optional[float]
    ProjectId: Optional[str]
    WaitForDevices: Optional[bool]
    InstanceParameters: Optional[Sequence["_InstanceParameters"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DevicesMax=json_data.get("DevicesMax"),
            DevicesMin=json_data.get("DevicesMin"),
            Facilities=json_data.get("Facilities"),
            MaxBidPrice=json_data.get("MaxBidPrice"),
            ProjectId=json_data.get("ProjectId"),
            WaitForDevices=json_data.get("WaitForDevices"),
            InstanceParameters=json_data.get("InstanceParameters"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class InstanceParameters:
    AlwaysPxe: Optional[str]
    BillingCycle: Optional[str]
    Description: Optional[str]
    Features: Optional[Sequence[str]]
    Hostname: Optional[str]
    Locked: Optional[str]
    OperatingSystem: Optional[str]
    Plan: Optional[str]
    ProjectSshKeys: Optional[Sequence[str]]
    UserSshKeys: Optional[Sequence[str]]
    Userdata: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceParameters"]:
        if not json_data:
            return None
        return cls(
            AlwaysPxe=json_data.get("AlwaysPxe"),
            BillingCycle=json_data.get("BillingCycle"),
            Description=json_data.get("Description"),
            Features=json_data.get("Features"),
            Hostname=json_data.get("Hostname"),
            Locked=json_data.get("Locked"),
            OperatingSystem=json_data.get("OperatingSystem"),
            Plan=json_data.get("Plan"),
            ProjectSshKeys=json_data.get("ProjectSshKeys"),
            UserSshKeys=json_data.get("UserSshKeys"),
            Userdata=json_data.get("Userdata"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceParameters = InstanceParameters


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


