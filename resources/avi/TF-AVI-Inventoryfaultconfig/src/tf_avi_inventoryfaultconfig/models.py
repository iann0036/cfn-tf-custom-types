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
    Name: Optional[str]
    TenantRef: Optional[str]
    Uuid: Optional[str]
    ControllerFaults: Optional[Sequence["_ControllerFaultsDefinition"]]
    ServiceengineFaults: Optional[Sequence["_ServiceengineFaultsDefinition"]]
    VirtualserviceFaults: Optional[Sequence["_VirtualserviceFaultsDefinition"]]

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
            Name=json_data.get("Name"),
            TenantRef=json_data.get("TenantRef"),
            Uuid=json_data.get("Uuid"),
            ControllerFaults=deserialize_list(json_data.get("ControllerFaults"), ControllerFaultsDefinition),
            ServiceengineFaults=deserialize_list(json_data.get("ServiceengineFaults"), ServiceengineFaultsDefinition),
            VirtualserviceFaults=deserialize_list(json_data.get("VirtualserviceFaults"), VirtualserviceFaultsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ControllerFaultsDefinition(BaseModel):
    BackupSchedulerFaults: Optional[bool]
    ClusterFaults: Optional[bool]
    DeprecatedApiVersionFaults: Optional[bool]
    LicenseFaults: Optional[bool]
    MigrationFaults: Optional[bool]
    SslprofileFaults: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ControllerFaultsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ControllerFaultsDefinition"]:
        if not json_data:
            return None
        return cls(
            BackupSchedulerFaults=json_data.get("BackupSchedulerFaults"),
            ClusterFaults=json_data.get("ClusterFaults"),
            DeprecatedApiVersionFaults=json_data.get("DeprecatedApiVersionFaults"),
            LicenseFaults=json_data.get("LicenseFaults"),
            MigrationFaults=json_data.get("MigrationFaults"),
            SslprofileFaults=json_data.get("SslprofileFaults"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ControllerFaultsDefinition = ControllerFaultsDefinition


@dataclass
class ServiceengineFaultsDefinition(BaseModel):
    DebugFaults: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceengineFaultsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceengineFaultsDefinition"]:
        if not json_data:
            return None
        return cls(
            DebugFaults=json_data.get("DebugFaults"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceengineFaultsDefinition = ServiceengineFaultsDefinition


@dataclass
class VirtualserviceFaultsDefinition(BaseModel):
    DebugFaults: Optional[bool]
    PoolServerFaults: Optional[bool]
    ScaleoutFaults: Optional[bool]
    SharedVipFaults: Optional[bool]
    SslCertExpiryFaults: Optional[bool]
    SslCertStatusFaults: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualserviceFaultsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualserviceFaultsDefinition"]:
        if not json_data:
            return None
        return cls(
            DebugFaults=json_data.get("DebugFaults"),
            PoolServerFaults=json_data.get("PoolServerFaults"),
            ScaleoutFaults=json_data.get("ScaleoutFaults"),
            SharedVipFaults=json_data.get("SharedVipFaults"),
            SslCertExpiryFaults=json_data.get("SslCertExpiryFaults"),
            SslCertStatusFaults=json_data.get("SslCertStatusFaults"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualserviceFaultsDefinition = VirtualserviceFaultsDefinition


