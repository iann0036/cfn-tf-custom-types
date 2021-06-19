# TF::Volterra::HttpLoadbalancer SpecDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#anyasn" title="AnyAsn">AnyAsn</a>" : <i>Boolean</i>,
    "<a href="#anyclient" title="AnyClient">AnyClient</a>" : <i>Boolean</i>,
    "<a href="#anyip" title="AnyIp">AnyIp</a>" : <i>Boolean</i>,
    "<a href="#clientname" title="ClientName">ClientName</a>" : <i>String</i>,
    "<a href="#disablechallenge" title="DisableChallenge">DisableChallenge</a>" : <i>Boolean</i>,
    "<a href="#enablecaptchachallenge" title="EnableCaptchaChallenge">EnableCaptchaChallenge</a>" : <i>Boolean</i>,
    "<a href="#enablejavascriptchallenge" title="EnableJavascriptChallenge">EnableJavascriptChallenge</a>" : <i>Boolean</i>,
    "<a href="#expirationtimestamp" title="ExpirationTimestamp">ExpirationTimestamp</a>" : <i>String</i>,
    "<a href="#argmatchers" title="ArgMatchers">ArgMatchers</a>" : <i>[ <a href="argmatchersdefinition.md">ArgMatchersDefinition</a>, ... ]</i>,
    "<a href="#asnlist" title="AsnList">AsnList</a>" : <i>[ <a href="asnlistdefinition.md">AsnListDefinition</a>, ... ]</i>,
    "<a href="#asnmatcher" title="AsnMatcher">AsnMatcher</a>" : <i>[ <a href="asnmatcherdefinition.md">AsnMatcherDefinition</a>, ... ]</i>,
    "<a href="#bodymatcher" title="BodyMatcher">BodyMatcher</a>" : <i>[ <a href="bodymatcherdefinition.md">BodyMatcherDefinition</a>, ... ]</i>,
    "<a href="#clientnamematcher" title="ClientNameMatcher">ClientNameMatcher</a>" : <i>[ <a href="clientnamematcherdefinition.md">ClientNameMatcherDefinition</a>, ... ]</i>,
    "<a href="#clientselector" title="ClientSelector">ClientSelector</a>" : <i>[ <a href="clientselectordefinition.md">ClientSelectorDefinition</a>, ... ]</i>,
    "<a href="#cookiematchers" title="CookieMatchers">CookieMatchers</a>" : <i>[ <a href="cookiematchersdefinition.md">CookieMatchersDefinition</a>, ... ]</i>,
    "<a href="#domainmatcher" title="DomainMatcher">DomainMatcher</a>" : <i>[ <a href="domainmatcherdefinition.md">DomainMatcherDefinition</a>, ... ]</i>,
    "<a href="#headers" title="Headers">Headers</a>" : <i>[ <a href="headersdefinition.md">HeadersDefinition</a>, ... ]</i>,
    "<a href="#httpmethod" title="HttpMethod">HttpMethod</a>" : <i>[ <a href="httpmethoddefinition.md">HttpMethodDefinition</a>, ... ]</i>,
    "<a href="#ipmatcher" title="IpMatcher">IpMatcher</a>" : <i>[ <a href="ipmatcherdefinition.md">IpMatcherDefinition</a>, ... ]</i>,
    "<a href="#ipprefixlist" title="IpPrefixList">IpPrefixList</a>" : <i>[ <a href="ipprefixlistdefinition.md">IpPrefixListDefinition</a>, ... ]</i>,
    "<a href="#path" title="Path">Path</a>" : <i>[ <a href="pathdefinition.md">PathDefinition</a>, ... ]</i>,
    "<a href="#queryparams" title="QueryParams">QueryParams</a>" : <i>[ <a href="queryparamsdefinition.md">QueryParamsDefinition</a>, ... ]</i>,
    "<a href="#tlsfingerprintmatcher" title="TlsFingerprintMatcher">TlsFingerprintMatcher</a>" : <i>[ <a href="tlsfingerprintmatcherdefinition.md">TlsFingerprintMatcherDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#anyasn" title="AnyAsn">AnyAsn</a>: <i>Boolean</i>
<a href="#anyclient" title="AnyClient">AnyClient</a>: <i>Boolean</i>
<a href="#anyip" title="AnyIp">AnyIp</a>: <i>Boolean</i>
<a href="#clientname" title="ClientName">ClientName</a>: <i>String</i>
<a href="#disablechallenge" title="DisableChallenge">DisableChallenge</a>: <i>Boolean</i>
<a href="#enablecaptchachallenge" title="EnableCaptchaChallenge">EnableCaptchaChallenge</a>: <i>Boolean</i>
<a href="#enablejavascriptchallenge" title="EnableJavascriptChallenge">EnableJavascriptChallenge</a>: <i>Boolean</i>
<a href="#expirationtimestamp" title="ExpirationTimestamp">ExpirationTimestamp</a>: <i>String</i>
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
<a href="#clientselector" title="ClientSelector">ClientSelector</a>: <i>
      - <a href="clientselectordefinition.md">ClientSelectorDefinition</a></i>
<a href="#cookiematchers" title="CookieMatchers">CookieMatchers</a>: <i>
      - <a href="cookiematchersdefinition.md">CookieMatchersDefinition</a></i>
<a href="#domainmatcher" title="DomainMatcher">DomainMatcher</a>: <i>
      - <a href="domainmatcherdefinition.md">DomainMatcherDefinition</a></i>
<a href="#headers" title="Headers">Headers</a>: <i>
      - <a href="headersdefinition.md">HeadersDefinition</a></i>
<a href="#httpmethod" title="HttpMethod">HttpMethod</a>: <i>
      - <a href="httpmethoddefinition.md">HttpMethodDefinition</a></i>
<a href="#ipmatcher" title="IpMatcher">IpMatcher</a>: <i>
      - <a href="ipmatcherdefinition.md">IpMatcherDefinition</a></i>
<a href="#ipprefixlist" title="IpPrefixList">IpPrefixList</a>: <i>
      - <a href="ipprefixlistdefinition.md">IpPrefixListDefinition</a></i>
<a href="#path" title="Path">Path</a>: <i>
      - <a href="pathdefinition.md">PathDefinition</a></i>
<a href="#queryparams" title="QueryParams">QueryParams</a>: <i>
      - <a href="queryparamsdefinition.md">QueryParamsDefinition</a></i>
<a href="#tlsfingerprintmatcher" title="TlsFingerprintMatcher">TlsFingerprintMatcher</a>: <i>
      - <a href="tlsfingerprintmatcherdefinition.md">TlsFingerprintMatcherDefinition</a></i>
</pre>

## Properties

#### AnyAsn

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AnyClient

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AnyIp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableChallenge

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableCaptchaChallenge

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableJavascriptChallenge

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpirationTimestamp

_Required_: No

_Type_: String

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

#### Path

_Required_: No

_Type_: List of <a href="pathdefinition.md">PathDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryParams

_Required_: No

_Type_: List of <a href="queryparamsdefinition.md">QueryParamsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsFingerprintMatcher

_Required_: No

_Type_: List of <a href="tlsfingerprintmatcherdefinition.md">TlsFingerprintMatcherDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

