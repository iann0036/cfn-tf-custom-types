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
    CookieMode: Optional[str]
    CookieName: Optional[str]
    EdgeGateway: Optional[str]
    EnablePoolSideSsl: Optional[bool]
    EnableSslPassthrough: Optional[bool]
    Expiration: Optional[float]
    HttpRedirectUrl: Optional[str]
    Id: Optional[str]
    InsertXForwardedHttpHeader: Optional[bool]
    Name: Optional[str]
    Org: Optional[str]
    PersistenceMechanism: Optional[str]
    Type: Optional[str]
    Vdc: Optional[str]

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
            CookieMode=json_data.get("CookieMode"),
            CookieName=json_data.get("CookieName"),
            EdgeGateway=json_data.get("EdgeGateway"),
            EnablePoolSideSsl=json_data.get("EnablePoolSideSsl"),
            EnableSslPassthrough=json_data.get("EnableSslPassthrough"),
            Expiration=json_data.get("Expiration"),
            HttpRedirectUrl=json_data.get("HttpRedirectUrl"),
            Id=json_data.get("Id"),
            InsertXForwardedHttpHeader=json_data.get("InsertXForwardedHttpHeader"),
            Name=json_data.get("Name"),
            Org=json_data.get("Org"),
            PersistenceMechanism=json_data.get("PersistenceMechanism"),
            Type=json_data.get("Type"),
            Vdc=json_data.get("Vdc"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


