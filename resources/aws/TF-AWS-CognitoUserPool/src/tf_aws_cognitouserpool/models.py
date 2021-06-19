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
    AliasAttributes: Optional[Sequence[str]]
    Arn: Optional[str]
    AutoVerifiedAttributes: Optional[Sequence[str]]
    CreationDate: Optional[str]
    CustomDomain: Optional[str]
    Domain: Optional[str]
    EmailVerificationMessage: Optional[str]
    EmailVerificationSubject: Optional[str]
    Endpoint: Optional[str]
    EstimatedNumberOfUsers: Optional[float]
    Id: Optional[str]
    LastModifiedDate: Optional[str]
    MfaConfiguration: Optional[str]
    Name: Optional[str]
    SmsAuthenticationMessage: Optional[str]
    SmsVerificationMessage: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    UsernameAttributes: Optional[Sequence[str]]
    AccountRecoverySetting: Optional[Sequence["_AccountRecoverySettingDefinition"]]
    AdminCreateUserConfig: Optional[Sequence["_AdminCreateUserConfigDefinition"]]
    DeviceConfiguration: Optional[Sequence["_DeviceConfigurationDefinition"]]
    EmailConfiguration: Optional[Sequence["_EmailConfigurationDefinition"]]
    LambdaConfig: Optional[Sequence["_LambdaConfigDefinition"]]
    PasswordPolicy: Optional[Sequence["_PasswordPolicyDefinition"]]
    Schema: Optional[Sequence["_SchemaDefinition"]]
    SmsConfiguration: Optional[Sequence["_SmsConfigurationDefinition"]]
    SoftwareTokenMfaConfiguration: Optional[Sequence["_SoftwareTokenMfaConfigurationDefinition"]]
    UserPoolAddOns: Optional[Sequence["_UserPoolAddOnsDefinition"]]
    UsernameConfiguration: Optional[Sequence["_UsernameConfigurationDefinition"]]
    VerificationMessageTemplate: Optional[Sequence["_VerificationMessageTemplateDefinition"]]

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
            AliasAttributes=json_data.get("AliasAttributes"),
            Arn=json_data.get("Arn"),
            AutoVerifiedAttributes=json_data.get("AutoVerifiedAttributes"),
            CreationDate=json_data.get("CreationDate"),
            CustomDomain=json_data.get("CustomDomain"),
            Domain=json_data.get("Domain"),
            EmailVerificationMessage=json_data.get("EmailVerificationMessage"),
            EmailVerificationSubject=json_data.get("EmailVerificationSubject"),
            Endpoint=json_data.get("Endpoint"),
            EstimatedNumberOfUsers=json_data.get("EstimatedNumberOfUsers"),
            Id=json_data.get("Id"),
            LastModifiedDate=json_data.get("LastModifiedDate"),
            MfaConfiguration=json_data.get("MfaConfiguration"),
            Name=json_data.get("Name"),
            SmsAuthenticationMessage=json_data.get("SmsAuthenticationMessage"),
            SmsVerificationMessage=json_data.get("SmsVerificationMessage"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            UsernameAttributes=json_data.get("UsernameAttributes"),
            AccountRecoverySetting=deserialize_list(json_data.get("AccountRecoverySetting"), AccountRecoverySettingDefinition),
            AdminCreateUserConfig=deserialize_list(json_data.get("AdminCreateUserConfig"), AdminCreateUserConfigDefinition),
            DeviceConfiguration=deserialize_list(json_data.get("DeviceConfiguration"), DeviceConfigurationDefinition),
            EmailConfiguration=deserialize_list(json_data.get("EmailConfiguration"), EmailConfigurationDefinition),
            LambdaConfig=deserialize_list(json_data.get("LambdaConfig"), LambdaConfigDefinition),
            PasswordPolicy=deserialize_list(json_data.get("PasswordPolicy"), PasswordPolicyDefinition),
            Schema=deserialize_list(json_data.get("Schema"), SchemaDefinition),
            SmsConfiguration=deserialize_list(json_data.get("SmsConfiguration"), SmsConfigurationDefinition),
            SoftwareTokenMfaConfiguration=deserialize_list(json_data.get("SoftwareTokenMfaConfiguration"), SoftwareTokenMfaConfigurationDefinition),
            UserPoolAddOns=deserialize_list(json_data.get("UserPoolAddOns"), UserPoolAddOnsDefinition),
            UsernameConfiguration=deserialize_list(json_data.get("UsernameConfiguration"), UsernameConfigurationDefinition),
            VerificationMessageTemplate=deserialize_list(json_data.get("VerificationMessageTemplate"), VerificationMessageTemplateDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class AccountRecoverySettingDefinition(BaseModel):
    RecoveryMechanism: Optional[Sequence["_RecoveryMechanismDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AccountRecoverySettingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccountRecoverySettingDefinition"]:
        if not json_data:
            return None
        return cls(
            RecoveryMechanism=deserialize_list(json_data.get("RecoveryMechanism"), RecoveryMechanismDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccountRecoverySettingDefinition = AccountRecoverySettingDefinition


@dataclass
class RecoveryMechanismDefinition(BaseModel):
    Name: Optional[str]
    Priority: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RecoveryMechanismDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecoveryMechanismDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecoveryMechanismDefinition = RecoveryMechanismDefinition


@dataclass
class AdminCreateUserConfigDefinition(BaseModel):
    AllowAdminCreateUserOnly: Optional[bool]
    InviteMessageTemplate: Optional[Sequence["_InviteMessageTemplateDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AdminCreateUserConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdminCreateUserConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowAdminCreateUserOnly=json_data.get("AllowAdminCreateUserOnly"),
            InviteMessageTemplate=deserialize_list(json_data.get("InviteMessageTemplate"), InviteMessageTemplateDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdminCreateUserConfigDefinition = AdminCreateUserConfigDefinition


@dataclass
class InviteMessageTemplateDefinition(BaseModel):
    EmailMessage: Optional[str]
    EmailSubject: Optional[str]
    SmsMessage: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InviteMessageTemplateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InviteMessageTemplateDefinition"]:
        if not json_data:
            return None
        return cls(
            EmailMessage=json_data.get("EmailMessage"),
            EmailSubject=json_data.get("EmailSubject"),
            SmsMessage=json_data.get("SmsMessage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InviteMessageTemplateDefinition = InviteMessageTemplateDefinition


@dataclass
class DeviceConfigurationDefinition(BaseModel):
    ChallengeRequiredOnNewDevice: Optional[bool]
    DeviceOnlyRememberedOnUserPrompt: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DeviceConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeviceConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            ChallengeRequiredOnNewDevice=json_data.get("ChallengeRequiredOnNewDevice"),
            DeviceOnlyRememberedOnUserPrompt=json_data.get("DeviceOnlyRememberedOnUserPrompt"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeviceConfigurationDefinition = DeviceConfigurationDefinition


@dataclass
class EmailConfigurationDefinition(BaseModel):
    ConfigurationSet: Optional[str]
    EmailSendingAccount: Optional[str]
    FromEmailAddress: Optional[str]
    ReplyToEmailAddress: Optional[str]
    SourceArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EmailConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EmailConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            ConfigurationSet=json_data.get("ConfigurationSet"),
            EmailSendingAccount=json_data.get("EmailSendingAccount"),
            FromEmailAddress=json_data.get("FromEmailAddress"),
            ReplyToEmailAddress=json_data.get("ReplyToEmailAddress"),
            SourceArn=json_data.get("SourceArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EmailConfigurationDefinition = EmailConfigurationDefinition


@dataclass
class LambdaConfigDefinition(BaseModel):
    CreateAuthChallenge: Optional[str]
    CustomMessage: Optional[str]
    DefineAuthChallenge: Optional[str]
    KmsKeyId: Optional[str]
    PostAuthentication: Optional[str]
    PostConfirmation: Optional[str]
    PreAuthentication: Optional[str]
    PreSignUp: Optional[str]
    PreTokenGeneration: Optional[str]
    UserMigration: Optional[str]
    VerifyAuthChallengeResponse: Optional[str]
    CustomEmailSender: Optional[Sequence["_CustomEmailSenderDefinition"]]
    CustomSmsSender: Optional[Sequence["_CustomSmsSenderDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            CreateAuthChallenge=json_data.get("CreateAuthChallenge"),
            CustomMessage=json_data.get("CustomMessage"),
            DefineAuthChallenge=json_data.get("DefineAuthChallenge"),
            KmsKeyId=json_data.get("KmsKeyId"),
            PostAuthentication=json_data.get("PostAuthentication"),
            PostConfirmation=json_data.get("PostConfirmation"),
            PreAuthentication=json_data.get("PreAuthentication"),
            PreSignUp=json_data.get("PreSignUp"),
            PreTokenGeneration=json_data.get("PreTokenGeneration"),
            UserMigration=json_data.get("UserMigration"),
            VerifyAuthChallengeResponse=json_data.get("VerifyAuthChallengeResponse"),
            CustomEmailSender=deserialize_list(json_data.get("CustomEmailSender"), CustomEmailSenderDefinition),
            CustomSmsSender=deserialize_list(json_data.get("CustomSmsSender"), CustomSmsSenderDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LambdaConfigDefinition = LambdaConfigDefinition


@dataclass
class CustomEmailSenderDefinition(BaseModel):
    LambdaArn: Optional[str]
    LambdaVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomEmailSenderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomEmailSenderDefinition"]:
        if not json_data:
            return None
        return cls(
            LambdaArn=json_data.get("LambdaArn"),
            LambdaVersion=json_data.get("LambdaVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomEmailSenderDefinition = CustomEmailSenderDefinition


@dataclass
class CustomSmsSenderDefinition(BaseModel):
    LambdaArn: Optional[str]
    LambdaVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomSmsSenderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomSmsSenderDefinition"]:
        if not json_data:
            return None
        return cls(
            LambdaArn=json_data.get("LambdaArn"),
            LambdaVersion=json_data.get("LambdaVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomSmsSenderDefinition = CustomSmsSenderDefinition


@dataclass
class PasswordPolicyDefinition(BaseModel):
    MinimumLength: Optional[float]
    RequireLowercase: Optional[bool]
    RequireNumbers: Optional[bool]
    RequireSymbols: Optional[bool]
    RequireUppercase: Optional[bool]
    TemporaryPasswordValidityDays: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PasswordPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PasswordPolicyDefinition"]:
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
_PasswordPolicyDefinition = PasswordPolicyDefinition


@dataclass
class SchemaDefinition(BaseModel):
    AttributeDataType: Optional[str]
    DeveloperOnlyAttribute: Optional[bool]
    Mutable: Optional[bool]
    Name: Optional[str]
    Required: Optional[bool]
    NumberAttributeConstraints: Optional[Sequence["_NumberAttributeConstraintsDefinition"]]
    StringAttributeConstraints: Optional[Sequence["_StringAttributeConstraintsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SchemaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SchemaDefinition"]:
        if not json_data:
            return None
        return cls(
            AttributeDataType=json_data.get("AttributeDataType"),
            DeveloperOnlyAttribute=json_data.get("DeveloperOnlyAttribute"),
            Mutable=json_data.get("Mutable"),
            Name=json_data.get("Name"),
            Required=json_data.get("Required"),
            NumberAttributeConstraints=deserialize_list(json_data.get("NumberAttributeConstraints"), NumberAttributeConstraintsDefinition),
            StringAttributeConstraints=deserialize_list(json_data.get("StringAttributeConstraints"), StringAttributeConstraintsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SchemaDefinition = SchemaDefinition


@dataclass
class NumberAttributeConstraintsDefinition(BaseModel):
    MaxValue: Optional[str]
    MinValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NumberAttributeConstraintsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NumberAttributeConstraintsDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxValue=json_data.get("MaxValue"),
            MinValue=json_data.get("MinValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NumberAttributeConstraintsDefinition = NumberAttributeConstraintsDefinition


@dataclass
class StringAttributeConstraintsDefinition(BaseModel):
    MaxLength: Optional[str]
    MinLength: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StringAttributeConstraintsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StringAttributeConstraintsDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxLength=json_data.get("MaxLength"),
            MinLength=json_data.get("MinLength"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StringAttributeConstraintsDefinition = StringAttributeConstraintsDefinition


@dataclass
class SmsConfigurationDefinition(BaseModel):
    ExternalId: Optional[str]
    SnsCallerArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SmsConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SmsConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            ExternalId=json_data.get("ExternalId"),
            SnsCallerArn=json_data.get("SnsCallerArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SmsConfigurationDefinition = SmsConfigurationDefinition


@dataclass
class SoftwareTokenMfaConfigurationDefinition(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SoftwareTokenMfaConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SoftwareTokenMfaConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SoftwareTokenMfaConfigurationDefinition = SoftwareTokenMfaConfigurationDefinition


@dataclass
class UserPoolAddOnsDefinition(BaseModel):
    AdvancedSecurityMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserPoolAddOnsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserPoolAddOnsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdvancedSecurityMode=json_data.get("AdvancedSecurityMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserPoolAddOnsDefinition = UserPoolAddOnsDefinition


@dataclass
class UsernameConfigurationDefinition(BaseModel):
    CaseSensitive: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_UsernameConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UsernameConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            CaseSensitive=json_data.get("CaseSensitive"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UsernameConfigurationDefinition = UsernameConfigurationDefinition


@dataclass
class VerificationMessageTemplateDefinition(BaseModel):
    DefaultEmailOption: Optional[str]
    EmailMessage: Optional[str]
    EmailMessageByLink: Optional[str]
    EmailSubject: Optional[str]
    EmailSubjectByLink: Optional[str]
    SmsMessage: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VerificationMessageTemplateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VerificationMessageTemplateDefinition"]:
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
_VerificationMessageTemplateDefinition = VerificationMessageTemplateDefinition


