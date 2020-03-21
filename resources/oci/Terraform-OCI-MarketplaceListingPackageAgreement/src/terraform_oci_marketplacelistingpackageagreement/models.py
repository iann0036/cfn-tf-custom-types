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
    AgreementId: Optional[str]
    Author: Optional[str]
    CompartmentId: Optional[str]
    ContentUrl: Optional[str]
    ListingId: Optional[str]
    PackageVersion: Optional[str]
    Prompt: Optional[str]
    Signature: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AgreementId=json_data.get("AgreementId"),
            Author=json_data.get("Author"),
            CompartmentId=json_data.get("CompartmentId"),
            ContentUrl=json_data.get("ContentUrl"),
            ListingId=json_data.get("ListingId"),
            PackageVersion=json_data.get("PackageVersion"),
            Prompt=json_data.get("Prompt"),
            Signature=json_data.get("Signature"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


