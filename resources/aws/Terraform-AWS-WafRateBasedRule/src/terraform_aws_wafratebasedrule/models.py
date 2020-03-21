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
    Arn: Optional[str]
    Id: Optional[str]
    MetricName: Optional[str]
    Name: Optional[str]
    RateKey: Optional[str]
    RateLimit: Optional[float]
    Tags: Optional[Sequence["_Tags"]]
    Predicates: Optional[Sequence["_Predicates"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            Id=json_data.get("Id"),
            MetricName=json_data.get("MetricName"),
            Name=json_data.get("Name"),
            RateKey=json_data.get("RateKey"),
            RateLimit=json_data.get("RateLimit"),
            Tags=json_data.get("Tags"),
            Predicates=json_data.get("Predicates"),
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
class Predicates:
    DataId: Optional[str]
    Negated: Optional[bool]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Predicates"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Predicates"]:
        if not json_data:
            return None
        return cls(
            DataId=json_data.get("DataId"),
            Negated=json_data.get("Negated"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Predicates = Predicates


