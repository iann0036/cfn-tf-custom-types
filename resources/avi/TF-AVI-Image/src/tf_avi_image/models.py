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
    ControllerPatchName: Optional[str]
    ControllerPatchUuid: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    SePatchName: Optional[str]
    SePatchUuid: Optional[str]
    Status: Optional[str]
    TenantRef: Optional[str]
    Type: Optional[str]
    UberBundle: Optional[bool]
    Uuid: Optional[str]
    CloudInfoValues: Optional[Sequence["_CloudInfoValuesDefinition"]]
    ControllerInfo: Optional[Sequence["_ControllerInfoDefinition"]]
    Migrations: Optional[Sequence["_MigrationsDefinition"]]
    SeInfo: Optional[Sequence["_SeInfoDefinition"]]

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
            ControllerPatchName=json_data.get("ControllerPatchName"),
            ControllerPatchUuid=json_data.get("ControllerPatchUuid"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            SePatchName=json_data.get("SePatchName"),
            SePatchUuid=json_data.get("SePatchUuid"),
            Status=json_data.get("Status"),
            TenantRef=json_data.get("TenantRef"),
            Type=json_data.get("Type"),
            UberBundle=json_data.get("UberBundle"),
            Uuid=json_data.get("Uuid"),
            CloudInfoValues=deserialize_list(json_data.get("CloudInfoValues"), CloudInfoValuesDefinition),
            ControllerInfo=deserialize_list(json_data.get("ControllerInfo"), ControllerInfoDefinition),
            Migrations=deserialize_list(json_data.get("Migrations"), MigrationsDefinition),
            SeInfo=deserialize_list(json_data.get("SeInfo"), SeInfoDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CloudInfoValuesDefinition(BaseModel):
    CloudName: Optional[str]
    CloudDataValues: Optional[Sequence["_CloudDataValuesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CloudInfoValuesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudInfoValuesDefinition"]:
        if not json_data:
            return None
        return cls(
            CloudName=json_data.get("CloudName"),
            CloudDataValues=deserialize_list(json_data.get("CloudDataValues"), CloudDataValuesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudInfoValuesDefinition = CloudInfoValuesDefinition


@dataclass
class CloudDataValuesDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CloudDataValuesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudDataValuesDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudDataValuesDefinition = CloudDataValuesDefinition


@dataclass
class ControllerInfoDefinition(BaseModel):
    Hash: Optional[str]
    Path: Optional[str]
    Build: Optional[Sequence["_BuildDefinition"]]
    Patch: Optional[Sequence["_PatchDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ControllerInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ControllerInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Hash=json_data.get("Hash"),
            Path=json_data.get("Path"),
            Build=deserialize_list(json_data.get("Build"), BuildDefinition),
            Patch=deserialize_list(json_data.get("Patch"), PatchDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ControllerInfoDefinition = ControllerInfoDefinition


@dataclass
class BuildDefinition(BaseModel):
    BuildNo: Optional[float]
    Date: Optional[str]
    MinVersion: Optional[str]
    PatchVersion: Optional[str]
    Product: Optional[str]
    ProductName: Optional[str]
    Tag: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BuildDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BuildDefinition"]:
        if not json_data:
            return None
        return cls(
            BuildNo=json_data.get("BuildNo"),
            Date=json_data.get("Date"),
            MinVersion=json_data.get("MinVersion"),
            PatchVersion=json_data.get("PatchVersion"),
            Product=json_data.get("Product"),
            ProductName=json_data.get("ProductName"),
            Tag=json_data.get("Tag"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BuildDefinition = BuildDefinition


@dataclass
class PatchDefinition(BaseModel):
    PatchType: Optional[str]
    Reboot: Optional[bool]
    RebootList: Optional[Sequence["_RebootListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PatchDefinition"]:
        if not json_data:
            return None
        return cls(
            PatchType=json_data.get("PatchType"),
            Reboot=json_data.get("Reboot"),
            RebootList=deserialize_list(json_data.get("RebootList"), RebootListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PatchDefinition = PatchDefinition


@dataclass
class RebootListDefinition(BaseModel):
    PatchVersion: Optional[str]
    Reboot: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_RebootListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RebootListDefinition"]:
        if not json_data:
            return None
        return cls(
            PatchVersion=json_data.get("PatchVersion"),
            Reboot=json_data.get("Reboot"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RebootListDefinition = RebootListDefinition


@dataclass
class MigrationsDefinition(BaseModel):
    ApiVersion: Optional[str]
    ControllerHostMinFreeDiskSize: Optional[float]
    ControllerMinCores: Optional[float]
    ControllerMinFreeDiskSize: Optional[float]
    ControllerMinMemory: Optional[float]
    ControllerMinTotalDisk: Optional[float]
    MaxActiveVersions: Optional[float]
    RollbackControllerDiskSpace: Optional[float]
    RollbackSeDiskSpace: Optional[float]
    SeHostMinFreeDiskSize: Optional[float]
    SeMinCores: Optional[float]
    SeMinFreeDiskSize: Optional[float]
    SeMinMemory: Optional[float]
    SeMinTotalDisk: Optional[float]
    Versions: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MigrationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MigrationsDefinition"]:
        if not json_data:
            return None
        return cls(
            ApiVersion=json_data.get("ApiVersion"),
            ControllerHostMinFreeDiskSize=json_data.get("ControllerHostMinFreeDiskSize"),
            ControllerMinCores=json_data.get("ControllerMinCores"),
            ControllerMinFreeDiskSize=json_data.get("ControllerMinFreeDiskSize"),
            ControllerMinMemory=json_data.get("ControllerMinMemory"),
            ControllerMinTotalDisk=json_data.get("ControllerMinTotalDisk"),
            MaxActiveVersions=json_data.get("MaxActiveVersions"),
            RollbackControllerDiskSpace=json_data.get("RollbackControllerDiskSpace"),
            RollbackSeDiskSpace=json_data.get("RollbackSeDiskSpace"),
            SeHostMinFreeDiskSize=json_data.get("SeHostMinFreeDiskSize"),
            SeMinCores=json_data.get("SeMinCores"),
            SeMinFreeDiskSize=json_data.get("SeMinFreeDiskSize"),
            SeMinMemory=json_data.get("SeMinMemory"),
            SeMinTotalDisk=json_data.get("SeMinTotalDisk"),
            Versions=json_data.get("Versions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MigrationsDefinition = MigrationsDefinition


@dataclass
class SeInfoDefinition(BaseModel):
    Hash: Optional[str]
    Path: Optional[str]
    Build: Optional[Sequence["_BuildDefinition"]]
    Patch: Optional[Sequence["_PatchDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SeInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SeInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Hash=json_data.get("Hash"),
            Path=json_data.get("Path"),
            Build=deserialize_list(json_data.get("Build"), BuildDefinition),
            Patch=deserialize_list(json_data.get("Patch"), PatchDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SeInfoDefinition = SeInfoDefinition


