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
    CurrentPassword: Optional[str]
    Id: Optional[str]
    Password: Optional[str]
    Telemetry: Optional[bool]
    TempToken: Optional[str]
    TempTokenId: Optional[str]
    Token: Optional[str]
    TokenId: Optional[str]
    TokenTtl: Optional[float]
    TokenUpdate: Optional[bool]
    UiDefaultLanding: Optional[str]
    Url: Optional[str]
    User: Optional[str]

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
            CurrentPassword=json_data.get("CurrentPassword"),
            Id=json_data.get("Id"),
            Password=json_data.get("Password"),
            Telemetry=json_data.get("Telemetry"),
            TempToken=json_data.get("TempToken"),
            TempTokenId=json_data.get("TempTokenId"),
            Token=json_data.get("Token"),
            TokenId=json_data.get("TokenId"),
            TokenTtl=json_data.get("TokenTtl"),
            TokenUpdate=json_data.get("TokenUpdate"),
            UiDefaultLanding=json_data.get("UiDefaultLanding"),
            Url=json_data.get("Url"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


