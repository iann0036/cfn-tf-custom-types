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
    AccountNumber: Optional[str]
    AclTemplateId: Optional[str]
    AdditionalBandwidth: Optional[float]
    Asn: Optional[float]
    Byol: Optional[bool]
    CoreCount: Optional[float]
    Hostname: Optional[str]
    Ibx: Optional[str]
    Id: Optional[str]
    Interface: Optional[Sequence["_InterfaceDefinition"]]
    InterfaceCount: Optional[float]
    LicenseFile: Optional[str]
    LicenseFileId: Optional[str]
    LicenseStatus: Optional[str]
    LicenseToken: Optional[str]
    MetroCode: Optional[str]
    Name: Optional[str]
    Notifications: Optional[Sequence[str]]
    OrderReference: Optional[str]
    PackageCode: Optional[str]
    PurchaseOrderNumber: Optional[str]
    RedundancyType: Optional[str]
    RedundantId: Optional[str]
    Region: Optional[str]
    SelfManaged: Optional[bool]
    SshIpAddress: Optional[str]
    SshIpFqdn: Optional[str]
    Status: Optional[str]
    TermLength: Optional[float]
    Throughput: Optional[float]
    ThroughputUnit: Optional[str]
    TypeCode: Optional[str]
    Uuid: Optional[str]
    VendorConfiguration: Optional[Sequence["_VendorConfigurationDefinition"]]
    Version: Optional[str]
    ZoneCode: Optional[str]
    SecondaryDevice: Optional[Sequence["_SecondaryDeviceDefinition"]]
    SshKey: Optional[Sequence["_SshKeyDefinition"]]
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
            AccountNumber=json_data.get("AccountNumber"),
            AclTemplateId=json_data.get("AclTemplateId"),
            AdditionalBandwidth=json_data.get("AdditionalBandwidth"),
            Asn=json_data.get("Asn"),
            Byol=json_data.get("Byol"),
            CoreCount=json_data.get("CoreCount"),
            Hostname=json_data.get("Hostname"),
            Ibx=json_data.get("Ibx"),
            Id=json_data.get("Id"),
            Interface=deserialize_list(json_data.get("Interface"), InterfaceDefinition),
            InterfaceCount=json_data.get("InterfaceCount"),
            LicenseFile=json_data.get("LicenseFile"),
            LicenseFileId=json_data.get("LicenseFileId"),
            LicenseStatus=json_data.get("LicenseStatus"),
            LicenseToken=json_data.get("LicenseToken"),
            MetroCode=json_data.get("MetroCode"),
            Name=json_data.get("Name"),
            Notifications=json_data.get("Notifications"),
            OrderReference=json_data.get("OrderReference"),
            PackageCode=json_data.get("PackageCode"),
            PurchaseOrderNumber=json_data.get("PurchaseOrderNumber"),
            RedundancyType=json_data.get("RedundancyType"),
            RedundantId=json_data.get("RedundantId"),
            Region=json_data.get("Region"),
            SelfManaged=json_data.get("SelfManaged"),
            SshIpAddress=json_data.get("SshIpAddress"),
            SshIpFqdn=json_data.get("SshIpFqdn"),
            Status=json_data.get("Status"),
            TermLength=json_data.get("TermLength"),
            Throughput=json_data.get("Throughput"),
            ThroughputUnit=json_data.get("ThroughputUnit"),
            TypeCode=json_data.get("TypeCode"),
            Uuid=json_data.get("Uuid"),
            VendorConfiguration=deserialize_list(json_data.get("VendorConfiguration"), VendorConfigurationDefinition),
            Version=json_data.get("Version"),
            ZoneCode=json_data.get("ZoneCode"),
            SecondaryDevice=deserialize_list(json_data.get("SecondaryDevice"), SecondaryDeviceDefinition),
            SshKey=deserialize_list(json_data.get("SshKey"), SshKeyDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class InterfaceDefinition(BaseModel):
    AssignedType: Optional[str]
    Id: Optional[float]
    IpAddress: Optional[str]
    MacAddress: Optional[str]
    Name: Optional[str]
    OperationalStatus: Optional[str]
    Status: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InterfaceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InterfaceDefinition"]:
        if not json_data:
            return None
        return cls(
            AssignedType=json_data.get("AssignedType"),
            Id=json_data.get("Id"),
            IpAddress=json_data.get("IpAddress"),
            MacAddress=json_data.get("MacAddress"),
            Name=json_data.get("Name"),
            OperationalStatus=json_data.get("OperationalStatus"),
            Status=json_data.get("Status"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InterfaceDefinition = InterfaceDefinition


@dataclass
class VendorConfigurationDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VendorConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VendorConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VendorConfigurationDefinition = VendorConfigurationDefinition


@dataclass
class SecondaryDeviceDefinition(BaseModel):
    AccountNumber: Optional[str]
    AclTemplateId: Optional[str]
    AdditionalBandwidth: Optional[float]
    Hostname: Optional[str]
    LicenseFile: Optional[str]
    LicenseToken: Optional[str]
    MetroCode: Optional[str]
    Name: Optional[str]
    Notifications: Optional[Sequence[str]]
    VendorConfiguration: Optional[Sequence["_VendorConfigurationDefinition2"]]
    SshKey: Optional[Sequence["_SshKeyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SecondaryDeviceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecondaryDeviceDefinition"]:
        if not json_data:
            return None
        return cls(
            AccountNumber=json_data.get("AccountNumber"),
            AclTemplateId=json_data.get("AclTemplateId"),
            AdditionalBandwidth=json_data.get("AdditionalBandwidth"),
            Hostname=json_data.get("Hostname"),
            LicenseFile=json_data.get("LicenseFile"),
            LicenseToken=json_data.get("LicenseToken"),
            MetroCode=json_data.get("MetroCode"),
            Name=json_data.get("Name"),
            Notifications=json_data.get("Notifications"),
            VendorConfiguration=deserialize_list(json_data.get("VendorConfiguration"), VendorConfigurationDefinition2),
            SshKey=deserialize_list(json_data.get("SshKey"), SshKeyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecondaryDeviceDefinition = SecondaryDeviceDefinition


@dataclass
class VendorConfigurationDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VendorConfigurationDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VendorConfigurationDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VendorConfigurationDefinition2 = VendorConfigurationDefinition2


@dataclass
class SshKeyDefinition(BaseModel):
    KeyName: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SshKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SshKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            KeyName=json_data.get("KeyName"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SshKeyDefinition = SshKeyDefinition


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


