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
    MemoryStorage: Optional[str]
    Name: Optional[str]
    PaymentMethodId: Optional[str]
    PersistentStorageEncryption: Optional[bool]
    Allowlist: Optional[Sequence["_AllowlistDefinition"]]
    CloudProvider: Optional[Sequence["_CloudProviderDefinition"]]
    Database: Optional[Sequence["_DatabaseDefinition"]]
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
            MemoryStorage=json_data.get("MemoryStorage"),
            Name=json_data.get("Name"),
            PaymentMethodId=json_data.get("PaymentMethodId"),
            PersistentStorageEncryption=json_data.get("PersistentStorageEncryption"),
            Allowlist=deserialize_list(json_data.get("Allowlist"), AllowlistDefinition),
            CloudProvider=deserialize_list(json_data.get("CloudProvider"), CloudProviderDefinition),
            Database=deserialize_list(json_data.get("Database"), DatabaseDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AllowlistDefinition(BaseModel):
    Cidrs: Optional[Sequence[str]]
    SecurityGroupIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AllowlistDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllowlistDefinition"]:
        if not json_data:
            return None
        return cls(
            Cidrs=json_data.get("Cidrs"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllowlistDefinition = AllowlistDefinition


@dataclass
class CloudProviderDefinition(BaseModel):
    CloudAccountId: Optional[str]
    Provider: Optional[str]
    Region: Optional[Sequence["_RegionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CloudProviderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudProviderDefinition"]:
        if not json_data:
            return None
        return cls(
            CloudAccountId=json_data.get("CloudAccountId"),
            Provider=json_data.get("Provider"),
            Region=deserialize_list(json_data.get("Region"), RegionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudProviderDefinition = CloudProviderDefinition


@dataclass
class RegionDefinition(BaseModel):
    MultipleAvailabilityZones: Optional[bool]
    NetworkingDeploymentCidr: Optional[str]
    NetworkingVpcId: Optional[str]
    PreferredAvailabilityZones: Optional[Sequence[str]]
    Region: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RegionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RegionDefinition"]:
        if not json_data:
            return None
        return cls(
            MultipleAvailabilityZones=json_data.get("MultipleAvailabilityZones"),
            NetworkingDeploymentCidr=json_data.get("NetworkingDeploymentCidr"),
            NetworkingVpcId=json_data.get("NetworkingVpcId"),
            PreferredAvailabilityZones=json_data.get("PreferredAvailabilityZones"),
            Region=json_data.get("Region"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RegionDefinition = RegionDefinition


@dataclass
class DatabaseDefinition(BaseModel):
    AverageItemSizeInBytes: Optional[float]
    ClientSslCertificate: Optional[str]
    DataPersistence: Optional[str]
    ExternalEndpointForOssClusterApi: Optional[bool]
    HashingPolicy: Optional[Sequence[str]]
    MemoryLimitInGb: Optional[float]
    Name: Optional[str]
    Password: Optional[str]
    PeriodicBackupPath: Optional[str]
    Protocol: Optional[str]
    ReplicaOf: Optional[Sequence[str]]
    Replication: Optional[bool]
    SourceIps: Optional[Sequence[str]]
    SupportOssClusterApi: Optional[bool]
    ThroughputMeasurementBy: Optional[str]
    ThroughputMeasurementValue: Optional[float]
    Alert: Optional[Sequence["_AlertDefinition"]]
    Module: Optional[Sequence["_ModuleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DatabaseDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatabaseDefinition"]:
        if not json_data:
            return None
        return cls(
            AverageItemSizeInBytes=json_data.get("AverageItemSizeInBytes"),
            ClientSslCertificate=json_data.get("ClientSslCertificate"),
            DataPersistence=json_data.get("DataPersistence"),
            ExternalEndpointForOssClusterApi=json_data.get("ExternalEndpointForOssClusterApi"),
            HashingPolicy=json_data.get("HashingPolicy"),
            MemoryLimitInGb=json_data.get("MemoryLimitInGb"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            PeriodicBackupPath=json_data.get("PeriodicBackupPath"),
            Protocol=json_data.get("Protocol"),
            ReplicaOf=json_data.get("ReplicaOf"),
            Replication=json_data.get("Replication"),
            SourceIps=json_data.get("SourceIps"),
            SupportOssClusterApi=json_data.get("SupportOssClusterApi"),
            ThroughputMeasurementBy=json_data.get("ThroughputMeasurementBy"),
            ThroughputMeasurementValue=json_data.get("ThroughputMeasurementValue"),
            Alert=deserialize_list(json_data.get("Alert"), AlertDefinition),
            Module=deserialize_list(json_data.get("Module"), ModuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatabaseDefinition = DatabaseDefinition


@dataclass
class AlertDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AlertDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AlertDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AlertDefinition = AlertDefinition


@dataclass
class ModuleDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ModuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ModuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ModuleDefinition = ModuleDefinition


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


