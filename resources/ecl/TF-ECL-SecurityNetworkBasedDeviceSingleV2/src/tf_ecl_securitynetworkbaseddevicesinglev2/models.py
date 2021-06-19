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
    AzGroup: Optional[str]
    Id: Optional[str]
    LicenseKind: Optional[str]
    Locale: Optional[str]
    OperatingMode: Optional[str]
    TenantId: Optional[str]
    Port: Optional[Sequence["_PortDefinition"]]
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
            AzGroup=json_data.get("AzGroup"),
            Id=json_data.get("Id"),
            LicenseKind=json_data.get("LicenseKind"),
            Locale=json_data.get("Locale"),
            OperatingMode=json_data.get("OperatingMode"),
            TenantId=json_data.get("TenantId"),
            Port=deserialize_list(json_data.get("Port"), PortDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PortDefinition(BaseModel):
    Comment: Optional[str]
    Enable: Optional[str]
    IpAddress: Optional[str]
    IpAddressPrefix: Optional[float]
    Mtu: Optional[str]
    NetworkId: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PortDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortDefinition"]:
        if not json_data:
            return None
        return cls(
            Comment=json_data.get("Comment"),
            Enable=json_data.get("Enable"),
            IpAddress=json_data.get("IpAddress"),
            IpAddressPrefix=json_data.get("IpAddressPrefix"),
            Mtu=json_data.get("Mtu"),
            NetworkId=json_data.get("NetworkId"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortDefinition = PortDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


