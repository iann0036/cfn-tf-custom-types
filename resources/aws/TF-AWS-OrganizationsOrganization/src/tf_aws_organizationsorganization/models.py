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
    Accounts: Optional[Sequence["_AccountsDefinition"]]
    Arn: Optional[str]
    AwsServiceAccessPrincipals: Optional[Sequence[str]]
    EnabledPolicyTypes: Optional[Sequence[str]]
    FeatureSet: Optional[str]
    Id: Optional[str]
    MasterAccountArn: Optional[str]
    MasterAccountEmail: Optional[str]
    MasterAccountId: Optional[str]
    NonMasterAccounts: Optional[Sequence["_NonMasterAccountsDefinition"]]
    Roots: Optional[Sequence["_RootsDefinition2"]]

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
            Accounts=deserialize_list(json_data.get("Accounts"), AccountsDefinition),
            Arn=json_data.get("Arn"),
            AwsServiceAccessPrincipals=json_data.get("AwsServiceAccessPrincipals"),
            EnabledPolicyTypes=json_data.get("EnabledPolicyTypes"),
            FeatureSet=json_data.get("FeatureSet"),
            Id=json_data.get("Id"),
            MasterAccountArn=json_data.get("MasterAccountArn"),
            MasterAccountEmail=json_data.get("MasterAccountEmail"),
            MasterAccountId=json_data.get("MasterAccountId"),
            NonMasterAccounts=deserialize_list(json_data.get("NonMasterAccounts"), NonMasterAccountsDefinition),
            Roots=deserialize_list(json_data.get("Roots"), RootsDefinition2),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AccountsDefinition(BaseModel):
    Arn: Optional[str]
    Email: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccountsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccountsDefinition"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
            Email=json_data.get("Email"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccountsDefinition = AccountsDefinition


@dataclass
class NonMasterAccountsDefinition(BaseModel):
    Arn: Optional[str]
    Email: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NonMasterAccountsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NonMasterAccountsDefinition"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
            Email=json_data.get("Email"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NonMasterAccountsDefinition = NonMasterAccountsDefinition


@dataclass
class RootsDefinition2(BaseModel):
    Arn: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    PolicyTypes: Optional[Sequence["_RootsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RootsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RootsDefinition2"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PolicyTypes=deserialize_list(json_data.get("PolicyTypes"), RootsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RootsDefinition2 = RootsDefinition2


@dataclass
class RootsDefinition(BaseModel):
    Status: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RootsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RootsDefinition"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RootsDefinition = RootsDefinition


