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
    AdministratorAccount: Optional[str]
    Arn: Optional[str]
    Description: Optional[str]
    Domain: Optional[str]
    DomainOwner: Optional[str]
    Id: Optional[str]
    Repository: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    ExternalConnections: Optional[Sequence["_ExternalConnectionsDefinition"]]
    Upstream: Optional[Sequence["_UpstreamDefinition"]]

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
            AdministratorAccount=json_data.get("AdministratorAccount"),
            Arn=json_data.get("Arn"),
            Description=json_data.get("Description"),
            Domain=json_data.get("Domain"),
            DomainOwner=json_data.get("DomainOwner"),
            Id=json_data.get("Id"),
            Repository=json_data.get("Repository"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            ExternalConnections=deserialize_list(json_data.get("ExternalConnections"), ExternalConnectionsDefinition),
            Upstream=deserialize_list(json_data.get("Upstream"), UpstreamDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class ExternalConnectionsDefinition(BaseModel):
    ExternalConnectionName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExternalConnectionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExternalConnectionsDefinition"]:
        if not json_data:
            return None
        return cls(
            ExternalConnectionName=json_data.get("ExternalConnectionName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExternalConnectionsDefinition = ExternalConnectionsDefinition


@dataclass
class UpstreamDefinition(BaseModel):
    RepositoryName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UpstreamDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UpstreamDefinition"]:
        if not json_data:
            return None
        return cls(
            RepositoryName=json_data.get("RepositoryName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UpstreamDefinition = UpstreamDefinition


