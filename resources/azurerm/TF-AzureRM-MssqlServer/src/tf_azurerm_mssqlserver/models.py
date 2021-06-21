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
    AdministratorLogin: Optional[str]
    AdministratorLoginPassword: Optional[str]
    ConnectionPolicy: Optional[str]
    ExtendedAuditingPolicy: Optional[Sequence["_ExtendedAuditingPolicyDefinition"]]
    FullyQualifiedDomainName: Optional[str]
    Id: Optional[str]
    Location: Optional[str]
    MinimumTlsVersion: Optional[str]
    Name: Optional[str]
    PublicNetworkAccessEnabled: Optional[bool]
    ResourceGroupName: Optional[str]
    RestorableDroppedDatabaseIds: Optional[Sequence[str]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Version: Optional[str]
    AzureadAdministrator: Optional[Sequence["_AzureadAdministratorDefinition"]]
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
            AdministratorLogin=json_data.get("AdministratorLogin"),
            AdministratorLoginPassword=json_data.get("AdministratorLoginPassword"),
            ConnectionPolicy=json_data.get("ConnectionPolicy"),
            ExtendedAuditingPolicy=deserialize_list(json_data.get("ExtendedAuditingPolicy"), ExtendedAuditingPolicyDefinition),
            FullyQualifiedDomainName=json_data.get("FullyQualifiedDomainName"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            MinimumTlsVersion=json_data.get("MinimumTlsVersion"),
            Name=json_data.get("Name"),
            PublicNetworkAccessEnabled=json_data.get("PublicNetworkAccessEnabled"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            RestorableDroppedDatabaseIds=json_data.get("RestorableDroppedDatabaseIds"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Version=json_data.get("Version"),
            AzureadAdministrator=deserialize_list(json_data.get("AzureadAdministrator"), AzureadAdministratorDefinition),
            Identity=deserialize_list(json_data.get("Identity"), IdentityDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ExtendedAuditingPolicyDefinition(BaseModel):
    LogMonitoringEnabled: Optional[bool]
    RetentionInDays: Optional[float]
    StorageAccountAccessKey: Optional[str]
    StorageAccountAccessKeyIsSecondary: Optional[bool]
    StorageEndpoint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExtendedAuditingPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtendedAuditingPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            LogMonitoringEnabled=json_data.get("LogMonitoringEnabled"),
            RetentionInDays=json_data.get("RetentionInDays"),
            StorageAccountAccessKey=json_data.get("StorageAccountAccessKey"),
            StorageAccountAccessKeyIsSecondary=json_data.get("StorageAccountAccessKeyIsSecondary"),
            StorageEndpoint=json_data.get("StorageEndpoint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtendedAuditingPolicyDefinition = ExtendedAuditingPolicyDefinition


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
class AzureadAdministratorDefinition(BaseModel):
    LoginUsername: Optional[str]
    ObjectId: Optional[str]
    TenantId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureadAdministratorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureadAdministratorDefinition"]:
        if not json_data:
            return None
        return cls(
            LoginUsername=json_data.get("LoginUsername"),
            ObjectId=json_data.get("ObjectId"),
            TenantId=json_data.get("TenantId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureadAdministratorDefinition = AzureadAdministratorDefinition


@dataclass
class IdentityDefinition(BaseModel):
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IdentityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IdentityDefinition"]:
        if not json_data:
            return None
        return cls(
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

