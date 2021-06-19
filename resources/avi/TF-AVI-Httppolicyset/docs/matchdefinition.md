# TF::AVI::Httppolicyset MatchDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#clientip" title="ClientIp">ClientIp</a>" : <i>[ <a href="clientipdefinition.md">ClientIpDefinition</a>, ... ]</i>,
    "<a href="#cookie" title="Cookie">Cookie</a>" : <i>[ <a href="cookiedefinition.md">CookieDefinition</a>, ... ]</i>,
    "<a href="#hdrs" title="Hdrs">Hdrs</a>" : <i>[ <a href="hdrsdefinition.md">HdrsDefinition</a>, ... ]</i>,
    "<a href="#hosthdr" title="HostHdr">HostHdr</a>" : <i>[ <a href="hosthdrdefinition.md">HostHdrDefinition</a>, ... ]</i>,
    "<a href="#ipreputationtype" title="IpReputationType">IpReputationType</a>" : <i>[ <a href="ipreputationtypedefinition.md">IpReputationTypeDefinition</a>, ... ]</i>,
    "<a href="#method" title="Method">Method</a>" : <i>[ <a href="methoddefinition.md">MethodDefinition</a>, ... ]</i>,
    "<a href="#path" title="Path">Path</a>" : <i>[ <a href="pathdefinition.md">PathDefinition</a>, ... ]</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>[ <a href="protocoldefinition.md">ProtocolDefinition</a>, ... ]</i>,
    "<a href="#query" title="Query">Query</a>" : <i>[ <a href="querydefinition.md">QueryDefinition</a>, ... ]</i>,
    "<a href="#version" title="Version">Version</a>" : <i>[ <a href="versiondefinition.md">VersionDefinition</a>, ... ]</i>,
    "<a href="#vsport" title="VsPort">VsPort</a>" : <i>[ <a href="vsportdefinition.md">VsPortDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#clientip" title="ClientIp">ClientIp</a>: <i>
      - <a href="clientipdefinition.md">ClientIpDefinition</a></i>
<a href="#cookie" title="Cookie">Cookie</a>: <i>
      - <a href="cookiedefinition.md">CookieDefinition</a></i>
<a href="#hdrs" title="Hdrs">Hdrs</a>: <i>
      - <a href="hdrsdefinition.md">HdrsDefinition</a></i>
<a href="#hosthdr" title="HostHdr">HostHdr</a>: <i>
      - <a href="hosthdrdefinition.md">HostHdrDefinition</a></i>
<a href="#ipreputationtype" title="IpReputationType">IpReputationType</a>: <i>
      - <a href="ipreputationtypedefinition.md">IpReputationTypeDefinition</a></i>
<a href="#method" title="Method">Method</a>: <i>
      - <a href="methoddefinition.md">MethodDefinition</a></i>
<a href="#path" title="Path">Path</a>: <i>
      - <a href="pathdefinition.md">PathDefinition</a></i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>
      - <a href="protocoldefinition.md">ProtocolDefinition</a></i>
<a href="#query" title="Query">Query</a>: <i>
      - <a href="querydefinition.md">QueryDefinition</a></i>
<a href="#version" title="Version">Version</a>: <i>
      - <a href="versiondefinition.md">VersionDefinition</a></i>
<a href="#vsport" title="VsPort">VsPort</a>: <i>
      - <a href="vsportdefinition.md">VsPortDefinition</a></i>
</pre>

## Properties

#### ClientIp

_Required_: No

_Type_: List of <a href="clientipdefinition.md">ClientIpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cookie

_Required_: No

_Type_: List of <a href="cookiedefinition.md">CookieDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hdrs

_Required_: No

_Type_: List of <a href="hdrsdefinition.md">HdrsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostHdr

_Required_: No

_Type_: List of <a href="hosthdrdefinition.md">HostHdrDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpReputationType

_Required_: No

_Type_: List of <a href="ipreputationtypedefinition.md">IpReputationTypeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Method

_Required_: No

_Type_: List of <a href="methoddefinition.md">MethodDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

_Required_: No

_Type_: List of <a href="pathdefinition.md">PathDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: No

_Type_: List of <a href="protocoldefinition.md">ProtocolDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Query

_Required_: No

_Type_: List of <a href="querydefinition.md">QueryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: No

_Type_: List of <a href="versiondefinition.md">VersionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsPort

_Required_: No

_Type_: List of <a href="vsportdefinition.md">VsPortDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

