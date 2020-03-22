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
    AdministratorPw: Optional[str]
    Affinity: Optional[Sequence[str]]
    CloudConfig: Optional[str]
    ComputeNode: Optional[str]
    Created: Optional[str]
    Dataset: Optional[str]
    DeletionProtectionEnabled: Optional[bool]
    Disk: Optional[float]
    DomainNames: Optional[Sequence[str]]
    FirewallEnabled: Optional[bool]
    Id: Optional[str]
    Image: Optional[str]
    Ips: Optional[Sequence[str]]
    Memory: Optional[float]
    Metadata: Optional[Sequence["_Metadata"]]
    Name: Optional[str]
    Networks: Optional[Sequence[str]]
    Package: Optional[str]
    Primaryip: Optional[str]
    RootAuthorizedKeys: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Type: Optional[str]
    Updated: Optional[str]
    UserData: Optional[str]
    UserScript: Optional[str]
    Cns: Optional[Sequence["_Cns"]]
    Locality: Optional[Sequence["_Locality"]]
    Nic: Optional[Sequence["_Nic"]]
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
            AdministratorPw=json_data.get("AdministratorPw"),
            Affinity=json_data.get("Affinity"),
            CloudConfig=json_data.get("CloudConfig"),
            ComputeNode=json_data.get("ComputeNode"),
            Created=json_data.get("Created"),
            Dataset=json_data.get("Dataset"),
            DeletionProtectionEnabled=json_data.get("DeletionProtectionEnabled"),
            Disk=json_data.get("Disk"),
            DomainNames=json_data.get("DomainNames"),
            FirewallEnabled=json_data.get("FirewallEnabled"),
            Id=json_data.get("Id"),
            Image=json_data.get("Image"),
            Ips=json_data.get("Ips"),
            Memory=json_data.get("Memory"),
            Metadata=json_data.get("Metadata"),
            Name=json_data.get("Name"),
            Networks=json_data.get("Networks"),
            Package=json_data.get("Package"),
            Primaryip=json_data.get("Primaryip"),
            RootAuthorizedKeys=json_data.get("RootAuthorizedKeys"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
            Updated=json_data.get("Updated"),
            UserData=json_data.get("UserData"),
            UserScript=json_data.get("UserScript"),
            Cns=json_data.get("Cns"),
            Locality=json_data.get("Locality"),
            Nic=json_data.get("Nic"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Metadata:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Metadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metadata"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metadata = Metadata


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class Cns:
    Disable: Optional[bool]
    Services: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Cns"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Cns"]:
        if not json_data:
            return None
        return cls(
            Disable=json_data.get("Disable"),
            Services=json_data.get("Services"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Cns = Cns


@dataclass
class Locality:
    CloseTo: Optional[Sequence[str]]
    FarFrom: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Locality"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Locality"]:
        if not json_data:
            return None
        return cls(
            CloseTo=json_data.get("CloseTo"),
            FarFrom=json_data.get("FarFrom"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Locality = Locality


@dataclass
class Nic:
    Network: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Nic"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Nic"]:
        if not json_data:
            return None
        return cls(
            Network=json_data.get("Network"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Nic = Nic


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


