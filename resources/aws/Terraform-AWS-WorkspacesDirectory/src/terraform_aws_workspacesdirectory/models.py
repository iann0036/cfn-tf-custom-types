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
    DirectoryId: Optional[str]
    Id: Optional[str]
    SubnetIds: Optional[Sequence[str]]
    Tags: Optional[Sequence["_Tags"]]
    SelfServicePermissions: Optional[Sequence["_SelfServicePermissions"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DirectoryId=json_data.get("DirectoryId"),
            Id=json_data.get("Id"),
            SubnetIds=json_data.get("SubnetIds"),
            Tags=json_data.get("Tags"),
            SelfServicePermissions=json_data.get("SelfServicePermissions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class SelfServicePermissions:
    ChangeComputeType: Optional[bool]
    IncreaseVolumeSize: Optional[bool]
    RebuildWorkspace: Optional[bool]
    RestartWorkspace: Optional[bool]
    SwitchRunningMode: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SelfServicePermissions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SelfServicePermissions"]:
        if not json_data:
            return None
        return cls(
            ChangeComputeType=json_data.get("ChangeComputeType"),
            IncreaseVolumeSize=json_data.get("IncreaseVolumeSize"),
            RebuildWorkspace=json_data.get("RebuildWorkspace"),
            RestartWorkspace=json_data.get("RestartWorkspace"),
            SwitchRunningMode=json_data.get("SwitchRunningMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SelfServicePermissions = SelfServicePermissions


