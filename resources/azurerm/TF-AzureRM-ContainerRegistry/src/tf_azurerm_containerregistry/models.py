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
    AdminEnabled: Optional[bool]
    AdminPassword: Optional[str]
    AdminUsername: Optional[str]
    Encryption: Optional[Sequence["_EncryptionDefinition"]]
    GeoreplicationLocations: Optional[Sequence[str]]
    Georeplications: Optional[Sequence["_GeoreplicationsDefinition2"]]
    Id: Optional[str]
    Location: Optional[str]
    LoginServer: Optional[str]
    Name: Optional[str]
    NetworkRuleSet: Optional[Sequence["_NetworkRuleSetDefinition3"]]
    PublicNetworkAccessEnabled: Optional[bool]
    QuarantinePolicyEnabled: Optional[bool]
    ResourceGroupName: Optional[str]
    RetentionPolicy: Optional[Sequence["_RetentionPolicyDefinition"]]
    Sku: Optional[str]
    StorageAccountId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TrustPolicy: Optional[Sequence["_TrustPolicyDefinition"]]
    ZoneRedundancyEnabled: Optional[bool]
    Identity: Optional[Sequence["_IdentityDefinition"]]
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
            AdminEnabled=json_data.get("AdminEnabled"),
            AdminPassword=json_data.get("AdminPassword"),
            AdminUsername=json_data.get("AdminUsername"),
            Encryption=deserialize_list(json_data.get("Encryption"), EncryptionDefinition),
            GeoreplicationLocations=json_data.get("GeoreplicationLocations"),
            Georeplications=deserialize_list(json_data.get("Georeplications"), GeoreplicationsDefinition2),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            LoginServer=json_data.get("LoginServer"),
            Name=json_data.get("Name"),
            NetworkRuleSet=deserialize_list(json_data.get("NetworkRuleSet"), NetworkRuleSetDefinition3),
            PublicNetworkAccessEnabled=json_data.get("PublicNetworkAccessEnabled"),
            QuarantinePolicyEnabled=json_data.get("QuarantinePolicyEnabled"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            RetentionPolicy=deserialize_list(json_data.get("RetentionPolicy"), RetentionPolicyDefinition),
            Sku=json_data.get("Sku"),
            StorageAccountId=json_data.get("StorageAccountId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TrustPolicy=deserialize_list(json_data.get("TrustPolicy"), TrustPolicyDefinition),
            ZoneRedundancyEnabled=json_data.get("ZoneRedundancyEnabled"),
            Identity=deserialize_list(json_data.get("Identity"), IdentityDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EncryptionDefinition(BaseModel):
    Enabled: Optional[bool]
    IdentityClientId: Optional[str]
    KeyVaultKeyId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            IdentityClientId=json_data.get("IdentityClientId"),
            KeyVaultKeyId=json_data.get("KeyVaultKeyId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionDefinition = EncryptionDefinition


@dataclass
class GeoreplicationsDefinition2(BaseModel):
    Location: Optional[str]
    Tags: Optional[Sequence["_GeoreplicationsDefinition"]]
    ZoneRedundancyEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_GeoreplicationsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GeoreplicationsDefinition2"]:
        if not json_data:
            return None
        return cls(
            Location=json_data.get("Location"),
            Tags=deserialize_list(json_data.get("Tags"), GeoreplicationsDefinition),
            ZoneRedundancyEnabled=json_data.get("ZoneRedundancyEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GeoreplicationsDefinition2 = GeoreplicationsDefinition2


@dataclass
class GeoreplicationsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GeoreplicationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GeoreplicationsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GeoreplicationsDefinition = GeoreplicationsDefinition


@dataclass
class NetworkRuleSetDefinition3(BaseModel):
    DefaultAction: Optional[str]
    IpRule: Optional[Sequence["_NetworkRuleSetDefinition"]]
    VirtualNetwork: Optional[Sequence["_NetworkRuleSetDefinition2"]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkRuleSetDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkRuleSetDefinition3"]:
        if not json_data:
            return None
        return cls(
            DefaultAction=json_data.get("DefaultAction"),
            IpRule=deserialize_list(json_data.get("IpRule"), NetworkRuleSetDefinition),
            VirtualNetwork=deserialize_list(json_data.get("VirtualNetwork"), NetworkRuleSetDefinition2),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkRuleSetDefinition3 = NetworkRuleSetDefinition3


@dataclass
class NetworkRuleSetDefinition(BaseModel):
    Action: Optional[str]
    IpRange: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkRuleSetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkRuleSetDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            IpRange=json_data.get("IpRange"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkRuleSetDefinition = NetworkRuleSetDefinition


@dataclass
class NetworkRuleSetDefinition2(BaseModel):
    Action: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkRuleSetDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkRuleSetDefinition2"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkRuleSetDefinition2 = NetworkRuleSetDefinition2


@dataclass
class RetentionPolicyDefinition(BaseModel):
    Days: Optional[float]
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_RetentionPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetentionPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Days=json_data.get("Days"),
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetentionPolicyDefinition = RetentionPolicyDefinition


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
class TrustPolicyDefinition(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_TrustPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrustPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrustPolicyDefinition = TrustPolicyDefinition


@dataclass
class IdentityDefinition(BaseModel):
    IdentityIds: Optional[Sequence[str]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IdentityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IdentityDefinition"]:
        if not json_data:
            return None
        return cls(
            IdentityIds=json_data.get("IdentityIds"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IdentityDefinition = IdentityDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


