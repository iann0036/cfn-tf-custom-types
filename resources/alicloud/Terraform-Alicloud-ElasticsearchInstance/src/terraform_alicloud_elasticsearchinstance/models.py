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
    DataNodeAmount: Optional[float]
    DataNodeDiskSize: Optional[float]
    DataNodeDiskType: Optional[str]
    DataNodeSpec: Optional[str]
    Description: Optional[str]
    Domain: Optional[str]
    Id: Optional[str]
    InstanceChargeType: Optional[str]
    KibanaDomain: Optional[str]
    KibanaPort: Optional[float]
    KibanaWhitelist: Optional[Sequence[str]]
    KmsEncryptedPassword: Optional[str]
    KmsEncryptionContext: Optional[Sequence["_KmsEncryptionContext"]]
    MasterNodeSpec: Optional[str]
    Password: Optional[str]
    Period: Optional[float]
    Port: Optional[float]
    PrivateWhitelist: Optional[Sequence[str]]
    PublicWhitelist: Optional[Sequence[str]]
    Status: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Version: Optional[str]
    VswitchId: Optional[str]
    ZoneCount: Optional[float]
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
            DataNodeAmount=json_data.get("DataNodeAmount"),
            DataNodeDiskSize=json_data.get("DataNodeDiskSize"),
            DataNodeDiskType=json_data.get("DataNodeDiskType"),
            DataNodeSpec=json_data.get("DataNodeSpec"),
            Description=json_data.get("Description"),
            Domain=json_data.get("Domain"),
            Id=json_data.get("Id"),
            InstanceChargeType=json_data.get("InstanceChargeType"),
            KibanaDomain=json_data.get("KibanaDomain"),
            KibanaPort=json_data.get("KibanaPort"),
            KibanaWhitelist=json_data.get("KibanaWhitelist"),
            KmsEncryptedPassword=json_data.get("KmsEncryptedPassword"),
            KmsEncryptionContext=json_data.get("KmsEncryptionContext"),
            MasterNodeSpec=json_data.get("MasterNodeSpec"),
            Password=json_data.get("Password"),
            Period=json_data.get("Period"),
            Port=json_data.get("Port"),
            PrivateWhitelist=json_data.get("PrivateWhitelist"),
            PublicWhitelist=json_data.get("PublicWhitelist"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
            Version=json_data.get("Version"),
            VswitchId=json_data.get("VswitchId"),
            ZoneCount=json_data.get("ZoneCount"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class KmsEncryptionContext:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KmsEncryptionContext"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KmsEncryptionContext"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KmsEncryptionContext = KmsEncryptionContext


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
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


