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
    Admins: Optional[Sequence[float]]
    DeleteOnDestruction: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    Template: Optional[str]
    Users: Optional[Sequence[float]]
    Quotas: Optional[Sequence["_QuotasDefinition"]]

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
            Admins=json_data.get("Admins"),
            DeleteOnDestruction=json_data.get("DeleteOnDestruction"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Template=json_data.get("Template"),
            Users=json_data.get("Users"),
            Quotas=deserialize_list(json_data.get("Quotas"), QuotasDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class QuotasDefinition(BaseModel):
    DatastoreQuotas: Optional[Sequence["_DatastoreQuotasDefinition"]]
    ImageQuotas: Optional[Sequence["_ImageQuotasDefinition"]]
    NetworkQuotas: Optional[Sequence["_NetworkQuotasDefinition"]]
    VmQuotas: Optional[Sequence["_VmQuotasDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_QuotasDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QuotasDefinition"]:
        if not json_data:
            return None
        return cls(
            DatastoreQuotas=deserialize_list(json_data.get("DatastoreQuotas"), DatastoreQuotasDefinition),
            ImageQuotas=deserialize_list(json_data.get("ImageQuotas"), ImageQuotasDefinition),
            NetworkQuotas=deserialize_list(json_data.get("NetworkQuotas"), NetworkQuotasDefinition),
            VmQuotas=deserialize_list(json_data.get("VmQuotas"), VmQuotasDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_QuotasDefinition = QuotasDefinition


@dataclass
class DatastoreQuotasDefinition(BaseModel):
    Id: Optional[float]
    Images: Optional[float]
    Size: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DatastoreQuotasDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatastoreQuotasDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Images=json_data.get("Images"),
            Size=json_data.get("Size"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatastoreQuotasDefinition = DatastoreQuotasDefinition


@dataclass
class ImageQuotasDefinition(BaseModel):
    Id: Optional[float]
    RunningVms: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ImageQuotasDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImageQuotasDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            RunningVms=json_data.get("RunningVms"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImageQuotasDefinition = ImageQuotasDefinition


@dataclass
class NetworkQuotasDefinition(BaseModel):
    Id: Optional[float]
    Leases: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkQuotasDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkQuotasDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Leases=json_data.get("Leases"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkQuotasDefinition = NetworkQuotasDefinition


@dataclass
class VmQuotasDefinition(BaseModel):
    Cpu: Optional[float]
    Memory: Optional[float]
    RunningCpu: Optional[float]
    RunningMemory: Optional[float]
    RunningVms: Optional[float]
    SystemDiskSize: Optional[float]
    Vms: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_VmQuotasDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VmQuotasDefinition"]:
        if not json_data:
            return None
        return cls(
            Cpu=json_data.get("Cpu"),
            Memory=json_data.get("Memory"),
            RunningCpu=json_data.get("RunningCpu"),
            RunningMemory=json_data.get("RunningMemory"),
            RunningVms=json_data.get("RunningVms"),
            SystemDiskSize=json_data.get("SystemDiskSize"),
            Vms=json_data.get("Vms"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VmQuotasDefinition = VmQuotasDefinition


