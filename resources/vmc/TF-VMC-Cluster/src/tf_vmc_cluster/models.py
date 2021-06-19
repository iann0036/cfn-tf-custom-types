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
    ClusterInfo: Optional[Sequence["_ClusterInfoDefinition"]]
    EdrsPolicyType: Optional[str]
    EnableEdrs: Optional[bool]
    HostCpuCoresCount: Optional[float]
    HostInstanceType: Optional[str]
    Id: Optional[str]
    MaxHosts: Optional[float]
    MinHosts: Optional[float]
    NumHosts: Optional[float]
    SddcId: Optional[str]
    StorageCapacity: Optional[str]
    MicrosoftLicensingConfig: Optional[Sequence["_MicrosoftLicensingConfigDefinition"]]
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
            ClusterInfo=deserialize_list(json_data.get("ClusterInfo"), ClusterInfoDefinition),
            EdrsPolicyType=json_data.get("EdrsPolicyType"),
            EnableEdrs=json_data.get("EnableEdrs"),
            HostCpuCoresCount=json_data.get("HostCpuCoresCount"),
            HostInstanceType=json_data.get("HostInstanceType"),
            Id=json_data.get("Id"),
            MaxHosts=json_data.get("MaxHosts"),
            MinHosts=json_data.get("MinHosts"),
            NumHosts=json_data.get("NumHosts"),
            SddcId=json_data.get("SddcId"),
            StorageCapacity=json_data.get("StorageCapacity"),
            MicrosoftLicensingConfig=deserialize_list(json_data.get("MicrosoftLicensingConfig"), MicrosoftLicensingConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ClusterInfoDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterInfoDefinition = ClusterInfoDefinition


@dataclass
class MicrosoftLicensingConfigDefinition(BaseModel):
    MssqlLicensing: Optional[str]
    WindowsLicensing: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MicrosoftLicensingConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MicrosoftLicensingConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            MssqlLicensing=json_data.get("MssqlLicensing"),
            WindowsLicensing=json_data.get("WindowsLicensing"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MicrosoftLicensingConfigDefinition = MicrosoftLicensingConfigDefinition


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


