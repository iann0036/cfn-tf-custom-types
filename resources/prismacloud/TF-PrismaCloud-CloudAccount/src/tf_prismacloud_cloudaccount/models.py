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
    Id: Optional[str]
    AlibabaCloud: Optional[Sequence["_AlibabaCloudDefinition"]]
    Aws: Optional[Sequence["_AwsDefinition"]]
    Azure: Optional[Sequence["_AzureDefinition"]]
    Gcp: Optional[Sequence["_GcpDefinition"]]
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
            Id=json_data.get("Id"),
            AlibabaCloud=deserialize_list(json_data.get("AlibabaCloud"), AlibabaCloudDefinition),
            Aws=deserialize_list(json_data.get("Aws"), AwsDefinition),
            Azure=deserialize_list(json_data.get("Azure"), AzureDefinition),
            Gcp=deserialize_list(json_data.get("Gcp"), GcpDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AlibabaCloudDefinition(BaseModel):
    AccountId: Optional[str]
    Enabled: Optional[bool]
    GroupIds: Optional[Sequence[str]]
    Name: Optional[str]
    RamArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AlibabaCloudDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AlibabaCloudDefinition"]:
        if not json_data:
            return None
        return cls(
            AccountId=json_data.get("AccountId"),
            Enabled=json_data.get("Enabled"),
            GroupIds=json_data.get("GroupIds"),
            Name=json_data.get("Name"),
            RamArn=json_data.get("RamArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AlibabaCloudDefinition = AlibabaCloudDefinition


@dataclass
class AwsDefinition(BaseModel):
    AccountId: Optional[str]
    AccountType: Optional[str]
    Enabled: Optional[bool]
    ExternalId: Optional[str]
    GroupIds: Optional[Sequence[str]]
    Name: Optional[str]
    ProtectionMode: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDefinition"]:
        if not json_data:
            return None
        return cls(
            AccountId=json_data.get("AccountId"),
            AccountType=json_data.get("AccountType"),
            Enabled=json_data.get("Enabled"),
            ExternalId=json_data.get("ExternalId"),
            GroupIds=json_data.get("GroupIds"),
            Name=json_data.get("Name"),
            ProtectionMode=json_data.get("ProtectionMode"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDefinition = AwsDefinition


@dataclass
class AzureDefinition(BaseModel):
    AccountId: Optional[str]
    AccountType: Optional[str]
    ClientId: Optional[str]
    Enabled: Optional[bool]
    GroupIds: Optional[Sequence[str]]
    Key: Optional[str]
    MonitorFlowLogs: Optional[bool]
    Name: Optional[str]
    ProtectionMode: Optional[str]
    ServicePrincipalId: Optional[str]
    TenantId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureDefinition"]:
        if not json_data:
            return None
        return cls(
            AccountId=json_data.get("AccountId"),
            AccountType=json_data.get("AccountType"),
            ClientId=json_data.get("ClientId"),
            Enabled=json_data.get("Enabled"),
            GroupIds=json_data.get("GroupIds"),
            Key=json_data.get("Key"),
            MonitorFlowLogs=json_data.get("MonitorFlowLogs"),
            Name=json_data.get("Name"),
            ProtectionMode=json_data.get("ProtectionMode"),
            ServicePrincipalId=json_data.get("ServicePrincipalId"),
            TenantId=json_data.get("TenantId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureDefinition = AzureDefinition


@dataclass
class GcpDefinition(BaseModel):
    AccountId: Optional[str]
    AccountType: Optional[str]
    CompressionEnabled: Optional[bool]
    CredentialsJson: Optional[str]
    DataflowEnabledProject: Optional[str]
    Enabled: Optional[bool]
    FlowLogStorageBucket: Optional[str]
    GroupIds: Optional[Sequence[str]]
    Name: Optional[str]
    ProtectionMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GcpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GcpDefinition"]:
        if not json_data:
            return None
        return cls(
            AccountId=json_data.get("AccountId"),
            AccountType=json_data.get("AccountType"),
            CompressionEnabled=json_data.get("CompressionEnabled"),
            CredentialsJson=json_data.get("CredentialsJson"),
            DataflowEnabledProject=json_data.get("DataflowEnabledProject"),
            Enabled=json_data.get("Enabled"),
            FlowLogStorageBucket=json_data.get("FlowLogStorageBucket"),
            GroupIds=json_data.get("GroupIds"),
            Name=json_data.get("Name"),
            ProtectionMode=json_data.get("ProtectionMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GcpDefinition = GcpDefinition


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


