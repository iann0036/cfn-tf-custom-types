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
    AllowReadOnly: Optional[bool]
    CreationDate: Optional[str]
    ExternalAccountNumber: Optional[str]
    FullProtection: Optional[bool]
    IamSafe: Optional[Sequence["_IamSafeDefinition2"]]
    Id: Optional[str]
    IsFetchingSuspended: Optional[bool]
    Name: Optional[str]
    OrganizationalUnitId: Optional[str]
    Vendor: Optional[str]
    Credentials: Optional[Sequence["_CredentialsDefinition"]]
    NetSec: Optional[Sequence["_NetSecDefinition"]]

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
            AllowReadOnly=json_data.get("AllowReadOnly"),
            CreationDate=json_data.get("CreationDate"),
            ExternalAccountNumber=json_data.get("ExternalAccountNumber"),
            FullProtection=json_data.get("FullProtection"),
            IamSafe=deserialize_list(json_data.get("IamSafe"), IamSafeDefinition2),
            Id=json_data.get("Id"),
            IsFetchingSuspended=json_data.get("IsFetchingSuspended"),
            Name=json_data.get("Name"),
            OrganizationalUnitId=json_data.get("OrganizationalUnitId"),
            Vendor=json_data.get("Vendor"),
            Credentials=deserialize_list(json_data.get("Credentials"), CredentialsDefinition),
            NetSec=deserialize_list(json_data.get("NetSec"), NetSecDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IamSafeDefinition2(BaseModel):
    AwsGroupArn: Optional[str]
    AwsPolicyArn: Optional[str]
    Mode: Optional[str]
    RestrictedIamEntities: Optional[Sequence["_IamSafeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IamSafeDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IamSafeDefinition2"]:
        if not json_data:
            return None
        return cls(
            AwsGroupArn=json_data.get("AwsGroupArn"),
            AwsPolicyArn=json_data.get("AwsPolicyArn"),
            Mode=json_data.get("Mode"),
            RestrictedIamEntities=deserialize_list(json_data.get("RestrictedIamEntities"), IamSafeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IamSafeDefinition2 = IamSafeDefinition2


@dataclass
class IamSafeDefinition(BaseModel):
    RolesArns: Optional[Sequence[str]]
    UsersArns: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_IamSafeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IamSafeDefinition"]:
        if not json_data:
            return None
        return cls(
            RolesArns=json_data.get("RolesArns"),
            UsersArns=json_data.get("UsersArns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IamSafeDefinition = IamSafeDefinition


@dataclass
class CredentialsDefinition(BaseModel):
    ApiKey: Optional[str]
    Arn: Optional[str]
    IamUser: Optional[str]
    Secret: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CredentialsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CredentialsDefinition"]:
        if not json_data:
            return None
        return cls(
            ApiKey=json_data.get("ApiKey"),
            Arn=json_data.get("Arn"),
            IamUser=json_data.get("IamUser"),
            Secret=json_data.get("Secret"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CredentialsDefinition = CredentialsDefinition


@dataclass
class NetSecDefinition(BaseModel):
    Regions: Optional[Sequence["_RegionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NetSecDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetSecDefinition"]:
        if not json_data:
            return None
        return cls(
            Regions=deserialize_list(json_data.get("Regions"), RegionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetSecDefinition = NetSecDefinition


@dataclass
class RegionsDefinition(BaseModel):
    NewGroupBehavior: Optional[str]
    Region: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RegionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RegionsDefinition"]:
        if not json_data:
            return None
        return cls(
            NewGroupBehavior=json_data.get("NewGroupBehavior"),
            Region=json_data.get("Region"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RegionsDefinition = RegionsDefinition


