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
    HardExpiry: Optional[bool]
    MaxLoginAttempts: Optional[float]
    MaxPasswordAge: Optional[float]
    MinimumPasswordLength: Optional[float]
    PasswordReusePrevention: Optional[float]
    RequireLowercaseCharacters: Optional[bool]
    RequireNumbers: Optional[bool]
    RequireSymbols: Optional[bool]
    RequireUppercaseCharacters: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            HardExpiry=json_data.get("HardExpiry"),
            MaxLoginAttempts=json_data.get("MaxLoginAttempts"),
            MaxPasswordAge=json_data.get("MaxPasswordAge"),
            MinimumPasswordLength=json_data.get("MinimumPasswordLength"),
            PasswordReusePrevention=json_data.get("PasswordReusePrevention"),
            RequireLowercaseCharacters=json_data.get("RequireLowercaseCharacters"),
            RequireNumbers=json_data.get("RequireNumbers"),
            RequireSymbols=json_data.get("RequireSymbols"),
            RequireUppercaseCharacters=json_data.get("RequireUppercaseCharacters"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


