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
    Host1AzGroup: Optional[str]
    Host2AzGroup: Optional[str]
    Id: Optional[str]
    LicenseKind: Optional[str]
    Locale: Optional[str]
    OperatingMode: Optional[str]
    TenantId: Optional[str]
    HaLink1: Optional[Sequence["_HaLink1Definition"]]
    HaLink2: Optional[Sequence["_HaLink2Definition"]]
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
            Host1AzGroup=json_data.get("Host1AzGroup"),
            Host2AzGroup=json_data.get("Host2AzGroup"),
            Id=json_data.get("Id"),
            LicenseKind=json_data.get("LicenseKind"),
            Locale=json_data.get("Locale"),
            OperatingMode=json_data.get("OperatingMode"),
            TenantId=json_data.get("TenantId"),
            HaLink1=deserialize_list(json_data.get("HaLink1"), HaLink1Definition),
            HaLink2=deserialize_list(json_data.get("HaLink2"), HaLink2Definition),
            Port=deserialize_list(json_data.get("Port"), PortDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class HaLink1Definition(BaseModel):
    Host1IpAddress: Optional[str]
    Host2IpAddress: Optional[str]
    NetworkId: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HaLink1Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HaLink1Definition"]:
        if not json_data:
            return None
        return cls(
            Host1IpAddress=json_data.get("Host1IpAddress"),
            Host2IpAddress=json_data.get("Host2IpAddress"),
            NetworkId=json_data.get("NetworkId"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HaLink1Definition = HaLink1Definition


@dataclass
class HaLink2Definition(BaseModel):
    Host1IpAddress: Optional[str]
    Host2IpAddress: Optional[str]
    NetworkId: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HaLink2Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HaLink2Definition"]:
        if not json_data:
            return None
        return cls(
            Host1IpAddress=json_data.get("Host1IpAddress"),
            Host2IpAddress=json_data.get("Host2IpAddress"),
            NetworkId=json_data.get("NetworkId"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HaLink2Definition = HaLink2Definition


@dataclass
class PortDefinition(BaseModel):
    Comment: Optional[str]
    Enable: Optional[str]
    EnablePing: Optional[str]
    Host1IpAddress: Optional[str]
    Host1IpAddressPrefix: Optional[float]
    Host2IpAddress: Optional[str]
    Host2IpAddressPrefix: Optional[float]
    Mtu: Optional[str]
    NetworkId: Optional[str]
    Preempt: Optional[str]
    SubnetId: Optional[str]
    VrrpGrpId: Optional[str]
    VrrpId: Optional[str]
    VrrpIpAddress: Optional[str]

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
            EnablePing=json_data.get("EnablePing"),
            Host1IpAddress=json_data.get("Host1IpAddress"),
            Host1IpAddressPrefix=json_data.get("Host1IpAddressPrefix"),
            Host2IpAddress=json_data.get("Host2IpAddress"),
            Host2IpAddressPrefix=json_data.get("Host2IpAddressPrefix"),
            Mtu=json_data.get("Mtu"),
            NetworkId=json_data.get("NetworkId"),
            Preempt=json_data.get("Preempt"),
            SubnetId=json_data.get("SubnetId"),
            VrrpGrpId=json_data.get("VrrpGrpId"),
            VrrpId=json_data.get("VrrpId"),
            VrrpIpAddress=json_data.get("VrrpIpAddress"),
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


