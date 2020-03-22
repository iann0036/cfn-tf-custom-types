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
    AliasAttributes: Optional[Sequence[str]]
    Arn: Optional[str]
    AutoVerifiedAttributes: Optional[Sequence[str]]
    CreationDate: Optional[str]
    EmailVerificationMessage: Optional[str]
    EmailVerificationSubject: Optional[str]
    Endpoint: Optional[str]
    Id: Optional[str]
    LastModifiedDate: Optional[str]
    MfaConfiguration: Optional[str]
    Name: Optional[str]
    SmsAuthenticationMessage: Optional[str]
    SmsVerificationMessage: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    UsernameAttributes: Optional[Sequence[str]]
    AdminCreateUserConfig: Optional[Sequence["_AdminCreateUserConfig"]]
    DeviceConfiguration: Optional[Sequence["_DeviceConfiguration"]]
    EmailConfiguration: Optional[Sequence["_EmailConfiguration"]]
    LambdaConfig: Optional[Sequence["_LambdaConfig"]]
    PasswordPolicy: Optional[Sequence["_PasswordPolicy"]]
    Schema: Optional[Sequence["_Schema"]]
    SmsConfiguration: Optional[Sequence["_SmsConfiguration"]]
    SoftwareTokenMfaConfiguration: Optional[Sequence["_SoftwareTokenMfaConfiguration"]]
    UserPoolAddOns: Optional[Sequence["_UserPoolAddOns"]]
    UsernameConfiguration: Optional[Sequence["_UsernameConfiguration"]]
    VerificationMessageTemplate: Optional[Sequence["_VerificationMessageTemplate"]]
    InviteMessageTemplate: Optional[Sequence["_InviteMessageTemplate"]]
    NumberAttributeConstraints: Optional[Sequence["_NumberAttributeConstraints"]]
    StringAttributeConstraints: Optional[Sequence["_StringAttributeConstraints"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AliasAttributes=json_data.get("AliasAttributes"),
            Arn=json_data.get("Arn"),
            AutoVerifiedAttributes=json_data.get("AutoVerifiedAttributes"),
            CreationDate=json_data.get("CreationDate"),
            EmailVerificationMessage=json_data.get("EmailVerificationMessage"),
            EmailVerificationSubject=json_data.get("EmailVerificationSubject"),
            Endpoint=json_data.get("Endpoint"),
            Id=json_data.get("Id"),
            LastModifiedDate=json_data.get("LastModifiedDate"),
            MfaConfiguration=json_data.get("MfaConfiguration"),
            Name=json_data.get("Name"),
            SmsAuthenticationMessage=json_data.get("SmsAuthenticationMessage"),
            SmsVerificationMessage=json_data.get("SmsVerificationMessage"),
            Tags=json_data.get("Tags"),
            UsernameAttributes=json_data.get("UsernameAttributes"),
            AdminCreateUserConfig=json_data.get("AdminCreateUserConfig"),
            DeviceConfiguration=json_data.get("DeviceConfiguration"),
            EmailConfiguration=json_data.get("EmailConfiguration"),
            LambdaConfig=json_data.get("LambdaConfig"),
            PasswordPolicy=json_data.get("PasswordPolicy"),
            Schema=json_data.get("Schema"),
            SmsConfiguration=json_data.get("SmsConfiguration"),
            SoftwareTokenMfaConfiguration=json_data.get("SoftwareTokenMfaConfiguration"),
            UserPoolAddOns=json_data.get("UserPoolAddOns"),
            UsernameConfiguration=json_data.get("UsernameConfiguration"),
            VerificationMessageTemplate=json_data.get("VerificationMessageTemplate"),
            InviteMessageTemplate=json_data.get("InviteMessageTemplate"),
            NumberAttributeConstraints=json_data.get("NumberAttributeConstraints"),
            StringAttributeConstraints=json_data.get("StringAttributeConstraints"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class AdminCreateUserConfig:
    AllowAdminCreateUserOnly: Optional[bool]
    UnusedAccountValidityDays: Optional[float]
    InviteMessageTemplate: Optional[Sequence["_InviteMessageTemplate"]]

    @classmethod
    def _deserialize(
        cls: Type["_AdminCreateUserConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdminCreateUserConfig"]:
        if not json_data:
            return None
        return cls(
            AllowAdminCreateUserOnly=json_data.get("AllowAdminCreateUserOnly"),
            UnusedAccountValidityDays=json_data.get("UnusedAccountValidityDays"),
            InviteMessageTemplate=json_data.get("InviteMessageTemplate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdminCreateUserConfig = AdminCreateUserConfig


@dataclass
class InviteMessageTemplate:
    EmailMessage: Optional[str]
    EmailSubject: Optional[str]
    SmsMessage: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InviteMessageTemplate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InviteMessageTemplate"]:
        if not json_data:
            return None
        return cls(
            EmailMessage=json_data.get("EmailMessage"),
            EmailSubject=json_data.get("EmailSubject"),
            SmsMessage=json_data.get("SmsMessage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InviteMessageTemplate = InviteMessageTemplate


@dataclass
class DeviceConfiguration:
    ChallengeRequiredOnNewDevice: Optional[bool]
    DeviceOnlyRememberedOnUserPrompt: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DeviceConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeviceConfiguration"]:
        if not json_data:
            return None
        return cls(
            ChallengeRequiredOnNewDevice=json_data.get("ChallengeRequiredOnNewDevice"),
            DeviceOnlyRememberedOnUserPrompt=json_data.get("DeviceOnlyRememberedOnUserPrompt"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeviceConfiguration = DeviceConfiguration


@dataclass
class EmailConfiguration:
    EmailSendingAccount: Optional[str]
    FromEmailAddress: Optional[str]
    ReplyToEmailAddress: Optional[str]
    SourceArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EmailConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EmailConfiguration"]:
        if not json_data:
            return None
        return cls(
            EmailSendingAccount=json_data.get("EmailSendingAccount"),
            FromEmailAddress=json_data.get("FromEmailAddress"),
            ReplyToEmailAddress=json_data.get("ReplyToEmailAddress"),
            SourceArn=json_data.get("SourceArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EmailConfiguration = EmailConfiguration


@dataclass
class LambdaConfig:
    CreateAuthChallenge: Optional[str]
    CustomMessage: Optional[str]
    DefineAuthChallenge: Optional[str]
    PostAuthentication: Optional[str]
    PostConfirmation: Optional[str]
    PreAuthentication: Optional[str]
    PreSignUp: Optional[str]
    PreTokenGeneration: Optional[str]
    UserMigration: Optional[str]
    VerifyAuthChallengeResponse: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaConfig"]:
        if not json_data:
            return None
        return cls(
            CreateAuthChallenge=json_data.get("CreateAuthChallenge"),
            CustomMessage=json_data.get("CustomMessage"),
            DefineAuthChallenge=json_data.get("DefineAuthChallenge"),
            PostAuthentication=json_data.get("PostAuthentication"),
            PostConfirmation=json_data.get("PostConfirmation"),
            PreAuthentication=json_data.get("PreAuthentication"),
            PreSignUp=json_data.get("PreSignUp"),
            PreTokenGeneration=json_data.get("PreTokenGeneration"),
            UserMigration=json_data.get("UserMigration"),
            VerifyAuthChallengeResponse=json_data.get("VerifyAuthChallengeResponse"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LambdaConfig = LambdaConfig


@dataclass
class PasswordPolicy:
    MinimumLength: Optional[float]
    RequireLowercase: Optional[bool]
    RequireNumbers: Optional[bool]
    RequireSymbols: Optional[bool]
    RequireUppercase: Optional[bool]
    TemporaryPasswordValidityDays: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PasswordPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PasswordPolicy"]:
        if not json_data:
            return None
        return cls(
            MinimumLength=json_data.get("MinimumLength"),
            RequireLowercase=json_data.get("RequireLowercase"),
            RequireNumbers=json_data.get("RequireNumbers"),
            RequireSymbols=json_data.get("RequireSymbols"),
            RequireUppercase=json_data.get("RequireUppercase"),
            TemporaryPasswordValidityDays=json_data.get("TemporaryPasswordValidityDays"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PasswordPolicy = PasswordPolicy


@dataclass
class Schema:
    AttributeDataType: Optional[str]
    DeveloperOnlyAttribute: Optional[bool]
    Mutable: Optional[bool]
    Name: Optional[str]
    Required: Optional[bool]
    NumberAttributeConstraints: Optional[Sequence["_NumberAttributeConstraints"]]
    StringAttributeConstraints: Optional[Sequence["_StringAttributeConstraints"]]

    @classmethod
    def _deserialize(
        cls: Type["_Schema"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Schema"]:
        if not json_data:
            return None
        return cls(
            AttributeDataType=json_data.get("AttributeDataType"),
            DeveloperOnlyAttribute=json_data.get("DeveloperOnlyAttribute"),
            Mutable=json_data.get("Mutable"),
            Name=json_data.get("Name"),
            Required=json_data.get("Required"),
            NumberAttributeConstraints=json_data.get("NumberAttributeConstraints"),
            StringAttributeConstraints=json_data.get("StringAttributeConstraints"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Schema = Schema


@dataclass
class NumberAttributeConstraints:
    MaxValue: Optional[str]
    MinValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NumberAttributeConstraints"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NumberAttributeConstraints"]:
        if not json_data:
            return None
        return cls(
            MaxValue=json_data.get("MaxValue"),
            MinValue=json_data.get("MinValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NumberAttributeConstraints = NumberAttributeConstraints


@dataclass
class StringAttributeConstraints:
    MaxLength: Optional[str]
    MinLength: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StringAttributeConstraints"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StringAttributeConstraints"]:
        if not json_data:
            return None
        return cls(
            MaxLength=json_data.get("MaxLength"),
            MinLength=json_data.get("MinLength"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StringAttributeConstraints = StringAttributeConstraints


@dataclass
class SmsConfiguration:
    ExternalId: Optional[str]
    SnsCallerArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SmsConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SmsConfiguration"]:
        if not json_data:
            return None
        return cls(
            ExternalId=json_data.get("ExternalId"),
            SnsCallerArn=json_data.get("SnsCallerArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SmsConfiguration = SmsConfiguration


@dataclass
class SoftwareTokenMfaConfiguration:
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SoftwareTokenMfaConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SoftwareTokenMfaConfiguration"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SoftwareTokenMfaConfiguration = SoftwareTokenMfaConfiguration


@dataclass
class UserPoolAddOns:
    AdvancedSecurityMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserPoolAddOns"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserPoolAddOns"]:
        if not json_data:
            return None
        return cls(
            AdvancedSecurityMode=json_data.get("AdvancedSecurityMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserPoolAddOns = UserPoolAddOns


@dataclass
class UsernameConfiguration:
    CaseSensitive: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_UsernameConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UsernameConfiguration"]:
        if not json_data:
            return None
        return cls(
            CaseSensitive=json_data.get("CaseSensitive"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UsernameConfiguration = UsernameConfiguration


@dataclass
class VerificationMessageTemplate:
    DefaultEmailOption: Optional[str]
    EmailMessage: Optional[str]
    EmailMessageByLink: Optional[str]
    EmailSubject: Optional[str]
    EmailSubjectByLink: Optional[str]
    SmsMessage: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VerificationMessageTemplate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VerificationMessageTemplate"]:
        if not json_data:
            return None
        return cls(
            DefaultEmailOption=json_data.get("DefaultEmailOption"),
            EmailMessage=json_data.get("EmailMessage"),
            EmailMessageByLink=json_data.get("EmailMessageByLink"),
            EmailSubject=json_data.get("EmailSubject"),
            EmailSubjectByLink=json_data.get("EmailSubjectByLink"),
            SmsMessage=json_data.get("SmsMessage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VerificationMessageTemplate = VerificationMessageTemplate


