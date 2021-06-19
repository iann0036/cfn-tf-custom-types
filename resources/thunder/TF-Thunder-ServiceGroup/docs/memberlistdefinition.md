# TF::Thunder::ServiceGroup MemberListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#fqdnname" title="FqdnName">FqdnName</a>" : <i>String</i>,
    "<a href="#host" title="Host">Host</a>" : <i>String</i>,
    "<a href="#memberpriority" title="MemberPriority">MemberPriority</a>" : <i>Double</i>,
    "<a href="#memberstate" title="MemberState">MemberState</a>" : <i>String</i>,
    "<a href="#memberstatsdatadisable" title="MemberStatsDataDisable">MemberStatsDataDisable</a>" : <i>Double</i>,
    "<a href="#membertemplate" title="MemberTemplate">MemberTemplate</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#resolveas" title="ResolveAs">ResolveAs</a>" : <i>String</i>,
    "<a href="#serveripv6addr" title="ServerIpv6Addr">ServerIpv6Addr</a>" : <i>String</i>,
    "<a href="#usertag" title="UserTag">UserTag</a>" : <i>String</i>,
    "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
    "<a href="#samplingenable" title="SamplingEnable">SamplingEnable</a>" : <i>[ <a href="samplingenabledefinition.md">SamplingEnableDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#fqdnname" title="FqdnName">FqdnName</a>: <i>String</i>
<a href="#host" title="Host">Host</a>: <i>String</i>
<a href="#memberpriority" title="MemberPriority">MemberPriority</a>: <i>Double</i>
<a href="#memberstate" title="MemberState">MemberState</a>: <i>String</i>
<a href="#memberstatsdatadisable" title="MemberStatsDataDisable">MemberStatsDataDisable</a>: <i>Double</i>
<a href="#membertemplate" title="MemberTemplate">MemberTemplate</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#resolveas" title="ResolveAs">ResolveAs</a>: <i>String</i>
<a href="#serveripv6addr" title="ServerIpv6Addr">ServerIpv6Addr</a>: <i>String</i>
<a href="#usertag" title="UserTag">UserTag</a>: <i>String</i>
<a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
<a href="#samplingenable" title="SamplingEnable">SamplingEnable</a>: <i>
      - <a href="samplingenabledefinition.md">SamplingEnableDefinition</a></i>
</pre>

## Properties

#### FqdnName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Host

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemberPriority

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemberState

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemberStatsDataDisable

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemberTemplate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResolveAs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerIpv6Addr

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserTag

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SamplingEnable

_Required_: No

_Type_: List of <a href="samplingenabledefinition.md">SamplingEnableDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

