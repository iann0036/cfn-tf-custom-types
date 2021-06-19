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
    DomainController: Optional[str]
    DynamicSortSubtable: Optional[str]
    FssoAgentForNtlm: Optional[str]
    FssoGuest: Optional[str]
    Id: Optional[str]
    KerberosKeytab: Optional[str]
    Method: Optional[str]
    Name: Optional[str]
    NegotiateNtlm: Optional[str]
    RequireTfa: Optional[str]
    SshCa: Optional[str]
    Vdomparam: Optional[str]
    UserDatabase: Optional[Sequence["_UserDatabaseDefinition"]]

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
            DomainController=json_data.get("DomainController"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            FssoAgentForNtlm=json_data.get("FssoAgentForNtlm"),
            FssoGuest=json_data.get("FssoGuest"),
            Id=json_data.get("Id"),
            KerberosKeytab=json_data.get("KerberosKeytab"),
            Method=json_data.get("Method"),
            Name=json_data.get("Name"),
            NegotiateNtlm=json_data.get("NegotiateNtlm"),
            RequireTfa=json_data.get("RequireTfa"),
            SshCa=json_data.get("SshCa"),
            Vdomparam=json_data.get("Vdomparam"),
            UserDatabase=deserialize_list(json_data.get("UserDatabase"), UserDatabaseDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class UserDatabaseDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserDatabaseDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserDatabaseDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserDatabaseDefinition = UserDatabaseDefinition


