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
    Description: Optional[str]
    Id: Optional[str]
    KafkaVersions: Optional[Sequence[str]]
    LatestRevision: Optional[float]
    Name: Optional[str]
    ServerProperties: Optional[str]

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
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            KafkaVersions=json_data.get("KafkaVersions"),
            LatestRevision=json_data.get("LatestRevision"),
            Name=json_data.get("Name"),
            ServerProperties=json_data.get("ServerProperties"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


