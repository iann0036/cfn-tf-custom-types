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
    Autolasthop: Optional[str]
    FullPath: Optional[str]
    Mirror: Optional[str]
    Name: Optional[str]
    Partition: Optional[str]
    Snatpool: Optional[str]
    Sourceport: Optional[str]
    Translation: Optional[str]
    Vlans: Optional[Sequence[str]]
    Vlansdisabled: Optional[bool]
    Origins: Optional[Sequence["_Origins"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Autolasthop=json_data.get("Autolasthop"),
            FullPath=json_data.get("FullPath"),
            Mirror=json_data.get("Mirror"),
            Name=json_data.get("Name"),
            Partition=json_data.get("Partition"),
            Snatpool=json_data.get("Snatpool"),
            Sourceport=json_data.get("Sourceport"),
            Translation=json_data.get("Translation"),
            Vlans=json_data.get("Vlans"),
            Vlansdisabled=json_data.get("Vlansdisabled"),
            Origins=json_data.get("Origins"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Origins:
    AppService: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Origins"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Origins"]:
        if not json_data:
            return None
        return cls(
            AppService=json_data.get("AppService"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Origins = Origins


