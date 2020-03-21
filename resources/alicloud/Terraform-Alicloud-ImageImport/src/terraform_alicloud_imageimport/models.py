# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    Architecture: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    ImageName: Optional[str]
    LicenseType: Optional[str]
    OsType: Optional[str]
    Platform: Optional[str]
    DiskDeviceMapping: Optional[Sequence["_DiskDeviceMapping"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Architecture=json_data.get("Architecture"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            ImageName=json_data.get("ImageName"),
            LicenseType=json_data.get("LicenseType"),
            OsType=json_data.get("OsType"),
            Platform=json_data.get("Platform"),
            DiskDeviceMapping=json_data.get("DiskDeviceMapping"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DiskDeviceMapping:
    Device: Optional[str]
    DiskImageSize: Optional[float]
    Format: Optional[str]
    OssBucket: Optional[str]
    OssObject: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DiskDeviceMapping"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiskDeviceMapping"]:
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
_DiskDeviceMapping = DiskDeviceMapping


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


