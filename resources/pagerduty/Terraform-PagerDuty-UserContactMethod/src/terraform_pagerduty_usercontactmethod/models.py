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
    Address: Optional[str]
    Blacklisted: Optional[bool]
    CountryCode: Optional[float]
    Enabled: Optional[bool]
    Id: Optional[str]
    Label: Optional[str]
    SendShortEmail: Optional[bool]
    Type: Optional[str]
    UserId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Address=json_data.get("Address"),
            Blacklisted=json_data.get("Blacklisted"),
            CountryCode=json_data.get("CountryCode"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            Label=json_data.get("Label"),
            SendShortEmail=json_data.get("SendShortEmail"),
            Type=json_data.get("Type"),
            UserId=json_data.get("UserId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


