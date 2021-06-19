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
    AccessibilityErrorRedirectUrl: Optional[str]
    AccessibilityLoginRedirectUrl: Optional[str]
    AccessibilitySelfService: Optional[bool]
    AcsEndpoints: Optional[Sequence[str]]
    AppSettingsJson: Optional[str]
    AssertionSigned: Optional[bool]
    Audience: Optional[str]
    AuthnContextClassRef: Optional[str]
    AutoSubmitToolbar: Optional[bool]
    Certificate: Optional[str]
    DefaultRelayState: Optional[str]
    Destination: Optional[str]
    DigestAlgorithm: Optional[str]
    EntityKey: Optional[str]
    EntityUrl: Optional[str]
    Features: Optional[Sequence[str]]
    Groups: Optional[Sequence[str]]
    HideIos: Optional[bool]
    HideWeb: Optional[bool]
    HonorForceAuthn: Optional[bool]
    HttpPostBinding: Optional[str]
    HttpRedirectBinding: Optional[str]
    Id: Optional[str]
    IdpIssuer: Optional[str]
    KeyId: Optional[str]
    KeyName: Optional[str]
    KeyYearsValid: Optional[float]
    Label: Optional[str]
    Metadata: Optional[str]
    MetadataUrl: Optional[str]
    Name: Optional[str]
    PreconfiguredApp: Optional[str]
    Recipient: Optional[str]
    RequestCompressed: Optional[bool]
    ResponseSigned: Optional[bool]
    SignOnMode: Optional[str]
    SignatureAlgorithm: Optional[str]
    SingleLogoutCertificate: Optional[str]
    SingleLogoutIssuer: Optional[str]
    SingleLogoutUrl: Optional[str]
    SpIssuer: Optional[str]
    SsoUrl: Optional[str]
    Status: Optional[str]
    SubjectNameIdFormat: Optional[str]
    SubjectNameIdTemplate: Optional[str]
    UserNameTemplate: Optional[str]
    UserNameTemplateSuffix: Optional[str]
    UserNameTemplateType: Optional[str]
    AttributeStatements: Optional[Sequence["_AttributeStatementsDefinition"]]
    Users: Optional[Sequence["_UsersDefinition"]]

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
            AccessibilityErrorRedirectUrl=json_data.get("AccessibilityErrorRedirectUrl"),
            AccessibilityLoginRedirectUrl=json_data.get("AccessibilityLoginRedirectUrl"),
            AccessibilitySelfService=json_data.get("AccessibilitySelfService"),
            AcsEndpoints=json_data.get("AcsEndpoints"),
            AppSettingsJson=json_data.get("AppSettingsJson"),
            AssertionSigned=json_data.get("AssertionSigned"),
            Audience=json_data.get("Audience"),
            AuthnContextClassRef=json_data.get("AuthnContextClassRef"),
            AutoSubmitToolbar=json_data.get("AutoSubmitToolbar"),
            Certificate=json_data.get("Certificate"),
            DefaultRelayState=json_data.get("DefaultRelayState"),
            Destination=json_data.get("Destination"),
            DigestAlgorithm=json_data.get("DigestAlgorithm"),
            EntityKey=json_data.get("EntityKey"),
            EntityUrl=json_data.get("EntityUrl"),
            Features=json_data.get("Features"),
            Groups=json_data.get("Groups"),
            HideIos=json_data.get("HideIos"),
            HideWeb=json_data.get("HideWeb"),
            HonorForceAuthn=json_data.get("HonorForceAuthn"),
            HttpPostBinding=json_data.get("HttpPostBinding"),
            HttpRedirectBinding=json_data.get("HttpRedirectBinding"),
            Id=json_data.get("Id"),
            IdpIssuer=json_data.get("IdpIssuer"),
            KeyId=json_data.get("KeyId"),
            KeyName=json_data.get("KeyName"),
            KeyYearsValid=json_data.get("KeyYearsValid"),
            Label=json_data.get("Label"),
            Metadata=json_data.get("Metadata"),
            MetadataUrl=json_data.get("MetadataUrl"),
            Name=json_data.get("Name"),
            PreconfiguredApp=json_data.get("PreconfiguredApp"),
            Recipient=json_data.get("Recipient"),
            RequestCompressed=json_data.get("RequestCompressed"),
            ResponseSigned=json_data.get("ResponseSigned"),
            SignOnMode=json_data.get("SignOnMode"),
            SignatureAlgorithm=json_data.get("SignatureAlgorithm"),
            SingleLogoutCertificate=json_data.get("SingleLogoutCertificate"),
            SingleLogoutIssuer=json_data.get("SingleLogoutIssuer"),
            SingleLogoutUrl=json_data.get("SingleLogoutUrl"),
            SpIssuer=json_data.get("SpIssuer"),
            SsoUrl=json_data.get("SsoUrl"),
            Status=json_data.get("Status"),
            SubjectNameIdFormat=json_data.get("SubjectNameIdFormat"),
            SubjectNameIdTemplate=json_data.get("SubjectNameIdTemplate"),
            UserNameTemplate=json_data.get("UserNameTemplate"),
            UserNameTemplateSuffix=json_data.get("UserNameTemplateSuffix"),
            UserNameTemplateType=json_data.get("UserNameTemplateType"),
            AttributeStatements=deserialize_list(json_data.get("AttributeStatements"), AttributeStatementsDefinition),
            Users=deserialize_list(json_data.get("Users"), UsersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AttributeStatementsDefinition(BaseModel):
    FilterType: Optional[str]
    FilterValue: Optional[str]
    Name: Optional[str]
    Namespace: Optional[str]
    Type: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AttributeStatementsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttributeStatementsDefinition"]:
        if not json_data:
            return None
        return cls(
            FilterType=json_data.get("FilterType"),
            FilterValue=json_data.get("FilterValue"),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Type=json_data.get("Type"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttributeStatementsDefinition = AttributeStatementsDefinition


@dataclass
class UsersDefinition(BaseModel):
    Id: Optional[str]
    Password: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UsersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UsersDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Password=json_data.get("Password"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UsersDefinition = UsersDefinition


