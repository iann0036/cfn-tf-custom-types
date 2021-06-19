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
    ClientNodeAmount: Optional[float]
    ClientNodeSpec: Optional[str]
    DataNodeAmount: Optional[float]
    DataNodeDiskEncrypted: Optional[bool]
    DataNodeDiskSize: Optional[float]
    DataNodeDiskType: Optional[str]
    DataNodeSpec: Optional[str]
    Description: Optional[str]
    Domain: Optional[str]
    EnableKibanaPrivateNetwork: Optional[bool]
    EnableKibanaPublicNetwork: Optional[bool]
    EnablePublic: Optional[bool]
    Id: Optional[str]
    InstanceChargeType: Optional[str]
    KibanaDomain: Optional[str]
    KibanaPort: Optional[float]
    KibanaPrivateWhitelist: Optional[Sequence[str]]
    KibanaWhitelist: Optional[Sequence[str]]
    KmsEncryptedPassword: Optional[str]
    KmsEncryptionContext: Optional[Sequence["_KmsEncryptionContextDefinition"]]
    MasterNodeSpec: Optional[str]
    Password: Optional[str]
    Period: Optional[float]
    Port: Optional[float]
    PrivateWhitelist: Optional[Sequence[str]]
    Protocol: Optional[str]
    PublicWhitelist: Optional[Sequence[str]]
    ResourceGroupId: Optional[str]
    Status: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Version: Optional[str]
    VswitchId: Optional[str]
    ZoneCount: Optional[float]
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
            ClientNodeAmount=json_data.get("ClientNodeAmount"),
            ClientNodeSpec=json_data.get("ClientNodeSpec"),
            DataNodeAmount=json_data.get("DataNodeAmount"),
            DataNodeDiskEncrypted=json_data.get("DataNodeDiskEncrypted"),
            DataNodeDiskSize=json_data.get("DataNodeDiskSize"),
            DataNodeDiskType=json_data.get("DataNodeDiskType"),
            DataNodeSpec=json_data.get("DataNodeSpec"),
            Description=json_data.get("Description"),
            Domain=json_data.get("Domain"),
            EnableKibanaPrivateNetwork=json_data.get("EnableKibanaPrivateNetwork"),
            EnableKibanaPublicNetwork=json_data.get("EnableKibanaPublicNetwork"),
            EnablePublic=json_data.get("EnablePublic"),
            Id=json_data.get("Id"),
            InstanceChargeType=json_data.get("InstanceChargeType"),
            KibanaDomain=json_data.get("KibanaDomain"),
            KibanaPort=json_data.get("KibanaPort"),
            KibanaPrivateWhitelist=json_data.get("KibanaPrivateWhitelist"),
            KibanaWhitelist=json_data.get("KibanaWhitelist"),
            KmsEncryptedPassword=json_data.get("KmsEncryptedPassword"),
            KmsEncryptionContext=deserialize_list(json_data.get("KmsEncryptionContext"), KmsEncryptionContextDefinition),
            MasterNodeSpec=json_data.get("MasterNodeSpec"),
            Password=json_data.get("Password"),
            Period=json_data.get("Period"),
            Port=json_data.get("Port"),
            PrivateWhitelist=json_data.get("PrivateWhitelist"),
            Protocol=json_data.get("Protocol"),
            PublicWhitelist=json_data.get("PublicWhitelist"),
            ResourceGroupId=json_data.get("ResourceGroupId"),
            Status=json_data.get("Status"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Version=json_data.get("Version"),
            VswitchId=json_data.get("VswitchId"),
            ZoneCount=json_data.get("ZoneCount"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class KmsEncryptionContextDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KmsEncryptionContextDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KmsEncryptionContextDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KmsEncryptionContextDefinition = KmsEncryptionContextDefinition


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


