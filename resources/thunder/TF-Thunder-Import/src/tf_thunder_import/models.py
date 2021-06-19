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
    Aflex: Optional[str]
    AuthJwks: Optional[str]
    AuthPortal: Optional[str]
    AuthPortalImage: Optional[str]
    BwList: Optional[str]
    CaCert: Optional[str]
    CertificateType: Optional[str]
    ClassList: Optional[str]
    ClassListConvert: Optional[str]
    ClassListType: Optional[str]
    CloudConfig: Optional[str]
    CloudCreds: Optional[str]
    DnssecDnskey: Optional[str]
    DnssecDs: Optional[str]
    FileInspectionBwList: Optional[str]
    GeoLocation: Optional[str]
    GlmCert: Optional[str]
    GlmLicense: Optional[str]
    Id: Optional[str]
    IpMapList: Optional[str]
    LocalUriFile: Optional[str]
    Lw4o6: Optional[str]
    Overwrite: Optional[float]
    Password: Optional[str]
    PfxPassword: Optional[str]
    Policy: Optional[str]
    RemoteFile: Optional[str]
    Secured: Optional[float]
    SslCert: Optional[str]
    SslCertKey: Optional[str]
    SslCrl: Optional[str]
    SslKey: Optional[str]
    StoreName: Optional[str]
    Terminal: Optional[float]
    ThalesKmdata: Optional[str]
    ThalesSecworld: Optional[str]
    UsbLicense: Optional[str]
    UseMgmtPort: Optional[float]
    UserTag: Optional[str]
    WebCategoryLicense: Optional[str]
    Wsdl: Optional[str]
    XmlSchema: Optional[str]
    AuthSamlIdp: Optional[Sequence["_AuthSamlIdpDefinition"]]
    HealthExternal: Optional[Sequence["_HealthExternalDefinition"]]
    HealthPostfile: Optional[Sequence["_HealthPostfileDefinition"]]
    Store: Optional[Sequence["_StoreDefinition"]]
    ToDevice: Optional[Sequence["_ToDeviceDefinition"]]

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
            Aflex=json_data.get("Aflex"),
            AuthJwks=json_data.get("AuthJwks"),
            AuthPortal=json_data.get("AuthPortal"),
            AuthPortalImage=json_data.get("AuthPortalImage"),
            BwList=json_data.get("BwList"),
            CaCert=json_data.get("CaCert"),
            CertificateType=json_data.get("CertificateType"),
            ClassList=json_data.get("ClassList"),
            ClassListConvert=json_data.get("ClassListConvert"),
            ClassListType=json_data.get("ClassListType"),
            CloudConfig=json_data.get("CloudConfig"),
            CloudCreds=json_data.get("CloudCreds"),
            DnssecDnskey=json_data.get("DnssecDnskey"),
            DnssecDs=json_data.get("DnssecDs"),
            FileInspectionBwList=json_data.get("FileInspectionBwList"),
            GeoLocation=json_data.get("GeoLocation"),
            GlmCert=json_data.get("GlmCert"),
            GlmLicense=json_data.get("GlmLicense"),
            Id=json_data.get("Id"),
            IpMapList=json_data.get("IpMapList"),
            LocalUriFile=json_data.get("LocalUriFile"),
            Lw4o6=json_data.get("Lw4o6"),
            Overwrite=json_data.get("Overwrite"),
            Password=json_data.get("Password"),
            PfxPassword=json_data.get("PfxPassword"),
            Policy=json_data.get("Policy"),
            RemoteFile=json_data.get("RemoteFile"),
            Secured=json_data.get("Secured"),
            SslCert=json_data.get("SslCert"),
            SslCertKey=json_data.get("SslCertKey"),
            SslCrl=json_data.get("SslCrl"),
            SslKey=json_data.get("SslKey"),
            StoreName=json_data.get("StoreName"),
            Terminal=json_data.get("Terminal"),
            ThalesKmdata=json_data.get("ThalesKmdata"),
            ThalesSecworld=json_data.get("ThalesSecworld"),
            UsbLicense=json_data.get("UsbLicense"),
            UseMgmtPort=json_data.get("UseMgmtPort"),
            UserTag=json_data.get("UserTag"),
            WebCategoryLicense=json_data.get("WebCategoryLicense"),
            Wsdl=json_data.get("Wsdl"),
            XmlSchema=json_data.get("XmlSchema"),
            AuthSamlIdp=deserialize_list(json_data.get("AuthSamlIdp"), AuthSamlIdpDefinition),
            HealthExternal=deserialize_list(json_data.get("HealthExternal"), HealthExternalDefinition),
            HealthPostfile=deserialize_list(json_data.get("HealthPostfile"), HealthPostfileDefinition),
            Store=deserialize_list(json_data.get("Store"), StoreDefinition),
            ToDevice=deserialize_list(json_data.get("ToDevice"), ToDeviceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AuthSamlIdpDefinition(BaseModel):
    Overwrite: Optional[float]
    Password: Optional[str]
    RemoteFile: Optional[str]
    SamlIdpName: Optional[str]
    UseMgmtPort: Optional[float]
    VerifyXmlSignature: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AuthSamlIdpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthSamlIdpDefinition"]:
        if not json_data:
            return None
        return cls(
            Overwrite=json_data.get("Overwrite"),
            Password=json_data.get("Password"),
            RemoteFile=json_data.get("RemoteFile"),
            SamlIdpName=json_data.get("SamlIdpName"),
            UseMgmtPort=json_data.get("UseMgmtPort"),
            VerifyXmlSignature=json_data.get("VerifyXmlSignature"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthSamlIdpDefinition = AuthSamlIdpDefinition


@dataclass
class HealthExternalDefinition(BaseModel):
    Description: Optional[str]
    Externalfilename: Optional[str]
    Overwrite: Optional[float]
    Password: Optional[str]
    RemoteFile: Optional[str]
    UseMgmtPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HealthExternalDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthExternalDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Externalfilename=json_data.get("Externalfilename"),
            Overwrite=json_data.get("Overwrite"),
            Password=json_data.get("Password"),
            RemoteFile=json_data.get("RemoteFile"),
            UseMgmtPort=json_data.get("UseMgmtPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthExternalDefinition = HealthExternalDefinition


@dataclass
class HealthPostfileDefinition(BaseModel):
    Overwrite: Optional[float]
    Password: Optional[str]
    Postfilename: Optional[str]
    RemoteFile: Optional[str]
    UseMgmtPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HealthPostfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthPostfileDefinition"]:
        if not json_data:
            return None
        return cls(
            Overwrite=json_data.get("Overwrite"),
            Password=json_data.get("Password"),
            Postfilename=json_data.get("Postfilename"),
            RemoteFile=json_data.get("RemoteFile"),
            UseMgmtPort=json_data.get("UseMgmtPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthPostfileDefinition = HealthPostfileDefinition


@dataclass
class StoreDefinition(BaseModel):
    Create: Optional[float]
    Delete: Optional[float]
    Name: Optional[str]
    RemoteFile: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StoreDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StoreDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Name=json_data.get("Name"),
            RemoteFile=json_data.get("RemoteFile"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StoreDefinition = StoreDefinition


@dataclass
class ToDeviceDefinition(BaseModel):
    Device: Optional[float]
    GlmCert: Optional[str]
    GlmLicense: Optional[str]
    Overwrite: Optional[float]
    RemoteFile: Optional[str]
    UseMgmtPort: Optional[float]
    WebCategoryLicense: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ToDeviceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ToDeviceDefinition"]:
        if not json_data:
            return None
        return cls(
            Device=json_data.get("Device"),
            GlmCert=json_data.get("GlmCert"),
            GlmLicense=json_data.get("GlmLicense"),
            Overwrite=json_data.get("Overwrite"),
            RemoteFile=json_data.get("RemoteFile"),
            UseMgmtPort=json_data.get("UseMgmtPort"),
            WebCategoryLicense=json_data.get("WebCategoryLicense"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ToDeviceDefinition = ToDeviceDefinition


