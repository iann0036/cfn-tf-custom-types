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
    Address: Optional[str]
    AdminPassword: Optional[str]
    AdminType: Optional[str]
    AdminUsername: Optional[str]
    HttpsPort: Optional[float]
    Id: Optional[str]
    ListenPort: Optional[float]
    Name: Optional[str]
    RestApiAuth: Optional[str]
    SerialNumber: Optional[str]
    UploadPort: Optional[float]
    Vdomparam: Optional[str]

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
            Address=json_data.get("Address"),
            AdminPassword=json_data.get("AdminPassword"),
            AdminType=json_data.get("AdminType"),
            AdminUsername=json_data.get("AdminUsername"),
            HttpsPort=json_data.get("HttpsPort"),
            Id=json_data.get("Id"),
            ListenPort=json_data.get("ListenPort"),
            Name=json_data.get("Name"),
            RestApiAuth=json_data.get("RestApiAuth"),
            SerialNumber=json_data.get("SerialNumber"),
            UploadPort=json_data.get("UploadPort"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


