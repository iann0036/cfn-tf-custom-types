# TF::AVI::Ssopolicy MatchDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accesstoken" title="AccessToken">AccessToken</a>" : <i>[ <a href="accesstokendefinition.md">AccessTokenDefinition</a>, ... ]</i>,
    "<a href="#attrmatches" title="AttrMatches">AttrMatches</a>" : <i>[ <a href="attrmatchesdefinition.md">AttrMatchesDefinition</a>, ... ]</i>,
    "<a href="#hosthdr" title="HostHdr">HostHdr</a>" : <i>[ <a href="hosthdrdefinition.md">HostHdrDefinition</a>, ... ]</i>,
    "<a href="#method" title="Method">Method</a>" : <i>[ <a href="methoddefinition.md">MethodDefinition</a>, ... ]</i>,
    "<a href="#path" title="Path">Path</a>" : <i>[ <a href="pathdefinition.md">PathDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#accesstoken" title="AccessToken">AccessToken</a>: <i>
      - <a href="accesstokendefinition.md">AccessTokenDefinition</a></i>
<a href="#attrmatches" title="AttrMatches">AttrMatches</a>: <i>
      - <a href="attrmatchesdefinition.md">AttrMatchesDefinition</a></i>
<a href="#hosthdr" title="HostHdr">HostHdr</a>: <i>
      - <a href="hosthdrdefinition.md">HostHdrDefinition</a></i>
<a href="#method" title="Method">Method</a>: <i>
      - <a href="methoddefinition.md">MethodDefinition</a></i>
<a href="#path" title="Path">Path</a>: <i>
      - <a href="pathdefinition.md">PathDefinition</a></i>
</pre>

## Properties

#### AccessToken

_Required_: No

_Type_: List of <a href="accesstokendefinition.md">AccessTokenDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AttrMatches

_Required_: No

_Type_: List of <a href="attrmatchesdefinition.md">AttrMatchesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostHdr

_Required_: No

_Type_: List of <a href="hosthdrdefinition.md">HostHdrDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Method

_Required_: No

_Type_: List of <a href="methoddefinition.md">MethodDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

_Required_: No

_Type_: List of <a href="pathdefinition.md">PathDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

