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
    ConsoleLogin: Optional[bool]
    CountryCode: Optional[str]
    Email: Optional[str]
    ForceDelete: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    NeedResetPassword: Optional[bool]
    Password: Optional[str]
    PhoneNum: Optional[str]
    Remark: Optional[str]
    SecretId: Optional[str]
    SecretKey: Optional[str]
    Uid: Optional[float]
    Uin: Optional[float]
    UseApi: Optional[bool]

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
            ConsoleLogin=json_data.get("ConsoleLogin"),
            CountryCode=json_data.get("CountryCode"),
            Email=json_data.get("Email"),
            ForceDelete=json_data.get("ForceDelete"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NeedResetPassword=json_data.get("NeedResetPassword"),
            Password=json_data.get("Password"),
            PhoneNum=json_data.get("PhoneNum"),
            Remark=json_data.get("Remark"),
            SecretId=json_data.get("SecretId"),
            SecretKey=json_data.get("SecretKey"),
            Uid=json_data.get("Uid"),
            Uin=json_data.get("Uin"),
            UseApi=json_data.get("UseApi"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


