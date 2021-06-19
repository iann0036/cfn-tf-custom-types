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
    Cpu: Optional[float]
    Firewall: Optional[bool]
    Host: Optional[float]
    Hostname: Optional[str]
    Id: Optional[str]
    Mem: Optional[float]
    Metadata: Optional[bool]
    Plan: Optional[str]
    Tags: Optional[Sequence[str]]
    Title: Optional[str]
    UserData: Optional[str]
    Zone: Optional[str]
    Login: Optional[Sequence["_LoginDefinition"]]
    NetworkInterface: Optional[Sequence["_NetworkInterfaceDefinition"]]
    StorageDevices: Optional[Sequence["_StorageDevicesDefinition"]]
    Template: Optional[Sequence["_TemplateDefinition"]]

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
            Cpu=json_data.get("Cpu"),
            Firewall=json_data.get("Firewall"),
            Host=json_data.get("Host"),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            Mem=json_data.get("Mem"),
            Metadata=json_data.get("Metadata"),
            Plan=json_data.get("Plan"),
            Tags=json_data.get("Tags"),
            Title=json_data.get("Title"),
            UserData=json_data.get("UserData"),
            Zone=json_data.get("Zone"),
            Login=deserialize_list(json_data.get("Login"), LoginDefinition),
            NetworkInterface=deserialize_list(json_data.get("NetworkInterface"), NetworkInterfaceDefinition),
            StorageDevices=deserialize_list(json_data.get("StorageDevices"), StorageDevicesDefinition),
            Template=deserialize_list(json_data.get("Template"), TemplateDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LoginDefinition(BaseModel):
    CreatePassword: Optional[bool]
    Keys: Optional[Sequence[str]]
    PasswordDelivery: Optional[str]
    User: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoginDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoginDefinition"]:
        if not json_data:
            return None
        return cls(
            CreatePassword=json_data.get("CreatePassword"),
            Keys=json_data.get("Keys"),
            PasswordDelivery=json_data.get("PasswordDelivery"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoginDefinition = LoginDefinition


@dataclass
class NetworkInterfaceDefinition(BaseModel):
    Bootable: Optional[bool]
    IpAddress: Optional[str]
    IpAddressFamily: Optional[str]
    Network: Optional[str]
    SourceIpFiltering: Optional[bool]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkInterfaceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInterfaceDefinition"]:
        if not json_data:
            return None
        return cls(
            Bootable=json_data.get("Bootable"),
            IpAddress=json_data.get("IpAddress"),
            IpAddressFamily=json_data.get("IpAddressFamily"),
            Network=json_data.get("Network"),
            SourceIpFiltering=json_data.get("SourceIpFiltering"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkInterfaceDefinition = NetworkInterfaceDefinition


@dataclass
class StorageDevicesDefinition(BaseModel):
    Address: Optional[str]
    Storage: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StorageDevicesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageDevicesDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Storage=json_data.get("Storage"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageDevicesDefinition = StorageDevicesDefinition


@dataclass
class TemplateDefinition(BaseModel):
    Address: Optional[str]
    Size: Optional[float]
    Storage: Optional[str]
    Title: Optional[str]
    BackupRule: Optional[Sequence["_BackupRuleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TemplateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TemplateDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Size=json_data.get("Size"),
            Storage=json_data.get("Storage"),
            Title=json_data.get("Title"),
            BackupRule=deserialize_list(json_data.get("BackupRule"), BackupRuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TemplateDefinition = TemplateDefinition


@dataclass
class BackupRuleDefinition(BaseModel):
    Interval: Optional[str]
    Retention: Optional[float]
    Time: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BackupRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackupRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Interval=json_data.get("Interval"),
            Retention=json_data.get("Retention"),
            Time=json_data.get("Time"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackupRuleDefinition = BackupRuleDefinition


