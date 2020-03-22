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
    AccountName: Optional[str]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    PoolName: Optional[str]
    Protocols: Optional[Sequence[str]]
    ResourceGroupName: Optional[str]
    ServiceLevel: Optional[str]
    StorageQuotaInGb: Optional[float]
    SubnetId: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    VolumePath: Optional[str]
    ExportPolicyRule: Optional[Sequence["_ExportPolicyRule"]]
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
            AccountName=json_data.get("AccountName"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            PoolName=json_data.get("PoolName"),
            Protocols=json_data.get("Protocols"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            ServiceLevel=json_data.get("ServiceLevel"),
            StorageQuotaInGb=json_data.get("StorageQuotaInGb"),
            SubnetId=json_data.get("SubnetId"),
            Tags=json_data.get("Tags"),
            VolumePath=json_data.get("VolumePath"),
            ExportPolicyRule=json_data.get("ExportPolicyRule"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class ExportPolicyRule:
    AllowedClients: Optional[Sequence[str]]
    CifsEnabled: Optional[bool]
    Nfsv3Enabled: Optional[bool]
    Nfsv4Enabled: Optional[bool]
    ProtocolsEnabled: Optional[Sequence[str]]
    RuleIndex: Optional[float]
    UnixReadOnly: Optional[bool]
    UnixReadWrite: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ExportPolicyRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExportPolicyRule"]:
        if not json_data:
            return None
        return cls(
            AllowedClients=json_data.get("AllowedClients"),
            CifsEnabled=json_data.get("CifsEnabled"),
            Nfsv3Enabled=json_data.get("Nfsv3Enabled"),
            Nfsv4Enabled=json_data.get("Nfsv4Enabled"),
            ProtocolsEnabled=json_data.get("ProtocolsEnabled"),
            RuleIndex=json_data.get("RuleIndex"),
            UnixReadOnly=json_data.get("UnixReadOnly"),
            UnixReadWrite=json_data.get("UnixReadWrite"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExportPolicyRule = ExportPolicyRule


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


