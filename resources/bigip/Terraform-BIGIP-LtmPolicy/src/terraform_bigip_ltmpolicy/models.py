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
    Controls: Optional[Sequence[str]]
    Name: Optional[str]
    PublishedCopy: Optional[str]
    Requires: Optional[Sequence[str]]
    Strategy: Optional[str]
    Rule: Optional[Sequence["_Rule"]]
    Action: Optional[Sequence["_Action"]]
    Condition: Optional[Sequence["_Condition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Controls=json_data.get("Controls"),
            Name=json_data.get("Name"),
            PublishedCopy=json_data.get("PublishedCopy"),
            Requires=json_data.get("Requires"),
            Strategy=json_data.get("Strategy"),
            Rule=json_data.get("Rule"),
            Action=json_data.get("Action"),
            Condition=json_data.get("Condition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Rule:
    Name: Optional[str]
    Action: Optional[Sequence["_Action"]]
    Condition: Optional[Sequence["_Condition"]]

    @classmethod
    def _deserialize(
        cls: Type["_Rule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Rule"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Action=json_data.get("Action"),
            Condition=json_data.get("Condition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Rule = Rule


@dataclass
class Action:
    AppService: Optional[str]
    Application: Optional[str]
    Asm: Optional[bool]
    Avr: Optional[bool]
    Cache: Optional[bool]
    Carp: Optional[bool]
    Category: Optional[str]
    Classify: Optional[bool]
    ClonePool: Optional[str]
    Code: Optional[float]
    Compress: Optional[bool]
    Content: Optional[str]
    CookieHash: Optional[bool]
    CookieInsert: Optional[bool]
    CookiePassive: Optional[bool]
    CookieRewrite: Optional[bool]
    Decompress: Optional[bool]
    Defer: Optional[bool]
    DestinationAddress: Optional[bool]
    Disable: Optional[bool]
    Domain: Optional[str]
    Enable: Optional[bool]
    Expiry: Optional[str]
    ExpirySecs: Optional[float]
    Expression: Optional[str]
    Extension: Optional[str]
    Facility: Optional[str]
    Forward: Optional[bool]
    FromProfile: Optional[str]
    Hash: Optional[bool]
    Host: Optional[str]
    Http: Optional[bool]
    HttpBasicAuth: Optional[bool]
    HttpCookie: Optional[bool]
    HttpHeader: Optional[bool]
    HttpHost: Optional[bool]
    HttpReferer: Optional[bool]
    HttpReply: Optional[bool]
    HttpSetCookie: Optional[bool]
    HttpUri: Optional[bool]
    Ifile: Optional[str]
    Insert: Optional[bool]
    InternalVirtual: Optional[str]
    IpAddress: Optional[str]
    Key: Optional[str]
    L7dos: Optional[bool]
    Length: Optional[float]
    Location: Optional[str]
    Log: Optional[bool]
    LtmPolicy: Optional[bool]
    Member: Optional[str]
    Message: Optional[str]
    Netmask: Optional[str]
    Nexthop: Optional[str]
    Node: Optional[str]
    Offset: Optional[float]
    Path: Optional[str]
    Pem: Optional[bool]
    Persist: Optional[bool]
    Pin: Optional[bool]
    Policy: Optional[str]
    Pool: Optional[str]
    Port: Optional[float]
    Priority: Optional[str]
    Profile: Optional[str]
    Protocol: Optional[str]
    QueryString: Optional[str]
    Rateclass: Optional[str]
    Redirect: Optional[bool]
    Remove: Optional[bool]
    Replace: Optional[bool]
    Request: Optional[bool]
    RequestAdapt: Optional[bool]
    Reset: Optional[bool]
    Response: Optional[bool]
    ResponseAdapt: Optional[bool]
    Scheme: Optional[str]
    Script: Optional[str]
    Select: Optional[bool]
    ServerSsl: Optional[bool]
    SetVariable: Optional[bool]
    Snat: Optional[str]
    Snatpool: Optional[str]
    SourceAddress: Optional[bool]
    SslClientHello: Optional[bool]
    SslServerHandshake: Optional[bool]
    SslServerHello: Optional[bool]
    SslSessionId: Optional[bool]
    Status: Optional[float]
    Tcl: Optional[bool]
    TcpNagle: Optional[bool]
    Text: Optional[str]
    Timeout: Optional[float]
    TmName: Optional[str]
    Uie: Optional[bool]
    Universal: Optional[bool]
    Value: Optional[str]
    Virtual: Optional[str]
    Vlan: Optional[str]
    VlanId: Optional[float]
    Wam: Optional[bool]
    Write: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Action"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Action"]:
        if not json_data:
            return None
        return cls(
            AppService=json_data.get("AppService"),
            Application=json_data.get("Application"),
            Asm=json_data.get("Asm"),
            Avr=json_data.get("Avr"),
            Cache=json_data.get("Cache"),
            Carp=json_data.get("Carp"),
            Category=json_data.get("Category"),
            Classify=json_data.get("Classify"),
            ClonePool=json_data.get("ClonePool"),
            Code=json_data.get("Code"),
            Compress=json_data.get("Compress"),
            Content=json_data.get("Content"),
            CookieHash=json_data.get("CookieHash"),
            CookieInsert=json_data.get("CookieInsert"),
            CookiePassive=json_data.get("CookiePassive"),
            CookieRewrite=json_data.get("CookieRewrite"),
            Decompress=json_data.get("Decompress"),
            Defer=json_data.get("Defer"),
            DestinationAddress=json_data.get("DestinationAddress"),
            Disable=json_data.get("Disable"),
            Domain=json_data.get("Domain"),
            Enable=json_data.get("Enable"),
            Expiry=json_data.get("Expiry"),
            ExpirySecs=json_data.get("ExpirySecs"),
            Expression=json_data.get("Expression"),
            Extension=json_data.get("Extension"),
            Facility=json_data.get("Facility"),
            Forward=json_data.get("Forward"),
            FromProfile=json_data.get("FromProfile"),
            Hash=json_data.get("Hash"),
            Host=json_data.get("Host"),
            Http=json_data.get("Http"),
            HttpBasicAuth=json_data.get("HttpBasicAuth"),
            HttpCookie=json_data.get("HttpCookie"),
            HttpHeader=json_data.get("HttpHeader"),
            HttpHost=json_data.get("HttpHost"),
            HttpReferer=json_data.get("HttpReferer"),
            HttpReply=json_data.get("HttpReply"),
            HttpSetCookie=json_data.get("HttpSetCookie"),
            HttpUri=json_data.get("HttpUri"),
            Ifile=json_data.get("Ifile"),
            Insert=json_data.get("Insert"),
            InternalVirtual=json_data.get("InternalVirtual"),
            IpAddress=json_data.get("IpAddress"),
            Key=json_data.get("Key"),
            L7dos=json_data.get("L7dos"),
            Length=json_data.get("Length"),
            Location=json_data.get("Location"),
            Log=json_data.get("Log"),
            LtmPolicy=json_data.get("LtmPolicy"),
            Member=json_data.get("Member"),
            Message=json_data.get("Message"),
            Netmask=json_data.get("Netmask"),
            Nexthop=json_data.get("Nexthop"),
            Node=json_data.get("Node"),
            Offset=json_data.get("Offset"),
            Path=json_data.get("Path"),
            Pem=json_data.get("Pem"),
            Persist=json_data.get("Persist"),
            Pin=json_data.get("Pin"),
            Policy=json_data.get("Policy"),
            Pool=json_data.get("Pool"),
            Port=json_data.get("Port"),
            Priority=json_data.get("Priority"),
            Profile=json_data.get("Profile"),
            Protocol=json_data.get("Protocol"),
            QueryString=json_data.get("QueryString"),
            Rateclass=json_data.get("Rateclass"),
            Redirect=json_data.get("Redirect"),
            Remove=json_data.get("Remove"),
            Replace=json_data.get("Replace"),
            Request=json_data.get("Request"),
            RequestAdapt=json_data.get("RequestAdapt"),
            Reset=json_data.get("Reset"),
            Response=json_data.get("Response"),
            ResponseAdapt=json_data.get("ResponseAdapt"),
            Scheme=json_data.get("Scheme"),
            Script=json_data.get("Script"),
            Select=json_data.get("Select"),
            ServerSsl=json_data.get("ServerSsl"),
            SetVariable=json_data.get("SetVariable"),
            Snat=json_data.get("Snat"),
            Snatpool=json_data.get("Snatpool"),
            SourceAddress=json_data.get("SourceAddress"),
            SslClientHello=json_data.get("SslClientHello"),
            SslServerHandshake=json_data.get("SslServerHandshake"),
            SslServerHello=json_data.get("SslServerHello"),
            SslSessionId=json_data.get("SslSessionId"),
            Status=json_data.get("Status"),
            Tcl=json_data.get("Tcl"),
            TcpNagle=json_data.get("TcpNagle"),
            Text=json_data.get("Text"),
            Timeout=json_data.get("Timeout"),
            TmName=json_data.get("TmName"),
            Uie=json_data.get("Uie"),
            Universal=json_data.get("Universal"),
            Value=json_data.get("Value"),
            Virtual=json_data.get("Virtual"),
            Vlan=json_data.get("Vlan"),
            VlanId=json_data.get("VlanId"),
            Wam=json_data.get("Wam"),
            Write=json_data.get("Write"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Action = Action


@dataclass
class Condition:
    Address: Optional[bool]
    All: Optional[bool]
    AppService: Optional[str]
    BrowserType: Optional[bool]
    BrowserVersion: Optional[bool]
    CaseInsensitive: Optional[bool]
    CaseSensitive: Optional[bool]
    Cipher: Optional[bool]
    CipherBits: Optional[bool]
    ClientSsl: Optional[bool]
    Code: Optional[bool]
    CommonName: Optional[bool]
    Contains: Optional[bool]
    Continent: Optional[bool]
    CountryCode: Optional[bool]
    CountryName: Optional[bool]
    CpuUsage: Optional[bool]
    DeviceMake: Optional[bool]
    DeviceModel: Optional[bool]
    Domain: Optional[bool]
    EndsWith: Optional[bool]
    Equals: Optional[bool]
    Expiry: Optional[bool]
    Extension: Optional[bool]
    External: Optional[bool]
    Geoip: Optional[bool]
    Greater: Optional[bool]
    GreaterOrEqual: Optional[bool]
    Host: Optional[bool]
    HttpBasicAuth: Optional[bool]
    HttpCookie: Optional[bool]
    HttpHeader: Optional[bool]
    HttpHost: Optional[bool]
    HttpMethod: Optional[bool]
    HttpReferer: Optional[bool]
    HttpSetCookie: Optional[bool]
    HttpStatus: Optional[bool]
    HttpUri: Optional[bool]
    HttpUserAgent: Optional[bool]
    HttpVersion: Optional[bool]
    Index: Optional[float]
    Internal: Optional[bool]
    Isp: Optional[bool]
    Last15secs: Optional[bool]
    Last1min: Optional[bool]
    Last5mins: Optional[bool]
    Less: Optional[bool]
    LessOrEqual: Optional[bool]
    Local: Optional[bool]
    Major: Optional[bool]
    Matches: Optional[bool]
    Minor: Optional[bool]
    Missing: Optional[bool]
    Mss: Optional[bool]
    Not: Optional[bool]
    Org: Optional[bool]
    Password: Optional[bool]
    Path: Optional[bool]
    PathSegment: Optional[bool]
    Port: Optional[bool]
    Present: Optional[bool]
    Protocol: Optional[bool]
    QueryParameter: Optional[bool]
    QueryString: Optional[bool]
    RegionCode: Optional[bool]
    RegionName: Optional[bool]
    Remote: Optional[bool]
    Request: Optional[bool]
    Response: Optional[bool]
    RouteDomain: Optional[bool]
    Rtt: Optional[bool]
    Scheme: Optional[bool]
    ServerName: Optional[bool]
    SslCert: Optional[bool]
    SslClientHello: Optional[bool]
    SslExtension: Optional[bool]
    SslServerHandshake: Optional[bool]
    SslServerHello: Optional[bool]
    StartsWith: Optional[bool]
    Tcp: Optional[bool]
    Text: Optional[bool]
    TmName: Optional[str]
    UnnamedQueryParameter: Optional[bool]
    UserAgentToken: Optional[bool]
    Username: Optional[bool]
    Value: Optional[bool]
    Values: Optional[Sequence[str]]
    Version: Optional[bool]
    Vlan: Optional[bool]
    VlanId: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Condition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Condition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            All=json_data.get("All"),
            AppService=json_data.get("AppService"),
            BrowserType=json_data.get("BrowserType"),
            BrowserVersion=json_data.get("BrowserVersion"),
            CaseInsensitive=json_data.get("CaseInsensitive"),
            CaseSensitive=json_data.get("CaseSensitive"),
            Cipher=json_data.get("Cipher"),
            CipherBits=json_data.get("CipherBits"),
            ClientSsl=json_data.get("ClientSsl"),
            Code=json_data.get("Code"),
            CommonName=json_data.get("CommonName"),
            Contains=json_data.get("Contains"),
            Continent=json_data.get("Continent"),
            CountryCode=json_data.get("CountryCode"),
            CountryName=json_data.get("CountryName"),
            CpuUsage=json_data.get("CpuUsage"),
            DeviceMake=json_data.get("DeviceMake"),
            DeviceModel=json_data.get("DeviceModel"),
            Domain=json_data.get("Domain"),
            EndsWith=json_data.get("EndsWith"),
            Equals=json_data.get("Equals"),
            Expiry=json_data.get("Expiry"),
            Extension=json_data.get("Extension"),
            External=json_data.get("External"),
            Geoip=json_data.get("Geoip"),
            Greater=json_data.get("Greater"),
            GreaterOrEqual=json_data.get("GreaterOrEqual"),
            Host=json_data.get("Host"),
            HttpBasicAuth=json_data.get("HttpBasicAuth"),
            HttpCookie=json_data.get("HttpCookie"),
            HttpHeader=json_data.get("HttpHeader"),
            HttpHost=json_data.get("HttpHost"),
            HttpMethod=json_data.get("HttpMethod"),
            HttpReferer=json_data.get("HttpReferer"),
            HttpSetCookie=json_data.get("HttpSetCookie"),
            HttpStatus=json_data.get("HttpStatus"),
            HttpUri=json_data.get("HttpUri"),
            HttpUserAgent=json_data.get("HttpUserAgent"),
            HttpVersion=json_data.get("HttpVersion"),
            Index=json_data.get("Index"),
            Internal=json_data.get("Internal"),
            Isp=json_data.get("Isp"),
            Last15secs=json_data.get("Last15secs"),
            Last1min=json_data.get("Last1min"),
            Last5mins=json_data.get("Last5mins"),
            Less=json_data.get("Less"),
            LessOrEqual=json_data.get("LessOrEqual"),
            Local=json_data.get("Local"),
            Major=json_data.get("Major"),
            Matches=json_data.get("Matches"),
            Minor=json_data.get("Minor"),
            Missing=json_data.get("Missing"),
            Mss=json_data.get("Mss"),
            Not=json_data.get("Not"),
            Org=json_data.get("Org"),
            Password=json_data.get("Password"),
            Path=json_data.get("Path"),
            PathSegment=json_data.get("PathSegment"),
            Port=json_data.get("Port"),
            Present=json_data.get("Present"),
            Protocol=json_data.get("Protocol"),
            QueryParameter=json_data.get("QueryParameter"),
            QueryString=json_data.get("QueryString"),
            RegionCode=json_data.get("RegionCode"),
            RegionName=json_data.get("RegionName"),
            Remote=json_data.get("Remote"),
            Request=json_data.get("Request"),
            Response=json_data.get("Response"),
            RouteDomain=json_data.get("RouteDomain"),
            Rtt=json_data.get("Rtt"),
            Scheme=json_data.get("Scheme"),
            ServerName=json_data.get("ServerName"),
            SslCert=json_data.get("SslCert"),
            SslClientHello=json_data.get("SslClientHello"),
            SslExtension=json_data.get("SslExtension"),
            SslServerHandshake=json_data.get("SslServerHandshake"),
            SslServerHello=json_data.get("SslServerHello"),
            StartsWith=json_data.get("StartsWith"),
            Tcp=json_data.get("Tcp"),
            Text=json_data.get("Text"),
            TmName=json_data.get("TmName"),
            UnnamedQueryParameter=json_data.get("UnnamedQueryParameter"),
            UserAgentToken=json_data.get("UserAgentToken"),
            Username=json_data.get("Username"),
            Value=json_data.get("Value"),
            Values=json_data.get("Values"),
            Version=json_data.get("Version"),
            Vlan=json_data.get("Vlan"),
            VlanId=json_data.get("VlanId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Condition = Condition


