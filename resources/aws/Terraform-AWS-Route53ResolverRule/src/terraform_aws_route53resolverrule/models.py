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
    DomainName: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    OwnerId: Optional[str]
    ResolverEndpointId: Optional[str]
    RuleType: Optional[str]
    ShareStatus: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    TargetIp: Optional[Sequence["_TargetIp"]]
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
            Arn=json_data.get("Arn"),
            DomainName=json_data.get("DomainName"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            OwnerId=json_data.get("OwnerId"),
            ResolverEndpointId=json_data.get("ResolverEndpointId"),
            RuleType=json_data.get("RuleType"),
            ShareStatus=json_data.get("ShareStatus"),
            Tags=json_data.get("Tags"),
            TargetIp=json_data.get("TargetIp"),
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
class TargetIp:
    Ip: Optional[str]
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TargetIp"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetIp"]:
        if not json_data:
            return None
        return cls(
            Ip=json_data.get("Ip"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetIp = TargetIp


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


