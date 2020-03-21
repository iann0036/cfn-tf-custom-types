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
    AllowInsecure: Optional[bool]
    CreatedOn: Optional[str]
    Description: Optional[str]
    ExpectedBody: Optional[str]
    ExpectedCodes: Optional[str]
    FollowRedirects: Optional[bool]
    Id: Optional[str]
    Interval: Optional[float]
    Method: Optional[str]
    ModifiedOn: Optional[str]
    Path: Optional[str]
    Port: Optional[float]
    Retries: Optional[float]
    Timeout: Optional[float]
    Type: Optional[str]
    Header: Optional[Sequence["_Header"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AllowInsecure=json_data.get("AllowInsecure"),
            CreatedOn=json_data.get("CreatedOn"),
            Description=json_data.get("Description"),
            ExpectedBody=json_data.get("ExpectedBody"),
            ExpectedCodes=json_data.get("ExpectedCodes"),
            FollowRedirects=json_data.get("FollowRedirects"),
            Id=json_data.get("Id"),
            Interval=json_data.get("Interval"),
            Method=json_data.get("Method"),
            ModifiedOn=json_data.get("ModifiedOn"),
            Path=json_data.get("Path"),
            Port=json_data.get("Port"),
            Retries=json_data.get("Retries"),
            Timeout=json_data.get("Timeout"),
            Type=json_data.get("Type"),
            Header=json_data.get("Header"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Header:
    Header: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Header"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Header"]:
        if not json_data:
            return None
        return cls(
            Header=json_data.get("Header"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Header = Header


