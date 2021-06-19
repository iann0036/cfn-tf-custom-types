# TF::Volterra::ServicePolicyRule

CloudFormation equivalent of volterra_service_policy_rule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Volterra::ServicePolicyRule",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#annotations" title="Annotations">Annotations</a>" : <i>[ <a href="annotationsdefinition.md">AnnotationsDefinition</a>, ... ]</i>,
        "<a href="#anyasn" title="AnyAsn">AnyAsn</a>" : <i>Boolean</i>,
        "<a href="#anyclient" title="AnyClient">AnyClient</a>" : <i>Boolean</i>,
        "<a href="#anydstasn" title="AnyDstAsn">AnyDstAsn</a>" : <i>Boolean</i>,
        "<a href="#anydstip" title="AnyDstIp">AnyDstIp</a>" : <i>Boolean</i>,
        "<a href="#anyip" title="AnyIp">AnyIp</a>" : <i>Boolean</i>,
        "<a href="#challengeaction" title="ChallengeAction">ChallengeAction</a>" : <i>String</i>,
        "<a href="#clientname" title="ClientName">ClientName</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#disable" title="Disable">Disable</a>" : <i>Boolean</i>,
        "<a href="#expirationtimestamp" title="ExpirationTimestamp">ExpirationTimestamp</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#malicioususermitigationbypass" title="MaliciousUserMitigationBypass">MaliciousUserMitigationBypass</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
        "<a href="#scheme" title="Scheme">Scheme</a>" : <i>[ String, ... ]</i>,
        "<a href="#apigroupmatcher" title="ApiGroupMatcher">ApiGroupMatcher</a>" : <i>[ <a href="apigroupmatcherdefinition.md">ApiGroupMatcherDefinition</a>, ... ]</i>,
        "<a href="#argmatchers" title="ArgMatchers">ArgMatchers</a>" : <i>[ <a href="argmatchersdefinition.md">ArgMatchersDefinition</a>, ... ]</i>,
        "<a href="#asnlist" title="AsnList">AsnList</a>" : <i>[ <a href="asnlistdefinition.md">AsnListDefinition</a>, ... ]</i>,
        "<a href="#asnmatcher" title="AsnMatcher">AsnMatcher</a>" : <i>[ <a href="asnmatcherdefinition.md">AsnMatcherDefinition</a>, ... ]</i>,
        "<a href="#bodymatcher" title="BodyMatcher">BodyMatcher</a>" : <i>[ <a href="bodymatcherdefinition.md">BodyMatcherDefinition</a>, ... ]</i>,
        "<a href="#clientnamematcher" title="ClientNameMatcher">ClientNameMatcher</a>" : <i>[ <a href="clientnamematcherdefinition.md">ClientNameMatcherDefinition</a>, ... ]</i>,
        "<a href="#clientrole" title="ClientRole">ClientRole</a>" : <i>[ <a href="clientroledefinition.md">ClientRoleDefinition</a>, ... ]</i>,
        "<a href="#clientselector" title="ClientSelector">ClientSelector</a>" : <i>[ <a href="clientselectordefinition.md">ClientSelectorDefinition</a>, ... ]</i>,
        "<a href="#cookiematchers" title="CookieMatchers">CookieMatchers</a>" : <i>[ <a href="cookiematchersdefinition.md">CookieMatchersDefinition</a>, ... ]</i>,
        "<a href="#domainmatcher" title="DomainMatcher">DomainMatcher</a>" : <i>[ <a href="domainmatcherdefinition.md">DomainMatcherDefinition</a>, ... ]</i>,
        "<a href="#dstasnlist" title="DstAsnList">DstAsnList</a>" : <i>[ <a href="dstasnlistdefinition.md">DstAsnListDefinition</a>, ... ]</i>,
        "<a href="#dstasnmatcher" title="DstAsnMatcher">DstAsnMatcher</a>" : <i>[ <a href="dstasnmatcherdefinition.md">DstAsnMatcherDefinition</a>, ... ]</i>,
        "<a href="#dstipmatcher" title="DstIpMatcher">DstIpMatcher</a>" : <i>[ <a href="dstipmatcherdefinition.md">DstIpMatcherDefinition</a>, ... ]</i>,
        "<a href="#dstipprefixlist" title="DstIpPrefixList">DstIpPrefixList</a>" : <i>[ <a href="dstipprefixlistdefinition.md">DstIpPrefixListDefinition</a>, ... ]</i>,
        "<a href="#gotopolicy" title="GotoPolicy">GotoPolicy</a>" : <i>[ <a href="gotopolicydefinition.md">GotoPolicyDefinition</a>, ... ]</i>,
        "<a href="#headers" title="Headers">Headers</a>" : <i>[ <a href="headersdefinition.md">HeadersDefinition</a>, ... ]</i>,
        "<a href="#httpmethod" title="HttpMethod">HttpMethod</a>" : <i>[ <a href="httpmethoddefinition.md">HttpMethodDefinition</a>, ... ]</i>,
        "<a href="#ipmatcher" title="IpMatcher">IpMatcher</a>" : <i>[ <a href="ipmatcherdefinition.md">IpMatcherDefinition</a>, ... ]</i>,
        "<a href="#ipprefixlist" title="IpPrefixList">IpPrefixList</a>" : <i>[ <a href="ipprefixlistdefinition.md">IpPrefixListDefinition</a>, ... ]</i>,
        "<a href="#l4destmatcher" title="L4DestMatcher">L4DestMatcher</a>" : <i>[ <a href="l4destmatcherdefinition.md">L4DestMatcherDefinition</a>, ... ]</i>,
        "<a href="#labelmatcher" title="LabelMatcher">LabelMatcher</a>" : <i>[ <a href="labelmatcherdefinition.md">LabelMatcherDefinition</a>, ... ]</i>,
        "<a href="#path" title="Path">Path</a>" : <i>[ <a href="pathdefinition.md">PathDefinition</a>, ... ]</i>,
        "<a href="#portmatcher" title="PortMatcher">PortMatcher</a>" : <i>[ <a href="portmatcherdefinition.md">PortMatcherDefinition</a>, ... ]</i>,
        "<a href="#queryparams" title="QueryParams">QueryParams</a>" : <i>[ <a href="queryparamsdefinition.md">QueryParamsDefinition</a>, ... ]</i>,
        "<a href="#ratelimiter" title="RateLimiter">RateLimiter</a>" : <i>[ <a href="ratelimiterdefinition.md">RateLimiterDefinition</a>, ... ]</i>,
        "<a href="#serverselector" title="ServerSelector">ServerSelector</a>" : <i>[ <a href="serverselectordefinition.md">ServerSelectorDefinition</a>, ... ]</i>,
        "<a href="#tlsfingerprintmatcher" title="TlsFingerprintMatcher">TlsFingerprintMatcher</a>" : <i>[ <a href="tlsfingerprintmatcherdefinition.md">TlsFingerprintMatcherDefinition</a>, ... ]</i>,
        "<a href="#urlmatcher" title="UrlMatcher">UrlMatcher</a>" : <i>[ <a href="urlmatcherdefinition.md">UrlMatcherDefinition</a>, ... ]</i>,
        "<a href="#virtualhostmatcher" title="VirtualHostMatcher">VirtualHostMatcher</a>" : <i>[ <a href="virtualhostmatcherdefinition.md">VirtualHostMatcherDefinition</a>, ... ]</i>,
        "<a href="#wafaction" title="WafAction">WafAction</a>" : <i>[ <a href="wafactiondefinition.md">WafActionDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Volterra::ServicePolicyRule
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#annotations" title="Annotations">Annotations</a>: <i>
      - <a href="annotationsdefinition.md">AnnotationsDefinition</a></i>
    <a href="#anyasn" title="AnyAsn">AnyAsn</a>: <i>Boolean</i>
    <a href="#anyclient" title="AnyClient">AnyClient</a>: <i>Boolean</i>
    <a href="#anydstasn" title="AnyDstAsn">AnyDstAsn</a>: <i>Boolean</i>
    <a href="#anydstip" title="AnyDstIp">AnyDstIp</a>: <i>Boolean</i>
    <a href="#anyip" title="AnyIp">AnyIp</a>: <i>Boolean</i>
    <a href="#challengeaction" title="ChallengeAction">ChallengeAction</a>: <i>String</i>
    <a href="#clientname" title="ClientName">ClientName</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#disable" title="Disable">Disable</a>: <i>Boolean</i>
    <a href="#expirationtimestamp" title="ExpirationTimestamp">ExpirationTimestamp</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#malicioususermitigationbypass" title="MaliciousUserMitigationBypass">MaliciousUserMitigationBypass</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
    <a href="#scheme" title="Scheme">Scheme</a>: <i>
      - String</i>
    <a href="#apigroupmatcher" title="ApiGroupMatcher">ApiGroupMatcher</a>: <i>
      - <a href="apigroupmatcherdefinition.md">ApiGroupMatcherDefinition</a></i>
    <a href="#argmatchers" title="ArgMatchers">ArgMatchers</a>: <i>
      - <a href="argmatchersdefinition.md">ArgMatchersDefinition</a></i>
    <a href="#asnlist" title="AsnList">AsnList</a>: <i>
      - <a href="asnlistdefinition.md">AsnListDefinition</a></i>
    <a href="#asnmatcher" title="AsnMatcher">AsnMatcher</a>: <i>
      - <a href="asnmatcherdefinition.md">AsnMatcherDefinition</a></i>
    <a href="#bodymatcher" title="BodyMatcher">BodyMatcher</a>: <i>
      - <a href="bodymatcherdefinition.md">BodyMatcherDefinition</a></i>
    <a href="#clientnamematcher" title="ClientNameMatcher">ClientNameMatcher</a>: <i>
      - <a href="clientnamematcherdefinition.md">ClientNameMatcherDefinition</a></i>
    <a href="#clientrole" title="ClientRole">ClientRole</a>: <i>
      - <a href="clientroledefinition.md">ClientRoleDefinition</a></i>
    <a href="#clientselector" title="ClientSelector">ClientSelector</a>: <i>
      - <a href="clientselectordefinition.md">ClientSelectorDefinition</a></i>
    <a href="#cookiematchers" title="CookieMatchers">CookieMatchers</a>: <i>
      - <a href="cookiematchersdefinition.md">CookieMatchersDefinition</a></i>
    <a href="#domainmatcher" title="DomainMatcher">DomainMatcher</a>: <i>
      - <a href="domainmatcherdefinition.md">DomainMatcherDefinition</a></i>
    <a href="#dstasnlist" title="DstAsnList">DstAsnList</a>: <i>
      - <a href="dstasnlistdefinition.md">DstAsnListDefinition</a></i>
    <a href="#dstasnmatcher" title="DstAsnMatcher">DstAsnMatcher</a>: <i>
      - <a href="dstasnmatcherdefinition.md">DstAsnMatcherDefinition</a></i>
    <a href="#dstipmatcher" title="DstIpMatcher">DstIpMatcher</a>: <i>
      - <a href="dstipmatcherdefinition.md">DstIpMatcherDefinition</a></i>
    <a href="#dstipprefixlist" title="DstIpPrefixList">DstIpPrefixList</a>: <i>
      - <a href="dstipprefixlistdefinition.md">DstIpPrefixListDefinition</a></i>
    <a href="#gotopolicy" title="GotoPolicy">GotoPolicy</a>: <i>
      - <a href="gotopolicydefinition.md">GotoPolicyDefinition</a></i>
    <a href="#headers" title="Headers">Headers</a>: <i>
      - <a href="headersdefinition.md">HeadersDefinition</a></i>
    <a href="#httpmethod" title="HttpMethod">HttpMethod</a>: <i>
      - <a href="httpmethoddefinition.md">HttpMethodDefinition</a></i>
    <a href="#ipmatcher" title="IpMatcher">IpMatcher</a>: <i>
      - <a href="ipmatcherdefinition.md">IpMatcherDefinition</a></i>
    <a href="#ipprefixlist" title="IpPrefixList">IpPrefixList</a>: <i>
      - <a href="ipprefixlistdefinition.md">IpPrefixListDefinition</a></i>
    <a href="#l4destmatcher" title="L4DestMatcher">L4DestMatcher</a>: <i>
      - <a href="l4destmatcherdefinition.md">L4DestMatcherDefinition</a></i>
    <a href="#labelmatcher" title="LabelMatcher">LabelMatcher</a>: <i>
      - <a href="labelmatcherdefinition.md">LabelMatcherDefinition</a></i>
    <a href="#path" title="Path">Path</a>: <i>
      - <a href="pathdefinition.md">PathDefinition</a></i>
    <a href="#portmatcher" title="PortMatcher">PortMatcher</a>: <i>
      - <a href="portmatcherdefinition.md">PortMatcherDefinition</a></i>
    <a href="#queryparams" title="QueryParams">QueryParams</a>: <i>
      - <a href="queryparamsdefinition.md">QueryParamsDefinition</a></i>
    <a href="#ratelimiter" title="RateLimiter">RateLimiter</a>: <i>
      - <a href="ratelimiterdefinition.md">RateLimiterDefinition</a></i>
    <a href="#serverselector" title="ServerSelector">ServerSelector</a>: <i>
      - <a href="serverselectordefinition.md">ServerSelectorDefinition</a></i>
    <a href="#tlsfingerprintmatcher" title="TlsFingerprintMatcher">TlsFingerprintMatcher</a>: <i>
      - <a href="tlsfingerprintmatcherdefinition.md">TlsFingerprintMatcherDefinition</a></i>
    <a href="#urlmatcher" title="UrlMatcher">UrlMatcher</a>: <i>
      - <a href="urlmatcherdefinition.md">UrlMatcherDefinition</a></i>
    <a href="#virtualhostmatcher" title="VirtualHostMatcher">VirtualHostMatcher</a>: <i>
      - <a href="virtualhostmatcherdefinition.md">VirtualHostMatcherDefinition</a></i>
    <a href="#wafaction" title="WafAction">WafAction</a>: <i>
      - <a href="wafactiondefinition.md">WafActionDefinition</a></i>
</pre>

## Properties

#### Action

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Annotations

_Required_: No

_Type_: List of <a href="annotationsdefinition.md">AnnotationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AnyAsn

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AnyClient

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AnyDstAsn

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AnyDstIp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AnyIp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChallengeAction

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpirationTimestamp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaliciousUserMitigationBypass

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scheme

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApiGroupMatcher

_Required_: No

_Type_: List of <a href="apigroupmatcherdefinition.md">ApiGroupMatcherDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ArgMatchers

_Required_: No

_Type_: List of <a href="argmatchersdefinition.md">ArgMatchersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AsnList

_Required_: No

_Type_: List of <a href="asnlistdefinition.md">AsnListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AsnMatcher

_Required_: No

_Type_: List of <a href="asnmatcherdefinition.md">AsnMatcherDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BodyMatcher

_Required_: No

_Type_: List of <a href="bodymatcherdefinition.md">BodyMatcherDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientNameMatcher

_Required_: No

_Type_: List of <a href="clientnamematcherdefinition.md">ClientNameMatcherDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientRole

_Required_: No

_Type_: List of <a href="clientroledefinition.md">ClientRoleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientSelector

_Required_: No

_Type_: List of <a href="clientselectordefinition.md">ClientSelectorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CookieMatchers

_Required_: No

_Type_: List of <a href="cookiematchersdefinition.md">CookieMatchersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainMatcher

_Required_: No

_Type_: List of <a href="domainmatcherdefinition.md">DomainMatcherDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DstAsnList

_Required_: No

_Type_: List of <a href="dstasnlistdefinition.md">DstAsnListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DstAsnMatcher

_Required_: No

_Type_: List of <a href="dstasnmatcherdefinition.md">DstAsnMatcherDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DstIpMatcher

_Required_: No

_Type_: List of <a href="dstipmatcherdefinition.md">DstIpMatcherDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DstIpPrefixList

_Required_: No

_Type_: List of <a href="dstipprefixlistdefinition.md">DstIpPrefixListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GotoPolicy

_Required_: No

_Type_: List of <a href="gotopolicydefinition.md">GotoPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Headers

_Required_: No

_Type_: List of <a href="headersdefinition.md">HeadersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpMethod

_Required_: No

_Type_: List of <a href="httpmethoddefinition.md">HttpMethodDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpMatcher

_Required_: No

_Type_: List of <a href="ipmatcherdefinition.md">IpMatcherDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpPrefixList

_Required_: No

_Type_: List of <a href="ipprefixlistdefinition.md">IpPrefixListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L4DestMatcher

_Required_: No

_Type_: List of <a href="l4destmatcherdefinition.md">L4DestMatcherDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LabelMatcher

_Required_: No

_Type_: List of <a href="labelmatcherdefinition.md">LabelMatcherDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

_Required_: No

_Type_: List of <a href="pathdefinition.md">PathDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortMatcher

_Required_: No

_Type_: List of <a href="portmatcherdefinition.md">PortMatcherDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryParams

_Required_: No

_Type_: List of <a href="queryparamsdefinition.md">QueryParamsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RateLimiter

_Required_: No

_Type_: List of <a href="ratelimiterdefinition.md">RateLimiterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerSelector

_Required_: No

_Type_: List of <a href="serverselectordefinition.md">ServerSelectorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsFingerprintMatcher

_Required_: No

_Type_: List of <a href="tlsfingerprintmatcherdefinition.md">TlsFingerprintMatcherDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlMatcher

_Required_: No

_Type_: List of <a href="urlmatcherdefinition.md">UrlMatcherDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualHostMatcher

_Required_: No

_Type_: List of <a href="virtualhostmatcherdefinition.md">VirtualHostMatcherDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WafAction

_Required_: No

_Type_: List of <a href="wafactiondefinition.md">WafActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

