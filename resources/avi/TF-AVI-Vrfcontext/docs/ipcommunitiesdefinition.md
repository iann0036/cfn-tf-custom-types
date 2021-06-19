# TF::AVI::Vrfcontext IpCommunitiesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#community" title="Community">Community</a>" : <i>[ String, ... ]</i>,
    "<a href="#ipbegin" title="IpBegin">IpBegin</a>" : <i>[ <a href="ipbegindefinition.md">IpBeginDefinition</a>, ... ]</i>,
    "<a href="#ipend" title="IpEnd">IpEnd</a>" : <i>[ <a href="ipenddefinition.md">IpEndDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#community" title="Community">Community</a>: <i>
      - String</i>
<a href="#ipbegin" title="IpBegin">IpBegin</a>: <i>
      - <a href="ipbegindefinition.md">IpBeginDefinition</a></i>
<a href="#ipend" title="IpEnd">IpEnd</a>: <i>
      - <a href="ipenddefinition.md">IpEndDefinition</a></i>
</pre>

## Properties

#### Community

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpBegin

_Required_: No

_Type_: List of <a href="ipbegindefinition.md">IpBeginDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpEnd

_Required_: No

_Type_: List of <a href="ipenddefinition.md">IpEndDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

