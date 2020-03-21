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
    CustomSslOptions: Optional[Sequence["_CustomSslOptions"]]
    ExpiresOn: Optional[str]
    Hosts: Optional[Sequence[str]]
    Issuer: Optional[str]
    ModifiedOn: Optional[str]
    Priority: Optional[float]
    Signature: Optional[str]
    Status: Optional[str]
    UploadedOn: Optional[str]
    ZoneId: Optional[str]
    CustomSslPriority: Optional[Sequence["_CustomSslPriority"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CustomSslOptions=json_data.get("CustomSslOptions"),
            ExpiresOn=json_data.get("ExpiresOn"),
            Hosts=json_data.get("Hosts"),
            Issuer=json_data.get("Issuer"),
            ModifiedOn=json_data.get("ModifiedOn"),
            Priority=json_data.get("Priority"),
            Signature=json_data.get("Signature"),
            Status=json_data.get("Status"),
            UploadedOn=json_data.get("UploadedOn"),
            ZoneId=json_data.get("ZoneId"),
            CustomSslPriority=json_data.get("CustomSslPriority"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CustomSslOptions:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomSslOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomSslOptions"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomSslOptions = CustomSslOptions


@dataclass
class CustomSslPriority:
    Id: Optional[str]
    Priority: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CustomSslPriority"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomSslPriority"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Priority=json_data.get("Priority"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomSslPriority = CustomSslPriority


