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
    Architecture: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    ImageName: Optional[str]
    LicenseType: Optional[str]
    OsType: Optional[str]
    Platform: Optional[str]
    DiskDeviceMapping: Optional[Sequence["_DiskDeviceMappingDefinition"]]
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
            Architecture=json_data.get("Architecture"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            ImageName=json_data.get("ImageName"),
            LicenseType=json_data.get("LicenseType"),
            OsType=json_data.get("OsType"),
            Platform=json_data.get("Platform"),
            DiskDeviceMapping=deserialize_list(json_data.get("DiskDeviceMapping"), DiskDeviceMappingDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DiskDeviceMappingDefinition(BaseModel):
    Device: Optional[str]
    DiskImageSize: Optional[float]
    Format: Optional[str]
    OssBucket: Optional[str]
    OssObject: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DiskDeviceMappingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiskDeviceMappingDefinition"]:
        if not json_data:
            return None
        return cls(
            Device=json_data.get("Device"),
            DiskImageSize=json_data.get("DiskImageSize"),
            Format=json_data.get("Format"),
            OssBucket=json_data.get("OssBucket"),
            OssObject=json_data.get("OssObject"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiskDeviceMappingDefinition = DiskDeviceMappingDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


