# TF::AVI::Virtualservice SslProfileSelectorsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#sslprofileref" title="SslProfileRef">SslProfileRef</a>" : <i>String</i>,
    "<a href="#clientiplist" title="ClientIpList">ClientIpList</a>" : <i>[ <a href="clientiplistdefinition.md">ClientIpListDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#sslprofileref" title="SslProfileRef">SslProfileRef</a>: <i>String</i>
<a href="#clientiplist" title="ClientIpList">ClientIpList</a>: <i>
      - <a href="clientiplistdefinition.md">ClientIpListDefinition</a></i>
</pre>

## Properties

#### SslProfileRef

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientIpList

_Required_: No

_Type_: List of <a href="clientiplistdefinition.md">ClientIpListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

