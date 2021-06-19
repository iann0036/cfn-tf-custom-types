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
    ApiUrl: Optional[str]
    HttpUrl: Optional[str]
    Id: Optional[str]
    OauthToken: Optional[str]
    OauthTokenId: Optional[str]
    Organization: Optional[str]
    PrivateKey: Optional[str]
    ServiceProvider: Optional[str]

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
            ApiUrl=json_data.get("ApiUrl"),
            HttpUrl=json_data.get("HttpUrl"),
            Id=json_data.get("Id"),
            OauthToken=json_data.get("OauthToken"),
            OauthTokenId=json_data.get("OauthTokenId"),
            Organization=json_data.get("Organization"),
            PrivateKey=json_data.get("PrivateKey"),
            ServiceProvider=json_data.get("ServiceProvider"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


