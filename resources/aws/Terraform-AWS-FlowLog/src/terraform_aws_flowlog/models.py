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
    EniId: Optional[str]
    IamRoleArn: Optional[str]
    Id: Optional[str]
    LogDestination: Optional[str]
    LogDestinationType: Optional[str]
    LogFormat: Optional[str]
    LogGroupName: Optional[str]
    SubnetId: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    TrafficType: Optional[str]
    VpcId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            EniId=json_data.get("EniId"),
            IamRoleArn=json_data.get("IamRoleArn"),
            Id=json_data.get("Id"),
            LogDestination=json_data.get("LogDestination"),
            LogDestinationType=json_data.get("LogDestinationType"),
            LogFormat=json_data.get("LogFormat"),
            LogGroupName=json_data.get("LogGroupName"),
            SubnetId=json_data.get("SubnetId"),
            Tags=json_data.get("Tags"),
            TrafficType=json_data.get("TrafficType"),
            VpcId=json_data.get("VpcId"),
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


