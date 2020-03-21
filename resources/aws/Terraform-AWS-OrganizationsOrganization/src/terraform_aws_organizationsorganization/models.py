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
    Accounts: Optional[Sequence["_Accounts"]]
    Arn: Optional[str]
    AwsServiceAccessPrincipals: Optional[Sequence[str]]
    EnabledPolicyTypes: Optional[Sequence[str]]
    FeatureSet: Optional[str]
    MasterAccountArn: Optional[str]
    MasterAccountEmail: Optional[str]
    MasterAccountId: Optional[str]
    NonMasterAccounts: Optional[Sequence["_NonMasterAccounts"]]
    Roots: Optional[Sequence["_Roots"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Accounts=json_data.get("Accounts"),
            Arn=json_data.get("Arn"),
            AwsServiceAccessPrincipals=json_data.get("AwsServiceAccessPrincipals"),
            EnabledPolicyTypes=json_data.get("EnabledPolicyTypes"),
            FeatureSet=json_data.get("FeatureSet"),
            MasterAccountArn=json_data.get("MasterAccountArn"),
            MasterAccountEmail=json_data.get("MasterAccountEmail"),
            MasterAccountId=json_data.get("MasterAccountId"),
            NonMasterAccounts=json_data.get("NonMasterAccounts"),
            Roots=json_data.get("Roots"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Accounts:
    Arn: Optional[str]
    Email: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Accounts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Accounts"]:
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
_Accounts = Accounts


@dataclass
class NonMasterAccounts:
    Arn: Optional[str]
    Email: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NonMasterAccounts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NonMasterAccounts"]:
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
_NonMasterAccounts = NonMasterAccounts


@dataclass
class Roots:
    Arn: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    PolicyTypes: Optional[Sequence["_PolicyTypes"]]

    @classmethod
    def _deserialize(
        cls: Type["_Roots"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Roots"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PolicyTypes=json_data.get("PolicyTypes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Roots = Roots


@dataclass
class PolicyTypes:
    Status: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PolicyTypes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PolicyTypes"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PolicyTypes = PolicyTypes


