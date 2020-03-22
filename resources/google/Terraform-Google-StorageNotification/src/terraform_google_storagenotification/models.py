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
    Bucket: Optional[str]
    CustomAttributes: Optional[Sequence["_CustomAttributes"]]
    EventTypes: Optional[Sequence[str]]
    Id: Optional[str]
    NotificationId: Optional[str]
    ObjectNamePrefix: Optional[str]
    PayloadFormat: Optional[str]
    SelfLink: Optional[str]
    Topic: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Bucket=json_data.get("Bucket"),
            CustomAttributes=json_data.get("CustomAttributes"),
            EventTypes=json_data.get("EventTypes"),
            Id=json_data.get("Id"),
            NotificationId=json_data.get("NotificationId"),
            ObjectNamePrefix=json_data.get("ObjectNamePrefix"),
            PayloadFormat=json_data.get("PayloadFormat"),
            SelfLink=json_data.get("SelfLink"),
            Topic=json_data.get("Topic"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CustomAttributes:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomAttributes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomAttributes"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomAttributes = CustomAttributes


