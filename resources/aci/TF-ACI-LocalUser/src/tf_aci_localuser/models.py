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
    AccountStatus: Optional[str]
    Annotation: Optional[str]
    CertAttribute: Optional[str]
    ClearPwdHistory: Optional[str]
    Description: Optional[str]
    Email: Optional[str]
    Expiration: Optional[str]
    Expires: Optional[str]
    FirstName: Optional[str]
    Id: Optional[str]
    LastName: Optional[str]
    Name: Optional[str]
    NameAlias: Optional[str]
    Otpenable: Optional[str]
    Otpkey: Optional[str]
    Phone: Optional[str]
    Pwd: Optional[str]
    PwdLifeTime: Optional[str]
    PwdUpdateRequired: Optional[str]
    RbacString: Optional[str]
    UnixUserId: Optional[str]

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
            AccountStatus=json_data.get("AccountStatus"),
            Annotation=json_data.get("Annotation"),
            CertAttribute=json_data.get("CertAttribute"),
            ClearPwdHistory=json_data.get("ClearPwdHistory"),
            Description=json_data.get("Description"),
            Email=json_data.get("Email"),
            Expiration=json_data.get("Expiration"),
            Expires=json_data.get("Expires"),
            FirstName=json_data.get("FirstName"),
            Id=json_data.get("Id"),
            LastName=json_data.get("LastName"),
            Name=json_data.get("Name"),
            NameAlias=json_data.get("NameAlias"),
            Otpenable=json_data.get("Otpenable"),
            Otpkey=json_data.get("Otpkey"),
            Phone=json_data.get("Phone"),
            Pwd=json_data.get("Pwd"),
            PwdLifeTime=json_data.get("PwdLifeTime"),
            PwdUpdateRequired=json_data.get("PwdUpdateRequired"),
            RbacString=json_data.get("RbacString"),
            UnixUserId=json_data.get("UnixUserId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


