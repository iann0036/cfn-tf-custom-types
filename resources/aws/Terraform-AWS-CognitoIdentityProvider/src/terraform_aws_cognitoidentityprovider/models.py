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
    AttributeMapping: Optional[Sequence["_AttributeMapping"]]
    Id: Optional[str]
    IdpIdentifiers: Optional[Sequence[str]]
    ProviderDetails: Optional[Sequence["_ProviderDetails"]]
    ProviderName: Optional[str]
    ProviderType: Optional[str]
    UserPoolId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AttributeMapping=json_data.get("AttributeMapping"),
            Id=json_data.get("Id"),
            IdpIdentifiers=json_data.get("IdpIdentifiers"),
            ProviderDetails=json_data.get("ProviderDetails"),
            ProviderName=json_data.get("ProviderName"),
            ProviderType=json_data.get("ProviderType"),
            UserPoolId=json_data.get("UserPoolId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AttributeMapping:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AttributeMapping"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttributeMapping"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttributeMapping = AttributeMapping


@dataclass
class ProviderDetails:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProviderDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProviderDetails"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProviderDetails = ProviderDetails


