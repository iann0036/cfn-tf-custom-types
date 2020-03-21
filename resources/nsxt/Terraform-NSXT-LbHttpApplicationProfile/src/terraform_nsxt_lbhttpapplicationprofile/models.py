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
    Description: Optional[str]
    DisplayName: Optional[str]
    HttpRedirectTo: Optional[str]
    HttpRedirectToHttps: Optional[bool]
    IdleTimeout: Optional[float]
    Ntlm: Optional[bool]
    RequestBodySize: Optional[float]
    RequestHeaderSize: Optional[float]
    ResponseTimeout: Optional[float]
    Revision: Optional[float]
    XForwardedFor: Optional[str]
    Tag: Optional[Sequence["_Tag"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            HttpRedirectTo=json_data.get("HttpRedirectTo"),
            HttpRedirectToHttps=json_data.get("HttpRedirectToHttps"),
            IdleTimeout=json_data.get("IdleTimeout"),
            Ntlm=json_data.get("Ntlm"),
            RequestBodySize=json_data.get("RequestBodySize"),
            RequestHeaderSize=json_data.get("RequestHeaderSize"),
            ResponseTimeout=json_data.get("ResponseTimeout"),
            Revision=json_data.get("Revision"),
            XForwardedFor=json_data.get("XForwardedFor"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tag:
    Scope: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Scope=json_data.get("Scope"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


