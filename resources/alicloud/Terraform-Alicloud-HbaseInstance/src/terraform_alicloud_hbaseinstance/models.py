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
    AutoRenew: Optional[bool]
    ColdStorageSize: Optional[float]
    CoreDiskSize: Optional[float]
    CoreDiskType: Optional[str]
    CoreInstanceQuantity: Optional[float]
    CoreInstanceType: Optional[str]
    DeletionProtection: Optional[bool]
    Duration: Optional[float]
    Engine: Optional[str]
    EngineVersion: Optional[str]
    Id: Optional[str]
    MaintainEndTime: Optional[str]
    MaintainStartTime: Optional[str]
    MasterInstanceType: Optional[str]
    Name: Optional[str]
    PayType: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    VswitchId: Optional[str]
    ZoneId: Optional[str]
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
            AutoRenew=json_data.get("AutoRenew"),
            ColdStorageSize=json_data.get("ColdStorageSize"),
            CoreDiskSize=json_data.get("CoreDiskSize"),
            CoreDiskType=json_data.get("CoreDiskType"),
            CoreInstanceQuantity=json_data.get("CoreInstanceQuantity"),
            CoreInstanceType=json_data.get("CoreInstanceType"),
            DeletionProtection=json_data.get("DeletionProtection"),
            Duration=json_data.get("Duration"),
            Engine=json_data.get("Engine"),
            EngineVersion=json_data.get("EngineVersion"),
            Id=json_data.get("Id"),
            MaintainEndTime=json_data.get("MaintainEndTime"),
            MaintainStartTime=json_data.get("MaintainStartTime"),
            MasterInstanceType=json_data.get("MasterInstanceType"),
            Name=json_data.get("Name"),
            PayType=json_data.get("PayType"),
            Tags=json_data.get("Tags"),
            VswitchId=json_data.get("VswitchId"),
            ZoneId=json_data.get("ZoneId"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


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


